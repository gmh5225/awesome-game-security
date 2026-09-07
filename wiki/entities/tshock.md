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

Mature open-source **Terraria multiplayer server framework** (Pryaxis) built as a plugin on the Terraria Server API. Written in **C#** for .NET, it combines server administration with **Bouncer**, an anti-cheat and anti-hack layer that inspects network packets and player actions to block exploits and griefing. Also provides server-side characters, permission groups, item bans, regions, warps, and a large command set, backed by SQLite, MySQL, or PostgreSQL and exposed through a REST interface and extensible plugin system. Adds protocol guards and patches for known Terraria networking flaws—primary tooling for community server operators who need server-authoritative cheat prevention and moderation without a native Windows client AC stack. (source: wiki/sources/descriptions/Pryaxis__TShock.md)

## Bouncer anti-cheat

Packet and player-action validation layer; blocks exploit and griefing traffic; protocol guards and patches for known Terraria networking flaws.

## Administration

Server-side characters; permission groups; item bans; regions; warps; large command set; SQLite/MySQL/PostgreSQL persistence; REST API; extensible plugin system.

## Links

- Repo: https://github.com/Pryaxis/TShock

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[7dtd-anticheatmod]] · [[dead-anticheat]] · [[petal-anti-freecam]]
