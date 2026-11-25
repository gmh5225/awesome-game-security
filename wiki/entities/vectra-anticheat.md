---
title: Vectra AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ImNotGemsDc__Vectra-AntiCheat.md
updated: 2026-11-25
confidence: medium
---

# Vectra AntiCheat

**Vectra** is a server-side anti-cheat plugin for **Minecraft Java** on **Paper** (**1.21**, Java 21). It is built with **Maven**, combining Bukkit event listeners with **PacketEvents** packet hooks for movement, combat, and protocol validation alongside game-state inspection. (source: wiki/sources/descriptions/ImNotGemsDc__Vectra-AntiCheat.md)

Detection spans fly and movement exploits, kill aura and reach, scaffold and block-interaction cheats, timer and blink, autoclicker, inventory abuse, and packet-spoofing patterns—using ray tracing, bounding boxes, and per-player state with **ping-aware** thresholds. Staff receive in-game violation alerts backed by a **decaying violation-level** counter; repeat offenders can be kicked automatically. Operators can toggle alerts and grant bypass permissions.

Targets Paper-compatible survival or PvP server administrators and game-security practitioners who want a lightweight, inspectable open-source anti-cheat.

## Links

- Repo: https://github.com/ImNotGemsDc/Vectra-AntiCheat

## Related

[[rekt-anti-cheat]] · [[virgola-anticheat]] · [[grim]] · [[kozy-anticheat]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[detector-operations]]