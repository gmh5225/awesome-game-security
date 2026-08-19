---
title: rwProcMem33
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/abcz316__rwProcMem33.md
updated: 2026-08-19
confidence: medium
---

# rwProcMem33

ARM64 Linux kernel driver suite for cross-process memory read/write and hardware-breakpoint debugging on Android. Implemented mainly in C with C++ user-space demos for memory search, dump, remote control, and Cheat Engine–style server workflows. Exposed interfaces include process open/close, memory access, process and mapping queries, privilege elevation, and kernel module hiding — aimed at Android game-security researchers and reverse engineers doing low-level runtime instrumentation. (source: wiki/sources/descriptions/abcz316__rwProcMem33.md)

Upstream project for forks such as [[rwmem]]; sits in the same Android root / kernel memory-ops lane as [[root-socket-kit]], [[kernel-hack]], [[skroot-linux-kernel-root]], and CLI scanners such as [[mypower]].

## Links

- Repo: https://github.com/abcz316/rwProcMem33

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[rwmem]] · [[root-socket-kit]] · [[kernel-hack]] · [[skroot-linux-kernel-root]] · [[mypower]] · [[android-kernel-hacking-toolkit]] · [[compile-android-driver]]
