#!/usr/bin/env python3
"""
Check which GitHub repos in README.md have NOT been archived yet.

Usage:
    python scripts/check-missing-archives.py
    python scripts/check-missing-archives.py --no-group      # flat list, no category headers
    python scripts/check-missing-archives.py --urls-only     # bare URLs, easy to pipe/grep
"""

import re
import argparse
from pathlib import Path

from description_paths import NON_REPO_ROUTES, archive_path

ROOT_DIR          = Path(__file__).resolve().parent.parent
README_PATH       = ROOT_DIR / "README.md"
ARCHIVE_DIR       = ROOT_DIR / "archive"
SCAN_START_MARKER = "## Game Engine"

GITHUB_REPO_PATTERN = re.compile(
    r"https://github\.com/([^/\s\)\]>\"']+)/([^/\s\)\]>\"'#]+)"
)
CATEGORY_PATTERN = re.compile(r"^#{1,3}\s+(.+)", re.MULTILINE)


def extract_repos_with_categories(text: str) -> list[tuple[str, str, str]]:
    """Return [(owner, repo, category), ...] in README order."""
    marker_pos = text.find(SCAN_START_MARKER)
    if marker_pos == -1:
        print(f"[WARN] Marker '{SCAN_START_MARKER}' not found — scanning full README.")
        scan_text = text
        offset = 0
    else:
        scan_text = text[marker_pos:]
        offset = marker_pos

    # Build a sorted list of (pos, category_name) for headings
    headings: list[tuple[int, str]] = []
    for m in CATEGORY_PATTERN.finditer(scan_text):
        headings.append((m.start(), m.group(1).strip()))

    def category_at(pos: int) -> str:
        name = "Uncategorized"
        for h_pos, h_name in headings:
            if h_pos <= pos:
                name = h_name
            else:
                break
        return name

    seen: set[tuple[str, str]] = set()
    result = []
    for m in GITHUB_REPO_PATTERN.finditer(scan_text):
        owner, repo = m.group(1), m.group(2).rstrip(".,;:")
        if owner == "gmh5225" and repo == "awesome-game-security":
            continue
        if owner.casefold() in NON_REPO_ROUTES:
            continue
        key = (owner.lower(), repo.lower())
        if key in seen:
            continue
        seen.add(key)
        result.append((owner, repo, category_at(m.start())))
    return result


def is_archived(owner: str, repo: str) -> bool:
    return archive_path(owner, repo, archive_dir=ARCHIVE_DIR).is_file()


def main() -> None:
    parser = argparse.ArgumentParser(description="Show repos in README not yet archived.")
    parser.add_argument("--no-group",  action="store_true",
                        help="Print flat list without category grouping")
    parser.add_argument("--urls-only", action="store_true",
                        help="Print bare URLs only (implies --no-group)")
    args = parser.parse_args()

    text = README_PATH.read_text(encoding="utf-8")
    all_repos = extract_repos_with_categories(text)

    missing = [(o, r, cat) for o, r, cat in all_repos if not is_archived(o, r)]

    total   = len(all_repos)
    n_arch  = total - len(missing)
    n_miss  = len(missing)

    if not (args.no_group or args.urls_only):
        print(f"Total in README : {total}")
        print(f"Archived        : {n_arch}")
        print(f"Missing         : {n_miss}")
        print()

    if args.urls_only:
        for o, r, _ in missing:
            print(f"https://github.com/{o}/{r}")
        return

    if args.no_group:
        for o, r, _ in missing:
            print(f"https://github.com/{o}/{r}")
        return

    # Group by category
    from collections import defaultdict
    by_cat: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for o, r, cat in missing:
        by_cat[cat].append((o, r))

    for cat, repos in by_cat.items():
        print(f"── {cat} ({len(repos)})")
        for o, r in repos:
            print(f"   https://github.com/{o}/{r}")
        print()


if __name__ == "__main__":
    main()
