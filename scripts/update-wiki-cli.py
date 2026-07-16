#!/usr/bin/env python3
"""
Maintain the awesome-game-security LLM wiki via Cursor CLI.

Karpathy-style compiled wiki under wiki/: sources → concepts/entities/overviews.
Does NOT use llm-wiki-compiler; drives the local `agent` binary like
generate-descriptions-cli.py / translate-descriptions-cli.py.

Modes:
  bootstrap   — create overview skeletons + core concepts from skills + README map
  ingest      — process pending source deltas (README / skills / descriptions)
  lint        — repair index orphans, broken wikilinks, light freshness
  skill-sync  — strengthen .claude/skills from wiki overviews

Ingest queues hash-changed tracked descriptions plus up to 5 never-tracked
description_en.txt files per scan (newest first). Failed agent runs do not
mark sources as ingested. --list-pending is read-only (does not write state).

Usage:
  python3 scripts/update-wiki-cli.py --list-pending
  python3 scripts/update-wiki-cli.py --mode bootstrap --dry-run
  python3 scripts/update-wiki-cli.py --mode ingest --limit 5 --commit-every 1
  python3 scripts/update-wiki-cli.py --mode lint --commit-every 1
  python3 scripts/update-wiki-cli.py --mode skill-sync --topics anti-cheat
  WIKI_REPOS="owner/repo" python3 scripts/update-wiki-cli.py --mode ingest --repos-env WIKI_REPOS
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import date
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
SKILLS_DIR = ROOT_DIR / ".claude" / "skills"
README_PATH = ROOT_DIR / "README.md"
DESC_DIR = ROOT_DIR / "description"
STATE_PATH = WIKI_DIR / ".state.json"

DEFAULT_MODEL = "cursor-grok-4.5-high-fast"
REPO_SLUG_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$")
TOPIC_RE = re.compile(r"^[a-z0-9-]+$")

# Skill topics that map 1:1 to wiki/overviews/<topic>.md
SKILL_TOPICS: tuple[str, ...] = (
    "overview",
    "anti-cheat",
    "dma-attack",
    "game-engine",
    "game-hacking",
    "graphics-api",
    "mobile-security",
    "reverse-engineering",
    "windows-kernel",
)

# Truncation budgets for projected sources (agent context).
SKILL_PROJECT_MAX_BYTES = 120_000
DESC_PROJECT_MAX_BYTES = 8_000
README_LINKS_PER_SECTION = 12
# Daily/auto scan: how many never-before-tracked description_en.txt files to queue.
NEW_DESCRIPTION_DISCOVER_LIMIT = 5
README_SKIP_SECTIONS = frozenset(
    {
        "how to contribute?",
        "skills for ai agents",
        "contents",
        "donate",
    }
)

WIKI_KEEP_RE = re.compile(
    r"^wiki/(?:AGENTS\.md|index\.md|log\.md|\.state\.json|"
    r"(?:concepts|entities|overviews)/[^/]+\.md|"
    r"sources/(?:README-categories\.md|skills/[^/]+\.md|descriptions/[^/]+\.md))$"
)
SKILL_KEEP_RE = re.compile(r"^\.claude/skills/[a-z0-9-]+/SKILL\.md$")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


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
    # (e.g. Grok's `agent`) cannot shadow the intended binary.
    home_bin = Path.home() / ".cursor" / "bin" / "agent"
    if home_bin.is_file():
        return str(home_bin)
    for name in ("cursor-agent", "agent"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit(
        "ERROR: Cursor CLI `agent` not found on PATH.\n"
        "Install with: curl https://cursor.com/install -fsS | bash"
    )


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state() -> dict[str, Any]:
    if not STATE_PATH.is_file():
        return {
            "version": 1,
            "last_run": None,
            "last_mode": None,
            "source_hashes": {},
            "pending": [],
            "ingested": [],
        }
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        data = {}
    data.setdefault("version", 1)
    data.setdefault("source_hashes", {})
    data.setdefault("pending", [])
    data.setdefault("ingested", [])
    return data


def save_state(state: dict[str, Any]) -> None:
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


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
    raw = os.environ.get(var_name, "")
    return [tok for tok in raw.replace("\n", " ").split(" ") if tok]


def parse_topics(raw: str | None) -> list[str]:
    if not raw:
        return []
    out: list[str] = []
    for part in raw.replace(",", " ").split():
        t = part.strip().lower()
        if not TOPIC_RE.fullmatch(t):
            sys.exit(f"ERROR: invalid topic {part!r}")
        if t not in SKILL_TOPICS:
            sys.exit(
                f"ERROR: unknown topic {t!r}; "
                f"expected one of: {', '.join(SKILL_TOPICS)}"
            )
        if t not in out:
            out.append(t)
    return out


def ensure_wiki_dirs() -> None:
    for sub in (
        WIKI_DIR / "concepts",
        WIKI_DIR / "entities",
        WIKI_DIR / "overviews",
        SOURCES_DIR / "skills",
        SOURCES_DIR / "descriptions",
    ):
        sub.mkdir(parents=True, exist_ok=True)


def has_overview_pages() -> bool:
    return any(
        (WIKI_DIR / "overviews" / f"{t}.md").is_file() for t in SKILL_TOPICS
    )


def overview_topics_present() -> list[str]:
    return [
        t
        for t in SKILL_TOPICS
        if (WIKI_DIR / "overviews" / f"{t}.md").is_file()
    ]


def wiki_paths_excluding_state(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    state_resolved = STATE_PATH.resolve()
    for p in paths:
        try:
            if p.resolve() == state_resolved:
                continue
        except OSError:
            pass
        out.append(p)
    return out


# ---------------------------------------------------------------------------
# Source projection
# ---------------------------------------------------------------------------


def project_readme_categories() -> tuple[Path, str]:
    """Build a compact category map from README.md (not the full file)."""
    ensure_wiki_dirs()
    text = README_PATH.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip()
            if current:
                sections.append(current)
            current = {
                "title": title,
                "subcategories": [],
                "links": [],
            }
            continue
        if current is None:
            continue
        if line.startswith("> "):
            current["subcategories"].append(line[2:].strip())
            continue
        if line.startswith("- http"):
            # "- https://... [desc]" or plain URL
            current["links"].append(line[2:].strip())

    if current:
        sections.append(current)

    out_lines = [
        "# README category projection",
        "",
        f"Generated from README.md ({len(sections)} top-level sections).",
        "Link samples are truncated; see README.md for the full list.",
        "",
    ]
    for sec in sections:
        key = sec["title"].strip().lower()
        if key in README_SKIP_SECTIONS:
            continue
        links: list[str] = sec["links"]
        out_lines.append(f"## {sec['title']}")
        out_lines.append(f"- link_count: {len(links)}")
        if sec["subcategories"]:
            out_lines.append(
                "- subcategories: " + "; ".join(sec["subcategories"][:40])
            )
        sample = links[:README_LINKS_PER_SECTION]
        if sample:
            out_lines.append("- sample_links:")
            for link in sample:
                # Keep line short
                out_lines.append(f"  - {link[:240]}")
        out_lines.append("")

    body = "\n".join(out_lines).rstrip() + "\n"
    path = SOURCES_DIR / "README-categories.md"
    path.write_text(body, encoding="utf-8")
    return path, text_sha256(body)


def project_skill(topic: str) -> tuple[Path, str]:
    ensure_wiki_dirs()
    src = SKILLS_DIR / topic / "SKILL.md"
    if not src.is_file():
        sys.exit(f"ERROR: missing skill file {src.relative_to(ROOT_DIR)}")
    raw = src.read_bytes()
    truncated = raw[:SKILL_PROJECT_MAX_BYTES]
    note = ""
    if len(raw) > SKILL_PROJECT_MAX_BYTES:
        note = (
            f"\n\n<!-- truncated: showing first {SKILL_PROJECT_MAX_BYTES} "
            f"of {len(raw)} bytes -->\n"
        )
    header = (
        f"# Skill projection: {topic}\n\n"
        f"Source: `.claude/skills/{topic}/SKILL.md`\n\n"
        "---\n\n"
    )
    body = header + truncated.decode("utf-8", errors="replace") + note
    path = SOURCES_DIR / "skills" / f"{topic}.md"
    path.write_text(body, encoding="utf-8")
    return path, file_sha256(src)


def project_description(owner: str, repo: str) -> tuple[Path, str]:
    ensure_wiki_dirs()
    src = DESC_DIR / owner / repo / "description_en.txt"
    if not src.is_file():
        sys.exit(
            f"ERROR: missing description {src.relative_to(ROOT_DIR)}"
        )
    raw = src.read_text(encoding="utf-8", errors="replace").strip()
    if len(raw) > DESC_PROJECT_MAX_BYTES:
        raw = raw[:DESC_PROJECT_MAX_BYTES] + "\n…(truncated)…\n"
    # Find README mention if present (lightweight)
    readme_hit = ""
    try:
        rm = README_PATH.read_text(encoding="utf-8", errors="replace")
        needle = f"github.com/{owner}/{repo}"
        for line in rm.splitlines():
            if needle.lower() in line.lower():
                readme_hit = line.strip()[:300]
                break
    except OSError:
        pass

    body_lines = [
        f"# Description projection: {owner}/{repo}",
        "",
        f"Source: `description/{owner}/{repo}/description_en.txt`",
        "",
        "## Summary",
        "",
        raw,
        "",
    ]
    if readme_hit:
        body_lines.extend(["## README entry", "", readme_hit, ""])
    body = "\n".join(body_lines)
    fname = f"{owner}__{repo}.md"
    path = SOURCES_DIR / "descriptions" / fname
    path.write_text(body, encoding="utf-8")
    return path, file_sha256(src)


def desc_slug_to_path(owner: str, repo: str) -> Path:
    return DESC_DIR / owner / repo / "description_en.txt"


# ---------------------------------------------------------------------------
# Pending / scan
# ---------------------------------------------------------------------------


def pending_item(
    kind: str,
    item_id: str,
    *,
    path: str = "",
    hash_: str = "",
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"kind": kind, "id": item_id}
    if path:
        item["path"] = path
    if hash_:
        item["hash"] = hash_
    if extra:
        item.update(extra)
    return item


def scan_pending(
    *,
    force_readme: bool = False,
    force_skills: list[str] | None = None,
    force_repos: list[tuple[str, str]] | None = None,
    include_all_skills_if_bootstrap: bool = False,
    only_forced: bool = False,
) -> list[dict[str, Any]]:
    """Compare current sources to wiki/.state.json hashes; return pending work."""
    state = load_state()
    hashes: dict[str, str] = dict(state.get("source_hashes") or {})
    pending: list[dict[str, Any]] = []

    # README
    if README_PATH.is_file() and (not only_forced or force_readme):
        _, body_hash = project_readme_categories()
        key = "readme:categories"
        if force_readme or hashes.get(key) != body_hash:
            pending.append(
                pending_item(
                    "readme",
                    key,
                    path="wiki/sources/README-categories.md",
                    hash_=body_hash,
                )
            )

    # Skills
    if only_forced:
        topics = list(force_skills or [])
    else:
        topics = list(force_skills or [])
        if include_all_skills_if_bootstrap and not topics:
            topics = list(SKILL_TOPICS)
        elif not force_skills:
            topics = list(SKILL_TOPICS)

    seen_topics: set[str] = set()
    for topic in topics:
        if topic in seen_topics:
            continue
        seen_topics.add(topic)
        src = SKILLS_DIR / topic / "SKILL.md"
        if not src.is_file():
            continue
        _, h = project_skill(topic)
        key = f"skill:{topic}"
        force = bool(force_skills and topic in force_skills) or include_all_skills_if_bootstrap
        if force or hashes.get(key) != h:
            pending.append(
                pending_item(
                    "skill",
                    key,
                    path=f"wiki/sources/skills/{topic}.md",
                    hash_=h,
                    extra={"topic": topic},
                )
            )

    # Descriptions
    if force_repos:
        for owner, repo in force_repos:
            src = desc_slug_to_path(owner, repo)
            if not src.is_file():
                print(f"WARNING: skip missing description {owner}/{repo}")
                continue
            _, h = project_description(owner, repo)
            key = f"description:{owner}/{repo}"
            pending.append(
                pending_item(
                    "description",
                    key,
                    path=f"wiki/sources/descriptions/{owner}__{repo}.md",
                    hash_=h,
                    extra={"owner": owner, "repo": repo},
                )
            )
    elif not only_forced:
        # Detect description files whose hash changed vs previously tracked state.
        for key, old_h in list(hashes.items()):
            if not key.startswith("description:"):
                continue
            slug = key.split(":", 1)[1]
            if not REPO_SLUG_RE.fullmatch(slug):
                continue
            owner, repo = slug.split("/", 1)
            src = desc_slug_to_path(owner, repo)
            if not src.is_file():
                continue
            h = file_sha256(src)
            if h != old_h:
                project_description(owner, repo)
                pending.append(
                    pending_item(
                        "description",
                        key,
                        path=f"wiki/sources/descriptions/{owner}__{repo}.md",
                        hash_=h,
                        extra={"owner": owner, "repo": repo},
                    )
                )

        # Discover never-tracked description_en.txt (newest mtime first), capped.
        tracked_desc = {
            k.split(":", 1)[1]
            for k in hashes
            if k.startswith("description:") and REPO_SLUG_RE.fullmatch(k.split(":", 1)[1])
        }
        pending_ids = {item["id"] for item in pending}
        discoveries: list[tuple[float, str, str, Path]] = []
        if DESC_DIR.is_dir():
            for src in DESC_DIR.glob("*/*/description_en.txt"):
                try:
                    rel_parts = src.relative_to(DESC_DIR).parts
                except ValueError:
                    continue
                if len(rel_parts) != 3:
                    continue
                owner, repo, _fname = rel_parts
                slug = f"{owner}/{repo}"
                if not REPO_SLUG_RE.fullmatch(slug):
                    continue
                if slug in tracked_desc:
                    continue
                key = f"description:{slug}"
                if key in pending_ids:
                    continue
                try:
                    mtime = src.stat().st_mtime
                except OSError:
                    continue
                discoveries.append((mtime, owner, repo, src))
        discoveries.sort(key=lambda x: x[0], reverse=True)
        for _mtime, owner, repo, _src in discoveries[:NEW_DESCRIPTION_DISCOVER_LIMIT]:
            _, h = project_description(owner, repo)
            key = f"description:{owner}/{repo}"
            pending.append(
                pending_item(
                    "description",
                    key,
                    path=f"wiki/sources/descriptions/{owner}__{repo}.md",
                    hash_=h,
                    extra={"owner": owner, "repo": repo},
                )
            )

    # Deduplicate by id (keep last)
    by_id: dict[str, dict[str, Any]] = {}
    for item in pending:
        by_id[item["id"]] = item
    return list(by_id.values())


def mark_ingested(state: dict[str, Any], item: dict[str, Any]) -> None:
    hid = item.get("hash") or ""
    key = item["id"]
    if hid:
        state.setdefault("source_hashes", {})[key] = hid
    ingested = state.setdefault("ingested", [])
    entry = {
        "id": key,
        "kind": item.get("kind"),
        "at": date.today().isoformat(),
    }
    ingested.append(entry)
    # Cap history
    if len(ingested) > 500:
        state["ingested"] = ingested[-500:]


def print_pending_report(pending: list[dict[str, Any]]) -> None:
    print("Wiki pending sources")
    print(f"  pending_count: {len(pending)}")
    print(f"PENDING_COUNT={len(pending)}")
    by_kind: dict[str, int] = {}
    for item in pending:
        by_kind[item["kind"]] = by_kind.get(item["kind"], 0) + 1
    for k, v in sorted(by_kind.items()):
        print(f"  {k}: {v}")
    preview = pending[:40]
    for item in preview:
        print(f"  - [{item['kind']}] {item['id']}")
    if len(pending) > 40:
        print(f"  ... and {len(pending) - 40} more")


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------


def run_agent(
    agent_bin: str,
    model: str,
    prompt: str,
    dry_run: bool,
) -> int:
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
        print(prompt[:1200])
        if len(prompt) > 1200:
            print(f"... ({len(prompt)} chars total)")
        print("---")
        return 0

    print(f"  $ {agent_bin} -p --force --trust --sandbox disabled --model {model} ...")
    started = time.time()
    proc = subprocess.run(
        cmd,
        cwd=ROOT_DIR,
        env=os.environ.copy(),
        timeout=None,
        check=False,
    )
    elapsed = time.time() - started
    print(f"  exit={proc.returncode}  elapsed={elapsed:.1f}s")
    if proc.returncode != 0 and "--trust" in cmd and elapsed < 2.0:
        print("  retrying without --trust (possible older CLI) ...")
        cmd_no_trust = [c for c in cmd if c != "--trust"]
        proc = subprocess.run(
            cmd_no_trust,
            cwd=ROOT_DIR,
            env=os.environ.copy(),
            timeout=None,
            check=False,
        )
        print(f"  exit={proc.returncode}  elapsed={time.time() - started:.1f}s (no --trust)")
    return proc.returncode


def build_bootstrap_prompt() -> str:
    skill_list = ", ".join(SKILL_TOPICS)
    return f"""\
