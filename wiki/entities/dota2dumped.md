---
title: dota2dumped
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/ikhsanprasetyo__dota2dumped.md
updated: 2026-08-04
confidence: medium
---

# dota2dumped

Maintained **Dota 2 offset dumper** (`[Offset dumper]`) publishing netvar offsets, interface pointers, and Source 2 class structure definitions extracted from Dota 2 client binaries. Ships C++ headers with entity field offsets, ability data structures, and game-state layouts refreshed after patches—for modders and game-security researchers tracking Source 2 memory layout in Dota 2. (source: wiki/sources/descriptions/ikhsanprasetyo__dota2dumped.md)

Treat as a live layout feed that rots per Dota 2 update; pair with [[source-netvars]] and Source 2 SDK tooling such as [[source2gen]] / [[source2sdk]].

## Links

- Repo: https://github.com/ikhsanprasetyo/dota2dumped

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-netvars]] · [[source2gen]] · [[source2sdk]] · [[cs2-offsets]] · [[dota2-overlay-2-0]]
