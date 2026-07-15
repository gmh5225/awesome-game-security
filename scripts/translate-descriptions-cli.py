#!/usr/bin/env python3
"""
Translate English repo descriptions via the Cursor CLI.

For each description/{owner}/{repo}/description_en.txt, the agent writes:
  description/{owner}/{repo}/description_{lang}.txt

Languages (default):
  zh-CN 简体中文 | zh-TW 繁體中文 | ja 日本語 | ko 한국어 |
  fr Français | de Deutsch | es Español | it Italiano | ru Русский

Prerequisites:
    curl https://cursor.com/install -fsS | bash
    export CURSOR_API_KEY=<your key from https://cursor.com/settings>
    # Max Mode in ~/.cursor/cli-config.json + CURSOR_CONFIG_DIR on CI.

Usage:
    python scripts/translate-descriptions-cli.py                  # fill all missing
    python scripts/translate-descriptions-cli.py --list-missing   # scan only
    python scripts/translate-descriptions-cli.py --repos owner/repo
    DESC_REPOS="owner/repo" python scripts/translate-descriptions-cli.py --repos-env DESC_REPOS
    python scripts/translate-descriptions-cli.py --langs zh-CN,ja --limit 5
    python scripts/translate-descriptions-cli.py --force --repos owner/repo
    python scripts/translate-descriptions-cli.py --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DESC_DIR = ROOT_DIR / "description"

DEFAULT_MODEL = "cursor-grok-4.5-high-fast"
# No per-agent wall clock — long Max Mode runs must not be killed mid-write.
# GitHub-hosted jobs still have a platform cap (~6h); --commit-every saves progress.
REPO_SLUG_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$")
LANG_CODE_RE = re.compile(r"^[A-Za-z]{2}(-[A-Za-z]{2})?$")

# code → native display name (used in prompts)
LANGS: dict[str, str] = {
    "zh-CN": "简体中文",
    "zh-TW": "繁體中文",
    "ja": "日本語",
    "ko": "한국어",
    "fr": "Français",
    "de": "Deutsch",
    "es": "Español",
    "it": "Italiano",
    "ru": "Русский",
}
# Derived from LANGS so keep/discard cannot drift when a language is added.
TRANSLATION_KEEP_RE = re.compile(
    r"^description/[^/]+/[^/]+/description_("
    + "|".join(re.escape(c) for c in LANGS)
    + r")\.txt$"
)


def get_api_key() -> str:
    key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not key:
        sys.exit(
            "ERROR: CURSOR_API_KEY environment variable is not set.\n"
            "Obtain a key from https://cursor.com/settings"
        )
    return key


def find_agent_bin() -> str:
    home_bin = Path.home() / ".cursor" / "bin" / "agent"
    if home_bin.is_file():
        return str(home_bin)
    for name in ("cursor-agent", "agent"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit(
        "ERROR: Cursor CLI `agent` not found on PATH.\n"
        "Install with: curl https://cursor.com/install -fsS | bash"
    )


def parse_repo_slug(slug: str) -> tuple[str, str]:
    cleaned = slug.strip().strip("/")
    if not REPO_SLUG_RE.fullmatch(cleaned):
        sys.exit(
            f"ERROR: invalid repo slug {slug!r} "
            "(expected owner/repo with [A-Za-z0-9._-] only)"
        )
    owner, repo = cleaned.split("/", 1)
    return owner, repo


def slugs_from_env(var_name: str) -> list[str]:
    raw = os.environ.get(var_name, "")
    return [tok for tok in raw.replace("\n", " ").split(" ") if tok]


def parse_lang_codes(raw: str) -> list[str]:
    """Parse comma/space-separated lang codes; empty ⇒ all default langs."""
    if not raw.strip():
        return list(LANGS.keys())
    codes: list[str] = []
    for tok in raw.replace(",", " ").split():
        if not LANG_CODE_RE.fullmatch(tok):
            sys.exit(f"ERROR: invalid language code {tok!r}")
        if tok not in LANGS:
            sys.exit(
                f"ERROR: unsupported language {tok!r}. "
                f"Supported: {', '.join(LANGS)}"
            )
        if tok not in codes:
            codes.append(tok)
    return codes


def en_path(owner: str, repo: str) -> Path:
    return DESC_DIR / owner / repo / "description_en.txt"


def lang_path(owner: str, repo: str, code: str) -> Path:
    return DESC_DIR / owner / repo / f"description_{code}.txt"


def has_en(owner: str, repo: str) -> bool:
    path = en_path(owner, repo)
    return path.is_file() and path.stat().st_size > 0


def needs_lang(owner: str, repo: str, code: str) -> bool:
    path = lang_path(owner, repo, code)
    return not (path.is_file() and path.stat().st_size > 0)


def list_repos_with_en() -> list[tuple[str, str]]:
    repos: list[tuple[str, str]] = []
    if not DESC_DIR.is_dir():
        return repos
    for owner_dir in sorted(DESC_DIR.iterdir()):
        if not owner_dir.is_dir():
            continue
        for repo_dir in sorted(owner_dir.iterdir()):
            if not repo_dir.is_dir():
                continue
            if has_en(owner_dir.name, repo_dir.name):
                repos.append((owner_dir.name, repo_dir.name))
    return repos


def missing_langs_for(
    owner: str, repo: str, langs: list[str], force: bool
) -> list[str]:
    if force:
        return list(langs)
    return [c for c in langs if needs_lang(owner, repo, c)]


def list_missing_work(
    langs: list[str], force: bool
) -> list[tuple[str, str, list[str]]]:
    """Repos that have EN but still need one or more translations."""
    work: list[tuple[str, str, list[str]]] = []
    for owner, repo in list_repos_with_en():
        missing = missing_langs_for(owner, repo, langs, force=force)
        if missing:
            work.append((owner, repo, missing))
    return work


def print_scan_report(work: list[tuple[str, str, list[str]]], langs: list[str]) -> None:
    with_en = list_repos_with_en()
    print("Scan description_en.txt vs translations")
    print(f"  repos with EN        : {len(with_en)}")
    print(f"  target languages     : {', '.join(langs)}")
    print(f"  repos needing work   : {len(work)}")
    print(f"MISSING_COUNT={len(work)}")
    preview = work if len(work) <= 40 else work[:40]
    for owner, repo, missing in preview:
        print(f"  - {owner}/{repo}  ({', '.join(missing)})")
    if len(work) > 40:
        print(f"  ... and {len(work) - 40} more")


def build_prompt(owner: str, repo: str, langs: list[str]) -> str:
    src = f"description/{owner}/{repo}/description_en.txt"
    targets = "\n".join(
        f"  - description/{owner}/{repo}/description_{code}.txt"
        f"  ({LANGS[code]})"
        for code in langs
    )
    return f"""\
