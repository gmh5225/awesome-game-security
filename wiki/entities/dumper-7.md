---
title: Dumper-7
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Encryqed__Dumper-7.md
updated: 2026-08-25
confidence: medium
---

# Dumper-7

**C++ Unreal Engine SDK generator for UE4 and UE5** (Encryqed). Injects a DLL into the target process, locates engine structures and offsets, and emits generated headers and SDK code for analysis and downstream tooling. The codebase includes configurable offset overrides, multiple build options, and guidance for integrating generated output into other projects. Primary use cases are Unreal Engine reverse engineering—game security research, modding analysis, and internal structure mapping. Listed under cheat / SDK Dump for all of UE4 and UE5. (source: wiki/sources/descriptions/Encryqed__Dumper-7.md)

Sits in the canonical in-process Unreal SDK-generation lane beside live-scripting dumpers such as [[re-ue4ss]], runtime reflection generators such as [[ue4genny]], all-in-one dumpers such as [[uedumper]], and external pattern-scan workflows—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/Encryqed/Dumper-7

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[re-ue4ss]] · [[ue4genny]] · [[uedumper]] · [[shh0yauedumper]] · [[unrealdumper-4-25]] · [[patternsleuth]]
