---
title: Speedhack
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/absoIute__Speedhack.md
  - wiki/sources/descriptions/Letomaniy__Speed-Hack.md
updated: 2026-08-23
confidence: medium
---

# Speedhack

Lightweight **Windows speed-manipulation** sample by absoIute. Written in C++, buildable as an injectable DLL that hooks timing-related APIs via **Microsoft Detours** to change a target process's perceived execution speed — accelerate, slow down, or pause runtime behavior. Commonly used in cheat-development experiments and anti-cheat research around **time tampering** (`Detection:SpeedHack`). (source: wiki/sources/descriptions/absoIute__Speedhack.md)

Simpler and more focused than the integrated speedhack feature in [[cheat-engine]]; illustrates the Detours-based timing-hook pattern that AC stacks may monitor via clock-drift or API-integrity checks. Cheat Engine–style siblings [[speed-hack]] (Letomaniy; Visual Studio DLL; keyboard slowdown/accelerate/restore) and compact learner sample [[ce-speed-hack]] (IamSanjid; core Detours hooking logic) extend the same lane. (source: wiki/sources/descriptions/Letomaniy__Speed-Hack.md) (source: wiki/sources/descriptions/IamSanjid__ce_speed_hack.md)

## Links

- Repo: https://github.com/absoIute/Speedhack

## Related

[[speed-hack]] · [[ce-speed-hack]] · [[detours]] · [[cheat-engine]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