You are translating one English repository description for the
awesome-game-security curated list.

Repository: {owner}/{repo}
Source file: {src}

Target files (create/overwrite):
{targets}

Follow these steps exactly:

1. Read ONLY {src}. Do not read archives or other paths.
2. Translate the English text into each target language listed above.
3. Write each translation to its target file (plain UTF-8 text).
4. Translation rules:
   - Preserve meaning, technical terms, and tone
   - Keep roughly the same length (3–5 sentences when the source is)
   - Plain text only: no markdown, no headers, no bullet points
   - Do NOT add the repo URL or owner/repo slug
   - Do NOT wrap the text in quotes
   - Keep well-known product/tool names (e.g. Unreal Engine, IDA, DirectX)
     in their common local form or original English when that is natural
5. If the source is missing or empty, write a single line to each target:
   No description available.

Hard constraints:
- ONLY create/modify the target files listed above
- Do NOT modify {src} or any other path
- Do NOT run git, gh, push, or commit
- When finished, print one line: Done: {owner}/{repo} ({', '.join(langs)})
"""


def run_agent(
    agent_bin: str,
    model: str,
    prompt: str,
    dry_run: bool,
) -> int:
    cmd = [
        agent_bin,
        "-p",
        "--force",
        "--trust",
        "--sandbox",
        "disabled",
        "--workspace",
        str(ROOT_DIR),
        "--model",
        model,
        "--output-format",
        "text",
        prompt,
    ]
    if dry_run:
        print("[DRY-RUN] would run:")
        print(" ", " ".join(cmd[:-1]), "... <prompt>")
        print("--- prompt preview ---")
        print(prompt[:600])
        print("---")
        return 0

    print(f"  $ {agent_bin} -p --force --trust --sandbox disabled --model {model} ...")
    started = time.time()
    proc = subprocess.run(
        cmd,
        cwd=ROOT_DIR,
        env=os.environ.copy(),
        timeout=None,
        check=False,
    )

    elapsed = time.time() - started
    print(f"  exit={proc.returncode}  elapsed={elapsed:.1f}s")
    if proc.returncode != 0 and "--trust" in cmd and elapsed < 2.0:
        print("  retrying without --trust (possible older CLI) ...")
        cmd_no_trust = [c for c in cmd if c != "--trust"]
        proc = subprocess.run(
            cmd_no_trust,
            cwd=ROOT_DIR,
            env=os.environ.copy(),
            timeout=None,
            check=False,
        )
        elapsed2 = time.time() - started
        print(f"  exit={proc.returncode}  elapsed={elapsed2:.1f}s (no --trust)")
    return proc.returncode


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT_DIR,
        capture_output=True,
        check=check,
    )


def _discard_path(rel: str) -> None:
    path = ROOT_DIR / rel
    checked = _git("checkout", "--", rel, check=False)
    if checked.returncode != 0 and path.exists():
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)


def discard_non_translations(keep: list[Path]) -> None:
    """Drop agent side-effects; only preserve the translation paths we intend to commit."""
    keep_set = {str(p.relative_to(ROOT_DIR)) for p in keep}
    proc = _git("ls-files", "-m", "-o", "--exclude-standard", check=False)
    for line in proc.stdout.decode().splitlines():
        rel = line.strip()
        if not rel:
            continue
        if TRANSLATION_KEEP_RE.match(rel):
            # Revert other repos' translation edits; keep only this commit batch.
            if rel not in keep_set:
                _discard_path(rel)
            continue
        _discard_path(rel)


def git_commit_and_push_translations(paths: list[Path], branch: str) -> bool:
    """Commit+push translation files. False ⇒ caller should exit so CI Final can save."""
    if not paths:
        return True
    discard_non_translations(paths)
    rels = [str(p.relative_to(ROOT_DIR)) for p in paths if p.is_file()]
    if not rels:
        return True
    try:
        _git("add", "--", *rels)
        if _git("diff", "--cached", "--quiet", check=False).returncode == 0:
            return True
        msg = f"description: translate {len(rels)} file(s) via Cursor CLI [skip ci]"
        _git("commit", "-m", msg)
    except subprocess.CalledProcessError as e:
        err = (e.stderr or b"").decode().strip()[:200]
        print(f"  [GIT ERROR] commit: {err or e}")
        return False

    for attempt in range(1, 6):
        try:
            _git("push", "origin", f"HEAD:{branch}")
            print(f"  [GIT] committed+pushed {len(rels)} file(s) → {branch}")
            return True
        except subprocess.CalledProcessError as e:
            err = (e.stderr or b"").decode().strip()
            if attempt >= 5:
                print(f"  [GIT ERROR] push failed after 5 retries: {err[:200]}")
                _git("reset", "HEAD~1", check=False)
                return False
            if any(k in err for k in ("rejected", "fetch first", "non-fast-forward")):
                print(f"  [GIT] push rejected (attempt {attempt}/5), rebasing ...")
                try:
                    _git("pull", "--rebase", "origin", branch)
                except subprocess.CalledProcessError as re_err:
                    re_msg = (re_err.stderr or b"").decode().strip()[:200]
                    print(f"  [GIT ERROR] rebase failed: {re_msg}")
                    _git("rebase", "--abort", check=False)
                    _git("reset", "HEAD~1", check=False)
                    return False
            elif any(
                k in err
                for k in ("408", "RPC failed", "unexpected disconnect", "timed out")
            ):
                wait = 5 * attempt
                print(f"  [GIT] push timeout, retrying in {wait}s ...")
                time.sleep(wait)
            else:
                print(f"  [GIT ERROR] push: {err[:200]}")
                _git("reset", "HEAD~1", check=False)
                return False
    return False


def _file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot_lang_hashes(owner: str, repo: str, langs: list[str]) -> dict[str, str]:
    """Content hashes of existing target files (used to detect --force no-ops)."""
    out: dict[str, str] = {}
    for code in langs:
        path = lang_path(owner, repo, code)
        if path.is_file() and path.stat().st_size > 0:
            out[code] = _file_sha256(path)
    return out


def collect_results(
    owner: str,
    repo: str,
    langs: list[str],
    *,
    force: bool,
    before_hashes: dict[str, str],
) -> tuple[list[str], list[str]]:
    ok: list[str] = []
    bad: list[str] = []
    for code in langs:
        path = lang_path(owner, repo, code)
        if path.is_file() and path.stat().st_size > 0:
            # --force must actually rewrite; stale pre-existing files are failure.
            if force and code in before_hashes and _file_sha256(path) == before_hashes[code]:
                print(
                    f"  FAILED {code}: file unchanged after --force "
                    f"({path.relative_to(ROOT_DIR)})"
                )
                bad.append(code)
            else:
                ok.append(code)
        else:
            bad.append(code)
            if path.is_file() and path.stat().st_size == 0:
                path.unlink()
                print(f"  removed empty stub {path.relative_to(ROOT_DIR)}")
    return ok, bad


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate description_en.txt via Cursor CLI (agent)"
    )
    parser.add_argument(
        "--repos",
        nargs="*",
        default=None,
        help="Only process these owner/repo slugs (default: all needing work)",
    )
    parser.add_argument(
        "--repos-env",
        type=str,
        default="",
        help="Env var name with space-separated owner/repo slugs (preferred in CI)",
    )
    parser.add_argument(
        "--langs",
        type=str,
        default="",
        help="Comma-separated lang codes (default: all supported)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max repos to process in this run (0 = all)",
    )
    parser.add_argument(
        "--commit-every",
        type=int,
        default=0,
        help="Git commit+push every N successful repos (0 = no auto-commit; CI uses 1)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Re-translate even when target files already exist",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"Cursor CLI model id (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Print prompts but do not call the agent",
    )
    parser.add_argument(
        "--list-missing",
        action="store_true",
        default=False,
        help="Only scan and print repos missing translations, then exit",
    )
    args = parser.parse_args()

    if args.limit < 0:
        sys.exit("ERROR: --limit must be >= 0")
    if args.commit_every < 0:
        sys.exit("ERROR: --commit-every must be >= 0")

    langs = parse_lang_codes(args.langs)
    scan_work = list_missing_work(langs, force=args.force)
    print_scan_report(scan_work, langs)
    if args.list_missing:
        return

    if not args.dry_run:
        get_api_key()
    agent_bin = "agent" if args.dry_run else find_agent_bin()

    explicit_repos = args.repos is not None or bool(args.repos_env)
    if args.repos_env:
        pending_slugs = [parse_repo_slug(s) for s in slugs_from_env(args.repos_env)]
    elif args.repos is not None:
        pending_slugs = [parse_repo_slug(s) for s in args.repos]
    else:
        pending_slugs = [(o, r) for o, r, _ in scan_work]

    missing_en = [(o, r) for o, r in pending_slugs if not has_en(o, r)]
    if missing_en:
        print(f"WARNING: {len(missing_en)} repo(s) have no description_en.txt — skipping:")
        for o, r in missing_en[:20]:
            print(f"  - {o}/{r}")
        pending_slugs = [(o, r) for o, r in pending_slugs if has_en(o, r)]

    pending: list[tuple[str, str, list[str]]] = []
    for owner, repo in pending_slugs:
        need = missing_langs_for(owner, repo, langs, force=args.force)
        if need:
            pending.append((owner, repo, need))

    print(f"Model                : {args.model}")
    print(f"Force overwrite      : {args.force}")
    print(f"Pending repos        : {len(pending)}")
    if args.limit:
        pending = pending[: args.limit]
        print(f"Limited to           : {len(pending)}")

    if not pending:
        print("Nothing to do.")
        if explicit_repos and missing_en:
            sys.exit(
                "ERROR: requested repo(s) have no description_en.txt — "
                "nothing to translate."
            )
        return

    ok = fail = 0
    pending_commit: list[Path] = []
    kept_outputs: list[Path] = []
    repos_since_commit = 0
    push_branch = os.environ.get("GIT_PUSH_BRANCH", "main").strip() or "main"
    if args.commit_every:
        print(f"Commit every         : {args.commit_every} (branch={push_branch})")

    def flush_commits() -> None:
        nonlocal pending_commit, repos_since_commit, kept_outputs
        if pending_commit:
            committed = list(pending_commit)
            if not git_commit_and_push_translations(pending_commit, push_branch):
                sys.exit(1)
            pending_commit = []
            # Stop protecting already-pushed files from later agent side-effects.
            committed_set = set(committed)
            kept_outputs = [p for p in kept_outputs if p not in committed_set]
        repos_since_commit = 0

    for i, (owner, repo, need) in enumerate(pending, start=1):
        print(f"\n[{i}/{len(pending)}] {owner}/{repo} → {', '.join(need)}")
        prompt = build_prompt(owner, repo, need)
        before_hashes = (
            snapshot_lang_hashes(owner, repo, need)
            if args.force and not args.dry_run
            else {}
        )
        code = run_agent(agent_bin, args.model, prompt, args.dry_run)
        if args.dry_run:
            ok += 1
            continue
        wrote, bad = collect_results(
            owner, repo, need, force=args.force, before_hashes=before_hashes
        )
        wrote_paths = [lang_path(owner, repo, c) for c in wrote]
        if wrote_paths:
            kept_outputs.extend(wrote_paths)
        # Drop agent side-effects; keep this run's outputs (+ unpushed commit batch).
        discard_non_translations(pending_commit + kept_outputs)
        if wrote:
            for path in wrote_paths:
                print(f"  wrote {path.relative_to(ROOT_DIR)} ({path.stat().st_size} bytes)")
            if args.commit_every:
                pending_commit.extend(wrote_paths)
                repos_since_commit += 1
                if repos_since_commit >= args.commit_every:
                    flush_commits()
        if bad:
            print(f"  FAILED langs: {', '.join(bad)} (agent exit={code})")
            fail += 1
        else:
            if code != 0:
                print(f"  note: agent exit={code}, but all target files present — ok")
            ok += 1

    if args.commit_every and not args.dry_run:
        flush_commits()

    print(f"\nSummary: ok={ok} fail={fail}")
    if fail:
        sys.exit(1)
    if explicit_repos and missing_en:
        sys.exit(
            f"ERROR: {len(missing_en)} requested repo(s) had no description_en.txt — "
            "translations were incomplete."
        )


if __name__ == "__main__":
    main()
