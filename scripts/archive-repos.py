#!/usr/bin/env python3
"""
Clone every GitHub repository listed in README.md, run code2prompt on each,
and save the output as archive/{owner}/{repo}.txt.

Prerequisites:
    cargo install code2prompt

Usage:
    python scripts/archive-repos.py                        # archive all new repos
    python scripts/archive-repos.py --commit-every 5       # commit to git every 5 archives
    python scripts/archive-repos.py --workers 4            # control parallelism
    python scripts/archive-repos.py --no-skip-existing     # re-archive everything
    python scripts/archive-repos.py --owner-filter gmh5225 # only one owner
    python scripts/archive-repos.py --limit 10 --dry-run   # preview first 10
"""

import os
import re
import time
import shutil
import argparse
import tempfile
import threading
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

README_PATH = "README.md"
ARCHIVE_DIR = "archive"
GITHUB_REPO_PATTERN = re.compile(
    r"https://github\.com/([^/\s\)\]>\"']+)/([^/\s\)\]>\"'#]+)"
)
MAX_WORKERS = 3
CLONE_TIMEOUT = 300       # seconds — large game trees need longer clones
CODE2PROMPT_TIMEOUT = 180 # seconds — abandon huge repos after a few minutes
MAX_FILE_MB = 95          # GitHub hard-rejects files > 100 MB; keep safely below

# Binary / large-asset extensions excluded from code2prompt output.
# Keeps archive files focused on source code and avoids TOOLARGE rejections
# on game repos that embed audio, textures, models, datasets, or compiled binaries.
CODE2PROMPT_EXCLUDE = ",".join([
    # Audio / video
    "*.wav", "*.mp3", "*.ogg", "*.flac", "*.aac", "*.wma", "*.m4a",
    "*.mp4", "*.avi", "*.mov", "*.mkv", "*.webm",
    # Images / textures
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.tga", "*.tiff",
    "*.webp", "*.ico", "*.psd", "*.hdr", "*.exr", "*.dds", "*.ktx",
    # 3-D assets
    "*.fbx", "*.obj", "*.3ds", "*.blend", "*.dae", "*.glb", "*.gltf",
    "*.uasset", "*.umap", "*.pak",
    # Compiled / binary
    "*.lib", "*.dll", "*.exe", "*.so", "*.dylib", "*.a", "*.o",
    "*.pdb", "*.ilk", "*.exp",
    # Archives & disk images
    "*.zip", "*.tar", "*.gz", "*.7z", "*.rar", "*.xz", "*.txz",
    "*.iso", "*.img", "*.bin",
    # ML model weights / datasets
    "*.pth", "*.ckpt", "*.pt", "*.model", "*.weights",
    "*.h5", "*.pb", "*.onnx", "*.npy", "*.npz", "*.parquet", "*.arrow",
    # Documents
    "*.pdf", "*.doc", "*.docx", "*.xls", "*.xlsx", "*.ppt", "*.pptx",
    # Fonts
    "*.ttf", "*.otf", "*.woff", "*.woff2",
    # Misc large data
    "*.db", "*.sqlite", "*.sqlite3", "*.csv",
])

SCAN_START_MARKER = "## Game Engine"

# ---------------------------------------------------------------------------
# Fallback: fetch repo content via content extraction API when clone/code2prompt fails.
# API endpoint is configurable via REPO_SNAPSHOT_HOST (set as a GitHub Actions secret).
# ---------------------------------------------------------------------------
import json as _json

_SNAPSHOT_API = os.environ.get("REPO_SNAPSHOT_HOST", "").strip()

# Binary/asset patterns to exclude when calling the extraction API
_SNAPSHOT_EXCLUDE = ",".join([
    "*.wav", "*.mp3", "*.ogg", "*.flac", "*.aac",
    "*.mp4", "*.avi", "*.mov", "*.mkv", "*.webm",
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.tga", "*.tiff",
    "*.webp", "*.ico", "*.psd", "*.hdr", "*.exr", "*.dds", "*.ktx",
    "*.fbx", "*.obj", "*.3ds", "*.blend", "*.dae", "*.glb", "*.gltf",
    "*.uasset", "*.umap", "*.pak",
    "*.lib", "*.dll", "*.exe", "*.so", "*.dylib", "*.a", "*.o",
    "*.zip", "*.tar", "*.gz", "*.7z", "*.rar", "*.xz", "*.txz",
    "*.iso", "*.img", "*.bin",
    "*.pth", "*.ckpt", "*.pt", "*.model", "*.weights",
    "*.h5", "*.pb", "*.onnx", "*.npy", "*.npz",
    "*.pdf", "*.doc", "*.docx", "*.xls", "*.xlsx",
    "*.ttf", "*.otf", "*.woff", "*.woff2",
    "*.db", "*.sqlite", "*.sqlite3",
])


