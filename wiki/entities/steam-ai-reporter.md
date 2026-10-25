---
title: steam-ai-reporter
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/jrv97__steam-ai-reporter.md
updated: 2026-10-25
confidence: medium
---

# steam-ai-reporter

**Tag Kit for Steam** (jrv97) is a Chromium/Firefox extension and Tampermonkey-style userscript that overlays Steam store listings with badges derived from Valve’s own store APIs and developer disclosures. A shared TypeScript core drives platform adapters that classify AI-generated content reports, anti-cheat software (including kernel-level AC), third-party DRM, account requirements, EULAs, and PvP via `GetItems` with HTML fallbacks; users can show, dim, or hide tagged games and tune per-tag banners. The runtime stays content-script-only and does not ship app metadata to third-party servers—store-policy visibility for shoppers and AC researchers, not enforcement. (source: wiki/sources/descriptions/jrv97__steam-ai-reporter.md)

## Links

- Repo: https://github.com/jrv97/steam-ai-reporter

## Related

[[are-we-anti-cheat-yet]] · [[ac-compat-research]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/overview]]
