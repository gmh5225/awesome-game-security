---
title: pubg-dump-offset
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__pubg_dump_offset.md
updated: 2026-08-07
confidence: medium
---

# pubg-dump-offset

Versioned **PUBG desktop memory-offset collection** (gmh5225; README `[Offset]`) spanning dozens of client builds from **19.1** through **24.2**. Each version-specific header hardcodes UE4 globals and gameplay fields: `GObjects`, `GWorld`, **Xenuine** decryption keys, `FNameEntry`, player state (`Health`, `GroggyHealth`, `TeamNum`), camera parameters, weapon data, bone indices, vehicle structures, and item/loot offsets. (source: wiki/sources/descriptions/gmh5225__pubg_dump_offset.md)

Per-patch files also track encrypted pointer bases (`XenuineDecrypt`), skeletal-mesh bone arrays, weapon trajectory/ballistics data, and replay/spectator detection fields—forming a historical record of how PUBG's UE4 memory layout and Xenuine encryption evolved across updates. Useful for studying offset drift, Xenuine scheme changes, and anti-cheat hardening across patch cycles.

## Links

- Repo: https://github.com/gmh5225/pubg_dump_offset

## Related

[[unreal-object-model]] · [[pubg-internal]] · [[pubgm-sdk-and-offsets]] · [[valorant-externals]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
