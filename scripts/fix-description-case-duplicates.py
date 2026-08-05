#!/usr/bin/env python3
"""
Merge case-only duplicate description/archive trees and remove extra paths.

Uses description_paths.canonical_repo_slug (prefers existing description/
casing, then largest archive file) and keeps the longest non-empty blob among
duplicates for each file.
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


def tracked_paths(prefix: str) -> list[str]:
    proc = git("ls-files", f"{prefix}/")
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
    prefix: str,
) -> dict[tuple[str, str], dict[str, object]]:
    repos_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    owners_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    files_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)

    for path in paths:
        parts = path.split("/")
        if len(parts) < 3:
            continue
        owner = parts[1]
        if prefix == "archive":
            repo = Path(parts[2]).stem
            rel = ""
        else:
            if len(parts) < 4:
                continue
            repo = parts[2]
            rel = "/".join(parts[3:])
        key = (owner.lower(), repo.lower())
        repos_by_key[key].add(repo)
        owners_by_key[key].add(owner)
        if rel:
            files_by_key[key].add(rel)

    groups: dict[tuple[str, str], dict[str, object]] = {}
    for key, repo_names in repos_by_key.items():
        owner_names = owners_by_key[key]
        if len(repo_names) <= 1 and len(owner_names) <= 1:
            continue
        groups[key] = {
            "owner_names": sorted(owner_names),
            "repo_names": sorted(repo_names),
            "rels": sorted(files_by_key[key]) if files_by_key[key] else [""],
            "prefix": prefix,
        }
    return groups


def clear_skip_worktree(paths: list[str]) -> None:
    for path in paths:
        git("update-index", "--no-skip-worktree", path)


def fix_tree(prefix: str) -> tuple[list[str], dict[str, str]]:
    paths = tracked_paths(prefix)
    groups = duplicate_repo_groups(paths, prefix)
    to_unindex: list[str] = []
    to_write: dict[str, str] = {}

    for (_owner_lower, repo_lower), info in sorted(groups.items()):
        owner_names = list(info["owner_names"])
        repo_names = list(info["repo_names"])
        rel_files = list(info["rels"])
        sample_owner = owner_names[0]
        canonical_owner, canonical_repo = canonical_repo_slug(
            sample_owner, repo_lower
        )

        print(f"Fixing {prefix}/{sample_owner}/{repo_lower} → {canonical_owner}/{canonical_repo}")
        for rel in rel_files:
            if prefix == "archive":
                variants = [
                    f"archive/{owner}/{repo}.txt"
                    for owner in owner_names
                    for repo in repo_names
                ]
            else:
                variants = [
                    f"description/{owner}/{repo}/{rel}"
                    for owner in owner_names
                    for repo in repo_names
                ]
            candidates = [
                (blob_content("HEAD", path), path)
                for path in variants
                if blob_content("HEAD", path) is not None
            ]
            if not candidates:
                print(f"  skip empty {rel or '(archive)'}")
                continue
            content, source = max(candidates, key=lambda item: len(item[0]))
            if prefix == "archive":
                canonical_path = f"archive/{canonical_owner}/{canonical_repo}.txt"
            else:
                canonical_path = (
                    f"description/{canonical_owner}/{canonical_repo}/{rel}"
                )
            to_write[canonical_path] = content
            label = rel or Path(source).name
            print(
                f"  {label}: kept {len(content)} chars from {source.split('/')[2]}"
            )
            for path in variants:
                if path != canonical_path:
                    to_unindex.append(path)

    return to_unindex, to_write


def main() -> int:
    archive_unindex, archive_write = fix_tree("archive")
    desc_unindex, desc_write = fix_tree("description")

    to_unindex = archive_unindex + desc_unindex
    to_write = {**archive_write, **desc_write}

    if not to_write and not to_unindex:
        print("No case-only duplicate description/archive repos found.")
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

    add_paths = sorted(set(to_write))
    if add_paths:
        git("add", "--", *add_paths)

    remaining = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check-description-case-duplicates.py")],
        cwd=ROOT,
    )
    return remaining.returncode


if __name__ == "__main__":
    raise SystemExit(main())