You are bootstrapping the awesome-game-security LLM wiki.

Read and follow: wiki/AGENTS.md

Goal: create initial compiled pages from skill projections + README category map.
Do NOT ingest the full description corpus.

Steps:
1. Read wiki/AGENTS.md, wiki/index.md, wiki/sources/README-categories.md.
2. Read each projected skill under wiki/sources/skills/ (topics: {skill_list}).
3. For EACH topic, create wiki/overviews/<topic>.md with required frontmatter:
   - kind: overview
   - topics: [<topic>]
   - sources: list the skill projection path(s) you used
   - 1–2 page synthesis: what the domain covers, key sub-areas, links to concepts you create
4. Create 8–15 high-value wiki/concepts/<slug>.md pages drawn from skills
   (examples: dma, easy-anti-cheat, battleye, vanguard, hvci, present-hook,
   il2cpp, kernel-callbacks, byovd — pick what the sources actually support).
5. Rewrite wiki/index.md to list all overviews and concepts with relative links.
6. Append a dated entry to wiki/log.md describing bootstrap.
7. Do NOT modify .claude/skills, README.md, description/, or archive/.
8. Do NOT read archive/ files.

Hard constraints:
- ONLY create/modify files under wiki/ (markdown + keep sources as-is)
- Touch at most ~30 new page files plus index.md and log.md
- Print one line when finished: Done: bootstrap
"""


def build_ingest_prompt(item: dict[str, Any]) -> str:
    kind = item["kind"]
    src_path = item.get("path", "")
    today = date.today().isoformat()
    extra = ""
    if kind == "skill":
        topic = item.get("topic", "")
        extra = f"""
