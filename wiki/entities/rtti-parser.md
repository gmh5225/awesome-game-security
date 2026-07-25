---
title: rtti-parser
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/rem0obb__rtti-parser.md
updated: 2026-07-24
confidence: medium
---

# rtti-parser

IDA script to parse RTTI information in executables, with support for IDA 9.2. Aimed at game-security researchers and reverse engineers in the cheat / IDA Plugins lane recovering C++ type metadata from binaries. (source: wiki/sources/descriptions/rem0obb__rtti-parser.md)

Scoped as RTTI recovery for IDA—not a full decompiler suite. Description notes a possible rename collision (“Can't rename byte at 'xxx' because the name is already used in the program”).

## Links

- Repo: https://github.com/rem0obb/rtti-parser

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[symless]] · [[ida-rust-demangler]] · [[dotniet]] · [[sark]]
