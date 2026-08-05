#!/usr/bin/env python3
"""
Generate English descriptions for archived repositories using Cursor Cloud Agents.

For each archive/{owner}/{repo}.txt, an agent:
  1. Fetches the archive file via raw GitHub URL
  2. Summarizes what the repo does (3-5 sentences, plain English)
  3. Writes the result to description/{owner}/{repo}/description_en.txt

Repos are processed in batches; each batch launches one Cloud Agent which creates
a pull request with the generated description files.

Prerequisites:
    export CURSOR_API_KEY=<your key from https://cursor.com/settings>

Usage:
    python scripts/generate-descriptions.py                   # process all pending
    python scripts/generate-descriptions.py --limit 30        # first 30 only
    python scripts/generate-descriptions.py --batch-size 10   # 10 repos per agent
    python scripts/generate-descriptions.py --no-skip-existing # re-generate all
    python scripts/generate-descriptions.py --dry-run         # print prompts, no API calls
"""

import os
import sys
import json
import time
import argparse
import requests
from pathlib import Path

from description_paths import normalize_repo_slug

# ── constants ──────────────────────────────────────────────────────────────────
CURSOR_API_BASE   = "https://api.cursor.com/v0"
GITHUB_REPO_URL   = "https://github.com/gmh5225/awesome-game-security"
RAW_ARCHIVE_BASE  = "https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive"

ROOT_DIR          = Path(__file__).resolve().parent.parent
ARCHIVE_DIR       = ROOT_DIR / "archive"
DESC_DIR          = ROOT_DIR / "description"

AGENT_POLL_INTERVAL = 15   # seconds between status checks
AGENT_TIMEOUT       = 600  # seconds before we give up on one agent


# ── helpers ───────────────────────────────────────────────────────────────────
def get_api_key() -> str:
    key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not key:
        sys.exit("ERROR: CURSOR_API_KEY environment variable is not set.\n"
                 "Obtain a key from https://cursor.com/settings")
    return key


def list_archived_repos() -> list[tuple[str, str]]:
    """Return [(owner, repo), ...] sorted by owner/repo."""
    repos: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for owner_dir in sorted(ARCHIVE_DIR.iterdir()):
        if not owner_dir.is_dir():
            continue
        for txt in sorted(owner_dir.glob("*.txt")):
            owner, repo = normalize_repo_slug(owner_dir.name, txt.stem)
            key = (owner.lower(), repo.lower())
            if key in seen:
                continue
            seen.add(key)
            repos.append((owner, repo))
    return repos


def needs_description(owner: str, repo: str) -> bool:
    return not (DESC_DIR / owner / repo / "description_en.txt").exists()


def build_batch_prompt(batch: list[tuple[str, str]]) -> str:
    """Build the instruction prompt for one Cloud Agent batch."""
    lines = []
    for owner, repo in batch:
        lines.append(
            f"- owner={owner}  repo={repo}\n"
            f"  archive : {RAW_ARCHIVE_BASE}/{owner}/{repo}.txt\n"
            f"  output  : description/{owner}/{repo}/description_en.txt"
        )
    repo_list = "\n".join(lines)

    return f"""\
You are processing a batch of archived GitHub repositories for the awesome-game-security project.

For EACH repository listed below, follow these steps exactly:

1. Fetch the archive file using curl (the file contains the repo's code snapshot):
      curl -fsSL "<archive URL>"

2. Analyse the fetched content:
   - Look at the README / top-level description sections
   - Identify the primary programming language(s)
   - Identify key features, techniques, or tools
   - Identify the target audience or use case (game security research, anti-cheat, etc.)

3. Write a plain-English description of 3–5 sentences to the output path shown below.
   Rules for the description file:
   - Plain text only (no markdown, no headers, no bullet points)
   - First sentence: what the project is / does
   - Remaining sentences: key features, technologies used, and primary use case
   - Do NOT include the repo URL or owner/repo slug in the text

4. Create parent directories if they do not exist (mkdir -p).

5. If the archive URL returns a 404 or the file is empty, write a single line:
      No archive available.

Repositories to process:
{repo_list}

After processing ALL repositories in the list, report a one-line summary:
  "Done: N descriptions written."
"""


