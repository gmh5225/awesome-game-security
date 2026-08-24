---
title: Hexze Anticheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Hexze__anticheat.md
updated: 2026-08-24
confidence: medium
---

# Hexze Anticheat

**Cheater Detector** is a Lua anti-cheat plugin for the **Starfish** framework that monitors in-game players and flags behavior patterns associated with cheating. Configurable detection modules include **NoSlow**, **AutoBlock**, **Eagle**, **Scaffold**, **Tower**, **LagRange**, and **NoBreakDelay**, each with enable toggles, violation thresholds, alert cooldowns, and optional sound alerts. The plugin tracks player movement, equipment, animations, metadata, and block-break timing, then raises alerts and emits events when violation levels are exceeded. Targets Minecraft-style game security and staff monitoring use cases where operators need to identify likely cheaters from client-side or plugin-side observation. (source: wiki/sources/descriptions/Hexze__anticheat.md)

## Detection modules

- **Movement/combat** — NoSlow, AutoBlock, Eagle, LagRange.
- **Block interaction** — Scaffold, Tower, NoBreakDelay.
- **Telemetry** — movement, equipment, animations, metadata, block-break timing.
- **Operator controls** — per-check enable toggles, violation thresholds, alert cooldowns, optional sound alerts, event emission on threshold breach.

Heuristic server-side/plugin-side observation lane for Starfish-hosted Minecraft-style worlds — distinct from Java Spigot/Paper plugins such as [[windfall-anticheat]] and Fabric server mods such as [[windfall-anticheatf]].

## Links

- Repo: https://github.com/Hexze/anticheat

## Related

[[windfall-anticheat]] · [[arrow-anticheat]] · [[paradox-anticheat]] · [[scythe-anticheat]] · [[ycbr-anticheat]] · [[minecraft-anticheat-list]] · [[the-dreamers-guards]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
