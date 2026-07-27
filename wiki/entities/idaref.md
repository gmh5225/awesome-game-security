---
title: IdaRef
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/nologic__idaref.md
updated: 2026-07-27
confidence: medium
---

# IdaRef

IDA Pro plugin that shows full CPU instruction documentation for the instruction under the cursor—richer than auto-comments, with complete reference text. Mainly Python; loads architecture-specific SQLite mnemonic/description DBs for x86-64, ARM, MIPS 32-bit, and Xtensa. Supports auto-refresh on navigation, refresh for the current instruction, manual lookup, and simple description redirects for shared docs. Offline assembly reference while analyzing binaries in IDA. (source: wiki/sources/descriptions/nologic__idaref.md)

Sits in the Cheat IDA Plugins / instruction-reference lane beside other IDA workflow helpers such as [[idarem]] and [[big5-decode-ida]].

## Links

- Repo: https://github.com/nologic/idaref

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idarem]] · [[big5-decode-ida]] · [[idaplugins]] · [[quickasm]]
