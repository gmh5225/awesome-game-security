---
title: LocalAnticheat 1.8.9
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/freezato__LocalAnticheat-1.8.9.md
updated: 2026-08-15
confidence: medium
---

# LocalAnticheat 1.8.9

Client-side Minecraft Forge mod for version **1.8.9** that passively monitors network packets the game client sends and receives to detect common combat and movement cheats without modifying traffic or reporting to servers. Written in Java (Gradle); detection results appear only in the player's local chat via configurable flag formats. (source: wiki/sources/descriptions/freezato__LocalAnticheat-1.8.9.md)

## Checks

Eleven automated checks: AutoClicker, KillAura, Reach, Speed, Fly, Velocity, NoFall, Timer, FastPlace, FastBreak, and Scaffold. Applies server-side anti-cheat design principles such as monotonic timing and knockback vector analysis. Can evaluate both the local player and other visible players on a server.

## Configuration

Integrates with OneConfig for settings. Intended for PvP players and security researchers who want on-client cheat awareness on multiplayer servers where server-side anti-cheat may be limited or absent.

## Links

- Repo: https://github.com/freezato/LocalAnticheat-1.8.9

## Related

[[phantom-client]] · [[avaanticheat]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[lenrete-mod]] · [[minecpp]] · [[oomph]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
