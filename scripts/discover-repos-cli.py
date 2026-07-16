#!/usr/bin/env python3
"""
Discover GitHub repos related to awesome-game-security themes, review them
with Cursor CLI (two passes), edit README.md only when confirmed, and commit
directly to main (Contents API — no git push / no PR).

Flow:
  1. Build gh search queries from README.md `##` / `>` headings (+ topic boosters)
  2. Dedupe against README, rank/cap candidates
  3. Cursor CLI pass 1 — relevance screen → screen.json (no README edits kept)
  4. Cursor CLI pass 2 — independent confirm + place into existing section
  5. Script validation gate (section exists, URL in README, ⊆ shortlist)
  6. Commit validated README edits to main via Contents API

Prerequisites:
    curl https://cursor.com/install -fsS | bash
    export CURSOR_API_KEY=<your key from https://cursor.com/settings>
    gh auth status

Usage:
    python3 scripts/discover-repos-cli.py --list-queries
    python3 scripts/discover-repos-cli.py --dry-run
    python3 scripts/discover-repos-cli.py --commit
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import quote

ROOT_DIR = Path(__file__).resolve().parent.parent
README_PATH = ROOT_DIR / "README.md"
DISCOVER_DIR = ROOT_DIR / ".github" / "discover"
CANDIDATES_PATH = DISCOVER_DIR / "candidates.json"
SCREEN_PATH = DISCOVER_DIR / "screen.json"
DECISION_PATH = DISCOVER_DIR / "decision.json"

DEFAULT_MODEL = "cursor-grok-4.5-high-fast"
SELF_REPO = "gmh5225/awesome-game-security"
_GH_BIN: str | None = None

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(line_buffering=True)
        sys.stderr.reconfigure(line_buffering=True)
    except Exception:
        pass

REPO_SLUG_RE = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$")
GITHUB_URL_RE = re.compile(
    r"https?://github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)",
    re.IGNORECASE,
)
ARCHIVE_PATH_RE = re.compile(
    r"(?:^|[\s/`])archive/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)(?:\.txt)?",
)
TOPIC_HINT_RE = re.compile(
    r"(game|cheat|anti[- ]?cheat|obfuscat|pack(?:er|ing)|vmprotect|themida|ollvm|"
    r"protect(?:ion|ed)?|harden(?:ing)?|dma|il2cpp|battleye|vanguard|ricochet|"
    r"easyanticheat|\beac\b|xigncode|byfron|faceit|kernel|driver|overlay|"
    r"inject|reverse.?engineer|memory.?edit|trainer|bypass|anticheat|"
    r"directx|opengl|vulkan|unreal|unity|godot|frida|magisk|ghidra|ida|"
    r"hwid|speedhack|wallhack|aimbot|hypervisor|efi|uefi|patchguard)",
    re.IGNORECASE,
)
HIGH_STAR_TOPIC_GATE = 2000

KEEP_RELS = frozenset(
    {
        "README.md",
        ".github/discover/candidates.json",
        ".github/discover/screen.json",
        ".github/discover/decision.json",
    }
)

DEFAULT_PER_QUERY_LIMIT = 8
SEARCH_MIN_INTERVAL_SEC = 2.2

SKIP_README_SECTIONS = frozenset(
    {
        "how to contribute?",
        "skills for ai agents",
        "contents",
        "donate",
    }
)

GENERIC_SUBS = frozenset(
    {
        "guide",
        "source",
        "tools",
        "api",
        "hook",
        "overlay",
        "compatibility",
        "emulation",
        "sample unpacker",
        "dump fix",
        "backup file",
        "backup drivers",
        "fuzzer",
        "opencv",
        "dynamic script",
        "sign tools",
        "black signature",
        "ui interface",
        "render/draw",
        "w2s",
        "rpm",
        "jwt / auth token",
        "location / geocoding",
        "mcp server",
        "mcp server security",
        "ai agents",
        "analysis framework",
        "driver unit test framework",
        "stress testing",
        "compile time",
        "lazy importer",
        "encrypt variable",
        "shellcode engine & tricks",
        "anti-cheat programming",
        "information system & forensics",
        "kernel mode winsock",
        "windows ring3 callback",
        "windows ring0 callback",
        "winows user dump analysis",
        "winows kernel dump analysis",
        "iot / smart devices",
        "cellular / sim",
        "ida themes",
        "ida signature database",
    }
)

TOPIC_BOOST_QUERIES: tuple[str, ...] = (
    "topic:anti-cheat",
    "topic:game-hacking",
    "topic:game-security",
    "topic:cheat-engine",
    "topic:game-engine",
    "topic:dma",
    "topic:reverse-engineering",
    "topic:obfuscation",
    "topic:code-protection",
    "topic:vmprotect",
    "topic:directx",
    "topic:vulkan",
    "topic:unreal-engine",
    "topic:unity3d",
    "topic:frida",
    "topic:ghidra",
    "topic:ida-pro",
)

ANTICHEAT_ALIASES: dict[str, tuple[str, ...]] = {
    "vac": ("VAC anti-cheat", "Valve Anti-Cheat"),
    "eac": ("EasyAntiCheat", "EAC anti-cheat"),
    "be": ("BattlEye", "BattlEye anti-cheat"),
    "equ8": ("EQU8 anti-cheat",),
    "ricochet": ("Ricochet anti-cheat",),
    "riot": ("Riot Vanguard", "Vanguard anti-cheat"),
    "xigncode": ("XignCode", "XignCode3"),
    "ace": ("ACE anti-cheat", "Tencent ACE"),
    "g-presto": ("G-Presto anti-cheat",),
    "neacsafe": ("NeacSafe",),
    "badlionanticheat": ("Badlion AntiCheat",),
    "byfron": ("Byfron", "Hyperion anti-cheat"),
    "faceit": ("FACEIT anti-cheat",),
    "cs2": ("CS2 anti-cheat",),
}

BROAD_QUERY_MARKERS: tuple[str, ...] = (
    "topic:obfuscation",
    "topic:code-protection",
    "topic:vmprotect",
    "topic:reverse-engineering",
    "topic:directx",
    "topic:vulkan",
    "topic:unreal-engine",
    "topic:unity3d",
    "topic:frida",
    "topic:ghidra",
    "topic:ida-pro",
    "topic:game-engine",
)

_BROAD_QUERY_SET: set[str] = set(BROAD_QUERY_MARKERS)
_SEARCH_LOCK = threading.Lock()
_LAST_SEARCH_TS = 0.0


def is_core_query(q: str) -> bool:
    return q not in _BROAD_QUERY_SET


def _throttle_search() -> None:
    global _LAST_SEARCH_TS
    with _SEARCH_LOCK:
        now = time.monotonic()
        wait = SEARCH_MIN_INTERVAL_SEC - (now - _LAST_SEARCH_TS)
        if wait > 0:
            time.sleep(wait)
        _LAST_SEARCH_TS = time.monotonic()


def _clean_heading(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s*\[[^\]]*\]\s*$", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _split_prefixed(sub: str) -> tuple[str, str] | None:
    if ":" not in sub:
        return None
    prefix, rest = sub.split(":", 1)
    prefix, rest = prefix.strip(), rest.strip()
    if not prefix or not rest:
        return None
    return prefix, rest


def _dedupe_queries(queries: list[str]) -> list[str]:
    seen: set[str] = set()
    uniq: list[str] = []
    for q in queries:
        q = re.sub(r"\s+", " ", q).strip()
        if not q:
            continue
        key = q.lower()
        if key in seen:
            continue
        seen.add(key)
        uniq.append(q)
    return uniq


def queries_from_section(section: str) -> list[str]:
    s = _clean_heading(section)
    low = s.lower()
    out: list[str] = []

    if low == "anti cheat":
        out.extend(["Anti Cheat", "anti-cheat", "anticheat", "kernel anti cheat"])
    elif low == "cheat":
        out.extend(["Cheat", "game cheat", "game hacking", "game hack"])
    elif low == "game engine":
        out.extend(["Game Engine", "custom game engine"])
    elif low == "game develop":
        out.extend(["Game Develop", "game development"])
    elif low == "game network":
        out.extend(["Game Network", "game networking"])
    elif low == "game hot patch":
        out.extend(["Game Hot Patch", "game hotfix"])
    elif low == "game testing":
        out.extend(["Game Testing", "game test automation"])
    elif low == "game tools":
        out.append("Game Tools")
    elif low == "windows security features":
        out.extend(
            [
                "Windows Security Features",
                "PatchGuard",
                "HVCI",
                "Driver Signature Enforcement",
            ]
        )
    elif low == "some tricks":
        out.extend(["Windows kernel tricks", "Ring0 game security"])
    elif low in {"wsl", "wsa"}:
        out.append(s)
    elif "emulator" in low:
        out.append(s)
        _BROAD_QUERY_SET.add(s)
    elif low in {"directx", "opengl", "vulkan"}:
        out.extend([s, f"{s} hook", f"{s} game"])
    elif low == "physx sdk":
        out.extend(["PhysX SDK", "PhysX", "NVIDIA PhysX"])
    elif low == "3d graphics":
        out.extend(["3D Graphics", "3D graphics game"])
    elif low == "ai":
        out.extend(["AI", "game AI machine learning"])
    elif low == "renderer":
        out.extend(["Renderer", "game renderer"])
    elif low in {
        "mathematics",
        "image codec",
        "wavefront obj",
        "task scheduler",
        "game assets",
        "game manager",
        "game ci",
        "game boy",
        "gamecube/wii",
        "nintendo 3ds",
        "nintendo switch",
        "xbox",
        "playstation",
    }:
        if low in {"xbox", "playstation"}:
            out.extend([f"{s} emulator", f"{s} reverse engineering"])
        else:
            out.append(s)
        for q in out:
            _BROAD_QUERY_SET.add(q)
    else:
        out.append(s)
    return out


def queries_from_subcategory(section: str, sub: str) -> list[str]:
    section = _clean_heading(section)
    sub = _clean_heading(sub)
    if not sub:
        return []

    low_sub = sub.lower()
    out: list[str] = []

    if low_sub in GENERIC_SUBS:
        if low_sub in {"guide", "source", "tools", "api"}:
            return []
        return [f"{section} {sub}"]

    prefixed = _split_prefixed(sub)
    if prefixed:
        prefix, rest = prefixed
        pl = prefix.lower()
        rest_clean = _clean_heading(rest)

        if pl == "game":
            return [f"{rest_clean} cheat"]
        if pl == "detection":
            return [f"{rest_clean} detection"]
        if pl == "explore anticheat system":
            key = re.sub(r"[^a-z0-9-]+", "", rest_clean.lower())
            aliases = ANTICHEAT_ALIASES.get(key)
            return list(aliases) if aliases else [f"{rest_clean} anti-cheat"]
        if pl == "injection":
            return [f"{rest_clean} injection game"]
        if pl.startswith("game engine"):
            out.append(f"{rest_clean} game engine")
            if "protection" in pl:
                out.append(f"{rest_clean} protection")
            elif "plugin" in pl:
                out.append(f"{rest_clean} plugin")
            elif "explorer" in pl:
                out.append(f"{rest_clean} SDK")
            return out
        if pl.startswith("explore"):
            return [f"{rest_clean} {section}"]
        return [f"{prefix} {rest_clean}"]

    if section.lower() == "some tricks":
        return [f"{sub} game security", f"{sub} kernel"]

    out.append(sub)
    if low_sub in {
        "dma",
        "hwid",
        "hide",
        "frida",
        "magisk",
        "xposed",
        "wine",
        "decompiler",
        "screenshot",
        "debugging",
        "hook",
        "overlay",
        "linux",
        "android",
    }:
        out.append(f"{sub} {section}")

    if low_sub == "fix vmp":
        out.extend(["VMProtect", "VMP unpack"])
    elif low_sub == "fix themida":
        out.extend(["Themida", "Themida unpack"])
    elif low_sub == "fix ollvm":
        out.extend(["OLLVM", "OLLVM deobfuscate"])
    elif low_sub == "binary packer":
        out.extend(["binary packer", "PE packer"])
    elif low_sub == "obfuscation engine":
        out.extend(["code obfuscation", "obfuscation engine"])
    elif low_sub == "dma":
        out.extend(["DMA cheat", "pcileech", "FPGA DMA"])
    elif low_sub == "efi driver":
        out.extend(["UEFI cheat", "EFI driver game"])
    elif low_sub == "vulnerable driver":
        out.extend(["vulnerable driver", "BYOVD"])
    elif low_sub == "dynamic binary instrumentation":
        out.append("dynamic binary instrumentation")
    elif low_sub == "triggerbot & aimbot":
        out.extend(["aimbot detection", "triggerbot"])
    elif low_sub == "ida plugins":
        out.append("IDA Pro plugin")
    elif low_sub == "ghidra plugins":
        out.append("Ghidra plugin")
    elif low_sub == "cheat engine plugins":
        out.append("Cheat Engine plugin")

    return out


def build_queries_from_readme(readme_text: str | None = None) -> list[str]:
    text = (
        readme_text
        if readme_text is not None
        else README_PATH.read_text(encoding="utf-8", errors="replace")
    )
    queries: list[str] = []
    current_section: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("## "):
            title = _clean_heading(line[3:])
            if title.lower() in SKIP_README_SECTIONS:
                current_section = None
                continue
            current_section = title
            queries.extend(queries_from_section(title))
            continue
        if line.startswith("> ") and current_section:
            sub = _clean_heading(line[2:])
            if sub.startswith("Show respect"):
                continue
            queries.extend(queries_from_subcategory(current_section, sub))

    queries.extend(TOPIC_BOOST_QUERIES)

    for q in queries:
        ql = q.lower()
        if any(
            k in ql
            for k in (
                "mathematics",
                "image codec",
                "wavefront",
                "task scheduler",
                "game assets",
                "game manager",
                "game ci",
                "game boy",
                "gamecube",
                "nintendo",
                "emulator",
            )
        ):
            _BROAD_QUERY_SET.add(q)

    return _dedupe_queries(queries)


def prioritize_queries(queries: list[str], max_queries: int) -> list[str]:
    if max_queries <= 0 or len(queries) <= max_queries:
        return queries

    def _bucket(q: str) -> int:
        ql = q.lower()
        if ql.startswith("topic:"):
            return 0
        if any(
            k in ql
            for k in (
                "anti-cheat",
                "anticheat",
                "anti cheat",
                "game cheat",
                "game hacking",
                "battleye",
                "easyanticheat",
                "vanguard",
                "obfuscat",
                "vmprotect",
                "themida",
                "dma",
                "pcileech",
                "byovd",
                "injection",
                "detection",
            )
        ):
            return 1
        if ql.endswith(" cheat") or " anti-cheat" in ql:
            return 2
        if is_core_query(q):
            return 3
        return 4

    ranked = sorted(enumerate(queries), key=lambda it: (_bucket(it[1]), it[0]))
    kept = {q for _, q in ranked[:max_queries]}
    return [q for q in queries if q in kept]


# ---------------------------------------------------------------------------
# Helpers / discovery
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


def find_gh_bin() -> str:
    global _GH_BIN
    if _GH_BIN:
        return _GH_BIN
    path = shutil.which("gh")
    if not path:
        sys.exit("ERROR: GitHub CLI `gh` not found on PATH.")
    _GH_BIN = path
    return path


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT_DIR,
        capture_output=True,
        check=check,
    )


def _gh(
    *args: str,
    check: bool = True,
    timeout: int | None = 120,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [find_gh_bin(), *args],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        check=check,
        timeout=timeout,
    )


def normalize_slug(owner: str, repo: str) -> str:
    return f"{owner}/{repo.removesuffix('.git')}"


def slugs_from_readme_text(text: str) -> set[str]:
    slugs: set[str] = set()
    for m in GITHUB_URL_RE.finditer(text):
        slugs.add(normalize_slug(m.group(1), m.group(2)).lower())
    for m in ARCHIVE_PATH_RE.finditer(text):
        slugs.add(normalize_slug(m.group(1), m.group(2)).lower())
    slugs.add(SELF_REPO.lower())
    return slugs


def existing_readme_slugs() -> set[str]:
    """Slugs currently present in the working-tree README.md."""
    text = README_PATH.read_text(encoding="utf-8", errors="replace")
    return slugs_from_readme_text(text)


def readme_text_at_head() -> str | None:
    """Committed README at HEAD (pre-agent edits)."""
    proc = _git("show", "HEAD:README.md", check=False)
    if proc.returncode != 0:
        return None
    return (proc.stdout or b"").decode("utf-8", errors="replace")


def existing_readme_slugs_at_head() -> set[str]:
    """
    Slugs from HEAD README — use this for duplicate checks after Pass 2,
    because the working tree already contains newly inserted candidates.
    """
    text = readme_text_at_head()
    if text is None:
        # Detached / missing blob: fall back to empty (+ self), never the
        # post-edit working tree (that would false-positive every approval).
        return {SELF_REPO.lower()}
    return slugs_from_readme_text(text)


def lookback_date(days: int) -> str:
    return (date.today() - timedelta(days=days)).isoformat()


def build_search_query(base: str, *, min_stars: int, pushed_after: str) -> str:
    return " ".join(
        [
            base.strip(),
            "fork:false",
            f"stars:>={min_stars}",
            f"pushed:>{pushed_after}",
        ]
    )


def search_repos(
    query: str,
    *,
    limit: int,
    min_stars: int,
    pushed_after: str,
    retries: int = 2,
) -> list[dict[str, Any]]:
    full_q = build_search_query(query, min_stars=min_stars, pushed_after=pushed_after)
    args = [
        "search",
        "repos",
        "--limit",
        str(limit),
        "--json",
        "fullName,description,url,stargazersCount,updatedAt,isFork,isArchived",
        "--",
        full_q,
    ]
    last_err = ""
    for attempt in range(1, retries + 2):
        _throttle_search()
        proc = _gh(*args, check=False, timeout=90)
        if proc.returncode == 0:
            try:
                rows = json.loads(proc.stdout or "[]")
            except json.JSONDecodeError:
                print(f"  [WARN] invalid JSON for query {query!r}")
                return []
            return rows if isinstance(rows, list) else []
        last_err = (proc.stderr or proc.stdout or "").strip()[:300]
        if attempt <= retries and any(
            code in last_err
            for code in ("502", "503", "403", "rate limit", "secondary rate")
        ):
            time.sleep(2 * attempt)
            continue
        break
    print(f"  [WARN] search failed for {query!r}: {last_err}")
    return []


def discover_candidates(
    queries: list[str],
    *,
    lookback_days: int,
    max_candidates: int,
    min_stars: int,
    per_query_limit: int,
    search_workers: int = 2,
) -> list[dict[str, Any]]:
    pushed_after = lookback_date(lookback_days)
    known = existing_readme_slugs()
    print(f"README known slugs   : {len(known)}")
    print(f"Lookback             : {lookback_days} day(s) (pushed:>{pushed_after})")
    print(f"Min stars            : {min_stars}")
    print(f"Queries              : {len(queries)}")
    print(f"Per-query limit      : {per_query_limit}")
    print(f"Search workers       : {search_workers}")
    print(f"Max candidates       : {max_candidates}")

    seen: dict[str, dict[str, Any]] = {}
    skipped_known = skipped_fork = skipped_archived = skipped_noise = 0

    def _one(q: str) -> tuple[str, list[dict[str, Any]]]:
        return q, search_repos(
            q,
            limit=per_query_limit,
            min_stars=min_stars,
            pushed_after=pushed_after,
        )

    def _passes_topic_gate(full: str, description: str, stars: int) -> bool:
        if stars < HIGH_STAR_TOPIC_GATE:
            return True
        return bool(TOPIC_HINT_RE.search(f"{full} {description}"))

    workers = max(1, min(search_workers, len(queries) or 1))
    results: list[tuple[str, list[dict[str, Any]]]] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_one, q): q for q in queries}
        done_n = 0
        for fut in as_completed(futures):
            done_n += 1
            q, rows = fut.result()
            print(f"[{done_n}/{len(queries)}] search: {q} → {len(rows)} hit(s)")
            results.append((q, rows))

    for q, rows in results:
        for row in rows:
            full = (row.get("fullName") or "").strip()
            if not REPO_SLUG_RE.fullmatch(full):
                continue
            key = full.lower()
            if key in known:
                skipped_known += 1
                continue
            if row.get("isFork"):
                skipped_fork += 1
                continue
            if row.get("isArchived"):
                skipped_archived += 1
                continue
            if key == SELF_REPO.lower():
                continue
            desc = (row.get("description") or "").strip()
            stars = int(row.get("stargazersCount") or 0)
            if not _passes_topic_gate(full, desc, stars):
                skipped_noise += 1
                continue
            if key not in seen:
                seen[key] = {
                    "fullName": full,
                    "url": f"https://github.com/{key}",
                    "description": desc,
                    "stargazersCount": stars,
                    "updatedAt": row.get("updatedAt") or "",
                    "isArchived": False,
                    "matchedQueries": [q],
                }
            else:
                mq = seen[key]["matchedQueries"]
                if q not in mq:
                    mq.append(q)

    def _rank_key(r: dict[str, Any]) -> tuple[int, int, int, str]:
        mq = r.get("matchedQueries") or []
        return (
            sum(1 for q in mq if is_core_query(q)),
            len(mq),
            int(r["stargazersCount"]),
            r.get("updatedAt") or "",
        )

    core_ranked = sorted(
        (
            r
            for r in seen.values()
            if any(is_core_query(q) for q in r["matchedQueries"])
        ),
        key=_rank_key,
        reverse=True,
    )
    broad_ranked = sorted(
        (
            r
            for r in seen.values()
            if not any(is_core_query(q) for q in r["matchedQueries"])
        ),
        key=_rank_key,
        reverse=True,
    )
    capped = (core_ranked + broad_ranked)[:max_candidates]

    print(f"\nUnique new candidates: {len(seen)}")
    print(f"Skipped (in README)  : {skipped_known}")
    print(f"Skipped (fork)       : {skipped_fork}")
    print(f"Skipped (archived)   : {skipped_archived}")
    print(f"Skipped (noise gate) : {skipped_noise}")
    print(f"Core-tier            : {len(core_ranked)}")
    print(f"Broad-tier           : {len(broad_ranked)}")
    print(f"Capped to            : {len(capped)}")
    print(f"CANDIDATE_COUNT={len(capped)}")
    return capped


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path.relative_to(ROOT_DIR)}")


def write_candidates(candidates: list[dict[str, Any]]) -> None:
    write_json(
        CANDIDATES_PATH,
        {
            "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "selfRepo": SELF_REPO,
            "count": len(candidates),
            "candidates": candidates,
        },
    )


# ---------------------------------------------------------------------------
# README section index + validation
# ---------------------------------------------------------------------------


def readme_heading_index(readme_text: str | None = None) -> dict[str, set[str]]:
    text = (
        readme_text
        if readme_text is not None
        else README_PATH.read_text(encoding="utf-8", errors="replace")
    )
    index: dict[str, set[str]] = {}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            title = _clean_heading(line[3:])
            if title.lower() in SKIP_README_SECTIONS:
                current = None
                continue
            current = title.lower()
            index.setdefault(current, set())
            continue
        if line.startswith("> ") and current:
            sub = _clean_heading(line[2:])
            if sub and not sub.startswith("Show respect"):
                index[current].add(sub.lower())
    return index


def parse_section_ref(section: str) -> tuple[str, str | None] | None:
    s = (section or "").strip()
    if not s:
        return None
    s = re.sub(r"^#+\s*", "", s)
    if ">" in s:
        left, right = s.split(">", 1)
        cat = _clean_heading(left).lower()
        sub = _clean_heading(right).lower()
        if not cat:
            return None
        return cat, sub or None
    cat = _clean_heading(s).lower()
    return (cat, None) if cat else None


def section_exists_in_readme(
    section: str, heading_index: dict[str, set[str]]
) -> bool:
    parsed = parse_section_ref(section)
    if not parsed:
        return False
    cat, sub = parsed
    if cat not in heading_index:
        return False
    if sub is None:
        return True
    return sub in heading_index[cat]


# ---------------------------------------------------------------------------
# Cursor CLI two-pass review
# ---------------------------------------------------------------------------


def build_screen_prompt(candidate_count: int) -> str:
    return f"""\
