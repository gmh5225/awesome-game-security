---
title: kernel-special-apc-readprocessmemory
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Kernel-Special-APC-ReadProcessMemory.md
updated: 2026-08-12
confidence: medium
---

# kernel-special-apc-readprocessmemory

Teaching example (gmh5225) for **cross-process memory read via special kernel APC insertion**: resolves `KeInitializeApc` / `KeInsertQueueApc`, selects a target thread with APC delivery still enabled, allocates a nonpaged staging buffer, and uses an APC callback to `memcpy` from the target address into kernel memory before copying results back to user space. The archived test program compares this APC path against ordinary `ReadProcessMemory`; the README frames memory read as a demo of special APC mechanics rather than the repo's sole purpose. Useful for Windows kernel researchers studying APC insertion, thread-selection constraints, and kernel-mediated memory collection. (source: wiki/sources/descriptions/gmh5225__Kernel-Special-APC-ReadProcessMemory.md)

## Links

- Repo: https://github.com/gmh5225/Kernel-Special-APC-ReadProcessMemory

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[apc-research]] · [[stealth-apc-dispatcher]] · [[injdrv]] · [[kinject]] · [[ntmemory]] · [[cheat-driver]] · [[kernel-callbacks]]
