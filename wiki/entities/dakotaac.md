---
title: DakotaAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/norbertbaricz__DakotaAC.md
updated: 2026-08-10
confidence: medium
---

# DakotaAC

Advanced anti-cheat plugin for Minecraft Java servers (Spigot/Paper). Written in Java (Maven); monitors player behavior in real time via **ProtocolLib** packet inspection and **Citizens2** NPCs. Modular checks cover combat (aimbot, kill aura, reach, velocity), movement, world interaction, and inventory exploits. Server operators configure individual modules, violation thresholds, and automated kick or ban actions through admin commands and YAML settings. (source: wiki/sources/descriptions/norbertbaricz__DakotaAC.md)

Targets survival, PvP, minigame, and competitive server operators needing configurable server-side protection against common client-side cheats — in the same Java-server operator lane as [[avaanticheat]] and [[minecraft-anticheatai]], distinct from kernel products such as [[easy-anti-cheat]].

## Links

- Repo: https://github.com/norbertbaricz/DakotaAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[avaanticheat]] · [[minecraft-anticheatai]] · [[oomph]] · [[phantom-client]] · [[minecpp]]