You are PASS 1 of 2 for curating awesome-game-security.

Goal: shortlist candidates that are TRULY on-topic for this README taxonomy.
Do NOT edit README.md in this pass.

Read first:
1. `.claude/skills/overview/SKILL.md`
2. `README.md` headings (`##` / `>`) — learn where things belong
3. `.github/discover/candidates.json` — {candidate_count} candidates

For EACH candidate:
1. Inspect with:
   `gh repo view OWNER/REPO --json nameWithOwner,description,url,stargazersCount,repositoryTopics,isArchived,isFork,updatedAt,homepageUrl`
2. Optionally peek at README:
   `gh api repos/OWNER/REPO/readme -H "Accept: application/vnd.github.raw"` (keep short)
3. Decide shortlist or reject.

Shortlist ONLY if ALL hold:
- Clearly related to this list's themes (game security / hacking / anti-cheat,
  game engines or graphics APIs in a security-relevant way, Windows kernel
  protection for games, DMA, reverse engineering for games, mobile game security,
  OR obfuscation / packer / binary protection / hardening relevant here)
- Not empty stub, spam, pure mirror, adware, or unrelated megaproject
- Not a near-duplicate of something already in README
- You can name an EXISTING README section for it:
  format exactly like `## Category > Subcategory` or `## Category`
  (Category/Subcategory must already exist in README.md — do not invent sections)

