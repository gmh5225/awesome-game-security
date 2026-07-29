#!/usr/bin/env python3
"""
Merge case-only duplicate description trees and remove the extra paths.

Prefers archive/{owner}/{repo}.txt casing for the canonical directory name and
keeps the longest non-empty blob among duplicates for each description file.
"""

from __future__ import annotations

import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from description_paths import canonical_repo_slug  # noqa: E402


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def tracked_description_paths() -> list[str]:
    proc = git("ls-files", "description/")
    proc.check_returncode()
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def blob_content(ref: str, path: str) -> str | None:
    show = git("show", f"{ref}:{path}")
    if show.returncode != 0:
        return None
    content = show.stdout
    if not content.strip():
        return None
    return content


def duplicate_repo_groups(
    paths: list[str],
) -> dict[tuple[str, str], dict[str, object]]:
    repos_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    files_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    owners_by_key: dict[tuple[str, str], str] = {}

    for path in paths:
        parts = path.split("/")
        if len(parts) < 4:
            continue
        owner, repo, rel = parts[1], parts[2], "/".join(parts[3:])
        key = (owner.lower(), repo.lower())
        repos_by_key[key].add(repo)
        files_by_key[key].add(rel)
        owners_by_key[key] = owner

    groups: dict[tuple[str, str], dict[str, object]] = {}
    for key, repo_names in repos_by_key.items():
        if len(repo_names) <= 1:
            continue
        groups[key] = {
            "owner": owners_by_key[key],
            "repo_names": sorted(repo_names),
            "rels": sorted(files_by_key[key]),
        }
    return groups


def clear_skip_worktree(paths: list[str]) -> None:
    for path in paths:
        git("update-index", "--no-skip-worktree", path)


def main() -> int:
    paths = tracked_description_paths()
    groups = duplicate_repo_groups(paths)
    if not groups:
        print("No case-only duplicate description repos found.")
        return 0

    to_unindex: list[str] = []
    to_write: dict[str, str] = {}

    for (_owner_lower, repo_lower), info in sorted(groups.items()):
        owner = str(info["owner"])
        repo_names = list(info["repo_names"])
        rel_files = list(info["rels"])
        canonical_owner, canonical_repo = canonical_repo_slug(owner, repo_lower)

        print(f"Fixing {owner}/{repo_lower} → {canonical_owner}/{canonical_repo}")
        for rel in rel_files:
            variants = [
                f"description/{owner}/{repo_name}/{rel}" for repo_name in repo_names
            ]
            candidates = [
                (blob_content("HEAD", path), path)
                for path in variants
                if blob_content("HEAD", path) is not None
            ]
            if not candidates:
                print(f"  skip empty {rel}")
                continue
            content, source = max(candidates, key=lambda item: len(item[0]))
            canonical_path = f"description/{canonical_owner}/{canonical_repo}/{rel}"
            to_write[canonical_path] = content
            print(
                f"  {rel}: kept {len(content)} chars from {source.split('/')[2]}"
            )
            for path in variants:
                if path != canonical_path:
                    to_unindex.append(path)

    if not to_write and not to_unindex:
        print("Nothing to change.")
        return 0

    all_touched = sorted(set(to_write) | set(to_unindex))
    clear_skip_worktree(all_touched)

    for path, content in sorted(to_write.items()):
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    for path in sorted(set(to_unindex)):
        print(f"  unindex {path}")
        git("rm", "--cached", "-f", "--", path)

    add_dirs = sorted({str(Path(path).parent) for path in to_write})
    git("add", "--", *add_dirs)

    remaining = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check-description-case-duplicates.py")],
        cwd=ROOT,
    )
    return remaining.returncode


if __name__ == "__main__":
    raise SystemExit(main())
