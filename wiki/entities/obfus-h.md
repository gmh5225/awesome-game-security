---
title: obfus.h
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/DosX-dev__obfus.h.md
updated: 2026-08-26
confidence: medium
---

# obfus.h

Macro-only C header for compile-time code obfuscation, oriented toward Tiny C Compiler (TCC) workflows on Windows x86/x64. Provides function-call obfuscation, control-flow mutation, string hiding, anti-debug techniques, anti-decompilation tricks, fake signature insertion, and optional virtualized math logic. Integration is a single `#include` with behavior toggled via preprocessor flags. Primarily used by low-level developers and security researchers exploring software protection and binary hardening (Anti Cheat → Obfuscation Engine / Compile Time). (source: wiki/sources/descriptions/DosX-dev__obfus.h.md)

C/macro-first alternative to C++ header libraries such as [[obfusheader-h]], [[obfusk8]], and [[crycall]]; complements string crypters like [[xorstr]] / [[obfuscate]] / [[crystr]]. Not a commercial packer or VM-based protector.

## Links

- Repo: https://github.com/DosX-dev/obfus.h

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfusheader-h]] · [[obfusk8]] · [[crycall]] · [[brkida]] · [[obfuscate]] · [[xorstr]]
