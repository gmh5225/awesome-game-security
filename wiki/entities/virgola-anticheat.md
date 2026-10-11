---
title: VirgolaAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ImNotVirgola__VirgolaAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: medium
---

# VirgolaAntiCheat

Server-side anti-cheat plugin for **Paper 1.21.11** Minecraft servers. Java 21 Maven build hooks movement, combat, and block-placement through Bukkit events plus **PacketEvents** network inspection. Built-in checks cover fly, speed, scaffold, Jesus (water walking), no-fall, invalid packets, and KillAura-style combat abuse (reach, aim angles, swing patterns) with lag compensation and per-player violation tracking. Staff workflows include in-game commands, a configuration GUI, player freeze, alerts, and optional Discord webhook notifications—aimed at multiplayer operators wanting lightweight cheat prevention without kernel or commercial AC stacks. (source: wiki/sources/descriptions/ImNotVirgola__VirgolaAntiCheat.md)

## Detection stack

Movement/combat/packet modules (fly, speed, killaura, scaffold, bad packets); PacketEvents + Bukkit event hooks; lag compensation and violation counters; staff GUI, freeze, and Discord alerts.

## Links

- Repo: https://github.com/ImNotVirgola/VirgolaAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[bs-anticheat]] · [[h-ac]] · [[novaguard]] · [[minecraft-anticheat-list]]
