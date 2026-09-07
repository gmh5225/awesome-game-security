---
title: TShock
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Pryaxis__TShock.md
updated: 2026-09-07
confidence: medium
---

# TShock

**Terraria server framework** (Pryaxis) built as a plugin on the Terraria Server API. Written in **C#** for .NET, it combines server administration with **Bouncer**, an anti-cheat and anti-hack layer that inspects network packets and player actions to block exploits and griefing. (source: wiki/sources/descriptions/Pryaxis__TShock.md)

## Features

Server-side characters, permission groups, item bans, regions, warps, and a large command set, backed by SQLite, MySQL, or PostgreSQL. Exposed through a REST interface and extensible plugin system. Adds protocol guards and patches for known Terraria networking flaws.

## Audience

Primary tool for **Terraria multiplayer server operators** who need server-authoritative cheat prevention, permissions, and community moderation without a native Windows client AC stack.

## Links

- Repo: https://github.com/Pryaxis/TShock

## Related

[[dead-anticheat]] · [[7dtd-anticheatmod]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
