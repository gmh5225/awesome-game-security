---
title: Titled Gui CS2
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/xfi0__Titled-Gui-CS2.md
updated: 2026-08-11
confidence: medium
---

# Titled Gui CS2

**Titled Gui** is an external Counter-Strike 2 cheat framework (C#; GPLv3) that attaches to the game process and draws a transparent ImGui overlay for configuration and on-screen visuals. It reads and writes game memory through Win32 APIs, automatically fetches updated offsets from cs2-dumper sources, and implements combat features such as aimbot, recoil control, and triggerbot alongside movement and quality-of-life tweaks. Visual modules include ESP, radar, chams rendered with DirectX 11 and VPK model loading, map-based visibility checks using pre-extracted geometry, and HUD overlays for players, bombs, and grenade lineups. README **External** tag; useful for game security researchers studying external cheat architecture, memory interaction patterns, overlay rendering, and techniques anti-cheat systems must detect in CS2. (source: wiki/sources/descriptions/xfi0__Titled-Gui-CS2.md)

## Links

- Repo: https://github.com/xfi0/Titled-Gui-CS2

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[cs2-external-cheat]] · [[cs2-ext]] · [[cs2-cheat]] · [[cs2-offsets]] · [[proext]] · [[present-hook]] · [[world-to-screen]]
