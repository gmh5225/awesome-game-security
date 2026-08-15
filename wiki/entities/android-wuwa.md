---
title: android-wuwa
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/fuqiuluo__android-wuwa.md
updated: 2026-08-15
confidence: medium
---

# android-wuwa

Android ARM64 loadable kernel module for stealthy cross-process memory access. It bypasses CFI and kprobe blacklists at load time, supports software page-table walking and hardware address translation via the ARM64 AT instruction, direct physical memory R/W through `phys_to_virt` (up to 50 MB per operation), PTE-level mapping injection that bypasses VMA structures, and DMA buffer sharing between processes. Communication uses IOCTL or a kernel-space socket protocol, with optional module and signal hiding. (source: wiki/sources/descriptions/fuqiuluo__android-wuwa.md)

Sits in the cheat / Android aarch64 rootkit lane alongside sibling LKM driver [[ovo]] and CFI/kprobe-aware research kits such as [[android-kernel-hacking-toolkit]].

## What it covers

- CFI and kprobe blacklist bypass at module load
- Software page-table walk plus ARM64 AT hardware address translation
- Direct physical memory R/W via `phys_to_virt` (≤50 MB per op)
- PTE injection mapping without VMA structures
- Inter-process DMA buffer sharing
- IOCTL or kernel-space socket IPC
- Optional module and signal hiding

## Links

- Repo: https://github.com/fuqiuluo/android-wuwa

## Related

[[ovo]] · [[android-kernel-hacking-toolkit]] · [[kpm-memreader]] · [[android-drivesignity]] · [[compile-android-driver]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
