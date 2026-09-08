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

**Hawkeye** (hawkeye-Leo) — Windows **kernel security research console** for anti-cheat analysis and live forensics, backed by a host-native kernel driver on Windows 10/11 x64. (source: wiki/sources/descriptions/hawkeye-Leo__hawkeye.md)

Interactive command bench for authorized kernel and anti-cheat researchers investigating driver behavior, memory access, anti-capture mechanisms, and related cheat techniques on systems they administer.

## Commands

| Command | Purpose |
|---------|---------|
| `!probe` | Live symbol and module inspection |
| `!etw` | ETW-based execution sampling and call-stack tracing |
| `!kernel_region` | Virtual address classification |
| (built-ins) | Memory read and disassembly utilities |

## Editions

- **Community** (GPL-3.0-or-later; source in hawkeye-community) — interactive command bench and core probing utilities.
- **Hawkeye Lab** — automated high-risk detection simulations plus `!analyze` workflow producing scored analysis reports across memory mapping, active pages, and kernel injection patterns.

## Links

- Site: https://github.com/hawkeye-Leo/hawkeye [Official GitHub Pages site; GPL source in hawkeye-community]

## Related

[[etw-threat-intelligence]] · [[kernel-callbacks]] · [[anti-cheat-emulator]] · [[irontrace]] · [[anticheat-scanner]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
