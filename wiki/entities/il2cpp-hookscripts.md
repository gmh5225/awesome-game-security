---
title: Il2CppHookScripts
kind: entity
topics: [game-engine, mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/axhlzy__Il2CppHookScripts.md
updated: 2026-08-18
confidence: medium
---

# Il2CppHookScripts

**Il2CppHookScripts** (axhlzy) is a **Frida-based runtime parsing and hooking framework** for Unity [[il2cpp]] games, published as the **il2cpp-hooker** npm package. The TypeScript codebase provides runtime parsing of IL2CPP methods, classes, fields, and instances; batch hooking utilities; function return-value modification; object hierarchy printing; disassembly with method info; and **QBDI-based function emulation**. It also includes JNI `RegisterNatives` hooking, `Il2CppMethod` inspection, game-object detail display, and an MCP companion build. Mainly useful for mobile game security researchers and reverse engineers performing runtime analysis and instrumentation of Unity IL2CPP titles with [[frida]]. (source: wiki/sources/descriptions/axhlzy__Il2CppHookScripts.md)

Complements script-template collections such as [[il2cpp-hook-scripts]] (gmh5225) and metadata bridges like [[frida-il2cpp-bridge]] when analysts need a structured TypeScript hooking framework rather than one-off scripts alone. Same author's static ARM inline-hook lane: [[pyasm-patch]].

## Links

- Repo: https://github.com/axhlzy/Il2CppHookScripts

## Related

[[il2cpp]] · [[frida]] · [[frida-il2cpp-bridge]] · [[frida-il2cpp-datacollector]] · [[il2cpp-hook-scripts]] · [[pyasm-patch]] · [[qbdi-tracer-android]] · [[overviews/mobile-security]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
