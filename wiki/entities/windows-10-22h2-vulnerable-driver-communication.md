---
title: Windows-10-22H2-Vulnerable-driver-communication
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Windows-10-22H2-Vulnerable-driver-communication.md
updated: 2026-08-09
confidence: medium
---

# Windows-10-22H2-Vulnerable-driver-communication

User-mode wrapper around ASUS **`asromgdrv.sys`** that demonstrates loading a still-blocklist-eligible vulnerable signed driver on Windows 10 22H2 and Windows 11 for kernel-side services. The communication layer opens `\\.\AsrOmgDrv` and drives vendor IOCTLs through `DeviceIoControl`; `communication.cpp` implements helpers for contiguous kernel memory allocation/free and control-register read/write—essentially a concise reversed interface for the signed driver. Useful for Windows kernel researchers studying [[byovd]] communication patterns, control-register abuse, and how small reversed IOCTL wrappers become foundations for more advanced kernel tooling. (source: wiki/sources/descriptions/gmh5225__Windows-10-22H2-Vulnerable-driver-communication.md)

Sits in the same IOCTL-wrapper / access-primitive lane as [[gdriver-lib]], [[kur]], and [[vdk]], but documents a single OEM backend (`asromgdrv.sys`) with explicit CR and contiguous-pool primitives rather than a multi-driver kit.

## Links

- Repo: https://github.com/gmh5225/Windows-10-22H2-Vulnerable-driver-communication

## Related

[[byovd]] · [[gdriver-lib]] · [[imxyvimapper]] · [[kur]] · [[vdk]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
