---
title: Lenrete Mod
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/lolizei__Lenrete-Mod.md
updated: 2026-08-12
confidence: medium
---

# Lenrete Mod

Client-side **Fabric** utility and cheat client for **Minecraft 26.2** with a modular in-game menu spanning combat, movement, rendering, world interaction, player automation, and HUD categories. Written in **Java 25** against official **Mojang mappings**, it ships **43** annotation-discovered modules—including KillAura, ESP, Reach, Flight, and packet-based Blinker—backed by a themeable click GUI, customizable HUD overlays, config profiles, and chat commands. Architecture uses fail-soft **Mixins**, reflection-driven settings with JSON persistence, and 2D screen-projected rendering for overlays. Intended for singleplayer and private-server experimentation as a reference for client-side game modification, packet manipulation, and how server-side anti-cheat detects or blocks common cheat techniques on public servers. (source: wiki/sources/descriptions/lolizei__Lenrete-Mod.md)

## Architecture

| Component | Role |
|-----------|------|
| Fabric + Mixins | Minimal fail-soft bytecode hooks into the Java client |
| Annotation module discovery | 43 pluggable feature modules (combat, movement, render, HUD, etc.) |
| Reflection + JSON | Configurable settings with profile persistence |
| Screen projection | 2D overlay rendering for ESP and HUD elements |

## Links

- Repo: https://github.com/lolizei/Lenrete-Mod

## Related

[[phantom-client]] · [[minecpp]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[avaanticheat]] · [[oomph]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
