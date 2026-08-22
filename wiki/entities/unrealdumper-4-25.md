---
title: UnrealDumper-4.25
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/guttir14__UnrealDumper-4.25.md
updated: 2026-08-06
confidence: medium
---

# UnrealDumper-4.25

C++ **external** Unreal Engine 4.25+ SDK dumper: pattern-scans `GObjects` and `GNames` in a live UE4 process, walks the `UObject` hierarchy, and emits C++ SDK headers with struct layouts, property offsets, function signatures, and inheritance chains. Reads memory via process handles without injection—useful when in-process dumpers like Dumper-7 are blocked or undesirable. Targets game hackers and reverse engineers generating UE SDKs for cheat development or title analysis. (source: wiki/sources/descriptions/guttir14__UnrealDumper-4.25.md)

## Links

- Repo: https://github.com/guttir14/UnrealDumper-4.25

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[qemu-unrealdumper-4-25]] · [[patternsleuth]] · [[ts-ue4dumper]] · [[ue4dumper]]
