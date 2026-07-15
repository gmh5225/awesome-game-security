#!/usr/bin/env python3
"""
Generate English descriptions for archived repositories using the Cursor CLI.

For each archive/{owner}/{repo}.txt, the Cursor agent:
  1. Reads a bounded prefix of the local archive (README / tree / top sources)
  2. Summarizes what the repo does (3-5 sentences, plain English)
  3. Writes description/{owner}/{repo}/description_en.txt

Unlike generate-descriptions.py (Cloud Agents API), this drives the local
`agent` binary installed by https://cursor.com/install.

Prerequisites:
    curl https://cursor.com/install -fsS | bash
    export CURSOR_API_KEY=<your key from https://cursor.com/settings>
    # Max Mode (required for some models) — set in ~/.cursor/cli-config.json:
    #   {"version":1,"editor":{"vimMode":false},"permissions":{"allow":[],"deny":[]},"maxMode":true,"approvalMode":"unrestricted"}
    # and export CURSOR_CONFIG_DIR=$HOME/.cursor on GitHub Actions runners.

Usage:
    python scripts/generate-descriptions-cli.py                  # fill all missing
    python scripts/generate-descriptions-cli.py --list-missing   # scan only
    python scripts/generate-descriptions-cli.py --repos owner/repo other/repo
    DESC_REPOS="owner/repo" python scripts/generate-descriptions-cli.py --repos-env DESC_REPOS
    python scripts/generate-descriptions-cli.py --limit 5
    python scripts/generate-descriptions-cli.py --model cursor-grok-4.5-high-fast
    python scripts/generate-descriptions-cli.py --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT_DIR / "archive"
DESC_DIR = ROOT_DIR / "description"

DEFAULT_MODEL = "cursor-grok-4.5-high-fast"
# Archives can be tens of MB; only ask the agent to read a bounded prefix.
ARCHIVE_READ_BYTES = 200_000
AGENT_TIMEOUT_SEC = 600
# GitHub owner/repo character set (reject shell metacharacters early).
REPO_SLUG_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$")


def get_api_key() -> str:
    key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not key:
        sys.exit(
            "ERROR: CURSOR_API_KEY environment variable is not set.\n"
            "Obtain a key from https://cursor.com/settings"
        )
    return key


def find_agent_bin() -> str:
    # Prefer the Cursor install path so a differently named `agent` on PATH
    # (e.g. Grok's `agent`, unrelated CLIs) cannot shadow the intended binary.
    home_bin = Path.home() / ".cursor" / "bin" / "agent"
    if home_bin.is_file():
        return str(home_bin)
    # Prefer cursor-agent before bare `agent` — many machines have a non-Cursor
    # `agent` earlier on PATH.
    for name in ("cursor-agent", "agent"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit(
        "ERROR: Cursor CLI `agent` not found on PATH.\n"
        "Install with: curl https://cursor.com/install -fsS | bash"
    )


def list_archived_repos() -> list[tuple[str, str]]:
    repos: list[tuple[str, str]] = []
    if not ARCHIVE_DIR.is_dir():
        return repos
    for owner_dir in sorted(ARCHIVE_DIR.iterdir()):
        if not owner_dir.is_dir():
            continue
        for txt in sorted(owner_dir.glob("*.txt")):
            repos.append((owner_dir.name, txt.stem))
    return repos


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
    """Read space/newline-separated owner/repo slugs from an env var (CI-safe)."""
    raw = os.environ.get(var_name, "")
    return [tok for tok in raw.replace("\n", " ").split(" ") if tok]


def needs_description(owner: str, repo: str) -> bool:
    # Treat missing OR empty files as needing work (failed runs may leave 0-byte stubs).
    path = DESC_DIR / owner / repo / "description_en.txt"
    return not (path.is_file() and path.stat().st_size > 0)


def archive_exists(owner: str, repo: str) -> bool:
    return (ARCHIVE_DIR / owner / f"{repo}.txt").is_file()


def list_missing_descriptions() -> list[tuple[str, str]]:
    """Archives that exist but have no description_en.txt yet."""
    return [(o, r) for o, r in list_archived_repos() if needs_description(o, r)]


def print_scan_report(missing: list[tuple[str, str]]) -> None:
    archived = list_archived_repos()
    print(f"Scan archive/ vs description/")
    print(f"  archived repos      : {len(archived)}")
    print(f"  missing descriptions: {len(missing)}")
    # Machine-readable line for GitHub Actions (must stay exact).
    print(f"MISSING_COUNT={len(missing)}")
    if missing:
        preview = missing if len(missing) <= 50 else missing[:50]
        for owner, repo in preview:
            print(f"  - {owner}/{repo}")
        if len(missing) > 50:
            print(f"  ... and {len(missing) - 50} more")


def build_prompt(owner: str, repo: str) -> str:
    archive_rel = f"archive/{owner}/{repo}.txt"
    output_rel = f"description/{owner}/{repo}/description_en.txt"
    return f"""\
