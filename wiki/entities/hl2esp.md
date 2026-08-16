---
title: hl2esp
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/codereversing__hl2esp.md
updated: 2026-08-16
confidence: medium
---

# hl2esp

**Half-Life 2** ESP research sample (codereversing). C/C++ codebase centered on **hooking** to implement player/world ESP for the Source 1 HL2 client—aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / game:half-life 2 lane. (source: wiki/sources/descriptions/codereversing__hl2esp.md)

Sits beside other Source 1 internal samples such as [[l4d2-basic]], [[l4d2-cheat]], [[teamfortress2-internal]], and GoldSrc-era [[1-6-c2]] for comparing hook and ESP patterns across Valve engine generations.

## Architecture highlights

| Component | Role |
|-----------|------|
| Hooking | In-process intercept of Source client/render paths for ESP draw |
| C/C++ | Native HL2 client-side implementation |
| ESP | World-to-screen entity visualization for HL2 targets |

## Links

- Repo: https://github.com/codereversing/hl2esp

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[world-to-screen]] · [[present-hook]] · [[source-engine]] · [[l4d2-basic]] · [[l4d2-cheat]] · [[teamfortress2-internal]] · [[1-6-c2]]
