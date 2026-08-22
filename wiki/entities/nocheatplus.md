---
title: NoCheatPlus
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/NoCheatPlus__NoCheatPlus.md
updated: 2026-08-22
confidence: medium
---

# NoCheatPlus

Open-source anti-cheat plugin for Minecraft **Bukkit** and **Spigot** servers. Written in Java as a multi-module Maven project with shared utilities, a Bukkit plugin core, and version-specific CraftBukkit and Spigot compatibility layers. Implements modular checks for movement, combat, block break and place, inventory abuse, chat spam, and suspicious network packet rates, with configurable violation actions such as cancel, log, and setback. Reflection-based Minecraft internals access and client-mod MOTD handling support broad server version coverage. (source: wiki/sources/descriptions/NoCheatPlus__NoCheatPlus.md)

Targets Minecraft server operators and game-security researchers studying server-side anti-cheat design — a long-standing reference in the same Java-server operator lane as [[avaanticheat]] and [[dakotaac]], and bridged by newer plugins such as [[minecraft-anti-cheat]], distinct from kernel products such as [[easy-anti-cheat]].

## Detection stack

Modular movement, combat, block, inventory, chat, and packet-rate checks; configurable cancel/log/setback violation actions; reflection-based internals access; client-mod MOTD handling for broad Bukkit/Spigot version coverage.

## Links

- Repo: https://github.com/NoCheatPlus/NoCheatPlus

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[avaanticheat]] · [[dakotaac]] · [[minecraft-anti-cheat]] · [[ycbr-anticheat]] · [[windfall-anticheat]] · [[minecraft-anticheatai]]
