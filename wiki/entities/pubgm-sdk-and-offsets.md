---
title: pubgm-sdk-and-offsets
kind: entity
topics: [mobile-security, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__pubgm_sdk_and_offsets.md
updated: 2026-08-07
confidence: medium
---

# pubgm-sdk-and-offsets

Dumped **SDK and offset collection** for PUBG Mobile client builds **1.5** and **1.9** (gmh5225). Full UE4 class hierarchy from the game's reflection system: member byte offsets, bitmask fields, virtual function pointers, function addresses, and type information for hundreds of classes (`World`, `Level`, `PlayerController`, `Character`, `PrimitiveComponent`, `SkeletalMeshComponent`, weapons, vehicles, rendering, physics, networking, gameplay). Targets the **ARM32** Android mobile build. (source: wiki/sources/descriptions/gmh5225__pubgm_sdk_and_offsets.md)

Useful for mobile game security researchers studying PUBG Mobile UE4 memory layout, external/internal cheat development, or Android anti-cheat coverage analysis. Sits beside generic Android UE4 dumpers such as [[ue4dumper]] and title-specific PUBG Mobile tooling such as [[bypass-pubg-mobile-imgui]] and [[pubg-mobile-pak-extract]].

## Links

- Repo: https://github.com/gmh5225/pubgm_sdk_and_offsets

## Related

[[unreal-object-model]] · [[ue4dumper]] · [[bypass-pubg-mobile-imgui]] · [[pubg-mobile-pak-extract]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
