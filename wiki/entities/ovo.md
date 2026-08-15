---
title: ovo
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/fuqiuluo__ovo.md
updated: 2026-08-15
confidence: medium
---

# ovo

Android ARM64 kernel driver module that exposes process memory read/write, MMU page-table manipulation (`mmuhack`), and touch input simulation through a kernel-space TCP socket server. It provides VMA traversal and address-to-PFN mapping for virtual-to-physical translation, a `peekaboo` module for stealth memory access, and client SDKs in C++ and Rust for userspace or cross-device communication. (source: wiki/sources/descriptions/fuqiuluo__ovo.md)

Sits in the cheat / Android kernel driver lane alongside LKM memory-ops toolkits such as [[android-kernel-hacking-toolkit]] and ioctl-based cross-process readers such as [[kpm-memreader]], but adds kernel TCP IPC and simulated touch for out-of-process cheat clients.

## What it covers

- Cross-process kernel memory R/W with fast remapping
- MMU / page-table manipulation (`mmuhack`) and virtual-to-physical helpers (VMA walk, address→PFN)
- Kernel-space TCP socket server for userspace or cross-device control
- Touch input simulation from kernel context
- `peekaboo` stealth memory access module
- C++ and Rust client SDKs

## Links

- Repo: https://github.com/fuqiuluo/ovo

## Related

[[android-wuwa]] · [[rnidbg]] · [[op7t]] · [[android-kernel-hacking-toolkit]] · [[kpm-memreader]] · [[root-socket-kit]] · [[android-virtual-touch]] · [[compile-android-driver]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