Focus topic: {topic}
Update wiki/overviews/{topic}.md (create if missing).
Update or create up to 3 related concept/entity pages.
"""
    elif kind == "description":
        owner = item.get("owner", "")
        repo = item.get("repo", "")
        extra = f"""
Repository: {owner}/{repo}
Prefer updating/creating wiki/entities/<slug>.md for this tool if notable,
and patch at most 2 related concept/overview pages with a short cite.
Slug: lowercase kebab from repo name (e.g. pcileech → pcileech).
"""
    elif kind == "readme":
        extra = """
README category map changed. Refresh wiki/overviews that map to major README
sections if their scope drifted; update index.md section notes lightly.
Do not create one page per README category.
"""

    return f"""\
You are ingesting one source delta into the awesome-game-security LLM wiki.

Read and follow: wiki/AGENTS.md

Source kind: {kind}
Source id: {item['id']}
Projected file: {src_path}
Date: {today}
{extra}
Steps:
1. Read wiki/AGENTS.md and wiki/index.md.
2. Read the projected source at {src_path}.
3. Read any existing related overview/concept/entity pages you will update.
4. Update or create a SMALL set of pages (≤8 wiki markdown files besides index/log).
5. Update wiki/index.md for touched pages.
6. Append a short bullet to wiki/log.md for {today}.
7. Do NOT read archive/. Do NOT modify skills, README, or description/.

