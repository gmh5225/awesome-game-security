---
title: code_injection
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Fahersto__code_injection.md
updated: 2026-08-25
confidence: medium
---

# code_injection

C++ **host-based Windows code injection** technique collection (Fahersto). Implements roughly two dozen PE, DLL, and shellcode injection paths—including process-hollowing variants, callback-based methods, and loader-abuse routes. Build scripts organize each technique as a separate executable and document compatibility across 32-bit, 64-bit, WoW64, and multiple Windows versions. Primary audience: security researchers studying offensive tradecraft and defensive detection coverage. (source: wiki/sources/descriptions/Fahersto__code_injection.md)

Complements broader catalogs such as [[windows-process-injection]] and [[process-injection-techniques]], focused PoCs such as [[thread-hijacking-injector]] and [[frankenstein-apc-injection]], and defensive blockers such as [[pi-defender]] and [[faultline]].

## Links

- Repo: https://github.com/Fahersto/code_injection

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[injectors]] · [[awesome-injection]]
