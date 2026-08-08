---
title: gdriver-lib
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__gdriver-lib.md
updated: 2026-08-08
confidence: medium
---

# gdriver-lib

C++ library wrapping Gigabyte's signed vulnerable **`gdrv64.sys`** driver interface for convenient kernel memory access. Exposes functions for reading and writing physical memory, mapping physical addresses, and performing kernel operations through gdrv's vulnerable IOCTLs — a reusable [[byovd]] access primitive for kernel researchers studying Gigabyte driver exploitation. (source: wiki/sources/descriptions/gmh5225__gdriver-lib.md)

Complements mapper-focused [[gdrv-loader]] / [[gdrv-loader-v2]] and multi-provider tooling such as [[kdu]] and [[vdk]].

## Links

- Repo: https://github.com/gmh5225/gdriver-lib

## Related

[[byovd]] · [[gdrv-loader]] · [[gdrv-loader-v2]] · [[kdu]] · [[vdk]] · [[loldrivers]] · [[msft-driverblocklist]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
