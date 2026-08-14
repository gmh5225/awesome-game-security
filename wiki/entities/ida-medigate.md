---
title: ida-medigate
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ida_medigate.md
updated: 2026-08-08
confidence: medium
---

# ida-medigate

IDA Pro Python plugin that reconstructs C++ class hierarchies and virtual function tables from stripped binaries by parsing **GCC RTTI** structures (typeinfo, vtables). Maps virtual calls to concrete implementations through union-based type disambiguation in the Hex-Rays decompiler; builds IDA structs with inheritance chains, assigns vtable member types, and cross-references virtual calls via a bundled xref tracker—all within IDA's native structure/union framework (architecture-agnostic). Especially useful for polymorphic C++ in IoT/embedded firmware and game engine components where manual vtable reconstruction is tedious. (source: wiki/sources/descriptions/gmh5225__ida_medigate.md)

Scoped as GCC RTTI–driven hierarchy/vtable recovery for IDA—not MSVC RTTI tooling. Complements [[classy]] (manual class/vtable organization and C header export), [[pyclassinformer]] / [[rtti-parser]] (MSVC/script RTTI), and [[ida-vtable-tools]] (vtable skeleton export / slot indexing).

## Links

- Repo: https://github.com/gmh5225/ida_medigate

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[pyclassinformer]] · [[rtti-parser]] · [[ida-vtable-tools]] · [[ida-missinglink]]
