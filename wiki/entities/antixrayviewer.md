---
title: AntiXrayViewer
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/RiseShieldDev__AntiXrayViewer.md
updated: 2026-08-21
confidence: medium
---

# AntiXrayViewer

Paper Minecraft server plugin that automatically detects suspected X-ray cheating and records player activity for later review. Written in Java 21 and built with Gradle, it monitors ore-breaking patterns such as diamond and ancient debris, triggers configurable threshold alerts, and captures roughly three minutes of movement, look direction, and block break or place events. Server administrators can replay sessions from the suspect's first-person perspective using smooth camera interpolation and dedicated commands to list, view, delete, and manage stored recordings. Targets Minecraft server operators and anti-cheat workflows that need evidence-based investigation of mining cheats rather than relying on heuristics alone. (source: wiki/sources/descriptions/RiseShieldDev__AntiXrayViewer.md)

## Detection stack

Ore-breaking pattern monitoring with configurable threshold alerts; ~3-minute session capture of movement, look direction, and block break/place events; first-person replay with smooth camera interpolation; admin commands to list, view, delete, and manage stored recordings.

## Links

- Repo: https://github.com/RiseShieldDev/AntiXrayViewer

## Related

[[minecraft-anti-cheat]] · [[jaranalyzer]] · [[mlanticheat]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[paradox-anticheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
