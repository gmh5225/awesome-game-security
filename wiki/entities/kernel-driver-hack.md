---
title: Kernel_driver_hack
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Jiang-Night__Kernel_driver_hack.md
updated: 2026-08-24
confidence: medium
---

# Kernel_driver_hack

**Android and Linux kernel driver** exposing **process memory read/write** through a **device interface** (Jiang-Night). Written primarily in **C**, with **ioctl commands** for memory access, **module base lookup**, and request dispatching. Includes kernel module build files and user-space components for driver communication. Used for low-level **game memory research**, reverse engineering experiments, and kernel-side tooling studies. (source: wiki/sources/descriptions/Jiang-Night__Kernel_driver_hack.md)

Sits in the same Android/Linux kernel memory-ops lane as [[memkernel]], [[kernel-hack]], and LKM toolkits such as [[android-kernel-hacking-toolkit]].

## Links

- Repo: https://github.com/Jiang-Night/Kernel_driver_hack

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[memkernel]] · [[kernel-hack]] · [[android-kernel-hacking-toolkit]] · [[compile-android-driver]] · [[rw-proc-mem33]] · [[root-socket-kit]]
