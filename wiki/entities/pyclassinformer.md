---
title: PyClassInformer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/herosi__PyClassInformer.md
updated: 2026-08-05
confidence: medium
---

# PyClassInformer

IDA Pro plugin that identifies and classifies C++ RTTI (Run-Time Type Information) structures in binaries. Provides class hierarchy visualization, automatic function renaming from RTTI data, library-flag classification, method classification, and configurable coloring for identified class members. Aimed at reverse engineers recovering C++ class layout and RTTI-based function identity from game clients and other MSVC/C++ PE targets. (source: wiki/sources/descriptions/herosi__PyClassInformer.md)

Scoped as RTTI-driven class recovery for IDA—not a full SDK generator. Complements [[rtti-parser]] (script-style RTTI parse) and [[ida-vtable-tools]] (vtable skeleton export / slot indexing).

## Links

- Repo: https://github.com/herosi/PyClassInformer

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[rtti-parser]] · [[ida-vtable-tools]] · [[ida-missinglink]] · [[symless]] · [[demumble]]
