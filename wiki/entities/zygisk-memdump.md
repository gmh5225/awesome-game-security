---
title: zygisk-memdump
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hackcatml__zygisk-memdump.md
updated: 2026-08-06
confidence: medium
---

# zygisk-memdump

Zygisk module (C/C++) that dumps shared library (`.so`) files from a target process memory. Runs in the Magisk Zygisk specialization path for early injection before app startup, in the same modding / hooking / memory-analysis lane as standalone dumpers such as [[memdumper]]. Useful for game-security researchers and reverse engineers extracting runtime native code from packed or protected Android games for offline IDA/Ghidra analysis. (source: wiki/sources/descriptions/hackcatml__zygisk-memdump.md)

Framework home: [[magisk]]. Adjacent Zygisk dump/inject peers include [[zygisk-dump-dex]] (DEX) and [[memdumper]] (standalone `/proc/<pid>/mem` ELF rebuild).

## Links

- Repo: https://github.com/hackcatml/zygisk-memdump

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[magisk]] · [[zygisk]] · [[memdumper]] · [[zygisk-dump-dex]] · [[jadx]]
