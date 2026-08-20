---
title: Arrow Anti-Cheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/StelGR__ArrowAntiCheat.md
updated: 2026-08-20
confidence: medium
---

# Arrow Anti-Cheat

Custom packet-based Minecraft anti-cheat plugin for Bukkit/Spigot servers, written in Java with support for both Java and Bedrock clients. Uses **PacketEvents** for packet listening and ships check suites for combat (aim assist, autoclicker, kill aura, reach, velocity, hitbox), movement (fly, speed, motion, ground, illegal move), and miscellaneous cheats (bad packets, scaffold, timer, inventory). Detection relies on statistical analysis, movement prediction utilities, and configurable violation handling with alerts, verbose mode, and logging. Targets Minecraft server operators seeking an open-source, **AGPLv3**-licensed anti-cheat, especially smaller servers that cannot afford commercial solutions. (source: wiki/sources/descriptions/StelGR__ArrowAntiCheat.md)

## Detection stack

PacketEvents packet intercept; combat, movement, and miscellaneous check modules; statistical analysis and movement prediction; configurable alerts, verbose mode, and violation logging. Java + Bedrock client support on Bukkit/Spigot.

## Links

- Repo: https://github.com/StelGR/ArrowAntiCheat

## Related

[[windfall-anticheat]] · [[dakotaac]] · [[minecraft-anti-cheat]] · [[ycbr-anticheat]] · [[avaanticheat]] · [[oomph]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
