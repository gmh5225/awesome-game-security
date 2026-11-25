#!/usr/bin/env python3
"""Canonical description/ path helpers (case-insensitive owner/repo resolution)."""

from __future__ import annotations

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT_DIR / "archive"
DESC_DIR = ROOT_DIR / "description"

NON_REPO_ROUTES = frozenset({
    "stars", "topics", "orgs", "organizations", "users", "sponsors",
    "collections", "settings", "features", "marketplace", "login", "signup",
    "search", "about", "enterprise", "security", "site", "notifications",
    "new", "apps", "codespaces", "pulls", "issues", "discussions", "explore",
    "events", "trending", "customer-stories",
})


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


def archive_path(owner: str, repo: str, archive_dir: Path | None = None) -> Path:
    if archive_dir is None or archive_dir == ARCHIVE_DIR:
        o, r = canonical_repo_slug(owner, repo)
        base_dir = ARCHIVE_DIR
    else:
        o, r = owner, repo
        base_dir = archive_dir

    owner_dir = _case_insensitive_child(base_dir, o)
    if owner_dir and owner_dir.is_dir():
        matches = _matching_archives(owner_dir, r)
        if matches:
            return matches[0]
        return owner_dir / f"{r}.txt"
    return base_dir / o / f"{r}.txt"
