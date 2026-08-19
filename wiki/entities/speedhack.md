---
title: Speedhack
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/absoIute__Speedhack.md
updated: 2026-08-19
confidence: medium
---

# Speedhack

Lightweight **Windows speed-manipulation** sample by absoIute. Written in C++, buildable as an injectable DLL that hooks timing-related APIs via **Microsoft Detours** to change a target process's perceived execution speed — accelerate, slow down, or pause runtime behavior. Commonly used in cheat-development experiments and anti-cheat research around **time tampering** (`Detection:SpeedHack`). (source: wiki/sources/descriptions/absoIute__Speedhack.md)

Simpler and more focused than the integrated speedhack feature in [[cheat-engine]]; illustrates the Detours-based timing-hook pattern that AC stacks may monitor via clock-drift or API-integrity checks.

## Links

- Repo: https://github.com/absoIute/Speedhack

## Related

[[detours]] · [[cheat-engine]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
