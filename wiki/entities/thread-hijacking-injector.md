---
title: ThreadHijackingInjector
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/NullTerminatorr__ThreadHijackingInjector.md
updated: 2026-08-22
confidence: medium
---

# ThreadHijackingInjector

Minimal **C++ proof-of-concept** for **DLL injection via thread hijacking** on Windows (NullTerminatorr). The project keeps a compact implementation that illustrates **remote thread context manipulation** and **execution redirection** in a target process. Its small code footprint makes the technique easier to study than full-featured injection frameworks. Primary use case: educational reverse engineering and security research into alternative process injection methods. (source: wiki/sources/descriptions/NullTerminatorr__ThreadHijackingInjector.md)

README lane: **Injection Testing** — thread-hijack DLL load study sample.

Complements broader injection corpora such as [[windows-process-injection]], thread-hijack usage in [[launcher-abuser]], and low-footprint inject PoCs such as [[frankenstein-apc-injection]] and [[idle-abuse]].

## Links

- Repo: https://github.com/NullTerminatorr/ThreadHijackingInjector

## Related

[[overviews/game-hacking]] · [[windows-process-injection]] · [[launcher-abuser]] · [[frankenstein-apc-injection]] · [[injectors]] · [[dll-thread-injection-detector]]
