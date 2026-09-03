---
title: 2k17-club
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/Akatsyk__2k17-club.md
updated: 2026-09-03
confidence: medium
---

# 2k17-club

Large **internal C++ cheat framework** for **Counter-Strike: Global Offensive** (Akatsyk). Ships common offensive modules—aimbot, anti-aim, autowall, chams, grenade helpers, and hook-based game-event handling—and embeds **DirectX9 ImGui** rendering plus **Lua/LuaJIT** scripting through **LuaBridge** for configurable in-game tooling. Primary use case is cheat development research and **Source engine** reverse engineering on legacy Source 1 titles. (source: wiki/sources/descriptions/Akatsyk__2k17-club.md)

Treat as a feature-rich internal reference for studying scriptable modular cheat architecture—not a maintained production cheat.

## Architecture highlights

| Component | Role |
|-----------|------|
| Combat modules | Aimbot, anti-aim, autowall calculations |
| Visual modules | Chams and related in-engine rendering hooks |
| Utility modules | Grenade helpers, hook-based game-event handling |
| DirectX9 ImGui | In-game overlay menu and debug UI |
| Lua/LuaJIT + LuaBridge | Scriptable configuration and in-game tooling |

See [[csgo]] and [[digital-sdk]] for comparable large internal CS:GO frameworks and [[csgo-cheat-base]] for a lighter MinHook-based scaffold.

## Links

- Repo: https://github.com/Akatsyk/2k17-club

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[csgo]] · [[csgo-cheat-base]] · [[digital-sdk]] · [[csgosimple]] · [[source-netvars]] · [[present-hook]]
