---
title: Grim (GrimAC)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/GrimAnticheat__Grim.md
updated: 2026-08-25
confidence: medium
---

# Grim (GrimAC)

Open-source **Minecraft** anticheat (**GrimAC**) for modern server versions and protocol combinations. Built primarily in **Java** and **Kotlin**, it implements detailed **movement simulation**, **world replication**, and **latency-aware validation** logic. The architecture is heavily **asynchronous** and **multithreaded** to scale checks while reducing false positives across complex gameplay edge cases. Primary use case is **server-side cheat detection** for Minecraft communities that need accurate and actively maintained protection. (source: wiki/sources/descriptions/GrimAnticheat__Grim.md)

## Detection stack

Movement simulation with world replication; latency-aware packet validation; async multithreaded check pipeline for throughput and low false-positive rates on modern Paper/Spigot server versions.

## Links

- Repo: https://github.com/GrimAnticheat/Grim

## Related

[[minecraft-anti-cheat]] · [[ycbr-anticheat]] · [[nocheatplus]] · [[minecraft-anticheat-list]] · [[yuri]] · [[phantom-client]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
