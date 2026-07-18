#!/usr/bin/env python3
"""
Discover repos from GitHub users tracked by github-follow-feed (following +
custom_users.txt), shallow-clone candidates, review with Cursor CLI (two
passes), and commit validated README additions to main via Contents API.

Flow:
  1. Load tracked logins: users/{source}/following + custom_users.txt
  2. List recently pushed non-fork repos owned by those users
  3. Dedupe against README, topic-prefilter, rank/cap
  4. Shallow-clone each candidate outside the workspace
  5. Cursor CLI pass 1 — relevance screen via local clone → screen.json
  6. Cursor CLI pass 2 — confirm + place into existing README section
  7. Script validation gate; commit via Contents API

Prerequisites:
    curl https://cursor.com/install -fsS | bash
    export CURSOR_API_KEY=<your key from https://cursor.com/settings>
    gh auth status

Usage:
    python3 scripts/discover-follow-repos-cli.py --self-test
    python3 scripts/discover-follow-repos-cli.py --list-users
    python3 scripts/discover-follow-repos-cli.py --discover-only
    python3 scripts/discover-follow-repos-cli.py --dry-run
    python3 scripts/discover-follow-repos-cli.py --commit
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
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from importlib import util as importlib_util
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent.parent


def _load_discover_repos_cli() -> Any:
    """Load scripts/discover-repos-cli.py (hyphenated filename)."""
    path = ROOT_DIR / "scripts" / "discover-repos-cli.py"
    spec = importlib_util.spec_from_file_location("discover_repos_cli", path)
    if spec is None or spec.loader is None:
        sys.exit(f"ERROR: cannot load {path}")
    mod = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


dr = _load_discover_repos_cli()
DEFAULT_SOURCE_USER = "gmh5225"
DEFAULT_FOLLOW_FEED_REPO = "gmh5225/github-follow-feed"
DEFAULT_CUSTOM_USERS_PATH = "custom_users.txt"
DEFAULT_MODEL = dr.DEFAULT_MODEL
CLONE_TIMEOUT = 180
DEFAULT_REPOS_PER_USER = 5
DEFAULT_USER_WORKERS = 4
LOGIN_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$")

# Pre-clone topic gate for follow-feed candidates.
# Edges use (?<![A-Za-z0-9])…(?![A-Za-z0-9]) so snake_case works ('_' is \w for \b,
# which would miss apex_dma_kvm / equ8_bypass) while still rejecting florida⊃ida
# and kdmapper⊃dma. Mega-star repos need FOLLOW_STRONG_HINT_RE.
_WB = r"(?<![A-Za-z0-9])"
_WE = r"(?![A-Za-z0-9])"


def _wb(token: str) -> str:
    """Token with underscore-friendly word edges."""
    return rf"{_WB}(?:{token}){_WE}"


FOLLOW_TOPIC_HINT_RE = re.compile(
    r"(?i)(?:"
    # Games / cheats / anti-cheat
    + _wb(r"games?")
    + r"|game[-_ ]?(?:hack|security|cheat|engine|overlay|mod)"
    + r"|"
    + _wb(r"cheats?|cheating")
    + r"|anti[-_ ]?cheat|anticheat"
    # Obfuscation / packers / protectors
    + r"|obfuscat\w*|"
    + _wb(r"pack(?:er|ing)")
    + r"|vmprotect|themida|ollvm|enigma[-_ ]?protector"
    + r"|"
    + _wb(r"protect(?:ion|ed)?|harden(?:ing)?")
    # DMA / AC vendors
    + r"|"
    + _wb(r"dma")
    + r"|pcileech|fpga[-_ ]?dma|il2cpp"
    + r"|battleye|vanguard|ricochet|easyanticheat|"
    + _wb(r"eac|vac|equ8|ace")
    + r"|xigncode|byfron|hyperion|faceit|neacsafe|g[-_ ]?presto|badlion"
    # Kernel / drivers / overlays / injection
    + r"|"
    + _wb(r"kernel|driver|overlay|trainer|bypass")
    + r"|"
    + _wb(r"inject(?:ion|or)?s?")
    + r"|speedhack|wallhack|aimbot|triggerbot|"
    + _wb(r"esp|offsets?|w2s")
    + r"|"
    + _wb(r"external|internal")
    # RE / memory / graphics / engines
    + r"|reverse[-_ ]?engineer(?:ing)?|memory[-_ ]?(?:edit|hack|tool|read|write)"
    + r"|"
    + _wb(r"directx|d3d\d*|dx\d*|opengl|vulkan|unreal|ue[45]|unity|godot")
    + r"|"
    + _wb(r"frida|magisk|zygisk|kernelsu|apatch|lsposed|xposed")
    + r"|"
    + _wb(r"ghidra|ida|ida[-_ ]?pro|x64dbg|windbg|binja|radare2?")
    + r"|binary[-_ ]?ninja|cheat[-_ ]?engine|"
    + _wb(r"ceserver")
    # Firmware / HV / mapping / spoof / dump
    + r"|"
    + _wb(r"hwid|efi|uefi|hypervisor|hvci|vbs|nmi|ioctl|syscall|shellcode")
    + r"|patchguard|byovd|manual[-_ ]?map|"
    + _wb(r"(?:kd)?mapper|drvmap")
    + r"|spoof(?:er|ing)?|ring[-_ ]?[03]"
    + r"|"
    + _wb(r"rootkit|dump(?:er|ing)?|unpacker|dll[-_ ]?hijack")
    + r"|anti[-_ ]?(?:debug(?:ger)?|detect(?:ion)?|tamper|forensics|screenshot)"
    + r"|vulnerable[-_ ]?driver|loldrivers?|"
    + _wb(r"gdrv|capcom|iqvw64e")
    # Hook / menu compounds (avoid bare "hook" → webhook; bare imgui → upstream lib)
    + r"|(?:d3d\d*|dx\d*|directx|imgui|present|wndproc|inline|vmt|iat|minhook|detours?)"
    + r"[-_ ]?hooks?|hooks?[-_ ]?(?:d3d\d*|dx\d*|imgui|present)"
    + r"|dear[-_ ]?imgui|imgui[-_ ]?(?:menu|hook|overlay|hack|base|dx|d3d)"
    + r"|mod[-_ ]?menu|"
    + _wb(r"minhook|detours?")
    + r"|dynamorio|qbdi|"
    + _wb(r"dbi|veh")
    # Distinctive game titles (edged short codes; never bare rust/lol/cod)
    + r"|"
    + _wb(
        r"csgo|cs2|valorant|fortnite|pubg|pubgm|genshin|palworld|maplestory|"
        r"warzone|overwatch2?|elden[-_ ]?ring|naraka|lostark|battlerite|"
        r"crossfire|bloodhunt|splitgate|dayz|arma3?|osu|tarkov|"
        r"apex(?:[-_ ]?legends)?|eft|r6(?:siege)?|rainbow[-_ ]?six|"
        r"honkai|zenless|wuthering|delta[-_ ]?force"
    )
    + r")"
)
# Megaprojects need a strong game-security phrase (not lone "kernel"/"driver").
FOLLOW_STRONG_HINT_RE = re.compile(
    r"(?i)(?:"
    r"anti[-_ ]?cheat|anticheat|game[-_ ]?(?:hack|security|cheat)|"
    r"battleye|vanguard|easyanticheat|ricochet|byfron|hyperion|faceit|"
    + _wb(r"eac|vac|equ8")
    + r"|pcileech|fpga[-_ ]?dma|"
    # Require a dma-* qualifier so bare "DMA" in megakernel docs stays weak.
    + _wb(r"dma")
    + r"[-_ ](?:cheat|hack|radar|board|card|attack|kvm|fpga|tool|base)|"
    r"il2cpp|vmprotect|themida|byovd|patchguard|"
    + _wb(r"kdmapper")
    + r"|vulnerable[-_ ]?driver"
    + r")"
)
FOLLOW_MEGA_STAR_GATE = 5000


def _topic_hint_rank(blob: str) -> int:
    """2 = strong game-sec signal, 1 = topic hint, 0 = none."""
    if FOLLOW_STRONG_HINT_RE.search(blob):
        return 2
    if FOLLOW_TOPIC_HINT_RE.search(blob):
        return 1
    return 0


def _configure_paths() -> Path:
    """Point discover_repos_cli I/O at .github/discover-follow/."""
    discover_dir = ROOT_DIR / ".github" / "discover-follow"
    dr.DISCOVER_DIR = discover_dir
    dr.CANDIDATES_PATH = discover_dir / "candidates.json"
    dr.SCREEN_PATH = discover_dir / "screen.json"
    dr.DECISION_PATH = discover_dir / "decision.json"
    dr.KEEP_RELS = frozenset(
        {
            "README.md",
            ".github/discover-follow/candidates.json",
            ".github/discover-follow/screen.json",
            ".github/discover-follow/decision.json",
        }
    )
    return discover_dir


def _parse_iso_dt(raw: str | None) -> datetime | None:
    if not raw:
        return None
    text = raw.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def load_custom_usernames_text(text: str) -> list[str]:
    logins: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@"):
            line = line[1:].strip()
        if LOGIN_RE.fullmatch(line):
            logins.append(line)
    return logins


def fetch_custom_usernames(follow_feed_repo: str, custom_users_path: str) -> list[str]:
    """Load custom_users.txt from github-follow-feed (Contents API)."""
    api_path = (
        f"repos/{follow_feed_repo}/contents/"
        f"{custom_users_path.lstrip('/')}"
    )
    try:
        meta = dr.gh_api_json(api_path)
    except RuntimeError as e:
        print(f"WARNING: could not fetch {follow_feed_repo}:{custom_users_path}: {e}")
        return []
    if not isinstance(meta, dict):
        return []
    content_b64 = (meta.get("content") or "").replace("\n", "")
    if not content_b64:
        return []
    try:
        text = base64.b64decode(content_b64).decode("utf-8", errors="replace")
    except Exception as e:
        print(f"WARNING: decode custom_users failed: {e}")
        return []
    logins = load_custom_usernames_text(text)
    print(f"Loaded {len(logins)} custom user(s) from {follow_feed_repo}:{custom_users_path}")
    return logins


def fetch_following_logins(source_user: str) -> list[str]:
    """Public following list for source_user (users only; skip orgs)."""
    logins: list[str] = []
    path = f"users/{source_user}/following?per_page=100"
    # gh api --paginate
    proc = subprocess.run(
        [dr.find_gh_bin(), "api", "--paginate", path],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        check=False,
        timeout=180,
    )
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()[:400]
        sys.exit(f"ERROR: failed to list following for {source_user}: {err}")
    # --paginate may concatenate JSON arrays; parse robustly.
    raw = (proc.stdout or "").strip()
    if not raw:
        return []
    rows: list[Any] = []
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list):
            rows = parsed
        else:
            sys.exit("ERROR: unexpected following payload (not a list)")
    except json.JSONDecodeError:
        # Rare: multiple arrays concatenated without newline handling.
        decoder = json.JSONDecoder()
        idx = 0
        while idx < len(raw):
            while idx < len(raw) and raw[idx].isspace():
                idx += 1
            if idx >= len(raw):
                break
            obj, offset = decoder.raw_decode(raw, idx)
            idx = offset
            if isinstance(obj, list):
                rows.extend(obj)
    for row in rows:
        if not isinstance(row, dict):
            continue
        if (row.get("type") or "") != "User":
            continue
        login = (row.get("login") or "").strip()
        if LOGIN_RE.fullmatch(login):
            logins.append(login)
    print(f"Loaded {len(logins)} following user(s) for {source_user}")
    return logins


def collect_tracked_logins(
    source_user: str,
    follow_feed_repo: str,
    custom_users_path: str,
) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for login in fetch_following_logins(source_user):
        key = login.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(login)
    for login in fetch_custom_usernames(follow_feed_repo, custom_users_path):
        key = login.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(login)
    print(f"Tracked logins total : {len(ordered)}")
    return ordered


_USER_REPO_LOCK = threading.Lock()
_LAST_USER_REPO_TS = 0.0
USER_REPO_MIN_INTERVAL_SEC = 0.05  # gentle pacing across parallel workers
USER_REPO_PER_PAGE = 100  # GitHub max; survive fork-heavy recent pushes
USER_REPO_MAX_PAGES = 3


def _throttle_user_repos() -> None:
    global _LAST_USER_REPO_TS
    with _USER_REPO_LOCK:
        now = time.monotonic()
        wait = USER_REPO_MIN_INTERVAL_SEC - (now - _LAST_USER_REPO_TS)
        if wait > 0:
            time.sleep(wait)
        _LAST_USER_REPO_TS = time.monotonic()


def list_user_repos(
    login: str,
    *,
    per_user: int,
    pushed_after: datetime,
) -> list[dict[str, Any]]:
    """
    Recently pushed owner repos for one user (sorted by push, newest first).

    Pages past fork/archived noise so a fork-heavy first page does not hide
    on-topic originals still inside the lookback window.
    """
    out: list[dict[str, Any]] = []
    for page in range(1, USER_REPO_MAX_PAGES + 1):
        path = (
            f"users/{login}/repos?type=owner&sort=pushed&direction=desc"
            f"&per_page={USER_REPO_PER_PAGE}&page={page}"
        )
        _throttle_user_repos()
        try:
            rows = dr.gh_api_json(path, timeout=60)
        except RuntimeError as e:
            print(f"  [WARN] repos list failed for {login} (page {page}): {str(e)[:200]}")
            break
        if not isinstance(rows, list) or not rows:
            break

        hit_lookback_floor = False
        for row in rows:
            if not isinstance(row, dict):
                continue
            pushed = _parse_iso_dt(row.get("pushed_at") or row.get("updated_at"))
            if pushed is None or pushed < pushed_after:
                # Sorted by pushed desc — older than lookback means stop paging.
                hit_lookback_floor = True
                break
            if row.get("fork") or row.get("archived"):
                continue
            full = (row.get("full_name") or "").strip()
            if not dr.REPO_SLUG_RE.fullmatch(full):
                continue
            out.append(
                {
                    "fullName": full,
                    "url": f"https://github.com/{full.lower()}",
                    "description": (row.get("description") or "").strip(),
                    "stargazersCount": int(row.get("stargazers_count") or 0),
                    "updatedAt": row.get("pushed_at") or row.get("updated_at") or "",
                    "isArchived": False,
                    "isFork": False,
                    "ownerLogin": login,
                    "matchedQueries": [f"follow:{login}"],
                }
            )
            if len(out) >= per_user:
                return out

        if hit_lookback_floor or len(rows) < USER_REPO_PER_PAGE:
            break
    return out


def _passes_topic_gate(full: str, description: str, stars: int) -> bool:
    """
    Pre-clone relevance gate. Followed users are trusted for discovery volume,
    but clones still require an on-topic name/description hint so we do not
    waste Cursor budget on unrelated activity.
    """
    rank = _topic_hint_rank(f"{full} {description}")
    # Megaprojects (linux, etc.): require a strong game-security phrase.
    if stars >= FOLLOW_MEGA_STAR_GATE:
        return rank >= 2
    return rank >= 1


def discover_follow_candidates(
    logins: list[str],
    *,
    lookback_days: int,
    max_candidates: int,
    min_stars: int,
    repos_per_user: int,
    user_workers: int,
) -> list[dict[str, Any]]:
    pushed_after = datetime.now(timezone.utc) - timedelta(days=lookback_days)
    known = dr.existing_readme_slugs()
    print(f"README known slugs   : {len(known)}")
    print(f"Lookback             : {lookback_days} day(s) (pushed>={pushed_after.date().isoformat()})")
    print(f"Min stars            : {min_stars}")
    print(f"Tracked users        : {len(logins)}")
    print(f"Repos / user         : {repos_per_user}")
    print(f"User workers         : {user_workers}")
    print(f"Max candidates       : {max_candidates}")

    seen: dict[str, dict[str, Any]] = {}
    skipped_known = skipped_stars = skipped_noise = skipped_self = 0

    def _one(login: str) -> tuple[str, list[dict[str, Any]]]:
        return login, list_user_repos(
            login, per_user=repos_per_user, pushed_after=pushed_after
        )

    workers = max(1, min(user_workers, len(logins) or 1))
    done_n = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_one, login): login for login in logins}
        for fut in as_completed(futures):
            done_n += 1
            login, rows = fut.result()
            if done_n % 25 == 0 or done_n == len(logins):
                print(f"[{done_n}/{len(logins)}] scanned users … (+{len(rows)} from {login})")
            for row in rows:
                full = row["fullName"]
                key = full.lower()
                if key in known:
                    skipped_known += 1
                    continue
                if key == dr.SELF_REPO.lower():
                    skipped_self += 1
                    continue
                stars = int(row["stargazersCount"])
                if stars < min_stars:
                    skipped_stars += 1
                    continue
                if not _passes_topic_gate(full, row.get("description") or "", stars):
                    skipped_noise += 1
                    continue
                if key not in seen:
                    seen[key] = row
                else:
                    # Prefer newer push timestamp if duplicate somehow.
                    prev = seen[key].get("updatedAt") or ""
                    cur = row.get("updatedAt") or ""
                    if cur > prev:
                        seen[key] = row

    ranked = sorted(
        seen.values(),
        key=lambda r: (
            _topic_hint_rank(f"{r['fullName']} {r.get('description') or ''}"),
            r.get("updatedAt") or "",
            int(r["stargazersCount"]),
        ),
        reverse=True,
    )
    capped = ranked[:max_candidates]

    print(f"\nUnique new candidates: {len(seen)}")
    print(f"Skipped (in README)  : {skipped_known}")
    print(f"Skipped (min stars)  : {skipped_stars}")
    print(f"Skipped (noise gate) : {skipped_noise}")
    print(f"Skipped (self)       : {skipped_self}")
    print(f"Capped to            : {len(capped)}")
    print(f"CANDIDATE_COUNT={len(capped)}")
    return capped


def clone_dir_name(full_name: str) -> str:
    return full_name.replace("/", "__")


def shallow_clone_repo(full_name: str, dest: Path) -> tuple[bool, str]:
    if dest.exists():
        shutil.rmtree(dest, ignore_errors=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    clone_url = f"https://github.com/{full_name}.git"
    clone_env = {"GIT_LFS_SKIP_SMUDGE": "1", **os.environ}
    cmd = [
        "git",
        "clone",
        "--depth",
        "1",
        "--single-branch",
        "--quiet",
        "--filter=blob:limit=5m",
        clone_url,
        str(dest),
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=CLONE_TIMEOUT,
            env=clone_env,
        )
    except subprocess.TimeoutExpired:
        shutil.rmtree(dest, ignore_errors=True)
        return False, "clone timeout"
    if proc.returncode != 0:
        # Retry without filter (some remotes reject filter-spec).
        shutil.rmtree(dest, ignore_errors=True)
        cmd_nofilter = [
            "git",
            "clone",
            "--depth",
            "1",
            "--single-branch",
            "--quiet",
            clone_url,
            str(dest),
        ]
        try:
            proc = subprocess.run(
                cmd_nofilter,
                capture_output=True,
                text=True,
                timeout=CLONE_TIMEOUT,
                env=clone_env,
            )
        except subprocess.TimeoutExpired:
            shutil.rmtree(dest, ignore_errors=True)
            return False, "clone timeout (retry)"
        if proc.returncode != 0:
            shutil.rmtree(dest, ignore_errors=True)
            err = (proc.stderr or proc.stdout or "").strip()[:200]
            return False, err or "clone failed"
    return True, str(dest)


def clone_candidates(
    candidates: list[dict[str, Any]],
    clones_root: Path,
) -> list[dict[str, Any]]:
    """Shallow-clone each candidate; drop those that fail to clone."""
    clones_root.mkdir(parents=True, exist_ok=True)
    kept: list[dict[str, Any]] = []
    for i, c in enumerate(candidates, 1):
        full = c["fullName"]
        dest = clones_root / clone_dir_name(full)
        print(f"[{i}/{len(candidates)}] clone {full} …")
        ok, detail = shallow_clone_repo(full, dest)
        if not ok:
            print(f"  [WARN] clone failed: {detail}")
            continue
        item = dict(c)
        item["clonePath"] = detail
        kept.append(item)
        print(f"  ok → {detail}")
    print(f"Cloned successfully  : {len(kept)}/{len(candidates)}")
    return kept


def write_follow_candidates(
    candidates: list[dict[str, Any]],
    *,
    source_user: str,
    follow_feed_repo: str,
    tracked_count: int,
) -> None:
    dr.write_json(
        dr.CANDIDATES_PATH,
        {
            "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "source": "follow-feed",
            "sourceUser": source_user,
            "followFeedRepo": follow_feed_repo,
            "trackedUserCount": tracked_count,
            "selfRepo": dr.SELF_REPO,
            "count": len(candidates),
            "candidates": candidates,
        },
    )


def build_follow_screen_prompt(candidate_count: int) -> str:
    return f"""\