Hard constraints:
- ONLY modify files under wiki/
- Keep frontmatter valid on new/updated pages
- Print: Done: ingest {item['id']}
"""


def build_lint_prompt() -> str:
    today = date.today().isoformat()
    return f"""\
You are linting the awesome-game-security LLM wiki.

Read and follow: wiki/AGENTS.md

Date: {today}

Steps:
1. Read wiki/index.md and list files under wiki/overviews, wiki/concepts, wiki/entities.
2. Fix index.md so it matches files on disk (add missing, remove dead entries).
3. Spot-check wikilinks on overview pages; fix broken [[links]] when the target
   clearly exists under another name, or remove dead links.
4. Do not invent large new content. Prefer structural repairs.
5. Append a lint entry to wiki/log.md.
6. If the wiki is still empty (only placeholders), note that bootstrap is needed
   and make minimal index cleanliness fixes only.

Hard constraints:
- ONLY modify files under wiki/
- Touch at most 20 files
- Print: Done: lint
"""


def build_skill_sync_prompt(topic: str) -> str:
    return f"""\
You are strengthening one agent skill from the compiled wiki.

Topic: {topic}
Wiki overview: wiki/overviews/{topic}.md
Skill file: .claude/skills/{topic}/SKILL.md

Read and follow: wiki/AGENTS.md (Skill sync section).

