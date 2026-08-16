---
title: osiris
kind: entity
topics: [game-hacking, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/danielkrupinski__Osiris.md
updated: 2026-08-16
confidence: medium
---

# osiris

Open-source **CS:GO internal cheat** in modern C++ (danielkrupinski). Feature-complete reference implementation: ESP (player boxes, health, names), glow outlines, aimbot, triggerbot, backtrack, skin changer, and inventory manipulation. Hooks the Source engine via **interface pointers**, **pattern scanning**, and **VMT hooking**—a canonical layout for studying Source 1 internal cheat architecture and the detection surfaces those techniques expose. (source: wiki/sources/descriptions/danielkrupinski__Osiris.md)

Aimed at game-security researchers and anti-cheat developers building detections for in-process Source cheats—not a production cheat guide.

## Architecture highlights

| Component | Role |
|-----------|------|
| Interface pointers | Resolve Source 1 engine/client exports (`CreateInterface` lane) |
| Pattern scanning | Locate game functions and globals across builds |
| VMT hooking | Intercept virtual methods on engine/client interfaces |
| Visuals | ESP, glow, skin/inventory manipulation |
| Combat | Aimbot, triggerbot, backtrack |

See [[source-netvars]] for netvar/interface layout work and [[csgo-internal-base]] / [[csgo-cheat-base]] for comparable internal scaffolds in the same lane.

## Links

- Repo: https://github.com/danielkrupinski/Osiris

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[source-netvars]] · [[csgo-internal-base]] · [[csgo-cheat-base]] · [[csgosimple]] · [[osiris-and-extra]] · [[vac-hooks]] · [[vac-bypass]] · [[vac]]
