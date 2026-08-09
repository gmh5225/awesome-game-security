---
title: valorant-external-p2c-leaked
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Valorant-External-P2C-Leaked.md
updated: 2026-08-09
confidence: medium
---

# valorant-external-p2c-leaked

Leaked Valorant **external pay-to-cheat (P2C)** source (C++; README `[External]`; gmh5225) operating out-of-process via a **kernel driver** for memory access. Implements **ESP**, **aimbot**, and **triggerbot** by reading Unreal Engine game state externally while [[vanguard]] anti-cheat is running — a typical commercial external Valorant cheat architecture. Aimed at anti-cheat researchers studying P2C cheat design patterns and Vanguard bypass techniques. (source: wiki/sources/descriptions/gmh5225__Valorant-External-P2C-Leaked.md)

Sits beside other gmh5225 external stacks such as [[valorant-external-source]], [[valorant-cheat-external]], and [[valorant-external]], kernel read drivers such as [[valo-driver]], and offset feeds such as [[valorant-externals]] rather than in-process internal bases.

## Links

- Repo: https://github.com/gmh5225/Valorant-External-P2C-Leaked

## Related

[[vanguard]] · [[valorant-external-source]] · [[valorant-cheat-external]] · [[valorant-external]] · [[valo-driver]] · [[valorant-externals]] · [[unreal-object-model]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
