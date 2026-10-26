---
title: Bloon AntiCheat
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/ValenMyHeartDev__BloonAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-26
confidence: medium
---

# Bloon AntiCheat

**Bloon AntiCheat** (ValenMyHeartDev/BloonAntiCheat) is a Paper and Spigot **Minecraft Java Edition** server plugin (Java 17; Maven; Paper API) that listens to **Bukkit player events** for lightweight movement, combat, and input heuristics plus staff-facing alerts and punishment tooling—not a commercial client-side AC stack. README category: Anti Cheat / Open Source Anti Cheat System. (source: wiki/sources/descriptions/ValenMyHeartDev__BloonAntiCheat.md)

## Detection stack

- **Autoclicker:** clicks-per-second limits on combat input.
- **Combat:** configurable reach distance; blocks killaura-style hits beyond allowed range.
- **Triggerbot:** accumulating combat buffer for suspicious firing patterns.
- **Movement:** fly violations.

## Staff / enforcement

Failed checks broadcast formatted alerts to the console and to online staff who hold the alerts permission. Privileged operators reload YAML settings, inspect per-player stats, and open a read-only in-game GUI listing sanction entries defined in config.

## Positioning

Event-driven server-side checks without client mods; targets server owners and moderators who want a simple configurable layer beside heuristic peers such as [[lavaguard-ac]] and alert-first Paper plugins such as [[aegis-ac]], and contrasts with PacketEvents-heavy Paper/Folia plugins ([[h-ac]], [[virgola-anticheat]], [[lino-ac]]) and injectable observers such as [[rain-injectable]].

## Links

- Repo: https://github.com/ValenMyHeartDev/BloonAntiCheat

[[lavaguard-ac]] · [[aegis-ac]] · [[h-ac]] · [[detector-operations]] · [[overviews/anti-cheat]]
