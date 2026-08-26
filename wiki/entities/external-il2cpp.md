---
title: external-il2cpp
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Compiled-Code__external-il2cpp.md
updated: 2026-08-26
confidence: medium
---

# external-il2cpp

External C++ framework for navigating [[il2cpp]] metadata and game structures from another process (Compiled-Code; cheat / `[Il2Cpp]`). Uses WinAPI process and module discovery with `ReadProcessMemory`-based access to enumerate assemblies, images, classes, and fields by name, and provides lightweight abstractions for resolving static and instance field addresses from `GameAssembly` offset data. (source: wiki/sources/descriptions/Compiled-Code__external-il2cpp.md)

Primary use case is Unity IL2CPP reverse engineering and external tooling development for game security research. Complements broader external Unity introspection such as [[unity202x-externalresolve]], IL2CPP-specific runtime resolvers such as [[il2cpp-resolver-external]], and static dump lanes such as [[il2cppdumper]] when analysts need no-inject structure navigation from a separate Windows process.

## Links

- Repo: https://github.com/Compiled-Code/external-il2cpp

## Related

[[il2cpp]] · [[il2cpp-resolver-external]] · [[unity202x-externalresolve]] · [[il2cpp-resolver]] · [[il2cppdumper]] · [[mono-external-lib]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
