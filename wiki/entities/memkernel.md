---
title: MemKernel
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Poko-Apps__MemKernel.md
updated: 2026-08-22
confidence: medium
---

# MemKernel

**Android kernel driver setup** for low-level **process memory read/write** (Poko-Apps). Combines **C/C++ kernel and userland** components that expose target memory access through a **custom interface**, with integration guidance for **compiling the driver into a kernel build** and pairing it with userland tooling. Aimed at advanced Android security and **game memory** researchers exploring kernel-assisted memory operations. README tag: `[RPM]`. (source: wiki/sources/descriptions/Poko-Apps__MemKernel.md)

Sits in the same Android kernel memory-ops lane as LKM toolkits such as [[android-kernel-hacking-toolkit]] and [[kernel-hack]], and out-of-tree driver build scaffolds such as [[compile-android-driver]].

## Links

- Repo: https://github.com/Poko-Apps/MemKernel

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernel-hack]] · [[android-kernel-hacking-toolkit]] · [[compile-android-driver]] · [[android-kernel-driver-template]] · [[rw-proc-mem33]] · [[root-socket-kit]]
