---
title: Classy
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Classy.md
updated: 2026-08-14
confidence: medium
---

# Classy

IDA Pro plugin for managing C++ classes, vtables, and function signatures during reverse engineering. PyQt5 GUI workflows include vtable generation from selected address ranges, function-to-class assignment, Itanium name mangling, IDA struct mapping, and C header export. (source: wiki/sources/descriptions/gmh5225__Classy.md)

Scoped as interactive C++ class/vtable organization in IDA—not RTTI-driven hierarchy recovery or standalone demangling. Complements [[ida-vtable-tools]] (vtable skeleton export / slot indexing), [[ida-medigate]] (GCC RTTI hierarchy reconstruction), [[pyclassinformer]] (MSVC RTTI rename), and [[happyida]] (Hex-Rays vtable navigation).

## Links

- Repo: https://github.com/gmh5225/Classy

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-vtable-tools]] · [[ida-medigate]] · [[pyclassinformer]] · [[happyida]] · [[demumble]] · [[rtti-parser]]