You are summarizing one archived GitHub repository for the awesome-game-security curated list.

Repository: {owner}/{repo}
Archive file: {archive_rel}
Output file: {output_rel}

Follow these steps exactly:

1. Read ONLY the first {ARCHIVE_READ_BYTES} bytes of the archive file
   (e.g. `head -c {ARCHIVE_READ_BYTES} {archive_rel}`). Do NOT load the whole file.
2. From that prefix, identify:
   - What the project is / does
   - Primary programming language(s)
   - Key features, techniques, or tools
   - Target audience / use case (game security, anti-cheat, reverse engineering, etc.)
3. Create parent directories if needed (`mkdir -p description/{owner}/{repo}`).
4. Write a plain-English description of 3–5 sentences to {output_rel}:
   - Plain text only (no markdown, no headers, no bullet points)
   - First sentence: what the project is / does
   - Remaining sentences: key features, technologies, and primary use case
   - Do NOT include the repo URL or owner/repo slug in the text
5. If the archive is missing or empty after the read, write a single line:
   No archive available.

Hard constraints:
- ONLY modify/create {output_rel}
- Do NOT run git, gh, push, commit, or touch any other paths
- When finished, print one line: Done: {owner}/{repo}
"""


def run_agent(
    agent_bin: str,
    model: str,
    prompt: str,
    dry_run: bool,
) -> int:
    # Headless CI: --trust skips the workspace-trust prompt (otherwise hangs until
    # timeout). --force + cli-config approvalMode=unrestricted allow writes.
    # See https://cursor.com/docs/cli/reference/parameters
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
        print(prompt[:500])
        print("---")
        return 0

    print(f"  $ {agent_bin} -p --force --trust --sandbox disabled --model {model} ...")
    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT_DIR,
            env=os.environ.copy(),
            timeout=AGENT_TIMEOUT_SEC,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT after {AGENT_TIMEOUT_SEC}s")
        return 124

    elapsed = time.time() - started
    print(f"  exit={proc.returncode}  elapsed={elapsed:.1f}s")
    # Older CLI builds may reject --trust as an unknown option (instant fail).
    # Retry once without it; real agent work is never <2s.
    if proc.returncode != 0 and "--trust" in cmd and elapsed < 2.0:
        print("  retrying without --trust (possible older CLI) ...")
        cmd_no_trust = [c for c in cmd if c != "--trust"]
        try:
            proc = subprocess.run(
                cmd_no_trust,
                cwd=ROOT_DIR,
                env=os.environ.copy(),
                timeout=AGENT_TIMEOUT_SEC,
                check=False,
            )
        except subprocess.TimeoutExpired:
            print(f"  TIMEOUT after {AGENT_TIMEOUT_SEC}s")
            return 124
        elapsed2 = time.time() - started
        print(f"  exit={proc.returncode}  elapsed={elapsed2:.1f}s (no --trust)")
    return proc.returncode


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate repo descriptions via Cursor CLI (agent)"
    )
    parser.add_argument(
        "--repos",
        nargs="*",
        default=None,
        help="Only process these owner/repo slugs (default: all missing)",
    )
    parser.add_argument(
        "--repos-env",
        type=str,
        default="",
        help="Env var name with space-separated owner/repo slugs (preferred in CI)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max repos to process in this run (0 = all)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip repos that already have description_en.txt (default: on)",
    )
    parser.add_argument(
        "--no-skip-existing",
        dest="skip_existing",
        action="store_false",
        help="Re-generate descriptions even if they exist",
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
        help="Only scan archive/ vs description/ and print missing repos, then exit",
    )
    args = parser.parse_args()

    if args.limit < 0:
        sys.exit("ERROR: --limit must be >= 0")

    # Default path (no --repos / --repos-env): fill every archive that lacks a description.
    scan_missing = list_missing_descriptions()
    print_scan_report(scan_missing)
    if args.list_missing:
        return

    if not args.dry_run:
        get_api_key()  # fail fast if missing
    agent_bin = "agent" if args.dry_run else find_agent_bin()

    # Explicit repo list (CLI args or CI env) must NOT fall back to "all missing".
    # Empty --repos / empty env ⇒ nothing to do (avoids accidental full backfill).
    explicit_repos = args.repos is not None or bool(args.repos_env)
    if args.repos_env:
        pending = [parse_repo_slug(s) for s in slugs_from_env(args.repos_env)]
    elif args.repos is not None:
        pending = [parse_repo_slug(s) for s in args.repos]
    else:
        # Manual / backfill default: only repos present in archive/ but not description/
        pending = list(scan_missing) if args.skip_existing else list_archived_repos()

    missing_archive = [(o, r) for o, r in pending if not archive_exists(o, r)]
    if missing_archive:
        print(f"WARNING: {len(missing_archive)} repo(s) have no archive yet — skipping them:")
        for o, r in missing_archive[:20]:
            print(f"  - {o}/{r}")
        pending = [(o, r) for o, r in pending if archive_exists(o, r)]

    if explicit_repos and args.skip_existing:
        pending = [(o, r) for o, r in pending if needs_description(o, r)]

    print(f"Model                : {args.model}")
    print(f"Pending descriptions : {len(pending)}")
    if args.limit:
        pending = pending[: args.limit]
        print(f"Limited to           : {len(pending)}")

    if not pending:
        print("Nothing to do.")
        # Explicit CI lists must not silently succeed when archives never landed
        # (archive-repos.py exits 0 even if every repo failed).
        if explicit_repos and missing_archive:
            sys.exit(
                "ERROR: requested repo(s) have no archive on disk — "
                "nothing to describe. Check the archive job logs."
            )
        return

    ok = fail = 0
    for i, (owner, repo) in enumerate(pending, start=1):
        print(f"\n[{i}/{len(pending)}] {owner}/{repo}")
        prompt = build_prompt(owner, repo)
        code = run_agent(agent_bin, args.model, prompt, args.dry_run)
        out = DESC_DIR / owner / repo / "description_en.txt"
        if args.dry_run:
            ok += 1
            continue
        # Prefer the artifact: agent may write the file then exit non-zero.
        if out.is_file() and out.stat().st_size > 0:
            print(f"  wrote {out.relative_to(ROOT_DIR)} ({out.stat().st_size} bytes)")
            if code != 0:
                print(f"  note: agent exit={code}, but description file is present — counting as ok")
            ok += 1
        else:
            print(f"  FAILED (exit={code}, exists={out.is_file()})")
            # Remove empty stubs so the next run still sees this repo as missing.
            if out.is_file() and out.stat().st_size == 0:
                out.unlink()
                print(f"  removed empty stub {out.relative_to(ROOT_DIR)}")
            fail += 1

    print(f"\nSummary: ok={ok} fail={fail}")
    if fail:
        sys.exit(1)
    # Partial archive loss on an explicit list: still fail so CI is red.
    if explicit_repos and missing_archive:
        sys.exit(
            f"ERROR: {len(missing_archive)} requested repo(s) had no archive — "
            "descriptions were incomplete."
        )


if __name__ == "__main__":
    main()
