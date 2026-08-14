---
title: ida-vtable-tools
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/oxiKKK__ida-vtable-tools.md
updated: 2026-07-26
confidence: medium
---

# ida-vtable-tools

IDA 9.X Python plugin for C++ vtable workflows: dump an interface skeleton (`.hpp`), rename members with a class prefix, set `this` pointer types, and show slot index/offset. Aimed at game-security researchers and reverse engineers in the cheat / IDA Plugins lane recovering C++ virtual interfaces from binaries. (source: wiki/sources/descriptions/oxiKKK__ida-vtable-tools.md)

Scoped as IDA vtable annotation/export tooling—not a full RTTI/SDK generator. Complements [[classy]] (PyQt5 class/vtable/signature management and C header export), type-metadata helpers such as [[rtti-parser]], and iOS vtable-aware helpers such as [[ida-ios-helper]].

## Links

- Repo: https://github.com/oxiKKK/ida-vtable-tools

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[rtti-parser]] · [[ida-ios-helper]] · [[symless]] · [[oxware]]
