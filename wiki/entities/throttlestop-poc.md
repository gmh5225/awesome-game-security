---
title: ThrottleStop-PoC
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/U65535F__ThrottleStopPoC.md
updated: 2026-08-20
confidence: medium
---

# ThrottleStop-PoC

Proof of concept for **CVE-2025-7771** in the signed **`ThrottleStop.sys`** CPU-throttling utility driver. User-mode C code documents and abuses vulnerable IOCTL handlers for physical memory read/write and I/O port read/write, yielding arbitrary physmem and port access from user mode. Helper routines implement virtual-to-physical address translation and basic `EPROCESS`-based checks on Windows. Intended for Windows kernel security research, vulnerable-driver analysis, and anti-cheat threat modeling—not a production bypass tool. (source: wiki/sources/descriptions/U65535F__ThrottleStopPoC.md)

Same [[byovd]] physmem-primitive lane as [[eneio64-driver-exploit]], [[badrentdrv2]], and [[speedfan-exploit]]; complements VA-translation research such as [[ntmemory]].

## Links

- Repo: https://github.com/U65535F/ThrottleStopPoC
- Driver: `ThrottleStop.sys`
- CVE: CVE-2025-7771

## Related

[[byovd]] · [[eneio64-driver-exploit]] · [[badrentdrv2]] · [[physmem-drivers]] · [[speedfan-exploit]] · [[windows-kernel-exploits]] · [[ntmemory]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
