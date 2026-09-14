---
title: ServerGuard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/trevorftp__ServerGuard.md
  - wiki/sources/README-categories.md
updated: 2026-09-14
confidence: medium
---

# ServerGuard

**Vintage Story** server mod that hardens multiplayer hosts against client-side cheating by intercepting world data before it reaches players. Written in C#, it uses **Harmony** patches on the server networking stack to conceal fully enclosed ore blocks and replace some visible ore with decoys in host rock, mitigating x-ray style resource exploits. It also filters entity visibility with server-side raycasts so occluded creatures and optionally players are not sent to clients, and can spawn configurable creature decoys to confuse wallhack tools. Administrators tune ore concealment, decoy density, chunk caching, entity ray budgets, and decoy counts through ModConfig and monitor protection via the `/serverguard` command. (source: wiki/sources/descriptions/trevorftp__ServerGuard.md)

Targets Vintage Story server operators needing practical server-side anti-cheat without client modification — in the packet/world-data mitigation lane beside Minecraft plugins such as [[petal-anti-freecam]] and [[antixrayviewer]].

## Mitigation stack

Harmony server-networking patches; enclosed-ore concealment + ore decoys in host rock; server-side entity raycast filtering (creatures/optional players); configurable creature decoys; ModConfig tuning; `/serverguard` admin command.

## Links

- Repo: https://github.com/trevorftp/ServerGuard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[petal-anti-freecam]] · [[antixrayviewer]] · [[minecraft-anticheat-list]]
