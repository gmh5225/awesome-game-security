#!/usr/bin/env python3
"""
Check all GitHub repository links in README.md for accessibility.
If a repo is not accessible (404/not found), replace the username with gmh5225.
"""

import re
import sys
import time
import argparse
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

from description_paths import NON_REPO_ROUTES

README_PATH = "README.md"
FALLBACK_USER = "gmh5225"
GITHUB_REPO_PATTERN = re.compile(
    r"https://github\.com/([^/\s\)\]>\"']+)/([^/\s\)\]>\"'#]+)"
)
# Concurrency and rate limiting
MAX_WORKERS = 10
REQUEST_TIMEOUT = 10  # seconds
RETRY_COUNT = 2

# Repos that require authentication or are intentionally access-restricted.
# These are not dead links — skip them entirely.
SKIPPED_URLS: set[str] = {
    "https://github.com/EpicGames/UnrealEngine",
}


def check_url(url: str) -> tuple[str, bool, int]:
    """Return (url, is_accessible, status_code). Retries on network errors.

    Only 404 and 451 are treated as confirmed dead links.
    429 (rate-limited), 403 (private/forbidden), 5xx (server error),
    and network timeouts are all treated as alive/unknown to avoid
    false-positive replacements.
    """
    clean_url = url.rstrip(".,;:")
    for attempt in range(RETRY_COUNT + 1):
        try:
            req = urllib.request.Request(
                clean_url,
                headers={"User-Agent": "Mozilla/5.0 (compatible; link-checker/1.0)"},
            )
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                return (clean_url, True, resp.status)
        except urllib.error.HTTPError as e:
            if e.code in (404, 451):
                # Confirmed dead: resource gone or legally unavailable
                return (clean_url, False, e.code)
            if e.code == 429:
                # Rate-limited — server is alive, back off and treat as OK
                time.sleep(2 ** attempt)
                if attempt < RETRY_COUNT:
                    continue
                return (clean_url, True, e.code)
            # 403, 5xx, etc. — treat as alive (private repo, transient error)
            if attempt < RETRY_COUNT:
                time.sleep(1)
                continue
            return (clean_url, True, e.code)
        except Exception:
            # Network error / timeout — treat as alive to avoid false positives
            if attempt < RETRY_COUNT:
                time.sleep(1)
                continue
            return (clean_url, True, 0)
    return (clean_url, True, 0)


def extract_github_urls(text: str) -> list[str]:
    """Extract unique GitHub repo URLs (owner/repo level) from text."""
    matches = GITHUB_REPO_PATTERN.findall(text)
    seen = set()
    urls = []
    for user, repo in matches:
        if user.casefold() in NON_REPO_ROUTES:
            continue
        # Strip trailing punctuation from repo name
        repo = repo.rstrip(".,;:")
        url = f"https://github.com/{user}/{repo}"
        if url in seen or url in SKIPPED_URLS:
            continue
        seen.add(url)
        urls.append(url)
    return urls


def build_replacement_map(
    dead_urls: list[str],
    verbose: bool = False,
) -> dict[str, str]:
    """
    For each dead URL, check if gmh5225/repo exists.
    Returns a mapping of original_url -> replacement_url.
    """
    replacements = {}

    def check_fallback(original_url: str) -> tuple[str, str | None]:
        parts = original_url.split("/")
        if len(parts) < 5:
            return original_url, None
        repo = parts[4].rstrip(".,;:")
        fallback_url = f"https://github.com/{FALLBACK_USER}/{repo}"
        if parts[3] == FALLBACK_USER:
            # Already gmh5225, skip
            return original_url, None
        _, accessible, status = check_url(fallback_url)
        if accessible:
            return original_url, fallback_url
        return original_url, None

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(check_fallback, url): url for url in dead_urls
        }
        for future in as_completed(futures):
            original, replacement = future.result()
            if replacement:
                replacements[original] = replacement
                if verbose:
                    print(f"  [FIXABLE] {original} -> {replacement}")
            else:
                if verbose:
                    print(f"  [NO FIX]  {original}")

    return replacements


def apply_replacements(text: str, replacements: dict[str, str]) -> str:
    """Replace all dead URLs with their gmh5225 equivalents."""
    for original, replacement in replacements.items():
        # Extract user/repo from both
        orig_parts = original.split("/")
        repl_parts = replacement.split("/")
        if len(orig_parts) >= 5 and len(repl_parts) >= 5:
            orig_user = orig_parts[3]
            repl_user = repl_parts[3]
            orig_repo = orig_parts[4]
            repl_repo = repl_parts[4]
            # Anchor the repo slug end so owner/foo does not rewrite owner/foobar or owner/foo.js
            pattern = re.compile(
                rf"github\.com/{re.escape(orig_user)}/{re.escape(orig_repo)}"
                rf"(?![A-Za-z0-9_-]|\.[A-Za-z0-9._-])"
            )
            text = pattern.sub(lambda _: f"github.com/{repl_user}/{repl_repo}", text)
    return text


def main():
    parser = argparse.ArgumentParser(
        description="Check GitHub links in README.md and fix dead ones with gmh5225 forks."
    )
    parser.add_argument(
        "--readme",
        default=README_PATH,
        help=f"Path to README.md (default: {README_PATH})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying the file",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed output"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=MAX_WORKERS,
        help=f"Number of concurrent workers (default: {MAX_WORKERS})",
    )
    args = parser.parse_args()

    print(f"Reading {args.readme} ...")
    with open(args.readme, "r", encoding="utf-8") as f:
        original_text = f.read()

    all_urls = extract_github_urls(original_text)
    print(f"Found {len(all_urls)} unique GitHub repo URLs")

    print(f"\nChecking accessibility with {args.workers} workers ...")
    dead_urls = []
    ok_count = 0
    dead_count = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(check_url, url): url for url in all_urls}
        total = len(futures)
        done = 0
        for future in as_completed(futures):
            url, accessible, status = future.result()
            done += 1
            if accessible:
                ok_count += 1
                if args.verbose:
                    label = "SKIP" if status in (429, 0) else "OK  "
                    print(f"  [{label} {status}] {url}")
            else:
                dead_count += 1
                dead_urls.append(url)
                print(f"  [DEAD {status:3d}] {url}")

            # Progress indicator every 50 URLs
            if done % 50 == 0 or done == total:
                print(f"  Progress: {done}/{total}", flush=True)

    print(f"\nResults: {ok_count} OK, {dead_count} dead")

    if not dead_urls:
        print("All links are accessible. Nothing to fix!")
        return

    print(f"\nChecking if {FALLBACK_USER} has mirrors for {len(dead_urls)} dead repos ...")
    replacements = build_replacement_map(dead_urls, verbose=args.verbose)

    if not replacements:
        print(f"No fixable links found (no mirrors exist under {FALLBACK_USER}).")
        return

    print(f"\nFound {len(replacements)} fixable link(s):")
    for orig, repl in sorted(replacements.items()):
        print(f"  {orig}")
        print(f"    -> {repl}")

    if args.dry_run:
        print("\n[DRY RUN] No changes written.")
        return

    new_text = apply_replacements(original_text, replacements)
    if new_text == original_text:
        print("\nNo text changes needed (URLs may have been partially matched).")
        return

    with open(args.readme, "w", encoding="utf-8") as f:
        f.write(new_text)

    print(f"\nDone! {len(replacements)} URL(s) updated in {args.readme}")


if __name__ == "__main__":
    main()
