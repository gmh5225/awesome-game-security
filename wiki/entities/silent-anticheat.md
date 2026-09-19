---
title: Silent AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/danielreytalan635-tech__silent-anticheat.md
updated: 2026-09-19
confidence: medium
---

# Silent AntiCheat

Server-side-only, **alert-only** anti-cheat mod for **Minecraft 26.2** on the **Fabric** loader. Written in Java, it detects suspicious **flight or hover**, **speed or teleport**, and **reach** cheats without ever kicking, banning, or rubberbanding players—styled alert messages go to the server console and online operators instead. Detection runs entirely on the server through **per-tick movement tracking** and **attack or block-break distance checks**, with conservative tunable thresholds to limit false positives. Uses Fabric API server tick and player event hooks; ships as a Gradle-built mod that regular connecting players do not need to install. Targets Minecraft server operators and game security staff who want lightweight, non-punitive cheat monitoring on Fabric servers. (source: wiki/sources/descriptions/danielreytalan635-tech__silent-anticheat.md)

## Detection stack

- **Movement heuristics** — per-tick tracking for flight/hover, speed, and teleport anomalies.
- **Combat/world reach** — attack and block-break distance checks against configurable thresholds.
- **Alert-only workflow** — console and online-operator styled alerts; no kicks, bans, or rubberbanding.
- **Server-side only** — no client mod required for connecting players.

## Links

- Repo: https://github.com/danielreytalan635-tech/silent-anticheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cheatcheck]] · [[sentinel-anticheat-neoforge]] · [[windfall-anticheatf]] · [[grim]] · [[minecraft-anticheat-list]] · [[the-dreamers-guards]]
