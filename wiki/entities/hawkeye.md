---
title: Hawkeye
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/hawkeye-Leo__hawkeye.md
updated: 2026-09-08
confidence: medium
---

# Hawkeye

**Hawkeye** (hawkeye-Leo) — Windows **kernel security research console** for anti-cheat analysis and live forensics, backed by a host-native kernel driver on Windows 10/11 x64. Interactive command bench with `!probe` (live symbol/module inspection), `!etw` (ETW execution sampling and call-stack tracing), `!kernel_region` (virtual address classification), and memory read/disassembly utilities. GPL-3.0-or-later **Community** edition; **Hawkeye Lab** adds automated high-risk detection simulations and `!analyze` scored reports across memory mapping, active pages, and kernel injection patterns. (source: wiki/sources/descriptions/hawkeye-Leo__hawkeye.md)

## Use cases

Authorized kernel and anti-cheat researchers investigating driver behavior, memory access, anti-capture mechanisms, and related cheat techniques on systems they administer.

## Links

- Site: https://github.com/hawkeye-Leo/hawkeye [Official GitHub Pages site; GPL source in hawkeye-community]

## Related

[[etw-threat-intelligence]] · [[kernel-callbacks]] · [[anti-cheat-emulator]] · [[irontrace]] · [[anticheat-scanner]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
