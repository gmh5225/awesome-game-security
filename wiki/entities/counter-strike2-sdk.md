---
title: counter-strike2-sdk
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Omn1z__Counter-Strike2-SDK.md
updated: 2026-08-22
confidence: medium
---

# counter-strike2-sdk

Header-only **Counter-Strike 2** SDK snapshot (Omn1z; `[SDK]`) exposing large sets of **Source 2** class declarations and enums. Provides structured C++ definitions for entities, gameplay systems, animation types, and engine data layouts with field offsets. Includes engine utility types such as bit-vector implementations used by networked game data structures. Primarily intended for reverse engineering, tooling, and game-security research requiring up-to-date internal type information. (source: wiki/sources/descriptions/Omn1z__Counter-Strike2-SDK.md)

Sits beside generated SDK output such as [[cs2-sdk-source2gen]], hand-maintained CS2 SDK scaffolds such as [[cs2-sdk]], live offset dumpers such as [[cs2-dumper]], and research collections such as [[cs2-things]] as a header-only Source 2 layout artifact.

## Links

- Repo: https://github.com/Omn1z/Counter-Strike2-SDK

## Related

[[cs2-sdk]] · [[cs2-sdk-source2gen]] · [[cs2-dumper]] · [[cs2-offsets]] · [[cs2-things]] · [[source2gen]] · [[source2sdk]] · [[source-netvars]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
