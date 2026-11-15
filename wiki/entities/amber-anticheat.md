---
title: AmberAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/phantantai73__AmberAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-15
confidence: medium
---

# AmberAntiCheat

**AmberAntiCheat** (phantantai73/AmberAntiCheat) is a **Paper/Spigot** Minecraft server plugin that combines movement/combat anti-cheat with **anti-x-ray**, **anti-block-ESP**, and player-visibility hardening for survival multiplayer (SMP). It is implemented in **Java 21** with **Maven**, targeting the Paper API and **PacketEvents** for packet-level inspection. (source: wiki/sources/descriptions/phantantai73__AmberAntiCheat.md)

## Detection and packets

- **Packet-based checks** — movement and combat packets analyzed for reach, clicks-per-second (CPS), and timer-style violations.
- **Server-side modules** — designed for **20 TPS** hosts without requiring a modified client.

## Anti-x-ray and ESP countermeasures

- **Asynchronous occlusion engine** — server-side visibility/occlusion work off the main thread where possible.
- **Ore and chest hiding** — mitigates x-ray and block-ESP clients.
- **Player visibility rules** — Y-layer splits and line-of-sight constraints on who can see whom.

## Staff tooling

In-game admin features include watch, freeze, reload, a seven-module settings GUI, and a suspect-list workflow for staff review.

## Links

- Repo: https://github.com/phantantai73/AmberAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[minecraft-anti-cheat]] · [[civ-anticheat]] · [[zyven-anticheat]] · [[larping-anti-cheat]] · [[thorium-minecraft-plugin]]