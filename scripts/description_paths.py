#!/usr/bin/env python3
"""Canonical description/ path helpers (case-insensitive owner/repo resolution)."""

from __future__ import annotations

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT_DIR / "archive"
DESC_DIR = ROOT_DIR / "description"


def _case_insensitive_child(parent: Path, name: str) -> Path | None:
    if not parent.is_dir():
        return None
    needle = name.lower()
    for child in parent.iterdir():
        if child.name.lower() == needle:
            return child
    return None


def _matching_archives(owner_dir: Path, repo: str) -> list[Path]:
    needle = repo.lower()
    matches = [p for p in owner_dir.glob("*.txt") if p.stem.lower() == needle]
    return sorted(matches, key=lambda p: (-p.stat().st_size, p.stem))


def canonical_repo_slug(owner: str, repo: str) -> tuple[str, str]:
    """
    Return stable (owner, repo) directory names for description/ and archive/.

    Prefer an existing description/ tree so Linux CI does not create a second
    case-only directory when archive/{owner}/{repo}.txt casing differs.
    Otherwise pick the largest matching archive file (tie-break by stem).
    """
    desc_owner = _case_insensitive_child(DESC_DIR, owner)
    if desc_owner and desc_owner.is_dir():
        repo_dir = _case_insensitive_child(desc_owner, repo)
        if repo_dir:
            return desc_owner.name, repo_dir.name

    owner_dir = _case_insensitive_child(ARCHIVE_DIR, owner)
    if owner_dir and owner_dir.is_dir():
        matches = _matching_archives(owner_dir, repo)
        if matches:
            return owner_dir.name, matches[0].stem

    return owner, repo


def normalize_repo_slug(owner: str, repo: str) -> tuple[str, str]:
    """Alias used by CLI entrypoints after slug parsing."""
    return canonical_repo_slug(owner, repo)


def description_dir(owner: str, repo: str) -> Path:
    o, r = canonical_repo_slug(owner, repo)
    return DESC_DIR / o / r


def description_en_path(owner: str, repo: str) -> Path:
    return description_dir(owner, repo) / "description_en.txt"


def description_lang_path(owner: str, repo: str, lang: str) -> Path:
    return description_dir(owner, repo) / f"description_{lang}.txt"


def archive_path(owner: str, repo: str) -> Path:
    o, r = canonical_repo_slug(owner, repo)
    owner_dir = ARCHIVE_DIR / o
    if owner_dir.is_dir():
        matches = _matching_archives(owner_dir, r)
        if matches:
            return matches[0]
    return ARCHIVE_DIR / o / f"{r}.txt"
