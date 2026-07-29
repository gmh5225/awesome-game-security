---
title: PTEditor
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/misc0110__PTEditor.md
updated: 2026-07-29
confidence: medium
---

# PTEditor

Cross-platform **page-table manipulation** toolkit: a Linux kernel module plus userspace library for directly reading and modifying all page-table levels (PGD, PUD, PMD, PTE) of any process from user space on **x86_64** and **ARMv8**. Supports virtual-to-physical address translation, PAT/MAIR memory-type programming, NX bit manipulation, and TLB flushing; ships with a companion **Windows kernel driver** for the same research surface. (source: wiki/sources/descriptions/misc0110__PTEditor.md)

Useful for low-level memory / hook / AC research in the Some Tricks / Windows Ring0 and PTE Hook lane—studying per-process page tables beside samples such as [[windows-kernel-pagehook]] and physical-read paths like [[readphys]].

## Links

- Repo: https://github.com/misc0110/PTEditor (README tag: PT Editor)

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[windows-kernel-pagehook]] · [[readphys]] · [[ntmemory]]
