---
title: uc-mcp
kind: entity
topics: [reverse-engineering, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/0111-0222__uc-mcp.md
updated: 2026-10-02
confidence: medium
---

# uc-mcp

**uc-mcp** (0111-0222/uc-mcp) is a **read-only Model Context Protocol server** that lets AI assistants search and read the UnknownCheats forum through the user's own logged-in browser session. Written in **Python**, it targets game security researchers, reverse engineers, and anti-cheat analysts who want MCP clients to query current community knowledge on game hacking and bypass techniques instead of relying on stale public documentation. (source: wiki/sources/descriptions/0111-0222__uc-mcp.md)

## Capabilities

- **Five MCP tools** — keyword search, thread reading, subforum browsing, page fetching, and session health checks.
- **Date-aware results** — every response stamped in UTC and labeled for staleness so outdated offsets and bypass write-ups are easier to spot.
- **Session-scoped access** — uses the caller's session cookies; strict read-only policy with rate limits, URL guards, and SQLite caching to keep traffic human-shaped and protect account credentials.
- **Cloudflare-aware fetch** — `curl_cffi` with Chrome TLS impersonation; vBulletin HTML parsed via BeautifulSoup and lxml.

Unlike [[cheat-mcp]] (Windows live memory R/W) or [[binary-ninja-headless-mcp]] (headless disassembly), uc-mcp is a **community-knowledge retrieval bridge** — it does not execute game code or mutate binaries.

## Links

- Repo: https://github.com/0111-0222/uc-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[research-rigor]] · [[cheat-mcp]] · [[open-reverselab]]
