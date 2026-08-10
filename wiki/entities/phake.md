---
title: phake
kind: entity
topics: [game-hacking, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__pHake.md
updated: 2026-08-08
confidence: medium
---

# phake

GTA V **mod menu and cheat framework** (gmh5225; cheat / `[Mod Menu]`). C++ codebase demonstrating open-world cheat architecture: vehicle spawning, teleportation, money modifications, player ESP, god mode, and other gameplay alterations. Hooks into GTA V's **RAGE engine** via **ScriptHookV** or **direct memory access** to manipulate game state. Aimed at game security researchers studying GTA V modding and anti-cheat evasion in Rockstar titles. (source: wiki/sources/descriptions/gmh5225__pHake.md)

Distinct from GTA:SA binary-compatible reimplementations such as [[gta-reversed-modern]], classic-trilogy reimplementations such as [[regta]], and GTA IV graphics remasters such as [[gta4-rtx]]; this is an **in-process ScriptHookV / memory-mod menu** lane for studying Rockstar open-world client-side cheat surfaces.

## Links

- Repo: https://github.com/gmh5225/pHake (README tag: [Mod Menu])

## Related

[[spookimystic-gta-leak]] · [[gta-reversed-modern]] · [[regta]] · [[gta4-rtx]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[research-rigor]]
