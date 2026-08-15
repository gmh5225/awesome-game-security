---
title: devilution
kind: entity
topics: [reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/galaxyhaxz__devilution.md
updated: 2026-08-15
confidence: medium
---

# devilution

Complete **reverse engineering** of the original Diablo 1 retail Windows binary into compilable C/C++ source. Reconstructs dungeon generation (`drlg_l1`–`l4`), the rendering pipeline, spell/item/monster data tables, multiplayer networking, save/load serialization, and the Storm MPQ archive library. Preserves the original MSVC 4.20 project structure and includes DiabloUI and Storm DLL sources, with build support for modern compilers alongside the original DSP/DSW files. (source: wiki/sources/descriptions/galaxyhaxz__devilution.md)

Sits in the Game Develop / source lane — a readable late-1990s Windows RPG codebase for decompilation and engine-structure study, not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/galaxyhaxz/devilution (README tag: [Reversed Devilution])

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[zelda3]] · [[gta-reversed-modern]] · [[research-rigor]]
