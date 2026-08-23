---
title: Rigel-Driver
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Lynnette177__Rigel-Driver.md
updated: 2026-08-23
confidence: medium
---

# Rigel-Driver

Windows kernel driver in C++ focused on **cross-process memory read/write** for low-level tooling. Exposes routines for **module base/export lookup**, **kernel memory access**, and **writes to protected memory regions**. Notes indicate **mapper-based loading** and **dxgkrnl-related hooking** (`NtGdiDdDDINetDispGetNextChunkInfo`) as the operational context rather than a conventional monitored device IOCTL surface. Primarily useful for game-security research into driver-assisted memory access and anti-cheat bypass techniques. (source: wiki/sources/descriptions/Lynnette177__Rigel-Driver.md)

Adjacent to dxgkrnl export-hijack covert-comms samples such as [[nulldriver-cheat]], [[kernel-cheat-for-directx3d]], and [[nullhook]], and to standalone KM R/W primitives such as [[ntmemory]] and [[driver-physical-rw]].

## Links

- Repo: https://github.com/Lynnette177/Rigel-Driver

## Related

[[nulldriver-cheat]] · [[kernel-cheat-for-directx3d]] · [[dxgkrnl-hook]] · [[kdmapper]] · [[ntmemory]] · [[driver-read-write]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
