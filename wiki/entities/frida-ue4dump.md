---
title: frida-ue4dump
kind: entity
topics: [game-engine, mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__frida-ue4dump.md
updated: 2026-08-08
confidence: medium
---

# frida-ue4dump

Frida script for dumping Unreal Engine 4 SDK information from **running Android** games: hooks UE4's reflection system at runtime to enumerate `UObject` classes, extract property offsets, dump function signatures, and generate SDK headers. Aimed at mobile game reverse engineers who prefer Frida attach/instrumentation over native inject dumpers. (source: wiki/sources/descriptions/gmh5225__frida-ue4dump.md)

## Links

- Repo: https://github.com/gmh5225/frida-ue4dump

## Related

[[frida]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[unreal-object-model]] · [[ts-ue4dumper]] · [[ue4dumper]] · [[game-engine-detector]]