You are PASS 1 of 2 for curating awesome-game-security (FOLLOW-FEED source).

Goal: shortlist candidates that are TRULY on-topic for this README taxonomy.
Candidates come from repos owned by users in gmh5225's GitHub following list
plus github-follow-feed/custom_users.txt. Do NOT edit README.md in this pass.

Read first:
1. `.claude/skills/overview/SKILL.md`
2. `README.md` headings (`##` / `>`) — learn where things belong
3. `.github/discover-follow/candidates.json` — {candidate_count} candidates

For EACH candidate:
1. Prefer the local shallow clone at `clonePath` (absolute path under /tmp).
   Inspect README, key source files, and project layout there.
2. If clonePath is missing/unreadable, fall back to:
   `gh repo view OWNER/REPO --json nameWithOwner,description,url,stargazersCount,repositoryTopics,isArchived,isFork,updatedAt`
   and a short README peek via gh api.
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

Write ONLY `.github/discover-follow/screen.json` with this shape:
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
- ONLY create/update `.github/discover-follow/screen.json`
- Do NOT modify README.md or any other path
- Do NOT git commit/push or open PRs
- Do NOT include {dr.SELF_REPO}
- When finished, print: Done: screen N shortlisted
"""


def build_follow_confirm_prompt(shortlist_count: int) -> str:
    return f"""\
