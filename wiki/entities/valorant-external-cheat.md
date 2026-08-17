---
title: valorant-external-cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/bootmgfw__Valorant-External-Cheat.md
updated: 2026-08-17
confidence: medium
---

# valorant-external-cheat

**valorant-external-cheat** (bootmgfw/Valorant-External-Cheat; **VEX**) is an open-source **external** cheat for **Valorant** implemented as a modular **C++20** Windows application. It reads **Unreal Engine 5** game state from outside the process through a **kernel driver abstraction** supporting cross-process memory access, pattern scanning, and mouse input, paired with an SDK for UWorld, actors, bones, and camera data. Feature modules include aimbot with bone mapping and FOV selection, triggerbot, ability lineup helpers, and a **DirectX 11** overlay GUI built with **ImGui**; a dedicated **VGK** subsystem handles Valorant-specific offsets and encrypted game data. The architecture separates application lifecycle, driver, rendering, and game logic behind injectable interfaces, and release builds add **LLVM-based obfuscation**. Intended for game security research, anti-cheat analysis, and studying external cheat design against [[vanguard]]-protected titles. (source: wiki/sources/descriptions/bootmgfw__Valorant-External-Cheat.md)

Sits in the kernel-assisted UE5 external lane beside other Valorant externals such as [[valorant-external-source]] and [[valorant-cheat-external]], bootmgfw driver primitives in [[lithium-kernel]], and title-specific SDK samples such as [[valorant-sdk-2024]].

## Links

- Repo: https://github.com/bootmgfw/valorant-external-cheat (External Valorant cheat with reversed UE SDK headers, kernel driver I/O, and aimbot/lineups)

## Related

[[vanguard]] · [[unreal-object-model]] · [[world-to-screen]] · [[present-hook]] · [[lithium-kernel]] · [[valorant-external-source]] · [[valorant-cheat-external]] · [[valorant-sdk-2024]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