def _fetch_via_snapshot(owner: str, repo: str) -> tuple[bool, str]:
    """Fetch repo content via the content extraction API.

    Returns (success, content_or_reason).
    """
    if not _SNAPSHOT_API:
        return False, "REPO_SNAPSHOT_HOST not configured"

    repo_url = f"https://github.com/{owner}/{repo}"
    payload = _json.dumps({
        "input_text": repo_url,
        "max_file_size": "243",   # KB — keeps output manageable
        "pattern_type": "exclude",
        "pattern": _SNAPSHOT_EXCLUDE,
    }).encode()

    try:
        req = urllib.request.Request(
            _SNAPSHOT_API,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (compatible; archive-bot/1.0)",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = _json.loads(resp.read().decode("utf-8", errors="replace"))
        tree    = result.get("tree", "")
        content = result.get("content", "")
        if not tree and not content:
            return False, "extraction service returned empty tree and content"
        return True, f"{tree}\n\n{content}".strip()
    except Exception as exc:
        return False, f"extraction service failed: {exc}"


def extract_github_repos(text: str) -> list[tuple[str, str]]:
    """Return unique (owner, repo) pairs from README, starting at SCAN_START_MARKER."""
    marker_pos = text.find(SCAN_START_MARKER)
    if marker_pos == -1:
        print(f"[WARN] Marker '{SCAN_START_MARKER}' not found — scanning full README.")
    else:
        text = text[marker_pos:]

    matches = GITHUB_REPO_PATTERN.findall(text)
    seen: set[tuple[str, str]] = set()
    result = []
    for owner, repo in matches:
        repo = repo.rstrip(".,;:")
        if owner == "gmh5225" and repo == "awesome-game-security":
            continue
        key = (owner.lower(), repo.lower())
        if key not in seen:
            seen.add(key)
            result.append((owner, repo))
    return result


def check_code2prompt() -> bool:
    return shutil.which("code2prompt") is not None


def install_code2prompt() -> bool:
    print("code2prompt not found — installing via cargo ...")
    try:
        subprocess.run(["cargo", "install", "code2prompt"], check=True, timeout=300)
        return True
    except Exception as e:
        print(f"  [ERROR] Install failed: {e}")
        return False


def _cleanup_oversized(archive_dir: Path) -> None:
    """Delete archive files that exceed GitHub's hard limit from the working tree."""
    limit = GITHUB_HARD_LIMIT_MB * 1024 * 1024
    for f in archive_dir.rglob("*.txt"):
        try:
            if f.stat().st_size > limit:
                print(f"  [GIT] Removed oversized file: {f.name} "
                      f"({f.stat().st_size / 1024 / 1024:.1f} MB)")
                f.unlink()
        except OSError:
            pass


def git_commit_and_push(archive_dir: Path, count: int, push_retries: int = 5) -> None:
    """Stage archive dir and push a commit. Called with the commit lock held.

    If the push is rejected because the remote moved ahead (concurrent pushes),
    pull --rebase and retry up to push_retries times.
    """
    try:
        subprocess.run(["git", "add", str(archive_dir)], check=True, capture_output=True)
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            capture_output=True,
        )
        if result.returncode == 0:
            return  # nothing staged

        subprocess.run(
            ["git", "commit", "-m",
             f"archive: add {count} repo prompt(s) [skip ci]"],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"  [GIT ERROR] commit: {e.stderr.decode().strip()[:200] if e.stderr else e}")
        return

    for attempt in range(1, push_retries + 1):
        try:
            subprocess.run(["git", "push"], check=True, capture_output=True)
            print(f"  [GIT] Committed and pushed {count} archive(s)")
            return
        except subprocess.CalledProcessError as e:
            err = e.stderr.decode().strip() if e.stderr else str(e)

            # File too large for GitHub (LFS rejection) — undo this commit
            # and delete oversized files so they don't pollute future commits.
            if any(k in err for k in ("gh.io/lfs", "large files",
                                      "exceeds GitHub's file size limit")):
                print(f"  [GIT] Push blocked by large file — undoing commit")
                subprocess.run(["git", "reset", "HEAD~1"], capture_output=True)
                _cleanup_oversized(archive_dir)
                return

            if attempt >= push_retries:
                print(f"  [GIT ERROR] push failed after {push_retries} retries: {err[:200]}")
                subprocess.run(["git", "reset", "HEAD~1"], capture_output=True)
                return

            # Remote moved ahead (conflict) — rebase then retry
            if any(k in err for k in ("rejected", "fetch first", "non-fast-forward")):
                print(f"  [GIT] Push rejected (attempt {attempt}/{push_retries}), rebasing ...")
                try:
                    subprocess.run(
                        ["git", "pull", "--rebase", "origin", "main"],
                        check=True, capture_output=True,
                    )
                except subprocess.CalledProcessError as re_err:
                    re_msg = re_err.stderr.decode().strip()[:200] if re_err.stderr else str(re_err)
                    print(f"  [GIT ERROR] rebase failed: {re_msg}")
                    subprocess.run(["git", "rebase", "--abort"], capture_output=True)
                    subprocess.run(["git", "reset", "HEAD~1"], capture_output=True)
                    return

            # Network / timeout error (408, RPC failure, disconnect) — just retry
            elif any(k in err for k in ("408", "RPC failed", "unexpected disconnect",
                                        "remote end hung up", "timed out")):
                wait = 5 * attempt
                print(f"  [GIT] Push timeout (attempt {attempt}/{push_retries}), "
                      f"retrying in {wait}s ...")
                time.sleep(wait)

            else:
                print(f"  [GIT ERROR] push: {err[:200]}")
                subprocess.run(["git", "reset", "HEAD~1"], capture_output=True)
                return

    print(f"  [GIT ERROR] push failed after {push_retries} retries — giving up")
    subprocess.run(["git", "reset", "HEAD~1"], capture_output=True)