You are PASS 2 of 2 for curating awesome-game-security (FOLLOW-FEED source).

Goal: INDEPENDENTLY re-confirm Pass 1 shortlist using the local clones, then
edit README ONLY for repos that still pass — and ONLY when a suitable existing
section is clear.

Read first:
1. `.claude/skills/overview/SKILL.md`
2. `README.md` (current structure and nearby entries)
3. `.github/discover-follow/screen.json` — Pass 1 shortlist ({shortlist_count} item(s))
4. `.github/discover-follow/candidates.json` — includes clonePath for each repo

For EACH shortlisted repo, re-check from scratch (do not rubber-stamp Pass 1):
1. Re-inspect the local clone at clonePath (README + representative source)
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

Always write `.github/discover-follow/decision.json`:
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
- ONLY modify/create: `README.md` and `.github/discover-follow/decision.json`
- Do NOT git commit/push or open PRs
- Do NOT touch other paths (including clone directories)
- Do NOT include {dr.SELF_REPO}
- When finished, print: Done: confirm N approved
"""


def run_follow_two_pass_review(
    agent_bin: str,
    model: str,
    candidates: list[dict[str, Any]],
    *,
    dry_run: bool = False,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    print("\n=== Pass 1/2: relevance screen via local clones (no README edits) ===")
    code1 = dr.run_agent(
        agent_bin,
        model,
        build_follow_screen_prompt(len(candidates)),
        dry_run=dry_run,
    )
    dr.revert_readme()
    dr.discard_side_effects()

    if dry_run:
        print("[DRY-RUN] pass 1 + pass 2 prompts only.")
        print("--- pass 2 prompt preview ---")
        print(build_follow_confirm_prompt(0)[:600])
        return None, None

    screen = dr.load_screen()
    if screen is None:
        sys.exit(
            f"ERROR: pass 1 finished (exit={code1}) but "
            f"{dr.SCREEN_PATH.relative_to(ROOT_DIR)} is missing/invalid"
        )
    if code1 != 0:
        print(f"note: pass 1 exit={code1}, but screen.json present — continuing")

    shortlisted = dr.validate_screen(screen, candidates)
    print(
        f"Pass 1 result: shortlisted={len(shortlisted)} "
        f"rejected={len(screen.get('rejected') or [])}"
    )
    if not shortlisted:
        print("Nothing shortlisted after pass 1 — no commit.")
        dr.write_json(
            dr.DECISION_PATH,
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
        return screen, dr.load_decision()

    print("\n=== Pass 2/2: confirm via clones + README placement ===")
    code2 = dr.run_agent(
        agent_bin,
        model,
        build_follow_confirm_prompt(len(shortlisted)),
        dry_run=False,
    )
    dr.discard_side_effects()

    decision = dr.load_decision()
    if decision is None:
        dr.revert_readme()
        sys.exit(
            f"ERROR: pass 2 finished (exit={code2}) but "
            f"{dr.DECISION_PATH.relative_to(ROOT_DIR)} is missing/invalid"
        )
    if code2 != 0:
        print(f"note: pass 2 exit={code2}, but decision.json present — continuing")

    decision = dr.validate_decision(decision, shortlisted, candidates)
    if not decision.get("approved"):
        print("No repos survived pass 2 + validation — reverting README.")
        dr.revert_readme()
    elif not dr.readme_has_diff():
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
        dr.write_json(dr.DECISION_PATH, decision)

    print(
        f"Pass 2 result: approved={len(decision.get('approved') or [])} "
        f"rejected={len(decision.get('rejected') or [])}"
    )
    return screen, decision


def cleanup_clones(clones_root: Path) -> None:
    if clones_root.exists():
        shutil.rmtree(clones_root, ignore_errors=True)
        print(f"Cleaned clones under {clones_root}")


def cleanup_runtime_files(*, keep_decision: bool = False) -> None:
    for path in (dr.CANDIDATES_PATH, dr.SCREEN_PATH):
        if path.exists():
            path.unlink(missing_ok=True)
    if not keep_decision and dr.DECISION_PATH.exists():
        dr.DECISION_PATH.unlink(missing_ok=True)
    if dr.DISCOVER_DIR.is_dir() and not any(dr.DISCOVER_DIR.iterdir()):
        dr.DISCOVER_DIR.rmdir()


def run_keyword_self_test() -> None:
    """Fail fast if topic/strong gates regress (run via --self-test)."""
    # (blob, want_topic, want_strong)
    cases: list[tuple[str, bool, bool]] = [
        # snake_case / DMA
        ("owner/apex_dma_kvm", True, True),
        ("owner/dma_cheat", True, True),
        ("owner/dma-radar", True, True),
        ("owner/DMA", True, False),
        ("owner/dmacheat", False, False),
        ("owner/kdmapper", True, True),
        ("PCIe DMA board", True, True),
        ("xdma", False, False),
        # edges / false positives
        ("owner/florida-tools", False, False),
        ("theft-tools", False, False),  # must not match eft
        ("left-pad", False, False),
        ("webhook-tools", False, False),
        ("owner/ManualInject", False, False),  # CamelCase tradeoff
        # AC / bypass / spoof (vendor tokens are strong)
        ("equ8_bypass", True, True),
        ("vac-bypass", True, True),
        ("owner/Vac-Emulator", True, True),
        ("negativespoofer", True, False),
        ("hwid-spoofer", True, False),
        ("faceit_ac", True, True),
        ("byovd-loader", True, True),
        ("pcileech-fpga", True, True),
        ("ricochet-research", True, True),
        # hooks / dump / mobile / RE
        ("imgui-hook", True, False),
        ("dear-imgui-menu", True, False),
        ("Android-Mod-Menu", True, False),
        ("ocornut/imgui", False, False),  # upstream lib, not a cheat menu
        ("d3d11-overlay", True, False),
        ("valorant-dumper", True, False),
        ("zygisk-module", True, False),
        ("x64dbg-plugin", True, False),
        ("minhook-lib", True, False),
        ("ring0-detect", True, False),
        ("nmi_callback", True, False),
        ("gdrv-loader", True, False),
        ("vulnerable-driver", True, True),
        # games
        ("cs2-offsets", True, False),
        ("fortnite-sdk", True, False),
        ("eft-radar", True, False),
        ("my-rust-cli", False, False),  # bare "rust" must not match
        ("lol-jokes", False, False),
        # mega-star gate samples (rank only; stars applied in _passes_topic_gate)
        ("game-security-tools", True, True),
        ("linux-kernel", True, False),
        ("anti-cheat-sdk", True, True),
    ]
    failed = 0
    for blob, want_t, want_s in cases:
        got_t = bool(FOLLOW_TOPIC_HINT_RE.search(blob))
        got_s = bool(FOLLOW_STRONG_HINT_RE.search(blob))
        if (got_t, got_s) != (want_t, want_s):
            failed += 1
            print(
                f"FAIL {blob!r}: topic={got_t} strong={got_s} "
                f"want=({want_t},{want_s})"
            )
    # Mega-star policy
    mega_cases = [
        ("torvalds/linux", "Linux kernel", 200_000, False),
        ("ufrisk/pcileech", "DMA attack", 10_000, True),
        ("x/apex_dma_kvm", "", 10, True),
        ("x/notes", "shopping list", 0, False),
    ]
    for full, desc, stars, want in mega_cases:
        got = _passes_topic_gate(full, desc, stars)
        if got != want:
            failed += 1
            print(
                f"FAIL gate {full!r} stars={stars}: got={got} want={want}"
            )
    if failed:
        sys.exit(f"ERROR: keyword self-test failed ({failed} case(s))")
    print(f"KEYWORD_SELF_TEST_OK cases={len(cases)} gates={len(mega_cases)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Discover theme-related repos from GitHub following + "
            "custom_users.txt, clone, and 2-pass Cursor CLI review"
        )
    )
    parser.add_argument(
        "--source-user",
        type=str,
        default=DEFAULT_SOURCE_USER,
        help="GitHub user whose following list is scanned",
    )
    parser.add_argument(
        "--follow-feed-repo",
        type=str,
        default=DEFAULT_FOLLOW_FEED_REPO,
        help="Repo hosting custom_users.txt (owner/name)",
    )
    parser.add_argument(
        "--custom-users-path",
        type=str,
        default=DEFAULT_CUSTOM_USERS_PATH,
        help="Path to custom users file inside follow-feed repo",
    )
    parser.add_argument("--lookback-days", type=int, default=3)
    parser.add_argument("--max-candidates", type=int, default=20)
    parser.add_argument("--min-stars", type=int, default=0)
    parser.add_argument("--repos-per-user", type=int, default=DEFAULT_REPOS_PER_USER)
    parser.add_argument("--user-workers", type=int, default=DEFAULT_USER_WORKERS)
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)
    parser.add_argument(
        "--clones-dir",
        type=str,
        default="",
        help="Directory for shallow clones (default: temp dir under /tmp)",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        default=False,
        help="Run keyword/gate regression checks and exit",
    )
    parser.add_argument(
        "--list-users",
        action="store_true",
        default=False,
        help="Print tracked logins and exit",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Discovery + clone + two-pass prompt preview; no agent / commit",
    )
    parser.add_argument(
        "--discover-only",
        action="store_true",
        default=False,
        help="Write candidates.json (and optionally clone) then exit",
    )
    parser.add_argument(
        "--skip-clone",
        action="store_true",
        default=False,
        help="Skip shallow clone (metadata-only; not recommended for review)",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        default=False,
        help="After 2-pass validation, commit README.md to main (Contents API)",
    )
    parser.add_argument("--run-id", type=str, default="")
    parser.add_argument(
        "--skip-agent",
        action="store_true",
        default=False,
        help="Skip Cursor agent (discovery / clone only)",
    )
    args = parser.parse_args()

    if args.self_test:
        run_keyword_self_test()
        return

    _configure_paths()

    if args.lookback_days < 1:
        sys.exit("ERROR: --lookback-days must be >= 1")
    if args.max_candidates < 1:
        sys.exit("ERROR: --max-candidates must be >= 1")
    if args.min_stars < 0:
        sys.exit("ERROR: --min-stars must be >= 0")
    if args.repos_per_user < 1:
        sys.exit("ERROR: --repos-per-user must be >= 1")
    if args.user_workers < 1:
        sys.exit("ERROR: --user-workers must be >= 1")
    if not dr.README_PATH.is_file():
        sys.exit("ERROR: README.md not found")
    if not dr.REPO_SLUG_RE.fullmatch(args.follow_feed_repo):
        sys.exit("ERROR: --follow-feed-repo must be owner/name")
    if not LOGIN_RE.fullmatch(args.source_user):
        sys.exit("ERROR: --source-user looks invalid")

    dr.find_gh_bin()

    logins = collect_tracked_logins(
        args.source_user,
        args.follow_feed_repo,
        args.custom_users_path,
    )
    if args.list_users:
        print(f"TRACKED_USER_COUNT={len(logins)}")
        for login in logins:
            print(login)
        return

    if not logins:
        print("No tracked users — nothing to do.")
        return

    candidates = discover_follow_candidates(
        logins,
        lookback_days=args.lookback_days,
        max_candidates=args.max_candidates,
        min_stars=args.min_stars,
        repos_per_user=args.repos_per_user,
        user_workers=args.user_workers,
    )

    clones_root = (
        Path(args.clones_dir)
        if args.clones_dir.strip()
        else Path(tempfile.mkdtemp(prefix="ags-discover-follow-"))
    )
    print(f"Clones root          : {clones_root}")

    try:
        if candidates and not args.skip_clone:
            candidates = clone_candidates(candidates, clones_root)
        elif args.skip_clone:
            print("Skipping clones (--skip-clone).")

        write_follow_candidates(
            candidates,
            source_user=args.source_user,
            follow_feed_repo=args.follow_feed_repo,
            tracked_count=len(logins),
        )

        if candidates:
            for c in candidates[:20]:
                clone_note = c.get("clonePath") or "(no clone)"
                print(
                    f"  - {c['fullName']} (★{c['stargazersCount']}) :: "
                    f"{(c.get('description') or '')[:60]} :: {clone_note}"
                )
            if len(candidates) > 20:
                print(f"  ... and {len(candidates) - 20} more")

        if args.discover_only or args.skip_agent:
            print("\nFollow-feed discovery complete (no agent).")
            return

        if args.dry_run:
            print("\nDiscovery complete — dry-run two-pass prompt preview.")
            run_follow_two_pass_review("agent", args.model, candidates, dry_run=True)
            print("[DRY-RUN] agents + commit skipped.")
            return

        if not candidates:
            print("No new candidates — nothing to review.")
            cleanup_runtime_files(keep_decision=False)
            return

        dr.get_api_key()
        agent_bin = dr.find_agent_bin()
        print(f"\nModel: {args.model}")
        _screen, decision = run_follow_two_pass_review(
            agent_bin, args.model, candidates, dry_run=False
        )
        if decision is None:
            sys.exit("ERROR: two-pass review returned no decision")

        approved = decision.get("approved") or []
        print(
            f"\nFinal: approved={len(approved)} "
            f"validated={bool(decision.get('validated'))}"
        )

        if not args.commit:
            print("README/decision left in working tree (--commit not set).")
            return

        if not approved or not decision.get("validated"):
            print("No validated approvals — not committing.")
            dr.revert_readme()
            cleanup_runtime_files(keep_decision=False)
            return

        run_id = (
            args.run_id.strip()
            or os.environ.get("GITHUB_RUN_ID", "").strip()
            or "local"
        )
        sha = dr.commit_to_main(
            decision, run_id=run_id, commit_label="discover-follow"
        )
        cleanup_runtime_files(keep_decision=False)
        dr.discard_side_effects()
        if sha:
            print(f"Committed to main: {sha}")
        else:
            print("No commit created.")
            dr.revert_readme()
    finally:
        # Always drop shallow clones — they can be large.
        if not args.clones_dir.strip():
            cleanup_clones(clones_root)
        elif os.environ.get("DISCOVER_FOLLOW_KEEP_CLONES", "").strip() not in {
            "1",
            "true",
            "yes",
        }:
            cleanup_clones(clones_root)


if __name__ == "__main__":
    main()
