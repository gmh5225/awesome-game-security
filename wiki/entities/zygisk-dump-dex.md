---
title: zygisk-dump-dex
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ri-char__zygisk-dump-dex.md
updated: 2026-07-24
confidence: medium
---

# zygisk-dump-dex

Zygisk module that hooks `libdexfile.so` to dump DEX from target processes. Tested by the author on Android 14 and 15. Useful for game-security and reverse-engineering workflows in the Cheat Magisk lane—runtime DEX recovery for packed/protected Android games before static decompile with tools such as [[jadx]]. (source: wiki/sources/descriptions/ri-char__zygisk-dump-dex.md)

Framework home: [[magisk]]. Adjacent Magisk modules include [[easypixel]] and [[move-certificate]]; static unpack / Sample Unpacker peers include [[android-unpacker]].

## Links

- Repo: https://github.com/ri-char/zygisk-dump-dex

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[magisk]] · [[jadx]] · [[android-unpacker]] · [[easypixel]] · [[move-certificate]] · [[delamain]] · [[frida]]
