---
title: UnrealSDKDumper-4.25
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/BobHUnrealTech__UnrealSDKDumper-4.25.md
updated: 2026-08-30
confidence: medium
---

# UnrealSDKDumper-4.25

**C++ Unreal Engine SDK generator for UE 4.23–4.27** (BobHUnrealTech). Emits compilable SDK output—dependency-aware class ordering, identifier sanitization, and a ready-to-include `sdk.h` plus an `SDK/` folder—for Unreal reverse engineering practitioners who need accurate metadata for analysis, tooling, or gameplay-modification research. The implementation adds wide-character Chinese name handling so exported classes, members, and functions remain usable when titles ship localized identifiers. Listed under cheat / SDK Dump for UE 4.23 - 4.27. (source: wiki/sources/descriptions/BobHUnrealTech__UnrealSDKDumper-4.25.md)

Sits in the UE4 mid-branch SDK-generation lane beside external dumpers such as [[unrealdumper-4-25]], in-process generators such as [[dumper-7]], and all-in-one dumpers such as [[uedumper]]—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/BobHUnrealTech/UnrealSDKDumper-4.25

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[unrealdumper-4-25]] · [[dumper-7]] · [[uedumper]] · [[shh0yauedumper]] · [[re-ue4ss]]
