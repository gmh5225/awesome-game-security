---
title: AntiCheat (raphvallee)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/raphvallee__AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-28
confidence: medium
---

# AntiCheat (raphvallee/AntiCheat)

**AntiCheat** (raphvallee/AntiCheat) is a modular **Paper** Minecraft server anti-cheat **plugin and framework** aimed at plugin authors and operators who want to add checks by implementing a single handler class instead of duplicating Bukkit listeners and punishment code. It targets **Java 25** on **Paper 26.3**, ships **Gradle** builds with **JUnit** tests, and documents strict architectural rules for extensions. (source: wiki/sources/descriptions/raphvallee__AntiCheat.md)

## Architecture

Event flow runs from Bukkit listeners through **movement and combat trackers** into **handler-based checks**, with **centralized exemptions**, violation logging, and configurable punishments.

Reference modules **SpeedA**, **FlyA**, and **ReachA** provide conservative starter detection for speed, flight, and reach.

## Operator tooling

Staff use a Brigadier-based **`/ac`** command for alerts, per-player debug streams, violation levels, and **hot reload** of configuration.

## Links

- Repo: https://github.com/raphvallee/AntiCheat

## Related

[[overviews/anti-cheat]] · [[detector-operations]] · [[minecraft-anticheat-docs]] · [[nova-anticheat]] · [[h-ac]] · [[vyx-anticheat]] · [[anticheat]] (gmh5225 C++ reference; distinct project)