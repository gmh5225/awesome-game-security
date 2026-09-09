#!/usr/bin/env python3
"""Read-only README section and local repository-layer lookup; standard library only."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


SLUG = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+")
URL = re.compile(r"https://github\.com/[^\s<>\"'\]\)]+", re.IGNORECASE)
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})(.*)$")
NON_REPO_ROUTES = {
    "stars", "topics", "orgs", "organizations", "users", "sponsors",
    "collections", "settings", "features", "marketplace", "login", "signup",
    "search", "about", "enterprise", "security", "site", "notifications",
    "new", "apps", "codespaces", "pulls", "issues", "discussions", "explore",
    "events", "trending", "customer-stories",
}


def repo_slug(value):
    """Identify a GitHub repository without discarding the original URL."""
    if value.lower().startswith("https://"):
        parsed = urlsplit(value)
        if parsed.netloc.lower() != "github.com":
            raise ValueError("Expected a github.com repository URL.")
        parts = unquote(parsed.path).strip("/").split("/")
        value = "/".join(parts[:2])
    if value.endswith(".git"):
        value = value[:-4]
    if not SLUG.fullmatch(value) or value.split("/")[1] in {".", ".."}:
        raise ValueError("Expected owner/repository or a GitHub repository URL.")
    if value.split("/")[0].casefold() in NON_REPO_ROUTES:
        raise ValueError("GitHub navigation URL is not a repository identity.")
    return value


def parse_readme(text):
    """Parse this repository's H2/blockquote/bullet convention, excluding fences."""
    sections, entries = [], []
    section = None
    subsection = None
    fence_char, fence_length = None, 0
    lines = text.splitlines()
    for number, line in enumerate(lines, 1):
        match = FENCE.match(line)
        if fence_char:
            if (match and match[1][0] == fence_char
                    and len(match[1]) >= fence_length and not match[2].strip()):
                fence_char = None
            continue
        if match:
            fence_char, fence_length = match[1][0], len(match[1])
            continue
        if line.startswith("## "):
            if section:
                section["end_line"] = number - 1
            section = {"title": line[3:].strip(), "line": number,
                       "end_line": len(lines), "subsections": [], "github_entries": 0}
            sections.append(section)
            subsection = None
        elif section and line.startswith("> "):
            subsection = line[2:].strip()
            section["subsections"].append({"title": subsection, "line": number})
        elif section and re.match(r"^\s*[-*+]\s+", line):
            for match in URL.finditer(line):
                original = match[0].rstrip(".,;:")
                try:
                    slug = repo_slug(original)
                except ValueError:
                    continue
                entries.append({"repo": slug, "url": original,
                                "repository_url": "https://github.com/" + slug,
                                "section": section["title"], "subsection": subsection,
                                "line": number})
                section["github_entries"] += 1
    return sections, entries


def matching_children(parent, name, directory):
    if not parent.is_dir():
        return []
    return sorted(
        (path for path in parent.iterdir()
         if path.name.casefold() == name.casefold()
         and (path.is_dir() if directory else path.is_file())),
        key=lambda path: path.name,
    )


def layer_paths(root, slug):
    """Resolve layers independently and expose every case-only match."""
    owner, repo = slug.split("/")
    descriptions, archives = [], []
    for owner_dir in matching_children(root / "description", owner, True):
        for repo_dir in matching_children(owner_dir, repo, True):
            descriptions.extend(matching_children(repo_dir, "description_en.txt", False))
    for owner_dir in matching_children(root / "archive", owner, True):
        archives.extend(matching_children(owner_dir, repo + ".txt", False))

    def result(paths):
        return {
            "status": "missing" if not paths else "present" if len(paths) == 1 else "ambiguous",
            "paths": [path.relative_to(root).as_posix() for path in paths],
        }

    return {"description": result(descriptions), "archive": result(archives)}


def find_root():
    candidates = [Path.cwd(), *Path.cwd().parents, *Path(__file__).resolve().parents]
    for candidate in candidates:
        if (candidate / "README.md").is_file() and (candidate / ".claude/skills").is_dir():
            return candidate
    raise ValueError("Repository checkout not found; pass --root explicitly.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="awesome-game-security checkout")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--section", help="Exact README H2 title (case-insensitive)")
    mode.add_argument("--repo", help="owner/repository or GitHub repository URL")
    parser.add_argument("--subsection", help="Exact blockquote title; requires --section")
    parser.add_argument("--limit", type=int, default=20, help="Maximum section entries (default 20)")
    args = parser.parse_args()
    if args.subsection and not args.section:
        parser.error("--subsection requires --section")
    if args.limit < 1:
        parser.error("--limit must be positive")
    try:
        root = args.root.resolve() if args.root else find_root()
        raw = (root / "README.md").read_bytes()
        sections, entries = parse_readme(raw.decode("utf-8"))
        report = {"root": str(root), "readme_sha256": hashlib.sha256(raw).hexdigest(),
                  "scope": "local discovery metadata; no upstream verification or code execution"}
        if args.repo:
            slug = repo_slug(args.repo)
            matches = [entry for entry in entries if entry["repo"].casefold() == slug.casefold()]
            report.update(repo=slug, occurrences=matches, layers=layer_paths(root, slug))
        elif args.section:
            selected = [section for section in sections
                        if section["title"].casefold() == args.section.casefold()]
            if not selected:
                raise ValueError("Unknown section; run without filters to list current headings.")
            if args.subsection and not any(
                sub["title"].casefold() == args.subsection.casefold()
                for section in selected for sub in section["subsections"]
            ):
                raise ValueError("Unknown subsection in the selected section.")
            matches = [entry for entry in entries
                       if entry["section"].casefold() == args.section.casefold()
                       and (not args.subsection or
                            (entry["subsection"] or "").casefold() == args.subsection.casefold())]
            report.update(sections=selected, total_matches=len(matches),
                          truncated=len(matches) > args.limit, entries=matches[:args.limit])
        else:
            report.update(section_count=len(sections), sections=sections)
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except (OSError, UnicodeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
