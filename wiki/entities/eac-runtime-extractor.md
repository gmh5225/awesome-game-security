---
title: EAC-Runtime-Extractor
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__EAC-Runtime-Extractor.md
updated: 2026-08-13
confidence: medium
---

# EAC-Runtime-Extractor

Injected DLL that captures [[easy-anti-cheat]]'s kernel driver **at runtime before it is written to disk** (gmh5225). Uses **MinHook** to intercept file I/O and driver-loading APIs, recording the EAC driver binary as it is loaded into memory so researchers can dump it for offline static analysis without relying on on-disk driver-store artifacts. Complements filesystem-oriented extractors such as [[eac-extractor-utility]] when the goal is the live load path rather than installed game/driver-store copies. (source: wiki/sources/descriptions/gmh5225__EAC-Runtime-Extractor.md)

## Links

- Repo: https://github.com/gmh5225/EAC-Runtime-Extractor

## Related

[[easy-anti-cheat]] · [[eac-extractor-utility]] · [[easyanticheat-reversing]] · [[eac]] · [[ntminhook]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