Steps:
1. Read wiki/overviews/{topic}.md and 1–3 linked concept pages if present.
2. Read .claude/skills/{topic}/SKILL.md.
3. Apply a SMALL patch to the skill only:
   - Add a short "Compiled wiki" section pointing to wiki/overviews/{topic}.md
     (and 2–5 key concept paths) if missing.
   - Fill clear factual gaps or fix outdated one-liners ONLY when the wiki
     has equal/higher confidence and cites sources.
4. Do NOT change YAML frontmatter `name`.
5. Do NOT add more than ~30 new lines.
6. Do NOT modify any other files (no wiki edits in this mode unless fixing a
   broken relative path mention inside the skill).

Hard constraints:
- ONLY modify .claude/skills/{topic}/SKILL.md
- Print: Done: skill-sync {topic}
"""


# ---------------------------------------------------------------------------
# Git safety
# ---------------------------------------------------------------------------


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT_DIR,
        capture_output=True,
        check=check,
    )


def _discard_path(rel: str) -> None:
    path = ROOT_DIR / rel
    checked = _git("checkout", "--", rel, check=False)
    if checked.returncode != 0 and path.exists():
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)


def discard_disallowed(keep: list[Path], *, allow_skills: bool) -> None:
    """Drop agent side-effects outside keep set / allowed patterns."""
    keep_set = {str(p.relative_to(ROOT_DIR)) for p in keep}
    # Re-scan workspace dirty files and drop agent side-effects.
    proc = _git("ls-files", "-m", "-o", "--exclude-standard", check=False)
    for line in proc.stdout.decode().splitlines():
        rel = line.strip()
        if not rel:
            continue
        if rel in keep_set:
            continue
        if WIKI_KEEP_RE.match(rel):
            # Wiki path but not in this batch — revert to avoid cross-talk
            # unless we are keeping all wiki writes from this run.
            # Policy: keep ALL wiki matches that exist under wiki/ for ingest,
            # because one agent may touch several pages. Only discard non-wiki.
            continue
        if allow_skills and SKILL_KEEP_RE.match(rel):
            # Only keep skills explicitly in keep_set
            if rel not in keep_set:
                _discard_path(rel)
            continue
        _discard_path(rel)


def collect_wiki_changes() -> list[Path]:
    proc = _git("ls-files", "-m", "-o", "--exclude-standard", check=False)
    paths: list[Path] = []
    for line in proc.stdout.decode().splitlines():
        rel = line.strip()
        if not rel.startswith("wiki/"):
            continue
        # Allow wiki markdown/json the agent created under known dirs.
        # (Source projections are gitignored and normally absent from this list.)
        if (
            rel.startswith("wiki/concepts/")
            or rel.startswith("wiki/entities/")
            or rel.startswith("wiki/overviews/")
            or rel.startswith("wiki/sources/")
            or rel
            in (
                "wiki/AGENTS.md",
                "wiki/index.md",
                "wiki/log.md",
                "wiki/.state.json",
            )
        ):
            paths.append(ROOT_DIR / rel)
    return paths


def collect_skill_changes(topics: list[str]) -> list[Path]:
    allowed = {f".claude/skills/{t}/SKILL.md" for t in topics}
    proc = _git("ls-files", "-m", "-o", "--exclude-standard", check=False)
    paths: list[Path] = []
    for line in proc.stdout.decode().splitlines():
        rel = line.strip()
        if rel in allowed:
            paths.append(ROOT_DIR / rel)
    return paths


def git_commit_and_push(paths: list[Path], branch: str, message: str) -> bool:
    if not paths:
        return True
    # Discard everything not in paths and not wiki (caller already filtered)
    rels = []
    for p in paths:
        if not p.exists():
            continue
        try:
            rels.append(str(p.relative_to(ROOT_DIR)))
        except ValueError:
            continue
    if not rels:
        return True
    try:
        _git("add", "--", *rels)
        if _git("diff", "--cached", "--quiet", check=False).returncode == 0:
            return True
        _git("commit", "-m", message)
    except subprocess.CalledProcessError as e:
        err = (e.stderr or b"").decode().strip()[:200]
        print(f"  [GIT ERROR] commit: {err or e}")
        return False

    for attempt in range(1, 6):
        try:
            _git("push", "origin", f"HEAD:{branch}")
            print(f"  [GIT] committed+pushed {len(rels)} file(s) → {branch}")
            return True
        except subprocess.CalledProcessError as e:
            err = (e.stderr or b"").decode().strip()
            if attempt >= 5:
                print(f"  [GIT ERROR] push failed after 5 retries: {err[:200]}")
                _git("reset", "HEAD~1", check=False)
                return False
            if any(k in err for k in ("rejected", "fetch first", "non-fast-forward")):
                print(f"  [GIT] push rejected (attempt {attempt}/5), rebasing ...")
                try:
                    _git("pull", "--rebase", "origin", branch)
                except subprocess.CalledProcessError as re_err:
                    re_msg = (re_err.stderr or b"").decode().strip()[:200]
                    print(f"  [GIT ERROR] rebase failed: {re_msg}")
                    _git("rebase", "--abort", check=False)
                    _git("reset", "HEAD~1", check=False)
                    return False
            elif any(
                k in err
                for k in ("408", "RPC failed", "unexpected disconnect", "timed out")
            ):
                wait = 5 * attempt
                print(f"  [GIT] push timeout, retrying in {wait}s ...")
                time.sleep(wait)
            else:
                print(f"  [GIT ERROR] push: {err[:200]}")
                _git("reset", "HEAD~1", check=False)
                return False
    return False


# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------


def mode_bootstrap(args: argparse.Namespace) -> int:
    ensure_wiki_dirs()
    # Project all skills + readme
    project_readme_categories()
    for topic in SKILL_TOPICS:
        if (SKILLS_DIR / topic / "SKILL.md").is_file():
            project_skill(topic)

    if not args.dry_run:
        get_api_key()
    agent_bin = "agent" if args.dry_run else find_agent_bin()
    prompt = build_bootstrap_prompt()
    print(f"Mode: bootstrap  model={args.model}")
    code = run_agent(agent_bin, args.model, prompt, args.dry_run)
    if args.dry_run:
        return 0

    # Discard non-wiki side effects; keep all wiki changes
    wiki_paths = collect_wiki_changes()
    discard_disallowed(wiki_paths, allow_skills=False)

    created = overview_topics_present()
    if not created:
        print("ERROR: bootstrap failed — no overview pages created")
        return 1

    state = load_state()
    # Only mark sources that actually produced an overview (partial OK).
    _, rh = project_readme_categories()
    mark_ingested(
        state,
        pending_item("readme", "readme:categories", hash_=rh),
    )
    for topic in created:
        src = SKILLS_DIR / topic / "SKILL.md"
        if src.is_file():
            mark_ingested(
                state,
                pending_item("skill", f"skill:{topic}", hash_=file_sha256(src)),
            )
    missing = [t for t in SKILL_TOPICS if t not in created]
    if missing:
        print(
            "WARNING: bootstrap incomplete — missing overviews for: "
            + ", ".join(missing)
            + " (left unmarked for later ingest)"
        )
    state["last_run"] = date.today().isoformat()
    state["last_mode"] = "bootstrap"
    save_state(state)
    wiki_paths = collect_wiki_changes()
    wiki_paths.append(STATE_PATH)

    if args.commit_every:
        branch = os.environ.get("GIT_PUSH_BRANCH", "main").strip() or "main"
        ok = git_commit_and_push(
            wiki_paths,
            branch,
            "wiki: bootstrap overviews and concepts via Cursor CLI [skip ci]",
        )
        if not ok:
            return 1

    print(f"Bootstrap finished ({len(created)}/{len(SKILL_TOPICS)} overviews).")
    return 0 if code == 0 or created else 1


def mode_ingest(args: argparse.Namespace) -> int:
    ensure_wiki_dirs()

    # PR / forced ingest on an empty wiki: bootstrap first so entities have context.
    if not has_overview_pages():
        print("No overview pages yet — running bootstrap before ingest")
        rc = mode_bootstrap(args)
        if rc != 0:
            return rc
        if args.dry_run and not has_overview_pages():
            print("Dry-run: bootstrap simulated; skipping ingest items")
            return 0

    force_repos: list[tuple[str, str]] | None = None
    if args.repos_env:
        force_repos = [parse_repo_slug(s) for s in slugs_from_env(args.repos_env)]
    elif args.repos is not None:
        force_repos = [parse_repo_slug(s) for s in args.repos]

    force_skills = parse_topics(args.topics) if args.topics else None
    only_forced = bool(force_repos or force_skills or args.force_readme)
    pending = scan_pending(
        force_readme=bool(args.force_readme),
        force_skills=force_skills,
        force_repos=force_repos,
        only_forced=only_forced,
    )
    print_pending_report(pending)

    if args.limit and args.limit > 0:
        pending = pending[: args.limit]
        print(f"Limited to: {len(pending)}")

    if not pending:
        print("Nothing to ingest.")
        return 0

    if not args.dry_run:
        get_api_key()
    agent_bin = "agent" if args.dry_run else find_agent_bin()
    push_branch = os.environ.get("GIT_PUSH_BRANCH", "main").strip() or "main"

    ok = fail = 0
    state = load_state()

    for i, item in enumerate(pending, start=1):
        print(f"\n[{i}/{len(pending)}] ingest {item['id']}")
        # Ensure projection exists
        if item["kind"] == "readme":
            project_readme_categories()
        elif item["kind"] == "skill":
            project_skill(item["topic"])
        elif item["kind"] == "description":
            project_description(item["owner"], item["repo"])

        prompt = build_ingest_prompt(item)
        code = run_agent(agent_bin, args.model, prompt, args.dry_run)
        if args.dry_run:
            ok += 1
            continue

        wiki_paths = collect_wiki_changes()
        discard_disallowed(wiki_paths, allow_skills=False)
        wiki_paths = collect_wiki_changes()
        content_paths = wiki_paths_excluding_state(wiki_paths)

        # Mark ingested only on success: agent OK (even if no edits), or pages written.
        # Never mark on hard failure with zero wiki content — otherwise the item
        # is permanently skipped until the source hash changes again.
        if code != 0 and not content_paths:
            fail += 1
            print(f"  FAILED ingest {item['id']} exit={code} (not marked)")
            continue

        mark_ingested(state, item)
        state["last_run"] = date.today().isoformat()
        state["last_mode"] = "ingest"
        save_state(state)
        wiki_paths = collect_wiki_changes()
        wiki_paths.append(STATE_PATH)

        ok += 1
        if args.commit_every:
            msg = f"wiki: ingest {item['id']} via Cursor CLI [skip ci]"
            if not git_commit_and_push(wiki_paths, push_branch, msg):
                return 1

    print(f"\nSummary: ok={ok} fail={fail}")
    return 1 if fail else 0


def mode_lint(args: argparse.Namespace) -> int:
    ensure_wiki_dirs()
    if not args.dry_run:
        get_api_key()
    agent_bin = "agent" if args.dry_run else find_agent_bin()
    print(f"Mode: lint  model={args.model}")
    code = run_agent(agent_bin, args.model, build_lint_prompt(), args.dry_run)
    if args.dry_run:
        return 0

    wiki_paths = collect_wiki_changes()
    discard_disallowed(wiki_paths, allow_skills=False)
    state = load_state()
    state["last_run"] = date.today().isoformat()
    state["last_mode"] = "lint"
    save_state(state)
    wiki_paths = collect_wiki_changes()
    wiki_paths.append(STATE_PATH)

    if args.commit_every:
        branch = os.environ.get("GIT_PUSH_BRANCH", "main").strip() or "main"
        if wiki_paths:
            if not git_commit_and_push(
                wiki_paths,
                branch,
                "wiki: lint index and links via Cursor CLI [skip ci]",
            ):
                return 1
        else:
            print("No wiki changes from lint.")
    content = wiki_paths_excluding_state(wiki_paths)
    if code == 0 or content:
        return 0
    return 1


def mode_skill_sync(args: argparse.Namespace) -> int:
    topics = parse_topics(args.topics) if args.topics else list(SKILL_TOPICS)
    if args.limit and args.limit > 0:
        topics = topics[: args.limit]

    # Only sync topics that have an overview page
    runnable: list[str] = []
    for t in topics:
        overview = WIKI_DIR / "overviews" / f"{t}.md"
        skill = SKILLS_DIR / t / "SKILL.md"
        if not overview.is_file():
            print(f"SKIP {t}: missing wiki/overviews/{t}.md (run bootstrap first)")
            continue
        if not skill.is_file():
            print(f"SKIP {t}: missing skill")
            continue
        runnable.append(t)

    print(f"Skill-sync topics: {runnable}")
    if not runnable:
        print("Nothing to skill-sync.")
        return 0

    if not args.dry_run:
        get_api_key()
    agent_bin = "agent" if args.dry_run else find_agent_bin()
    push_branch = os.environ.get("GIT_PUSH_BRANCH", "main").strip() or "main"

    ok = fail = 0
    for i, topic in enumerate(runnable, start=1):
        print(f"\n[{i}/{len(runnable)}] skill-sync {topic}")
        code = run_agent(
            agent_bin, args.model, build_skill_sync_prompt(topic), args.dry_run
        )
        if args.dry_run:
            ok += 1
            continue

        skill_paths = collect_skill_changes([topic])
        # Discard everything else (including accidental wiki edits)
        discard_disallowed(skill_paths, allow_skills=True)
        # Also discard any wiki changes in skill-sync mode
        proc = _git("ls-files", "-m", "-o", "--exclude-standard", check=False)
        for line in proc.stdout.decode().splitlines():
            rel = line.strip()
            if rel.startswith("wiki/"):
                _discard_path(rel)
            elif SKILL_KEEP_RE.match(rel) and rel not in {
                str(p.relative_to(ROOT_DIR)) for p in skill_paths
            }:
                _discard_path(rel)

        skill_paths = collect_skill_changes([topic])
        if skill_paths:
            ok += 1
            if args.commit_every:
                msg = (
                    f"skills: sync {topic} from wiki via Cursor CLI [skip ci]"
                )
                if not git_commit_and_push(skill_paths, push_branch, msg):
                    return 1
        elif code == 0:
            print("  no skill file changes (already up to date?)")
            ok += 1
        else:
            fail += 1
            print(f"  FAILED skill-sync {topic} exit={code}")

    print(f"\nSummary: ok={ok} fail={fail}")
    return 1 if fail else 0


def mode_auto(args: argparse.Namespace) -> int:
    """Daily/CI default: bootstrap if empty, else ingest pending, else lint."""
    if not has_overview_pages():
        print("Auto: no overview pages yet — running bootstrap")
        rc = mode_bootstrap(args)
        if rc != 0:
            return rc
        if args.dry_run and not has_overview_pages():
            print("Auto: dry-run bootstrap done (skipping ingest/lint)")
            return 0
        # Continue into ingest so the same run can pick up new descriptions.

    pending = scan_pending()
    print_pending_report(pending)
    if pending:
        print("Auto: running ingest for pending deltas")
        return mode_ingest(args)
    print("Auto: no pending deltas — running lint")
    return mode_lint(args)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Maintain wiki/ via Cursor CLI (LLM Wiki pattern)"
    )
    parser.add_argument(
        "--mode",
        choices=("bootstrap", "ingest", "lint", "skill-sync", "auto"),
        default="auto",
        help="Operation mode (default: auto = ingest pending else lint)",
    )
    parser.add_argument(
        "--list-pending",
        action="store_true",
        help="Scan and print pending source deltas, then exit",
    )
    parser.add_argument(
        "--repos",
        nargs="*",
        default=None,
        help="Force-ingest these description owner/repo slugs",
    )
    parser.add_argument(
        "--repos-env",
        type=str,
        default="",
        help="Env var with space-separated owner/repo slugs (CI-safe)",
    )
    parser.add_argument(
        "--topics",
        type=str,
        default="",
        help="Comma/space-separated skill topics (ingest force / skill-sync)",
    )
    parser.add_argument(
        "--force-readme",
        action="store_true",
        help="Force README category re-ingest even if hash matches",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max pending items / topics to process (0 = all)",
    )
    parser.add_argument(
        "--commit-every",
        type=int,
        default=0,
        help="Git commit+push after each unit of work (CI uses 1)",
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
        help="Print prompts; do not call agent or require API key",
    )
    args = parser.parse_args()

    if args.limit < 0:
        sys.exit("ERROR: --limit must be >= 0")
    if args.commit_every < 0:
        sys.exit("ERROR: --commit-every must be >= 0")

    ensure_wiki_dirs()

    if args.list_pending:
        force_repos = None
        if args.repos_env:
            force_repos = [parse_repo_slug(s) for s in slugs_from_env(args.repos_env)]
        elif args.repos is not None:
            force_repos = [parse_repo_slug(s) for s in args.repos]
        force_skills = parse_topics(args.topics) or None
        only_forced = bool(force_repos or force_skills or args.force_readme)
        pending = scan_pending(
            force_readme=args.force_readme,
            force_skills=force_skills,
            force_repos=force_repos,
            only_forced=only_forced,
        )
        print_pending_report(pending)
        # Read-only: do not write wiki/.state.json
        return

    dispatch = {
        "bootstrap": mode_bootstrap,
        "ingest": mode_ingest,
        "lint": mode_lint,
        "skill-sync": mode_skill_sync,
        "auto": mode_auto,
    }
    rc = dispatch[args.mode](args)
    sys.exit(rc)


if __name__ == "__main__":
    main()
