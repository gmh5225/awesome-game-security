---
title: android-kernel-hacking-toolkit
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/systemnb__android-kernel-hacking-toolkit.md
updated: 2026-07-21
confidence: medium
---

# android-kernel-hacking-toolkit

Collection of Android aarch64 loadable kernel modules (LKMs) for security research: process hiding via `task_struct` unlinking (`hideproc`), kernel VFS file copy (`filecopy`), property editing (`propedit`), and syscall-table hijacking (`syscall_hijack`). README highlights CFI bypass, kprobes, and `mmuhack` paths for locating `sys_call_table` — useful when studying Android LKM / syscall-hook surfaces adjacent to custom-kernel and driver tooling. (source: wiki/sources/descriptions/systemnb__android-kernel-hacking-toolkit.md)

## Links

- Repo: https://github.com/systemnb/android-kernel-hacking-toolkit

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[compile-android-driver]] · [[dpatch]] · [[vermagic]] · [[op7t]]
