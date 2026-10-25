---
title: steam-ai-reporter
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/jrv97__steam-ai-reporter.md
  - wiki/sources/README-categories.md
updated: 2026-10-25
confidence: high
---

# steam-ai-reporter

**Tag Kit for Steam** (jrv97/steam-ai-reporter) is a Chromium/Firefox browser extension and Tampermonkey-style userscript that annotates Steam store listings with tags derived from Valve’s own store data and developer disclosures—giving shoppers and game-security-minded users at-a-glance visibility into anti-cheat posture, DRM, and related store policies before buying or installing a title. (source: wiki/sources/descriptions/jrv97__steam-ai-reporter.md)

README category: Anti Cheat / Guide.

## Stack

Shared **TypeScript** core with platform-specific adapters (extension vs userscript). Classification uses Steam’s **GetItems** API with **HTML fallbacks** when API data is incomplete. (source: wiki/sources/descriptions/jrv97__steam-ai-reporter.md)

## Detected tags

Per-app labels include: **AI-generated content** reports; **anti-cheat software** (including **kernel-level** AC); **third-party DRM**; third-party **account** requirements; third-party **EULAs**; and **PvP**. (source: wiki/sources/descriptions/jrv97__steam-ai-reporter.md)

## UI and coverage

Overlays **badges**, **hover cards**, and **app-page banners** across store **search**, **wishlist**, **hubs**, and **sale** views. Per-tag settings let users **show**, **dim**, or **hide** labeled games, toggle banners, and maintain an **ignore list**. (source: wiki/sources/descriptions/jrv97__steam-ai-reporter.md)

## Privacy and positioning

Runtime stays **content-script-only** and does **not** send app metadata to third-party servers—store-policy visibility, not enforcement. Complements Linux AC compatibility trackers such as [[are-we-anti-cheat-yet]] and kernel AC primers in [[overviews/anti-cheat]]. (source: wiki/sources/descriptions/jrv97__steam-ai-reporter.md)

## Links

- Repo: https://github.com/jrv97/steam-ai-reporter

## Related

[[are-we-anti-cheat-yet]] · [[ac-compat-research]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/overview]]
