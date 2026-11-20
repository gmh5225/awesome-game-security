---
title: UmbraAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ShadowKuzey__UmbraAC.md
  - wiki/sources/README-categories.md
updated: 2026-11-20
confidence: medium
---

# UmbraAC

**UmbraAC** (ShadowKuzey/UmbraAC) is a **lightweight, modular anti-cheat plugin** for **Minecraft** multiplayer servers built on the **Paper API**. It is implemented in **Java 21** with **Gradle**, targeting modern Paper/Bukkit/Spigot hosts without requiring client modifications. (source: wiki/sources/descriptions/ShadowKuzey__UmbraAC.md)

README category: Open-source Bukkit/Spigot Minecraft plugin with fly, speed, reach, killaura, no-fall, and x-ray checks plus configurable staff alerts.

## Detection modules

Server-side modules cover common client cheats:

- **Movement** — fly, speed, no-fall (movement events and fall-damage heuristics)
- **Combat** — reach, kill aura (combat timing and hit-distance checks)
- **World** — x-ray (ore-mining heuristics)

## Staff tooling

A central **alert manager** routes violations to **in-game staff notifications** and **console logging**. Thresholds are tunable in **YAML**, and administrators can **reload configuration** at runtime.

## Positioning

Practical cheat monitoring for server operators who want a **modular but lightweight** server-side stack—not a full physics-simulation suite like [[grim]] or telemetry-heavy clients like [[thorium-minecraft-plugin]]. Sits beside similar Paper heuristic plugins such as [[zyven-anticheat]], [[nova-anticheat]], and [[amber-anticheat]].

## Links

- Repo: https://github.com/ShadowKuzey/UmbraAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[minecraft-anti-cheat]] · [[zyven-anticheat]] · [[nova-anticheat]] · [[amber-anticheat]] · [[h-ac]]