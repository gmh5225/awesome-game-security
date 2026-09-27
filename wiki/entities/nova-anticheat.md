---
title: NOVA AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Jdgshsvejevhevejeve__NOVA-AntiCheat.md
updated: 2026-09-27
confidence: medium
---

# NOVA AntiCheat

**NOVA AntiCheat** (Jdgshsvejevhevejeve/nova-anticheat) is a lightweight **server-side anti-cheat plugin** for **Minecraft Paper 1.21** servers. Written in **Java 21** with a **Gradle** build, it detects common client-side cheats without requiring players to install anything—monitoring movement, combat, and block interactions through **Bukkit event handlers**. (source: wiki/sources/descriptions/Jdgshsvejevhevejeve__NOVA-AntiCheat.md)

README category: Anti Cheat / Open Source Anti Cheat System / game:minecraft.

## Detection surface

Detection modules cover:

- **Movement** — speed, flight, no-fall, suspicious rotation
- **Combat** — reach, auto-clicker
- **World** — fast break/place

Checks use **buffered thresholds** and a **violation-level system** that decays over time to reduce false-positive escalation.

## Enforcement

When thresholds are exceeded, configurable actions can:

- Warn the player
- **Setback** (teleport to last-known safe position)
- Kick from the server

Admin commands support alerts, per-player violation info, and config reloads.

## Positioning

Starter **Paper 1.21** server-side AC framework for administrators who want a readable Bukkit-event baseline covering movement, combat, and block checks—not full physics simulation like [[grim]] or modular production stacks like [[h-ac]]. Sits beside fly-focused plugins such as [[nofly]] and heuristic Paper plugins such as [[bs-anticheat]].

## Peers

[[h-ac]] · [[nofly]] · [[bs-anticheat]] · [[grim]] · [[minecraft-anticheat-list]]

## Links

- Repo: https://github.com/jdgshsvejevhevejeve/nova-anticheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]]
