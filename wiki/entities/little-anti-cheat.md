---
title: Little Anti-Cheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/J-Tanzanite__Little-Anti-Cheat.md
updated: 2026-08-24
confidence: medium
---

# Little Anti-Cheat

Open-source **SourceMod anti-cheat plugin** for **Source engine** multiplayer dedicated servers. Written in **SourcePawn**, it targets community server administration for titles such as **Team Fortress 2** and **Counter-Strike** without requiring client-side installs—the same server-authoritative model as [[nocheatz-3]] and [[cs2ac]]. (source: wiki/sources/descriptions/J-Tanzanite__Little-Anti-Cheat.md)

## Detection surface

Behavioral and state checks include **aimbot** and **aimlock**, **abnormal angles**, **bunnyhop automation**, **fast duck** exploits, and **suspicious ConVar** states.

## Mitigation and operations

Optional **interpolation** and **backtrack countermeasures**, **high-ping enforcement**, plus extensive **logging** and **translation** support for operators running public community servers.

## Links

- Repo: https://github.com/J-Tanzanite/Little-Anti-Cheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[nocheatz-3]] · [[cs2ac]] · [[csgo-ac]] · [[source-engine]] · [[hl2sdk]] · [[source-netvars]] · [[ai-aimbot-detection]]
