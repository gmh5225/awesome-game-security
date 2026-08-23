---
title: Speed-Hack
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Letomaniy__Speed-Hack.md
updated: 2026-08-23
confidence: medium
---

# Speed-Hack

Windows **C++ injectable DLL** by Letomaniy that manipulates in-game time speed after injection into a target process. Follows a **Cheat Engine–style** approach: **Microsoft Detours** hooks on timing-related APIs, built with Visual Studio, plus keyboard controls to slow down, accelerate, or restore normal speed with configurable values in code. Used for cheat-development practice and for researching how games and anti-cheat systems handle **time manipulation** (`Detection:SpeedHack`). (source: wiki/sources/descriptions/Letomaniy__Speed-Hack.md)

Sibling to the lighter [[speedhack]] sample (absoIute); both illustrate the Detours-based timing-hook pattern that AC stacks may monitor via clock-drift or API-integrity checks.

## Links

- Repo: https://github.com/Letomaniy/Speed-Hack

## Related

[[speedhack]] · [[cheat-engine]] · [[detours]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
