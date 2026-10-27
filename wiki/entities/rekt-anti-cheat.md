---
title: RektAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/AndrewDisco__RektAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: medium
---

# RektAntiCheat

Java **Minecraft** server plugin (**RAC**) that detects and blocks common client cheats and unauthorized player behavior on **Spigot/Bukkit** hosts. Ships as a Maven-built JAR; integrates **PacketEvents** with Netty-style packet interception to inspect network traffic alongside in-game movement and combat state. (source: wiki/sources/descriptions/AndrewDisco__RektAntiCheat.md)

Targets server operators and developers hardening multiplayer survival and PvP against widespread hack clients; check modules consolidate community-sourced patterns rather than a single narrow exploit class.

## Detection stack

Combat (kill aura, reach, autoclicker); movement (fly, speed, phase, scaffold); packet, inventory, timer, and crash-related checks. Optional join-time tooling flags proxies and related connection metadata.

## Links

- Repo: https://github.com/AndrewDisco/RektAntiCheat

## Related

[[grim]] · [[minecraft-anti-cheat]] · [[nocheatplus]] · [[ycbr-anticheat]] · [[minecraft-anticheat-list]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
