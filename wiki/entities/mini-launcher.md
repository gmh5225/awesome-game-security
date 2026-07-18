---
title: Mini-Launcher
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/xan105__Mini-Launcher.md
updated: 2026-07-18
confidence: medium
---

# Mini-Launcher

Lightweight Windows game launcher that starts titles without the full Steam (or similar) client: emulates needed Steam API calls, sets environment variables, injects SteamAppID, and loads API stubs so the game executable can run outside normal platform constraints. README positions it as an application launcher with DLL injection and Lua scripting—aimed at modders and researchers who need out-of-platform launch for testing. (source: wiki/sources/descriptions/xan105__Mini-Launcher.md)

Sits in the Cheat → Launcher Abuser lane: useful for studying platform-bypass launch paths and early DLL/script injection surfaces, not as a production cheat stack.

## Links

- Repo: https://github.com/xan105/Mini-Launcher

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injectors]] · [[steam-overlay-x64]]
