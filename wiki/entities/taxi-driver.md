---
title: TaxiDriver
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ALittlePatate__TaxiDriver.md
updated: 2026-09-04
confidence: medium
---

# TaxiDriver

Linux **kernel module + user-mode** pair for cross-process memory read/write (ALittlePatate/TaxiDriver). Implemented in **C/C++** with kernel-module build scripts; exposes **base-address lookup**, **RPM**, and **WPM** through a **device interface**. Includes user-mode examples and test programs demonstrating driver communication. Intended for low-level **game memory tooling** and **Linux security research**. (source: wiki/sources/descriptions/ALittlePatate__TaxiDriver.md)

Sits in the Linux kernel memory-ops lane beside [[kernel-driver-hack]], [[kernel-hack]], and user-mode alternatives such as [[pince]] and [[mempeek]]. Same author as legacy FPS cheat RE sample [[ezfrags]].

## Links

- Repo: https://github.com/ALittlePatate/TaxiDriver

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[kernel-driver-hack]] · [[kernel-hack]] · [[pince]] · [[mempeek]] · [[ezfrags]] · [[vermagic]]
