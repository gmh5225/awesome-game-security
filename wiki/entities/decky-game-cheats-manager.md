---
title: Decky Game Cheats Manager
kind: entity
topics: [game-hacking]
sources:
  - wiki/sources/descriptions/Qiming-Liu__Decky-Game-Cheats-Manager.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# Decky Game Cheats Manager

**Decky Game Cheats Manager** (Qiming-Liu/Decky-Game-Cheats-Manager; marketed as **DeckyGCM**) is a **Decky Loader** plugin that exposes **Game Cheats Manager**–style trainer search, download, and library management on **Steam Deck** from the Quick Access menu and per-game library context menus. (source: wiki/sources/descriptions/Qiming-Liu__Decky-Game-Cheats-Manager.md)

## Architecture

| Layer | Role |
|-------|------|
| TypeScript/React UI | Quick Access panel and per-game Steam library context menus (Game Mode) |
| Python plugin backend | Embeds generated GCM core logic: catalog queries, authenticated downloads, archive extraction, local trainer metadata |
| Steam integration | Library scanning, Steam App ID binding, bilingual UI tied to Steam language settings |

## Catalog and workflow

Users search trainers from sources such as **FLiNG**, **XiaoXing**, cheat tables, and the **GCM catalog**, with English or Chinese name matching. The backend handles authenticated downloads, **ZIP / 7z / RAR** extraction, binding assets to **Steam App IDs**, importing local executables, and optional **Proton sidecar** launch through game launch options. **Offline catalog refresh** and **bounded concurrent downloads** keep trainer curation usable on-device rather than requiring desktop GCM or manual prefix setup. (source: wiki/sources/descriptions/Qiming-Liu__Decky-Game-Cheats-Manager.md)

## Positioning

Listed under **Cheat** beside [[deckcheatz]] (Proton compatibility-tool trainer launcher), [[ce-decky]] (Cheat Engine tables in Game Mode), and [[archmod]]. DeckyGCM targets standalone trainer binaries and GCM-style catalogs—not in-process memory-table editing—complementing CE Decky when researchers or players want FLiNG/XiaoXing-style downloads on handheld Linux.

## Links

- Repo: https://github.com/Qiming-Liu/Decky-Game-Cheats-Manager

## Related

[[deckcheatz]] · [[ce-decky]] · [[archmod]] · [[pointblank-linux]] · [[proton]] · [[are-we-anti-cheat-yet]] · [[overviews/game-hacking]]
