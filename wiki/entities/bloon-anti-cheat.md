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

Paper and Spigot **Minecraft Java Edition** server plugin (ValenMyHeartDev; Java 17; Maven; Paper API) with lightweight movement, combat, and input heuristics plus staff-facing alerts and punishment tooling. (source: wiki/sources/descriptions/ValenMyHeartDev__BloonAntiCheat.md)

## Detection stack

- **Autoclicker:** clicks-per-second limits.
- **Combat:** configurable reach / killaura-style hit blocking beyond distance.
- **Triggerbot:** accumulating combat buffer for suspicious firing patterns.
- **Movement:** fly violations.

## Staff / enforcement

Formatted alerts to console and online staff with the alerts permission; privileged operators reload YAML settings, inspect per-player stats, and open a read-only in-game GUI listing sanction entries. Targets small hosts wanting a simple configurable layer—not a commercial client-side AC.

## Positioning

Event-driven Bukkit checks without client mods; contrasts with PacketEvents-heavy Paper/Folia plugins ([[h-ac]], [[virgola-anticheat]], [[lino-ac]]) and injectable observers such as [[rain-injectable]].

## Links

- Repo: https://github.com/ValenMyHeartDev/BloonAntiCheat

[[lavaguard-ac]] · [[h-ac]] · [[detector-operations]] · [[overviews/anti-cheat]]