# ── Cursor Cloud Agents API ────────────────────────────────────────────────────
def launch_agent(api_key: str, batch_index: int, prompt: str, dry_run: bool,
                 model: str | None = None) -> str | None:
    # Slashes in branch names are rejected by the API — use hyphens only
    branch = f"descriptions-batch-{batch_index:04d}"
    payload: dict = {
        "prompt": {"text": prompt},
        "source": {"repository": GITHUB_REPO_URL, "ref": "main"},
        "target": {
            "autoCreatePr": False,
            "branchName": branch,
        },
    }
    if model:
        payload["model"] = model

    if dry_run:
        model_label = model or "auto"
        print(f"\n[DRY-RUN] Would launch agent for batch {batch_index} on branch {branch} (model={model_label})")
        print("--- prompt preview (first 400 chars) ---")
        print(prompt[:400])
        print("---")
        return None

    try:
        resp = requests.post(
            f"{CURSOR_API_BASE}/agents",
            auth=(api_key, ""),
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30,
        )
    except requests.RequestException as exc:
        print(f"  [batch {batch_index:04d}] network error — {exc} — skipping")
        return None

    if not resp.ok:
        print(f"  [batch {batch_index:04d}] HTTP {resp.status_code} — {resp.text} — skipping")
        return None

    agent_id = resp.json()["id"]
    print(f"  [batch {batch_index:04d}] launched agent {agent_id} → branch {branch}")
    return agent_id


def poll_agent(api_key: str, agent_id: str, batch_index: int) -> str:
    """Poll until the agent finishes; return final status string."""
    deadline = time.time() + AGENT_TIMEOUT
    while time.time() < deadline:
        try:
            resp = requests.get(
                f"{CURSOR_API_BASE}/agents/{agent_id}",
                auth=(api_key, ""),
                timeout=15,
            )
        except requests.RequestException as exc:
            print(f"  [batch {batch_index:04d}] poll network error — {exc} — retrying")
            time.sleep(AGENT_POLL_INTERVAL)
            continue

        if not resp.ok:
            print(f"  [batch {batch_index:04d}] poll HTTP {resp.status_code} — retrying")
            time.sleep(AGENT_POLL_INTERVAL)
            continue

        status = resp.json().get("status", "UNKNOWN")
        if status in ("FINISHED", "FAILED", "STOPPED"):
            print(f"  [batch {batch_index:04d}] agent {agent_id} → {status}")
            return status
        time.sleep(AGENT_POLL_INTERVAL)

    print(f"  [batch {batch_index:04d}] agent {agent_id} → TIMEOUT")
    return "TIMEOUT"


# ── main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(description="Generate repo descriptions via Cursor Cloud Agents")
    parser.add_argument("--batch-size",    type=int,  default=15,
                        help="Number of repos per Cloud Agent (default: 15)")
    parser.add_argument("--limit",         type=int,  default=0,
                        help="Max repos to process in this run (0 = all)")
    parser.add_argument("--skip-existing", action="store_true", default=True,
                        help="Skip repos that already have description_en.txt (default: on)")
    parser.add_argument("--no-skip-existing", dest="skip_existing", action="store_false",
                        help="Re-generate descriptions even if they exist")
    parser.add_argument("--model",         type=str, default=None,
                        help="LLM model for the Cloud Agent, e.g. claude-4-sonnet-thinking "
                             "(omit to let Cursor auto-select)")
    parser.add_argument("--no-poll",       action="store_true", default=False,
                        help="Fire-and-forget: don't wait for agents to finish")
    parser.add_argument("--dry-run",       action="store_true", default=False,
                        help="Print prompts but don't call the API")
    args = parser.parse_args()

    api_key = "" if args.dry_run else get_api_key()

    all_repos = list_archived_repos()
    print(f"Total archived repos : {len(all_repos)}")

    if args.skip_existing:
        pending = [(o, r) for o, r in all_repos if needs_description(o, r)]
    else:
        pending = list(all_repos)
    print(f"Pending descriptions : {len(pending)}")

    if args.limit:
        pending = pending[: args.limit]
        print(f"Limited to           : {len(pending)}")

    if not pending:
        print("Nothing to do.")
        return

    # Split into batches
    batches = [pending[i : i + args.batch_size] for i in range(0, len(pending), args.batch_size)]
    print(f"Batches              : {len(batches)}  (batch-size={args.batch_size})")
    print()

    results: dict[str, int] = {}
    for idx, batch in enumerate(batches, start=1):
        print(f"Batch {idx}/{len(batches)} — {len(batch)} repos")
        prompt   = build_batch_prompt(batch)
        agent_id = launch_agent(api_key, idx, prompt, args.dry_run, args.model)

        if agent_id and not args.no_poll:
            status = poll_agent(api_key, agent_id, idx)
            results[status] = results.get(status, 0) + 1
        elif agent_id:
            results["LAUNCHED"] = results.get("LAUNCHED", 0) + 1
        else:
            results["SKIPPED"] = results.get("SKIPPED", 0) + 1

    if results:
        print(f"\nSummary: {json.dumps(results)}")


if __name__ == "__main__":
    main()
