---
title: RektAntiCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/AndrewDisco__RektAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: medium
---

# RektAntiCheat

Java **Minecraft** server plugin (**RAC**) that detects and blocks common client cheats on **Spigot/Bukkit** hosts. Built with Maven; integrates **PacketEvents** and Netty-style packet interception to correlate network traffic with movement and combat state. (source: wiki/sources/descriptions/AndrewDisco__RektAntiCheat.md)

Detection modules cover combat abuses (kill aura, reach, autoclicker), movement hacks (fly, speed, phase, scaffold), and packet, inventory, timer, and crash-related checks. Optional join-time tooling can flag proxies and related connection metadata. Consolidates community-sourced checks for survival and PvP operators studying Paper/Folia server-side AC patterns.

## Links

- Repo: https://github.com/AndrewDisco/RektAntiCheat

## Related

[[overviews/anti-cheat]] · [[tfg-anticheat-serverside]] · [[virgola-anticheat]] · [[lino-ac]] · [[hero-anti-cheat]] · [[minecraft-anticheat-list]]
