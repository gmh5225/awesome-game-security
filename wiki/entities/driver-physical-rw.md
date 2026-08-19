---
title: Driver-physical-rw
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Vekor64__Driver-physical-rw.md
updated: 2026-08-19
confidence: medium
---

# Driver-physical-rw

Windows **kernel driver** from Vekor64 that exposes **IOCTL handlers** for physical and virtual memory operations. Written in C++, it defines request structures and a **DeviceIoControl**-based user–kernel communication pattern for usermode clients. Core routines cover read/write primitives, memory allocation and protection changes, module base lookup, and process-oriented helpers. Positioned for low-level security experimentation and cheat-oriented driver communication studies. README tag: **Kernel-mode W/RPM for Windows**. (source: wiki/sources/descriptions/Vekor64__Driver-physical-rw.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| IOCTL dispatch | User–kernel comm via `DeviceIoControl` |
| Memory primitives | Physical and virtual read/write |
| Process helpers | Allocation, protection changes, module-base lookup |
| Client pattern | Structured request buffers for usermode controllers |

## Links

- Repo: https://github.com/Vekor64/Driver-physical-rw

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ntmemory]] · [[driver-rpm-direct-page-manipulation]] · [[readwrite-kernel-stable]] · [[readphys]] · [[pythoncs2]]