Reject when uncertain. Precision over recall.

Write ONLY `.github/discover/screen.json` with this shape:
```json
{{
  "pass": 1,
  "shortlisted": [
    {{
      "fullName": "owner/repo",
      "url": "https://github.com/owner/repo",
      "proposedSection": "## Cheat > DMA",
      "proposedDescription": "brief description",
      "reason": "why related to this README"
    }}
  ],
  "rejected": [
    {{
      "fullName": "owner/repo",
      "reason": "why skipped"
    }}
  ]
}}
```

Every candidate must appear in shortlisted or rejected.

Hard constraints:
- ONLY create/update `.github/discover/screen.json`
- Do NOT modify README.md or any other path
- Do NOT git commit/push or open PRs
- Do NOT include {SELF_REPO}
- When finished, print: Done: screen N shortlisted
"""


def build_confirm_prompt(shortlist_count: int) -> str:
    return f"""\
You are PASS 2 of 2 for curating awesome-game-security.

Goal: INDEPENDENTLY re-confirm Pass 1 shortlist, then edit README ONLY for
repos that still pass — and ONLY when a suitable existing section is clear.

Read first:
1. `.claude/skills/overview/SKILL.md`
2. `README.md` (current structure and nearby entries)
3. `.github/discover/screen.json` — Pass 1 shortlist ({shortlist_count} item(s))
4. `.github/discover/candidates.json` — original discovery metadata (context only)

