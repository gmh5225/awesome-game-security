---
title: valorant-external-source
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Valorant-External-Source.md
updated: 2026-08-09
confidence: medium
---

# valorant-external-source

External Valorant cheat **source** (README `[External]`; gmh5225) providing **ESP**, **aimbot**, and **player information** via kernel-driver external memory reads of UE4 game state — no injection into the [[vanguard]]-protected process. Overlays render through a separate window or hijacked overlay. Aimed at anti-cheat researchers studying external Valorant cheat architecture and Vanguard kernel protection effectiveness. (source: wiki/sources/descriptions/gmh5225__Valorant-External-Source.md)

Sits beside other gmh5225 external stacks such as [[valorant-cheat-external]] and [[valorant-external]], kernel read drivers such as [[valo-driver]], and offset feeds such as [[valorant-externals]] rather than in-process internal bases.

## Links

- Repo: https://github.com/gmh5225/Valorant-External-Source

## Related

[[vanguard]] · [[valorant-cheat-external]] · [[valorant-external]] · [[valo-driver]] · [[valorant-externals]] · [[unreal-object-model]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
