---
title: pubg-dumper
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__pubg-dumper.md
updated: 2026-08-07
confidence: medium
---

# pubg-dumper

PUBG (PlayerUnknown's Battlegrounds) **SDK and offset dumper** (gmh5225; cheat / game:pubg `[Dump]`). Scans the running PUBG client process for Unreal Engine 4 structures and emits class definitions, property offsets, and function addresses—walking `GObjects`/`GNames` arrays, entity class hierarchies, and title-specific data layouts. (source: wiki/sources/descriptions/gmh5225__pubg-dumper.md)

Useful for game security researchers studying PUBG's UE4 memory layout and anti-cheat analysts mapping cheat tooling that depends on live SDK generation, complementing static offset archives such as [[pubg-dump-offset]] and offensive samples such as [[pubg-external-cheat]] / [[pubg-internal]].

## Links

- Repo: https://github.com/gmh5225/pubg-dumper

## Related

[[unreal-object-model]] · [[pubg-dump-offset]] · [[pubg-external-cheat]] · [[pubg-internal]] · [[unrealdumper-4-25]] · [[valorant-dumper]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
