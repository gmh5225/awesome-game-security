---
title: PalAntiCheat-poc
kind: entity
topics: [anti-cheat, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/g91__PalAntiCheat-poc.md
updated: 2026-08-15
confidence: medium
---

# PalAntiCheat-poc

**Palworld UE5 anti-cheat proof-of-concept** (g91) bundling a complete dumped SDK—class definitions, function signatures, and struct layouts for NPC, player, animation, audio, and AI modules—plus `PropertyFixup.hpp` routines that validate `UObject`/`UProperty` consistency. Useful for game security researchers studying SDK-level integrity checks as a foundation for detecting memory manipulation of game state in the cheat / game:palworld [UE5] lane. (source: wiki/sources/descriptions/g91__PalAntiCheat-poc.md)

Complements title-specific Palworld tooling such as [[palworld-anti-cheat]] (C# AC research), [[palworld-sdk-dump]] (pre-generated UE5 SDK headers), [[palworld-modding-kit]] (modding scaffold), and [[unreal-object-model]].

## Links

- Repo: https://github.com/g91/PalAntiCheat-poc

## Related

[[palworld-anti-cheat]] · [[palworld-sdk-dump]] · [[palworld-modding-kit]] · [[unreal-object-model]] · [[overviews/anti-cheat]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
