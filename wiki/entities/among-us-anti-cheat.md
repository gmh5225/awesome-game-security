---
title: Among Us Anti-Cheat (ACE)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/hckerelauk-git__AmongUsAntiCheat.md
updated: 2026-09-28
confidence: medium
---

# Among Us Anti-Cheat (ACE)

**Apex Cheat Ender (ACE)** is a client-side anti-cheat plugin for Among Us (IL2CPP) that detects and responds to common multiplayer cheats in hosted lobbies. Written in C# as a BepInEx 6 plugin using Harmony and Il2CppInterop, it combines static scanning of loaded BepInEx mods against a cheat signature database, event hooks on kills, tasks, vents, and position sync, and kinematic behavior analysis for teleport, speed, and wall-clip abuse. A verdict engine aggregates evidence with time decay and configurable thresholds, optionally auto-kicking offenders when the local player is host. Includes in-game monitoring and settings UI plus desktop splash feedback. (source: wiki/sources/descriptions/hckerelauk-git__AmongUsAntiCheat.md)

Targets Among Us hosts and mod developers who need explainable, rule-based client protection for private sessions. Sits beside host-moderation plugins such as [[banmod]] and [[wellsanticheat]]; distinct from kernel or server-authoritative products such as [[easy-anti-cheat]] or [[magnetite]].

## Detection surfaces

- **Mod signature scan** — static inspection of loaded BepInEx plugins against a cheat signature database.
- **Gameplay event hooks** — kills, tasks, vents, and position-sync RPC paths.
- **Kinematic analysis** — teleport, speed, and wall-clip heuristics from movement state.
- **Verdict engine** — time-decayed evidence aggregation with configurable thresholds and optional host auto-kick.
- **Operator UI** — in-game monitoring, settings UI, and desktop splash feedback; README also lists AI review and RPC flood protection.

## Links

- Repo: https://github.com/hckerelauk-git/amongusanticheat

## Related

[[banmod]] · [[wellsanticheat]] · [[bepinex]] · [[il2cpp]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