For EACH shortlisted repo, re-check from scratch (do not rubber-stamp Pass 1):
1. Re-inspect with `gh repo view` / short README peek
2. Confirm it is truly relevant to this README's themes
3. Confirm an EXISTING `##` / `>` placement is appropriate
4. Confirm it is not already listed and not a near-duplicate

Confirm (approve) ONLY if ALL hold; otherwise reject in this pass.

If you confirm one or more repos:
1. Edit ONLY `README.md`
2. Insert each confirmed repo as ONE line in the correct existing section:
   `- https://github.com/owner/repo [brief description]`
3. Description must be short and accurate; do not invent features
4. Do not reorder unrelated entries; insert near related items when obvious
5. Do not touch Contents/TOC
6. Do not create new `##` or `>` headings

If NONE are confirmed: do not change README.md.

Always write `.github/discover/decision.json`:
```json
{{
  "pass": 2,
  "approved": [
    {{
      "fullName": "owner/repo",
      "url": "https://github.com/owner/repo",
      "section": "## Cheat > DMA",
      "description": "brief description used in README",
      "reason": "why confirmed in pass 2",
      "pass1Section": "## Cheat > DMA"
    }}
  ],
  "rejected": [
    {{
      "fullName": "owner/repo",
      "reason": "why rejected in pass 2"
    }}
  ]
}}
```

