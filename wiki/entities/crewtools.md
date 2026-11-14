---
title: Crew Tools
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/swheettaos__crewtools.md
updated: 2026-11-14
confidence: medium
---

# Crew Tools

**Host-only** **BepInEx 6** **IL2CPP** plugin for **Moon Sweepers** crew multiplayer sessions. Implemented in **C#** with hooks into game methods (plus small Python utilities for API docs and packaging). Gives session hosts a full moderation and permission stack: per-player toggles for build, shop, and related actions; protected base zones; rolling spending caps; money-reconciliation anti-cheat; and a cheat watch for speed, flight, reach, deposits, and teleports. (source: wiki/sources/descriptions/swheettaos__crewtools.md)

## Operator tooling

In-game tabbed admin window for kicks, bans, and housekeeping (periodic cleanup, ban reclaim). Optional HTTP API under `/crew/` mirrors UI actions—list players, apply bans/kicks—for external dashboards or scripts. Targets operators who want practical server-side enforcement without restarting the game when paired with a hot-reload-capable loader. (source: wiki/sources/descriptions/swheettaos__crewtools.md)

## Posture

Runs on the **host client** only (not a dedicated headless server). Complements other Unity IL2CPP host-moderation stacks such as [[banmod]], [[au-anticheat]], and [[among-us-anti-cheat]]; distinct from kernel products such as [[easy-anti-cheat]].

## Links

- Repo: https://github.com/swheettaos/crewtools

## Related

[[bepinex]] · [[il2cpp]] · [[banmod]] · [[au-anticheat]] · [[among-us-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]