---
title: IDA-VTableExplorer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/K4ryuu__IDA-VTableExplorer.md
updated: 2026-08-24
confidence: medium
---

# IDA-VTableExplorer

C++ plugin for IDA Pro 9.x that automates C++ virtual table analysis. It detects GCC and MSVC vtable patterns, extracts class information, and annotates virtual function indexes and offsets. The plugin also performs RTTI-based inheritance analysis, override comparison, and hierarchy visualization—aimed at reverse engineering workflows where understanding polymorphism and virtual dispatch is critical. (source: wiki/sources/descriptions/K4ryuu__IDA-VTableExplorer.md)

Automated vtable detection, RTTI inheritance, and hierarchy visualization for IDA—not constructor-pseudocode class recovery or manual vtable skeleton export. Complements [[ida-vtable-tools]] (Python `.hpp` skeleton / rename / slot indexing), [[ida-medigate]] (GCC RTTI hierarchy recovery from stripped binaries), [[classy]] (manual class/vtable organization and C header export), and [[ghidra-cpp-class-analyzer]] (Ghidra-side C++ RTTI/vtable analysis).

## Links

- Repo: https://github.com/K4ryuu/IDA-VTableExplorer

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-vtable-tools]] · [[ida-medigate]] · [[classy]] · [[classmaker]] · [[pyclassinformer]] · [[ghidra-cpp-class-analyzer]]
