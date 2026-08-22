---
title: PoisonKiller BOF
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Muz1K1zuM__PoisonKiller_bof.md
updated: 2026-08-22
confidence: medium
---

# PoisonKiller BOF

Collection of **Beacon Object Files (BOFs)** that abuse the signed vulnerable kernel driver **`PoisonX.sys`** to perform process killing, driver loading and unloading, and file deletion from kernel mode. C-based BOFs are cross-compiled with MinGW for Cobalt Strike or similar C2 frameworks, with a Python helper script for build/load workflows. Aimed at red-team operators and security researchers studying BYOVD-based process termination and kernel-level file operations delivered as in-memory BOF payloads rather than standalone executables. (source: wiki/sources/descriptions/Muz1K1zuM__PoisonKiller_bof.md)

## Links

- Repo: https://github.com/Muz1K1zuM/PoisonKiller_bof

## Related

[[concepts/byovd]] · [[process-killer-byovd]] · [[killer]] · [[usb-monitor-bof]] · [[kernel-cactus]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
