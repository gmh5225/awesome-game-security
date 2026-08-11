---
title: MMFCodeInjection
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__MMFCodeInjection.md
updated: 2026-08-11
confidence: medium
---

# MMFCodeInjection

**Memory-mapped file (MMF) code injection** PoC from gmh5225 (README: User APC + File Mapping Testing). Maps executable code into a target process address space through **shared file mappings** rather than conventional `LoadLibrary` / remote `VirtualAllocEx` + write paths — a stealthier DLL-load vector that AC engineers use to stress-test image-load monitors, VAD/section enumeration, and User APC delivery coverage. (source: wiki/sources/descriptions/gmh5225__MMFCodeInjection.md)

Complements broader injection corpora such as [[injection]] and [[windows-process-injection]], user-mode PE manual-map samples such as [[modexmap]], and APC research such as [[apc-research]].

## Links

- Repo: https://github.com/gmh5225/MMFCodeInjection

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injection]] · [[windows-process-injection]] · [[modexmap]] · [[apc-research]] · [[setwindowshookex-injector]]
