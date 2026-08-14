---
title: Comm-data-ptr-driver
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Comm-data-ptr-driver.md
updated: 2026-08-14
confidence: medium
---

# Comm-data-ptr-driver

Kernel driver implementing **data-pointer-based communication** for stealthy user↔kernel interaction. Exchanges memory read/write requests through **shared data pointers** rather than traditional IOCTLs, aiming to evade IOCTL-based anti-cheat telemetry. The README tags the sample under **`[NtGdiPolyPolyDraw]`**, placing it in the win32k GDI syscall covert-comms lane. (source: wiki/sources/descriptions/gmh5225__Comm-data-ptr-driver.md)

Mainly useful for Windows kernel researchers studying data-pointer swap channels, non-IOCTL KM↔UM memory R/W, and win32k GDI syscall abuse — adjacent to [[interep-driver-leak]] (same `NtGdiPolyPolyDraw` tag), [[data-ptr-swap]], [[dataptrswap-driver]], and [[custom-data-ptr-swap-sample]].

## Links

- Repo: https://github.com/gmh5225/Comm-data-ptr-driver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[interep-driver-leak]] · [[data-ptr-swap]] · [[dataptrswap-driver]] · [[custom-data-ptr-swap-sample]] · [[read-write-driver]]