GITHUB_HARD_LIMIT_MB = 90   # Stay well below GitHub's 100 MB hard rejection


def _write_snapshot(out_dir: Path, out_file: Path, content: str) -> tuple[bool, float]:
    """Write snapshot content to disk if it's small enough for GitHub.

    Returns (written, size_kb).
    """
    size_bytes = len(content.encode("utf-8"))
    size_mb = size_bytes / 1024 / 1024
    if size_mb > GITHUB_HARD_LIMIT_MB:
        return False, size_mb
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file.write_text(content, encoding="utf-8")
    return True, size_bytes / 1024


def archive_repo(
    owner: str,
    repo: str,
    archive_dir: Path,
    skip_existing: bool,
) -> tuple[str, str, str]:
    """
    Clone owner/repo, run code2prompt, write to archive.
    Returns (slug, status, message).
    status: OK | SKIP | FAIL | TIMEOUT | TOOLARGE
    """
    slug = f"{owner}/{repo}"
    out_dir = archive_dir / owner
    out_file = out_dir / f"{repo}.txt"

    if skip_existing and out_file.exists():
        return (slug, "SKIP", "")

    clone_url = f"https://github.com/{owner}/{repo}.git"
    tmp_dir = tempfile.mkdtemp(prefix=f"arc_{owner}_{repo}_")

    # Skip LFS pointer downloads entirely — we only need source text.
    clone_env = {"GIT_LFS_SKIP_SMUDGE": "1", **__import__("os").environ}

    try:
        # First attempt: with blob size filter (faster, skips large files)
        r = subprocess.run(
            ["git", "clone", "--depth", "1", "--single-branch", "--quiet",
             "--filter=blob:limit:20m",
             clone_url, tmp_dir],
            capture_output=True, text=True, timeout=CLONE_TIMEOUT,
            env=clone_env,
        )
        # Some remotes/locales reject the filter-spec (e.g. Traditional Chinese
        # "無效的過濾器規格"). Always retry once without the filter on failure.
        if r.returncode != 0:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            tmp_dir = tempfile.mkdtemp(prefix=f"arc_{owner}_{repo}_")
            r = subprocess.run(
                ["git", "clone", "--depth", "1", "--single-branch", "--quiet",
                 clone_url, tmp_dir],
                capture_output=True, text=True, timeout=CLONE_TIMEOUT,
                env=clone_env,
            )
        if r.returncode != 0:
            clone_err = r.stderr.strip()[:200]
            ok, content = _fetch_via_snapshot(owner, repo)
            if ok:
                written, size = _write_snapshot(out_dir, out_file, content)
                if written:
                    return (slug, "OK", f"{size:.1f} KB [snapshot]")
                return (slug, "TOOLARGE", f"snapshot {size:.1f} MB still too large")
            return (slug, "FAIL", f"clone: {clone_err}; snapshot: {content}")

        out_dir.mkdir(parents=True, exist_ok=True)
        cp = subprocess.run(
            ["code2prompt",
             "--output-file", str(out_file),
             "--exclude", CODE2PROMPT_EXCLUDE,
             tmp_dir],
            capture_output=True, text=True, timeout=CODE2PROMPT_TIMEOUT,
        )
        if cp.returncode != 0:
            cp_err = cp.stderr.strip()[:200]
            ok, content = _fetch_via_snapshot(owner, repo)
            if ok:
                written, size = _write_snapshot(out_dir, out_file, content)
                if written:
                    return (slug, "OK", f"{size:.1f} KB [snapshot]")
                return (slug, "TOOLARGE", f"snapshot {size:.1f} MB still too large")
            return (slug, "FAIL", f"code2prompt: {cp_err}; snapshot: {content}")

        size_bytes = out_file.stat().st_size
        size_mb = size_bytes / 1024 / 1024
        if size_mb > MAX_FILE_MB:
            # Prefer a truncated local archive over dropping the repo entirely
            # when the snapshot API is unavailable or also too large.
            ok, content = _fetch_via_snapshot(owner, repo)
            if ok:
                written, size = _write_snapshot(out_dir, out_file, content)
                if written:
                    return (slug, "OK", f"{size:.1f} KB [snapshot, was {size_mb:.1f} MB]")
            # Truncate code2prompt output to fit GitHub's hard limit.
            max_bytes = int(MAX_FILE_MB * 1024 * 1024 * 0.98)
            raw = out_file.read_bytes()[:max_bytes]
            truncated = raw.decode("utf-8", errors="ignore").rstrip()
            truncated += (
                "\n\n[TRUNCATED: full code2prompt output was "
                f"{size_mb:.1f} MB; kept first {MAX_FILE_MB} MB for GitHub limits]\n"
            )
            out_file.write_text(truncated, encoding="utf-8")
            kept_kb = out_file.stat().st_size / 1024
            return (slug, "OK", f"{kept_kb:.1f} KB [truncated from {size_mb:.1f} MB]")

        return (slug, "OK", f"{size_bytes / 1024:.1f} KB")

    except subprocess.TimeoutExpired:
        # Prefer a lightweight tree+source archive over leaving a gap.
        light = _archive_lightweight(owner, repo, out_dir, out_file, tmp_dir if Path(tmp_dir).exists() else None)
        if light[0] == "OK":
            return light
        ok, content = _fetch_via_snapshot(owner, repo)
        if ok:
            written, size = _write_snapshot(out_dir, out_file, content)
            if written:
                return (slug, "OK", f"{size:.1f} KB [snapshot, after timeout]")
            return (slug, "TOOLARGE", f"snapshot {size:.1f} MB still too large after timeout")
        return (slug, "TIMEOUT", light[2] if light[0] != "OK" else "exceeded timeout")
    except Exception as e:
        return (slug, "ERROR", str(e))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def _archive_lightweight(
    owner: str,
    repo: str,
    out_dir: Path,
    out_file: Path,
    existing_clone: Path | None,
) -> tuple[str, str, str]:
    """Build a size-capped tree + source archive when code2prompt times out."""
    slug = f"{owner}/{repo}"
    max_bytes = int(MAX_FILE_MB * 1024 * 1024 * 0.95)
    max_single = 256 * 1024
    code_exts = {
        ".c", ".cc", ".cpp", ".cxx", ".h", ".hpp", ".hh", ".cs", ".java", ".kt",
        ".go", ".rs", ".py", ".js", ".ts", ".tsx", ".jsx", ".lua", ".gd", ".swift",
        ".m", ".mm", ".sh", ".ps1", ".cmake", ".md", ".txt", ".json", ".yml",
        ".yaml", ".toml", ".ini", ".cfg", ".xml", ".sln", ".vcxproj", ".gradle",
        ".mk", ".bat", ".cmd", ".sv", ".v", ".asm", ".s", ".idl", ".proto",
    }
    skip_dir = {".git", "node_modules", ".vs", "bin", "obj", "__pycache__", ".idea"}

    tmp_owned = False
    root = existing_clone
    try:
        if root is None or not Path(root).exists():
            root = Path(tempfile.mkdtemp(prefix=f"lw_{owner}_{repo}_"))
            tmp_owned = True
            clone_env = {"GIT_LFS_SKIP_SMUDGE": "1", **os.environ}
            r = subprocess.run(
                ["git", "clone", "--depth", "1", "--single-branch", "--quiet",
                 f"https://github.com/{owner}/{repo}.git", str(root)],
                capture_output=True, text=True, timeout=CLONE_TIMEOUT, env=clone_env,
            )
            if r.returncode != 0:
                return (slug, "FAIL", f"lightweight clone: {(r.stderr or '')[:200]}")

        root = Path(root)
        lines = [f"Project Path: {owner}/{repo}", "", "Source Tree:", "", "```txt", root.name]
        count = 0
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(
                d for d in dirnames if d not in skip_dir and not d.startswith(".")
            )
            rel = Path(dirpath).relative_to(root)
            depth = 0 if str(rel) == "." else len(rel.parts)
            indent = "│   " * depth
            for name in dirnames:
                lines.append(f"{indent}├── {name}/")
                count += 1
                if count >= 4000:
                    lines.append(f"{indent}└── ... [tree truncated]")
                    break
            if count >= 4000:
                break
            for name in sorted(filenames):
                if name.startswith("."):
                    continue
                lines.append(f"{indent}├── {name}")
                count += 1
                if count >= 4000:
                    lines.append(f"{indent}└── ... [tree truncated]")
                    break
            if count >= 4000:
                break
        lines.append("```")
        lines.append("")

        prefer: list[Path] = []
        other: list[Path] = []
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if any(part in skip_dir or part.startswith(".") for part in p.relative_to(root).parts[:-1]):
                continue
            low = p.name.lower()
            if low.startswith("readme") or low in {"license", "license.md", "copying"}:
                prefer.append(p)
            elif p.suffix.lower() in code_exts:
                other.append(p)
        other.sort(key=lambda p: (len(p.relative_to(root).parts), str(p).lower()))

        used = len("\n".join(lines).encode("utf-8"))
        included = 0
        for p in prefer + other:
            try:
                raw = p.read_bytes()
            except OSError:
                continue
            body = raw[:max_single].decode("utf-8", errors="replace")
            note = ""
            if len(raw) > max_single:
                note = f"\n\n[... truncated file; original {len(raw)} bytes ...]\n"
            block = f"`{p.relative_to(root)}`:\n\n```\n{body}{note}\n```\n"
            encoded = block.encode("utf-8")
            if used + len(encoded) > max_bytes:
                lines.append("\n[STOPPED: reached archive size budget]\n")
                break
            lines.append(block)
            used += len(encoded)
            included += 1

        out_dir.mkdir(parents=True, exist_ok=True)
        out_file.write_text("\n".join(lines), encoding="utf-8")
        size_kb = out_file.stat().st_size / 1024
        return (slug, "OK", f"{size_kb:.1f} KB [lightweight, {included} files]")
    except Exception as exc:
        return (slug, "FAIL", f"lightweight: {exc}")
    finally:
        if tmp_owned and root is not None:
            shutil.rmtree(root, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Archive GitHub repos from README.md as code2prompt text files."
    )
    parser.add_argument("--readme", default=README_PATH)
    parser.add_argument("--archive-dir", default=ARCHIVE_DIR)
    parser.add_argument("--workers", type=int, default=MAX_WORKERS)
    parser.add_argument("--skip-existing", action="store_true", default=True)
    parser.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--owner-filter", default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument(
        "--commit-every",
        type=int,
        default=0,
        metavar="N",
        help="Commit and push to git after every N successful archives (0 = disabled)",
    )
    parser.add_argument(
        "--repos",
        nargs="+",
        metavar="OWNER/REPO",
        help="Archive only these specific repos (e.g. --repos torvalds/linux foo/bar). "
             "Skips README scanning entirely.",
    )
    args = parser.parse_args()

    # ── preflight ─────────────────────────────────────────────────────────────
    if not args.dry_run:
        if not check_code2prompt():
            if not install_code2prompt():
                raise SystemExit("Abort: code2prompt is required.")
        print(f"code2prompt: {shutil.which('code2prompt')}")

    # ── resolve repo list ─────────────────────────────────────────────────────
    if args.repos:
        # Explicit list supplied — skip README scanning
        repos = []
        for slug in args.repos:
            parts = slug.strip().split("/")
            if len(parts) == 2:
                repos.append((parts[0], parts[1]))
            else:
                print(f"[WARN] Ignoring invalid repo slug: {slug!r}")
    else:
        # Default: scan README
        with open(args.readme, encoding="utf-8") as f:
            repos = extract_github_repos(f.read())

    if args.owner_filter:
        repos = [(o, r) for o, r in repos if o.lower() == args.owner_filter.lower()]

    archive_dir = Path(args.archive_dir)
    archive_dir.mkdir(exist_ok=True)

    # Filter out already-archived repos BEFORE applying --limit so that
    # "--limit N" means "process N repos that still need archiving".
    if args.skip_existing:
        pending = [(o, r) for o, r in repos
                   if not (archive_dir / o / f"{r}.txt").exists()]
        skipped_upfront = len(repos) - len(pending)
        if skipped_upfront:
            print(f"Already archived    : {skipped_upfront} (skipped)")
        repos = pending

    if args.limit:
        repos = repos[: args.limit]

    print(f"Repos to process: {len(repos)}  →  {archive_dir}/")

    if args.dry_run:
        for owner, repo in repos:
            # After pre-filtering, everything here is either TODO or re-archive
            flag = "TODO" if args.skip_existing else (
                "SKIP" if (archive_dir / owner / f"{repo}.txt").exists() else "TODO"
            )
            print(f"  [{flag}] {owner}/{repo}")
        return

    # ── archive with optional periodic git commits ────────────────────────────
    counters = {"ok": 0, "fail": 0, "skip": 0, "timeout": 0, "toolarge": 0}
    since_last_commit = 0            # OK archives since last commit
    commit_lock = threading.Lock()   # serialise git operations

    def on_ok(slug: str, msg: str, done: int, total: int) -> None:
        nonlocal since_last_commit
        counters["ok"] += 1
        since_last_commit += 1
        print(f"  [OK    {done:4d}/{total}] {slug}  ({msg})")
        if args.commit_every and since_last_commit >= args.commit_every:
            with commit_lock:
                batch = since_last_commit
                since_last_commit = 0
            git_commit_and_push(archive_dir, batch)

    total = len(repos)
    done = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                archive_repo, owner, repo, archive_dir, args.skip_existing
            ): (owner, repo)
            for owner, repo in repos
        }
        for future in as_completed(futures):
            slug, status, msg = future.result()
            done += 1
            if status == "OK":
                on_ok(slug, msg, done, total)
            elif status == "SKIP":
                counters["skip"] += 1
            elif status == "TIMEOUT":
                counters["timeout"] += 1
                print(f"  [TIME  {done:4d}/{total}] {slug}")
            elif status == "TOOLARGE":
                counters["toolarge"] += 1
                print(f"  [BIG   {done:4d}/{total}] {slug}  {msg}")
            else:
                counters["fail"] += 1
                print(f"  [FAIL  {done:4d}/{total}] {slug}  {msg}")

    # ── final commit for any remaining uncommitted archives ───────────────────
    if args.commit_every and since_last_commit > 0:
        with commit_lock:
            git_commit_and_push(archive_dir, since_last_commit)

    print(
        f"\nDone.  OK={counters['ok']}  SKIP={counters['skip']}  "
        f"TIMEOUT={counters['timeout']}  TOOLARGE={counters['toolarge']}  "
        f"FAIL={counters['fail']}  (total={total})"
    )


if __name__ == "__main__":
    main()
