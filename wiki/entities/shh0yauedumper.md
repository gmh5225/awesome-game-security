---
title: Shh0yaUEDumper
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Shhoya__Shh0yaUEDumper.md
updated: 2026-08-21
confidence: medium
---

# Shh0yaUEDumper

**Windows Unreal Engine dumper and SDK generator** for specific UE4 versions (Shhoya; C++). Uses process memory access, pattern scanning, and engine structure parsing to locate name and object data at runtime, then outputs names, objects, and generated SDK headers for inspected game builds. Configuration-driven version handling targets Unreal game reverse engineering and tooling development in game-security research. Listed under cheat / SDK Dump. (source: wiki/sources/descriptions/Shhoya__Shh0yaUEDumper.md)

Sits in the Unreal SDK-generation lane beside all-in-one dumpers such as [[uedumper]], external pattern-scan dumpers such as [[unrealdumper-4-25]], runtime reflection generators such as [[ue4genny]], and live-script modding via [[re-ue4ss]]—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/Shhoya/Shh0yaUEDumper

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[uedumper]] · [[unrealdumper-4-25]] · [[ue4genny]] · [[re-ue4ss]] · [[patternsleuth]]
