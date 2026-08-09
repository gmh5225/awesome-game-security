---
title: VulnerableKernel Driver
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__VulnerableKernel_Driver.md
updated: 2026-08-09
confidence: medium
---

# VulnerableKernel Driver

Deliberately vulnerable Windows kernel driver (**`MsIo64.sys`**) from gmh5225 for educational kernel exploitation practice. Exposes intentionally insecure IOCTL handlers demonstrating arbitrary kernel memory read/write, buffer overflow, use-after-free, and race conditions — aimed at kernel exploitation students and security trainers teaching driver vulnerability classes. (source: wiki/sources/descriptions/gmh5225__VulnerableKernel_Driver.md)

Sits in the same cheat / [[byovd]] training lane as [[hacksysextremevulnerabledriver]] and **`msIo64.sys`** physmem research such as [[ms-io-exploit]].

## Links

- Repo: https://github.com/gmh5225/VulnerableKernel_Driver

## Related

[[byovd]] · [[hacksysextremevulnerabledriver]] · [[ms-io-exploit]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
