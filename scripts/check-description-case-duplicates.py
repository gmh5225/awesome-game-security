#!/usr/bin/env python3
"""
Fail when description/{owner}/{repo}/ contains case-only duplicate paths.

On case-insensitive filesystems (default macOS) those duplicates alias to one
directory and produce phantom git diffs that cannot be discarded reliably.
"""

from __future__ import annotations

import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def tracked_description_paths() -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", "description/"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def find_duplicate_groups(paths: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        parts = path.split("/")
        if len(parts) < 4:
            continue
        key = "/".join([parts[0], parts[1], parts[2].lower()] + parts[3:])
        groups[key].append(path)
    return {k: sorted(set(v)) for k, v in groups.items() if len(set(v)) > 1}


def main() -> int:
    groups = find_duplicate_groups(tracked_description_paths())
    if not groups:
        print("OK: no case-only duplicate description paths.")
        return 0

    print(f"ERROR: found {len(groups)} case-only duplicate description path(s):", file=sys.stderr)
    for key in sorted(groups):
        variants = groups[key]
        print(f"  {key}", file=sys.stderr)
        for variant in variants:
            print(f"    - {variant}", file=sys.stderr)
    print(
        "\nRun: python3 scripts/fix-description-case-duplicates.py",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
