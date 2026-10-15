---
title: gtlibcpp
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/heaven-hm__gtlibcpp.md
updated: 2026-10-15
confidence: medium
---

# gtlibcpp

**gtlibcpp** (heaven-hm/gtlibcpp) is a C++17 library for scoped process memory work and a local JSON-RPC agent aimed at authorized offline trainers and automation against test processes—not online cheating. (source: wiki/sources/descriptions/heaven-hm__gtlibcpp.md)

## Core API

The modern **gtlibcpp** core exposes typed `MemorySession` reads and writes, pointer-chain resolution, value freeze with restore, policy gates (audit and kill-switch), and a strict Cheat Engine 7.x cheat-table (`.CT`) parser. A Windows-specific backend and named-pipe transport attach to live x86/x64 targets. (source: wiki/sources/descriptions/heaven-hm__gtlibcpp.md)

## Legacy and build

A legacy **GTLibc** trainer layer (cheat-table parsing and demo trainers) remains for backward compatibility; the gtlibcpp API is the supported path. CMake builds separate cross-platform core and Windows libraries, with examples, regression tests, and documentation for game memory research, trainer development, and local security testing. (source: wiki/sources/descriptions/heaven-hm__gtlibcpp.md)

## Links

- Repo: https://github.com/heaven-hm/gtlibcpp

## Related

[[cheat-agent]] · [[cheat-engine]] · [[freeplay]] · [[cttrainer]] · [[pymemory-editor]] · [[overviews/game-hacking]] · [[research-rigor]]
