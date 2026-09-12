---
title: UltimateMeteorAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/EpicLizard05013__UltimateMeteorAntiCheat.md
updated: 2026-09-12
confidence: medium
---

# UltimateMeteorAntiCheat

Java-based Minecraft **Paper** server plugin that combines anti-cheat detection with anti-duplication protections for multiplayer survival servers. Targets Paper **1.21.x** (README lists **1.21.11**).

Combat checks include reach, autoclicker, and aim-modulo detection. Movement checks cover fly, speed, nofall, and jesus exploits. World checks target fastplace and scaffold abuse. Beyond cheat heuristics, the plugin blocks common item-duplication vectors through inventory transaction auditing, nested-container restrictions, and packet desync mitigation.

Violations flow through a configurable escalation ladder with logging, whitelisting, admin commands, and optional Discord webhook alerts. Intended for server operators who need server-side cheat and exploit prevention on survival hosts. (source: wiki/sources/descriptions/EpicLizard05013__UltimateMeteorAntiCheat.md)

## Detection stack

Combat: reach, autoclicker, aim-modulo. Movement: fly, speed, nofall, jesus. World: fastplace, scaffold. Anti-dupe: inventory transaction auditing, nested-container restrictions, packet desync mitigation. Ops: configurable violation escalation, whitelisting, admin commands, optional Discord webhooks.

## Links

- Repo: https://github.com/EpicLizard05013/UltimateMeteorAntiCheat

## Related

[[bs-anticheat]] · [[larping-anti-cheat]] · [[uagc]] · [[icuac]] · [[grim]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
