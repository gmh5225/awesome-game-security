---
title: ue4genny
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/cursey__ue4genny.md
updated: 2026-08-16
confidence: medium
---

# ue4genny

**Runtime Unreal Engine 4 SDK generator** (cursey; C++). Scans UE4's reflection system at runtime—`UObject`, `UClass`, `UStruct`, `UEnum`, `UFunction`—and emits complete C++ SDK headers with class hierarchies, property offsets, and function signatures. The generated SDK enables direct interaction with game objects for modding or research when accurate UE4 layout dumps from a live instance are needed. Listed under cheat / SDK Generator. (source: wiki/sources/descriptions/cursey__ue4genny.md)

Sits in the in-process Unreal SDK-generation lane beside inject dumpers (Dumper-7 / UE4SS), external pattern-scan dumpers such as [[unrealdumper-4-25]], and modular Frida workflows such as [[ts-ue4dumper]]—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/cursey/ue4genny

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[unrealdumper-4-25]] · [[ts-ue4dumper]] · [[frida-ue4dump]] · [[ue4dumper]] · [[regenny]] · [[sdkgenny]] · [[luagenny]] · [[patternsleuth]]