Every Pass-1 shortlisted repo must appear in approved or rejected.
Do not approve any repo that was not shortlisted in screen.json.

Hard constraints:
- ONLY modify/create: `README.md` and `.github/discover/decision.json`
- Do NOT git commit/push or open PRs
- Do NOT touch other paths
- Do NOT include {SELF_REPO}
- When finished, print: Done: confirm N approved
"""


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
        print(prompt[:800])
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
        print(
            f"  exit={proc.returncode}  "
            f"elapsed={time.time() - started:.1f}s (no --trust)"
        )
    return proc.returncode


def _discard_path(rel: str) -> None:
    path = ROOT_DIR / rel
    checked = _git("checkout", "--", rel, check=False)
    if checked.returncode != 0 and path.exists():
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)


def discard_side_effects() -> None:
    proc = _git("ls-files", "-m", "-o", "--exclude-standard", check=False)
    for line in proc.stdout.decode().splitlines():
        rel = line.strip()
        if not rel or rel in KEEP_RELS:
            continue
        _discard_path(rel)


def revert_readme() -> None:
    _git("checkout", "--", "README.md", check=False)


def load_json_file(path: Path) -> dict[str, Any] | None:
    if not path.is_file() or path.stat().st_size == 0:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"WARNING: {path.name} invalid JSON: {e}")
        return None
    return data if isinstance(data, dict) else None


def load_screen() -> dict[str, Any] | None:
    data = load_json_file(SCREEN_PATH)
    if data is None:
        return None
    data.setdefault("shortlisted", [])
    data.setdefault("rejected", [])
    if not isinstance(data["shortlisted"], list):
        data["shortlisted"] = []
    if not isinstance(data["rejected"], list):
        data["rejected"] = []
    return data


def load_decision() -> dict[str, Any] | None:
    data = load_json_file(DECISION_PATH)
    if data is None:
        return None
    data.setdefault("approved", [])
    data.setdefault("rejected", [])
    if not isinstance(data["approved"], list):
        data["approved"] = []
    if not isinstance(data["rejected"], list):
        data["rejected"] = []
    return data


def candidate_slug_set(candidates: list[dict[str, Any]]) -> set[str]:
    out: set[str] = set()
    for c in candidates:
        full = (c.get("fullName") or "").strip()
        if REPO_SLUG_RE.fullmatch(full):
            out.add(full.lower())
    return out


def normalize_item_slug(item: dict[str, Any]) -> str | None:
    full = (item.get("fullName") or "").strip()
    if REPO_SLUG_RE.fullmatch(full):
        return full.lower()
    url = (item.get("url") or "").strip()
    m = GITHUB_URL_RE.search(url)
    if not m:
        return None
    slug = normalize_slug(m.group(1), m.group(2))
    return slug.lower() if REPO_SLUG_RE.fullmatch(slug) else None


def github_slug_from_url(url: str) -> str | None:
    """owner/repo from a GitHub URL; lowercase, strips .git. None if not parseable."""
    m = GITHUB_URL_RE.search((url or "").strip())
    if not m:
        return None
    slug = normalize_slug(m.group(1), m.group(2)).lower()
    return slug if REPO_SLUG_RE.fullmatch(slug) else None


def item_github_url(item: dict[str, Any]) -> str | None:
    slug = normalize_item_slug(item)
    if not slug:
        return None
    # Always canonicalize: lowercase slug, no .git, https — avoids case/.git
    # mismatches against README lines written by the agent.
    return f"https://github.com/{slug}"


def readme_has_diff() -> bool:
    return bool(_git("diff", "--", "README.md", check=False).stdout.strip())


def readme_contains_url(url: str, readme_text: str | None = None) -> bool:
    """True if README mentions this repo (slug match; not raw substring)."""
    target = github_slug_from_url(url)
    if not target:
        return False
    text = (
        readme_text
        if readme_text is not None
        else README_PATH.read_text(encoding="utf-8", errors="replace")
    )
    for m in GITHUB_URL_RE.finditer(text):
        if normalize_slug(m.group(1), m.group(2)).lower() == target:
            return True
    return False


def remove_urls_from_readme(urls: list[str]) -> int:
    """
    Remove list-entry lines that mention the given GitHub URLs.
    Used when Pass 2 inserted a row that later failed script validation.
    Matches by exact owner/repo slug (case-insensitive), not substring — so
    demoting owner/repo never deletes owner/repo-extra.
    """
    slugs = {s for u in urls if (s := github_slug_from_url(u))}
    if not slugs:
        return 0
    text = README_PATH.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    kept_lines: list[str] = []
    removed = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("-"):
            m = GITHUB_URL_RE.search(line)
            if m and normalize_slug(m.group(1), m.group(2)).lower() in slugs:
                removed += 1
                continue
        kept_lines.append(line)
    if removed:
        README_PATH.write_text("".join(kept_lines), encoding="utf-8")
        print(f"  [confirm] removed {removed} README line(s)")
    return removed


def _canonical_full_name(
    slug: str, candidates: list[dict[str, Any]]
) -> str:
    for c in candidates:
        if c["fullName"].lower() == slug:
            return c["fullName"]
    return slug


def validate_screen(
    screen: dict[str, Any],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    allowed = candidate_slug_set(candidates)
    heading_index = readme_heading_index()
    # Pre-pass-2 working tree == HEAD for README (pass 1 reverts edits).
    known = existing_readme_slugs()
    cleaned: list[dict[str, Any]] = []
    dropped = 0

    for item in screen.get("shortlisted") or []:
        if not isinstance(item, dict):
            dropped += 1
            continue
        slug = normalize_item_slug(item)
        if (
            not slug
            or slug not in allowed
            or slug in known
            or slug == SELF_REPO.lower()
        ):
            dropped += 1
            continue
        section = (item.get("proposedSection") or "").strip()
        if not section_exists_in_readme(section, heading_index):
            print(f"  [screen] drop {slug}: proposed section missing: {section!r}")
            dropped += 1
            continue
        item = dict(item)
        item["fullName"] = _canonical_full_name(slug, candidates)
        item["url"] = item_github_url(item) or f"https://github.com/{item['fullName']}"
        cleaned.append(item)

    if dropped:
        print(f"  [screen] dropped {dropped} invalid shortlist item(s)")
    screen["shortlisted"] = cleaned
    write_json(SCREEN_PATH, screen)
    return cleaned


def validate_decision(
    decision: dict[str, Any],
    shortlisted: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
) -> dict[str, Any]:
    allowed_short = {s for s in (normalize_item_slug(x) for x in shortlisted) if s}
    allowed_cand = candidate_slug_set(candidates)
    heading_index = readme_heading_index()
    # IMPORTANT: duplicate check must use HEAD, not the post-edit working tree.
    known_before = existing_readme_slugs_at_head()
    readme_text = README_PATH.read_text(encoding="utf-8", errors="replace")

    kept: list[dict[str, Any]] = []
    demoted: list[dict[str, Any]] = []
    demoted_urls: list[str] = []

    for item in decision.get("approved") or []:
        if not isinstance(item, dict):
            continue
        slug = normalize_item_slug(item)
        url = item_github_url(item)
        reason = None
        if not slug:
            reason = "invalid fullName/url"
        elif slug not in allowed_cand:
            reason = "not in discovery candidates"
        elif slug not in allowed_short:
            reason = "not in pass-1 shortlist"
        elif slug in known_before:
            reason = "already in README / self-repo"
        else:
            section = (item.get("section") or "").strip()
            if not section_exists_in_readme(section, heading_index):
                reason = f"section does not exist: {section!r}"
            elif not url or not readme_contains_url(url, readme_text):
                reason = "URL not found in README.md after confirm pass"

        if reason:
            print(f"  [confirm] demote {slug or '?'}: {reason}")
            demoted.append(
                {
                    "fullName": item.get("fullName") or slug or "?",
                    "reason": f"script validation: {reason}",
                }
            )
            # If Pass 2 inserted a row that we are rejecting, strip it.
            if url and reason != "URL not found in README.md after confirm pass":
                demoted_urls.append(url)
            continue

        item = dict(item)
        item["fullName"] = _canonical_full_name(slug, candidates)  # type: ignore[arg-type]
        item["url"] = url or f"https://github.com/{item['fullName']}"
        kept.append(item)

    if demoted_urls:
        remove_urls_from_readme(demoted_urls)

    # Drop accidental Pass-2 insertions that are not in the validated approved set.
    # Compare against HEAD so pre-existing README entries are never removed.
    approved_slugs = {
        s for s in (normalize_item_slug(x) for x in kept) if s
    }
    extra_urls = _unapproved_added_readme_urls(approved_slugs, known_before)
    if extra_urls:
        print(
            f"  [confirm] stripping {len(extra_urls)} unapproved README addition(s)"
        )
        remove_urls_from_readme(extra_urls)

    # Re-verify kept URLs survived cleanup; dedupe by slug.
    readme_text = README_PATH.read_text(encoding="utf-8", errors="replace")
    still_kept: list[dict[str, Any]] = []
    seen_kept: set[str] = set()
    for item in kept:
        slug = normalize_item_slug(item)
        url = item_github_url(item)
        if not slug or slug in seen_kept:
            continue
        if url and readme_contains_url(url, readme_text):
            seen_kept.add(slug)
            still_kept.append(item)
        else:
            demoted.append(
                {
                    "fullName": item.get("fullName") or slug or "?",
                    "reason": (
                        "script validation: URL missing after README cleanup"
                    ),
                }
            )
    kept = still_kept

    rejected = [r for r in (decision.get("rejected") or []) if isinstance(r, dict)]
    rejected.extend(demoted)
    decision["approved"] = kept
    decision["rejected"] = rejected
    decision["pass"] = 2
    decision["validated"] = True
    write_json(DECISION_PATH, decision)
    print(f"  [confirm] validated approved={len(kept)} demoted={len(demoted)}")
    return decision


def _unapproved_added_readme_urls(
    approved_slugs: set[str],
    known_before: set[str],
) -> list[str]:
    """GitHub list URLs added since HEAD that are not in approved_slugs."""
    text = README_PATH.read_text(encoding="utf-8", errors="replace")
    extras: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        stripped = line.lstrip()
        if not stripped.startswith("-"):
            continue
        m = GITHUB_URL_RE.search(line)
        if not m:
            continue
        slug = normalize_slug(m.group(1), m.group(2)).lower()
        if slug in known_before or slug in approved_slugs:
            continue
        url = f"https://github.com/{normalize_slug(m.group(1), m.group(2))}"
        if url not in seen:
            seen.add(url)
            extras.append(url)
    return extras


def _proc_err_text(proc: subprocess.CompletedProcess[Any]) -> str:
    err = proc.stderr or ""
    out = proc.stdout or ""
    if isinstance(err, bytes):
        err = err.decode("utf-8", errors="replace")
    if isinstance(out, bytes):
        out = out.decode("utf-8", errors="replace")
    return f"{err}\n{out}".strip()


def _is_transient_git_remote_error(err: str) -> bool:
    low = err.lower()
    return any(
        tok in low
        for tok in (
            "http 500",
            "http 502",
            "http 503",
            "http 429",
            "error 500",
            "error 502",
            "error 503",
            "timeout",
            "timed out",
            "unexpected disconnect",
            "remote end hung up",
            "rpc failed",
            "curl 22",
            "curl 56",
            "curl 28",
            "connection reset",
            "tls",
            "temporary failure",
            "internal server error",
            "secondary rate",
            "rate limit",
            "abuse detection",
            "http 409",
            "error 409",
            "sha does not match",
            "sha wasn't supplied",
        )
    )


def github_repo_slug() -> str:
    return (os.environ.get("GITHUB_REPOSITORY") or SELF_REPO).strip() or SELF_REPO


def gh_api_json(
    path: str,
    *,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    timeout: int = 120,
) -> Any:
    """Call `gh api` and parse JSON. Returns None for empty 204-style bodies."""
    cmd = [find_gh_bin(), "api", "--method", method, path]
    if body is not None:
        cmd.extend(["--input", "-"])
        proc = subprocess.run(
            cmd,
            cwd=ROOT_DIR,
            input=json.dumps(body),
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
    else:
        proc = subprocess.run(
            cmd,
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
    if proc.returncode != 0:
        raise RuntimeError(_proc_err_text(proc)[:600] or f"gh api {method} {path} failed")
    text = (proc.stdout or "").strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"gh api returned non-JSON: {e}: {text[:200]}") from e


def _api_with_retries(label: str, fn: Any, *, attempts: int = 5) -> Any:
    last_err = ""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except (RuntimeError, OSError, subprocess.TimeoutExpired) as e:
            last_err = str(e)
            print(f"{label} failed (attempt {attempt}/{attempts}): {last_err[:300]}")
            if attempt < attempts and _is_transient_git_remote_error(last_err):
                delay = min(2**attempt, 30)
                print(f"Transient API error — retrying in {delay}s ...")
                time.sleep(delay)
                continue
            break
    sys.exit(f"ERROR: {label} failed: {last_err[:400]}")


def commit_readme_via_contents_api(
    repo: str,
    branch: str,
    *,
    commit_message: str,
    readme_text: str,
) -> str:
    """
    Commit working-tree README.md to <branch> through the Contents API.
    Only uploads ~README size (hundreds of KB), never a git pack of the whole repo.
    """
    meta = gh_api_json(f"repos/{repo}/contents/README.md?ref={quote(branch, safe='')}")
    file_sha = (meta or {}).get("sha")
    if not file_sha:
        sys.exit("ERROR: cannot resolve README.md blob sha on branch via API")

    content_b64 = base64.b64encode(readme_text.encode("utf-8")).decode("ascii")
    # Contents API hard-limits content to 1 MiB encoded payload guidance (~1MB file).
    if len(content_b64) > 900_000:
        sys.exit(
            f"ERROR: README.md too large for Contents API "
            f"({len(readme_text)} bytes)"
        )

    print(
        f"Committing README.md on {branch} via Contents API "
        f"({len(readme_text)} bytes) ..."
    )
    result = gh_api_json(
        f"repos/{repo}/contents/README.md",
        method="PUT",
        body={
            "message": commit_message,
            "content": content_b64,
            "branch": branch,
            "sha": file_sha,
            "committer": {
                "name": "github-actions[bot]",
                "email": "41898282+github-actions[bot]@users.noreply.github.com",
            },
            "author": {
                "name": "github-actions[bot]",
                "email": "41898282+github-actions[bot]@users.noreply.github.com",
            },
        },
        timeout=180,
    )
    commit_sha = ((result or {}).get("commit") or {}).get("sha") or ""
    if not commit_sha:
        sys.exit("ERROR: Contents API commit returned no commit sha")
    print(f"Committed {commit_sha[:12]} on {branch} via API.")
    return commit_sha


def commit_to_main(
    decision: dict[str, Any],
    *,
    run_id: str = "",
) -> str | None:
    """
    Commit validated README.md edits directly to main via the Contents API.

    Avoids `git push` (this repo is multi-GB; pack protocol 500s in Actions).
    """
    approved = [a for a in (decision.get("approved") or []) if isinstance(a, dict)]
    if not approved:
        print("No validated approved repos — skipping commit.")
        return None
    if not decision.get("validated"):
        print("Decision not script-validated — refusing commit.")
        return None
    if not readme_has_diff():
        print("README.md unchanged — skipping commit.")
        return None

    readme_text = README_PATH.read_text(encoding="utf-8", errors="replace")
    for item in approved:
        url = item_github_url(item)
        if not url or not readme_contains_url(url, readme_text):
            print(f"Refusing commit: approved URL missing from README: {url}")
            return None

    n = len(approved)
    safe_run = re.sub(r"[^A-Za-z0-9._-]", "", run_id) or "local"
    msg = f"discover: add {n} repo(s) via Cursor CLI (2-pass) [{safe_run}]"

    discard_side_effects()
    readme_text = README_PATH.read_text(encoding="utf-8", errors="replace")
    if not readme_has_diff():
        print("README.md unchanged after cleanup — skipping commit.")
        return None

    repo = github_repo_slug()

    def _commit() -> str:
        return commit_readme_via_contents_api(
            repo,
            "main",
            commit_message=msg,
            readme_text=readme_text,
        )

    try:
        sha = _api_with_retries("commit README to main", _commit)
    finally:
        revert_readme()

    print(f"COMMIT_SHA={sha}")
    return sha or None


def run_two_pass_review(
    agent_bin: str,
    model: str,
    candidates: list[dict[str, Any]],
    *,
    dry_run: bool = False,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    print("\n=== Pass 1/2: relevance screen (no README edits) ===")
    code1 = run_agent(
        agent_bin, model, build_screen_prompt(len(candidates)), dry_run=dry_run
    )
    revert_readme()
    discard_side_effects()

    if dry_run:
        print("[DRY-RUN] pass 1 + pass 2 prompts only.")
        print("--- pass 2 prompt preview ---")
        print(build_confirm_prompt(0)[:600])
        return None, None

    screen = load_screen()
    if screen is None:
        sys.exit(
            f"ERROR: pass 1 finished (exit={code1}) but "
            f"{SCREEN_PATH.relative_to(ROOT_DIR)} is missing/invalid"
        )
    if code1 != 0:
        print(f"note: pass 1 exit={code1}, but screen.json present — continuing")

    shortlisted = validate_screen(screen, candidates)
    print(
        f"Pass 1 result: shortlisted={len(shortlisted)} "
        f"rejected={len(screen.get('rejected') or [])}"
    )
    if not shortlisted:
        print("Nothing shortlisted after pass 1 — no PR.")
        write_json(
            DECISION_PATH,
            {
                "pass": 2,
                "approved": [],
                "rejected": [
                    {
                        "fullName": "(none)",
                        "reason": "pass 1 shortlisted zero repos",
                    }
                ],
                "validated": True,
            },
        )
        return screen, load_decision()

    print("\n=== Pass 2/2: confirm relevance + README placement ===")
    code2 = run_agent(
        agent_bin,
        model,
        build_confirm_prompt(len(shortlisted)),
        dry_run=False,
    )
    discard_side_effects()

    decision = load_decision()
    if decision is None:
        revert_readme()
        sys.exit(
            f"ERROR: pass 2 finished (exit={code2}) but "
            f"{DECISION_PATH.relative_to(ROOT_DIR)} is missing/invalid"
        )
    if code2 != 0:
        print(f"note: pass 2 exit={code2}, but decision.json present — continuing")

    decision = validate_decision(decision, shortlisted, candidates)
    if not decision.get("approved"):
        print("No repos survived pass 2 + validation — reverting README.")
        revert_readme()
    elif not readme_has_diff():
        print("Approved set non-empty but README unchanged — clearing approved.")
        for item in list(decision.get("approved") or []):
            decision.setdefault("rejected", []).append(
                {
                    "fullName": item.get("fullName"),
                    "reason": "script validation: README not modified for approval",
                }
            )
        decision["approved"] = []
        decision["validated"] = True
        write_json(DECISION_PATH, decision)

    print(
        f"Pass 2 result: approved={len(decision.get('approved') or [])} "
        f"rejected={len(decision.get('rejected') or [])}"
    )
    return screen, decision


def parse_queries(
    raw: str | None,
    extra: list[str] | None,
    *,
    replace_defaults: bool = False,
) -> list[str]:
    extras: list[str] = []
    if raw:
        for part in re.split(r"\n|\|\|", raw):
            q = part.strip()
            if q:
                extras.append(q)
    if extra:
        for q in extra:
            q = q.strip()
            if q:
                extras.append(q)

    if replace_defaults and extras:
        return _dedupe_queries(extras)

    defaults = build_queries_from_readme()
    if not extras:
        return defaults
    return _dedupe_queries(defaults + extras)


def cleanup_runtime_files(*, keep_decision: bool = False) -> None:
    for path in (CANDIDATES_PATH, SCREEN_PATH):
        if path.exists():
            path.unlink(missing_ok=True)
    if not keep_decision and DECISION_PATH.exists():
        DECISION_PATH.unlink(missing_ok=True)
    if DISCOVER_DIR.is_dir() and not any(DISCOVER_DIR.iterdir()):
        DISCOVER_DIR.rmdir()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Discover theme-related GitHub repos via gh + 2-pass Cursor CLI"
    )
    parser.add_argument("--lookback-days", type=int, default=3)
    parser.add_argument("--max-candidates", type=int, default=30)
    parser.add_argument("--min-stars", type=int, default=3)
    parser.add_argument(
        "--per-query-limit", type=int, default=DEFAULT_PER_QUERY_LIMIT
    )
    parser.add_argument(
        "--max-queries",
        type=int,
        default=300,
        help="Cap README-derived queries after prioritization (0 = no cap)",
    )
    parser.add_argument(
        "--queries",
        nargs="*",
        default=None,
        help="Extra search queries appended to README-derived defaults",
    )
    parser.add_argument(
        "--queries-env",
        type=str,
        default="",
        help="Env var with queries separated by newlines or || (appended)",
    )
    parser.add_argument(
        "--queries-replace",
        action="store_true",
        default=False,
        help="Use only --queries/--queries-env (skip README headings)",
    )
    parser.add_argument(
        "--list-queries",
        action="store_true",
        default=False,
        help="Print README-derived search queries and exit",
    )
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Discovery + two-pass prompt preview; no agent / commit",
    )
    parser.add_argument(
        "--discover-only",
        action="store_true",
        default=False,
        help="Write candidates.json and exit (no agent)",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        default=False,
        help="After 2-pass validation, commit README.md directly to main (Contents API)",
    )
    parser.add_argument(
        "--create-pr",
        action="store_true",
        default=False,
        help=argparse.SUPPRESS,  # deprecated alias for --commit
    )
    parser.add_argument("--run-id", type=str, default="")
    parser.add_argument(
        "--skip-agent",
        action="store_true",
        default=False,
        help="Skip Cursor agent (discovery only)",
    )
    args = parser.parse_args()

    if args.lookback_days < 1:
        sys.exit("ERROR: --lookback-days must be >= 1")
    if args.max_candidates < 1:
        sys.exit("ERROR: --max-candidates must be >= 1")
    if args.min_stars < 0:
        sys.exit("ERROR: --min-stars must be >= 0")
    if args.per_query_limit < 1:
        sys.exit("ERROR: --per-query-limit must be >= 1")
    if args.max_queries < 0:
        sys.exit("ERROR: --max-queries must be >= 0")
    if not README_PATH.is_file():
        sys.exit("ERROR: README.md not found")

    if args.list_queries:
        queries = build_queries_from_readme()
        capped = prioritize_queries(queries, args.max_queries)
        print(f"QUERY_COUNT={len(queries)}")
        print(f"QUERY_COUNT_CAPPED={len(capped)} (max_queries={args.max_queries})")
        for q in capped:
            tier = "broad" if not is_core_query(q) else "core"
            print(f"  [{tier}] {q}")
        return

    find_gh_bin()

    queries_raw = ""
    if args.queries_env:
        queries_raw = os.environ.get(args.queries_env, "")
    queries = parse_queries(
        queries_raw,
        args.queries,
        replace_defaults=args.queries_replace,
    )
    before_cap = len(queries)
    if not args.queries_replace:
        queries = prioritize_queries(queries, args.max_queries)
    print(
        f"Search queries       : {len(queries)} "
        f"(README headings + topics; raw={before_cap}, max_queries={args.max_queries})"
    )

    candidates = discover_candidates(
        queries,
        lookback_days=args.lookback_days,
        max_candidates=args.max_candidates,
        min_stars=args.min_stars,
        per_query_limit=args.per_query_limit,
    )
    write_candidates(candidates)

    if candidates:
        for c in candidates[:20]:
            print(
                f"  - {c['fullName']} (★{c['stargazersCount']}) :: "
                f"{c['description'][:80]}"
            )
        if len(candidates) > 20:
            print(f"  ... and {len(candidates) - 20} more")

    if args.discover_only or args.skip_agent:
        print("\nDiscovery complete (no agent).")
        return

    if args.dry_run:
        print("\nDiscovery complete — dry-run two-pass prompt preview.")
        run_two_pass_review("agent", args.model, candidates, dry_run=True)
        print("[DRY-RUN] agents + commit skipped.")
        return

    if not candidates:
        print("No new candidates — nothing to review.")
        cleanup_runtime_files(keep_decision=False)
        return

    get_api_key()
    agent_bin = find_agent_bin()
    print(f"\nModel: {args.model}")
    _screen, decision = run_two_pass_review(
        agent_bin, args.model, candidates, dry_run=False
    )
    if decision is None:
        sys.exit("ERROR: two-pass review returned no decision")

    approved = decision.get("approved") or []
    print(
        f"\nFinal: approved={len(approved)} "
        f"validated={bool(decision.get('validated'))}"
    )

    do_commit = bool(args.commit or args.create_pr)
    if args.create_pr and not args.commit:
        print("note: --create-pr is deprecated; committing directly to main.")

    if not do_commit:
        print("README/decision left in working tree (--commit not set).")
        return

    if not approved or not decision.get("validated"):
        print("No validated approvals — not committing.")
        revert_readme()
        cleanup_runtime_files(keep_decision=False)
        return

    run_id = (
        args.run_id.strip()
        or os.environ.get("GITHUB_RUN_ID", "").strip()
        or "local"
    )
    sha = commit_to_main(decision, run_id=run_id)
    cleanup_runtime_files(keep_decision=False)
    discard_side_effects()
    if sha:
        print(f"Committed to main: {sha}")
    else:
        print("No commit created.")
        revert_readme()


if __name__ == "__main__":
    main()
