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


def canonical_repo_slug(owner: str, repo: str) -> tuple[str, str]:
    """
    Return (owner, repo) directory names aligned with archive/{owner}/{repo}.txt
    when that archive exists; otherwise reuse an existing description/ sibling;
    otherwise return the slug unchanged.
    """
    owner_dir = _case_insensitive_child(ARCHIVE_DIR, owner)
    canonical_owner = owner_dir.name if owner_dir else owner

    if owner_dir and owner_dir.is_dir():
        for archive in owner_dir.glob("*.txt"):
            if archive.stem.lower() == repo.lower():
                return canonical_owner, archive.stem

    desc_owner = _case_insensitive_child(DESC_DIR, owner)
    if desc_owner and desc_owner.is_dir():
        repo_dir = _case_insensitive_child(desc_owner, repo)
        if repo_dir:
            return desc_owner.name, repo_dir.name

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
    return ARCHIVE_DIR / o / f"{r}.txt"
