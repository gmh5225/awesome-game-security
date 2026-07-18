---
title: KACE
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/waryas__KACE.md
updated: 2026-07-18
confidence: medium
---

# KACE

Kernel Automated Compatibility Emulator (C++): runs Windows kernel-mode drivers in user mode for analysis by emulating essential kernel APIs, memory management, IRQL handling, and driver entry conventions. Supports self context mapping or Unicorn so researchers can load and study drivers (including anti-cheat components) without risking host stability. (source: wiki/sources/descriptions/waryas__KACE.md)

Sits in the README `Windows Emulator` / driver-analysis lane next to WHP user-mode PE guests such as [[winvisor]] — KACE targets ring-0 driver binaries in RING3 rather than hypervisor-hosted usermode PE.

## Links

- Repo: https://github.com/waryas/KACE (README: Emulate Drivers in RING3 with self context mapping or unicorn)

## Related

[[winvisor]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[waryasswhe]]
