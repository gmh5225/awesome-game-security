---
title: GuardAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/PalassCQ__GuardAC.md
updated: 2026-08-22
confidence: medium
---

# GuardAC

AI-assisted, free and open-source server-side anti-cheat plugin for Minecraft **1.21.x** on **Spigot**, **Paper**, or **Folia**. Written in Kotlin as a Gradle-built JavaPlugin (Java 17+ to run; JDK 21+ to build), it watches gameplay locally, sends aim-check requests to a cloud inference API, and applies alerts, violation tracking, and punishments on the server. Operators can run alert-only mode, share cross-server reputation, configure punishment ladders with optional ban animations, monitor suspects live with holograms, trigger on-demand deep scans, and automatically exempt Geyser Bedrock players and selected WorldGuard regions. The public repository ships only the plugin client; the remote inference backend stays private. Targets Minecraft server operators who want conservative, operator-controlled AI combat cheat detection. (source: wiki/sources/descriptions/PalassCQ__GuardAC.md)

## Detection stack

Local gameplay monitoring with cloud API aim-check verdicts; configurable alert-only mode; violation counters and punishment ladders; cross-server reputation sharing; live suspect monitoring and holograms; on-demand deep scans; Geyser Bedrock and WorldGuard region exemptions.

## Links

- Repo: https://github.com/PalassCQ/GuardAC

## Related

[[mlanticheat]] · [[minecraft-anticheatai]] · [[minecraft-anti-cheat]] · [[windfall-anticheat]] · [[dakotaac]] · [[antiguard]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
