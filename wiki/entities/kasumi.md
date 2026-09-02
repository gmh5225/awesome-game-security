---
title: Kasumi
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Anatdx__Kasumi.md
updated: 2026-09-02
confidence: medium
---

# Kasumi

Linux kernel module for **Android GKI** that hides root access from user-space integrity checks. Hooks **syscalls**, **VFS operations**, and **`/proc` filesystem** entries via **ftrace** and **tracepoints**, then spoofs mount metadata, **SELinux context**, and file attributes so root-detection probes see a clean environment. Positioned as a kernel-level path manipulation and hiding framework for Android GKI/Linux — complementary to Magisk/Zygisk userspace hide modules and LKM syscall-hook research toolkits. (source: wiki/sources/descriptions/Anatdx__Kasumi.md)

README category: Kernel-level path manipulation and hiding framework for Android GKI/Linux.

## Links

- Repo: https://github.com/Anatdx/Kasumi

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[hideroot]] · [[android-kernel-hacking-toolkit]] · [[kernelsu]] · [[mobile-anti-cheat]] · [[advanced-root-checker]] · [[magiskdetector]]
