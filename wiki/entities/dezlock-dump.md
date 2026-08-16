---
title: dezlock-dump
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/dougwithseismic__dezlock-dump.md
updated: 2026-08-16
confidence: medium
---

# dezlock-dump

**Runtime schema and RTTI extraction** tool for Source 2 engine games (Deadlock, CS2, Dota 2) that dumps class hierarchies, netvars, interfaces, protobuf definitions, and global singletons from live game processes. Includes pattern scanning, MSVC x64 RTTI hierarchy reconstruction, a WebSocket-based live bridge for real-time introspection, and a visual schema browser—useful for game-security researchers and modders reverse engineering Source 2 internals without running [[source2gen]] offline codegen. (source: wiki/sources/descriptions/dougwithseismic__dezlock-dump.md)

Complements offline SDK generators such as [[source2gen]] / [[source2sdk]], static offset dumps such as [[cs2-offsets]] and [[dota2dumped]], and educational Source 2 curricula such as [[cs2-internals]] as a live-process schema/RTTI lane.

## Links

- Repo: https://github.com/dougwithseismic/dezlock-dump

## Related

[[source2gen]] · [[source2sdk]] · [[source-netvars]] · [[cs2-offsets]] · [[dota2dumped]] · [[cs2-internals]] · [[sourceengineexplorer]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
