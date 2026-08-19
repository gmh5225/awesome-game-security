---
title: OxClient
kind: entity
topics: [game-hacking, mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/adanainv3-creator__OxClient.md
updated: 2026-08-19
confidence: medium
---

# OxClient

Android **Minecraft Bedrock Edition** client that sits between the game and remote servers via a **local packet relay**. Written mainly in **Kotlin** with Gradle/Android tooling; embeds **CloudburstMC Bedrock protocol codecs** plus **NBT** handling in Java for multi-version packet parsing. (source: wiki/sources/descriptions/adanainv3-creator__OxClient.md)

## Features

- **Auth** — Microsoft device-code login.
- **Combat / movement** — modular cheats such as KillAura, CrystalAura, fly, and speed.
- **Visuals** — ESP overlays and FOV changes.
- **Architecture** — packet listeners and an event bus drive session management, LAN broadcasting, and in-game overlays.

Aimed at Bedrock multiplayer cheating and **protocol reverse-engineering** research relevant to game security and anti-cheat analysis. Sits in the offensive Bedrock **MITM client** lane opposite defensive proxy AC such as [[oomph]], and beside Java in-process clients such as [[phantom-client]] and [[lenrete-mod]].

## Links

- Repo: https://github.com/adanainv3-creator/OxClient

## Related

[[oomph]] · [[phantom-client]] · [[lenrete-mod]] · [[windfall-anticheat]] · [[minecraft-anticheatai]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
