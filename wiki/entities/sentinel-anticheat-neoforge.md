---
title: Sentinel AntiCheat (NeoForge)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Charlie328402__Sentinel-Anti-Cheat.md
updated: 2026-08-30
confidence: medium
---

# Sentinel AntiCheat (NeoForge)

Server-side anti-cheat system for **NeoForge** Minecraft servers. Written in Java, the mod detects movement, combat, and world cheats through tick- and event-based checks without mixins or packet interception. Monitors speed, flight, water-walking, reach, killaura, autoclicker, and x-ray mining patterns, logging each violation to a JSONL audit file. A companion Python Discord bot tails that log, posts formatted embeds, pings staff when cumulative violation levels cross a configurable threshold, and persists history to a relational database with optional FTP log mirroring. Deliberately avoids automatic bans or kicks, focusing on staff alerting and audit trails for server administrators managing cheat-prone multiplayer worlds. Distinct from HEEAAP [[sentinel-anti-cheat]], the educational Windows usermode anti-debug daemon. (source: wiki/sources/descriptions/Charlie328402__Sentinel-Anti-Cheat.md)

## Detection stack

Tick- and event-based movement/combat/world checks (no mixins, no packet interception); speed, flight, water-walking, reach, killaura, autoclicker, and x-ray mining heuristics; JSONL violation logging; Python Discord bot with embed alerts, cumulative violation-level staff pings, relational DB history, and optional FTP log mirroring; alert-only design without automatic bans or kicks.

## Links

- Repo: https://github.com/Charlie328402/Sentinel-Anti-Cheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[katapult-anticheat]] · [[grim]] · [[cheatcheck]] · [[amethyst]] · [[bs-anticheat]] · [[minecraft-anticheat-list]] · [[inertia]] · [[sentinel-anti-cheat]]
