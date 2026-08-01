---
title: Unity202x-eXternalrEsolve
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/zushinzackery2-ship-it__Unity202x-eXternalrEsolve.md
updated: 2026-08-01
confidence: medium
---

# Unity202x-eXternalrEsolve

Header-only C++17 framework (**er2**) that reconstructs Unity engine runtime data structures from a live Windows x64 process via cross-process read-only memory access—without symbol tables, RTTI, filesystem reads, or code injection. Targets Unity 2020–2023 and auto-detects Mono and IL2CPP backends. (source: wiki/sources/descriptions/zushinzackery2-ship-it__Unity202x-eXternalrEsolve.md)

Core capabilities include blind discovery of the GameObjectManager and instance ID registries; remote rebuilding of IL2CPP metadata and field offsets; object and component introspection; transform and camera extraction; world-to-screen projection; and DumpSDK export of dump.cs-style artifacts. Positioned for academic research, authorized modding and plugin development, and reverse-engineering study of Unity game internals.

Complements Mono-only external readers such as [[mono-external-lib]], inject-based inspectors such as [[unityexplorer]], and IL2CPP resolver/dumper lanes such as [[il2cpp-resolver]] and [[il2cpp-runtime-dumper]] when the goal is symbol-free external runtime reconstruction across both Unity scripting backends.

## Links

- Repo: https://github.com/zushinzackery2-ship-it/Unity202x-eXternalrEsolve

## Related

[[il2cpp]] · [[mono]] · [[mono-external-lib]] · [[il2cpp-resolver]] · [[il2cpp-runtime-dumper]] · [[unityexplorer]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
