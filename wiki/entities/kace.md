---
title: KACE
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/waryas__KACE.md
  - wiki/sources/descriptions/Qfrost911__KACE.md
updated: 2026-08-22
confidence: medium
---

# KACE

**Kernel Automated Compatibility Emulator** (C++): a **kernel anti-cheat emulation framework** for studying how protected drivers behave under simulated kernel conditions. Runs Windows kernel-mode drivers in user mode by emulating essential kernel APIs, memory management, IRQL handling, and driver entry conventions — with **PE mapping**, **import resolution**, **memory tracking**, **exception handling**, and **privileged-instruction emulation**. The codebase models key kernel structures and monitors read/write behavior to investigate **anti-debug** and **anti-emulation** checks. Supports **self context mapping** or **Unicorn** so researchers can load and study drivers (including anti-cheat components) without risking host stability. (source: wiki/sources/descriptions/Qfrost911__KACE.md) (source: wiki/sources/descriptions/waryas__KACE.md)

Sits in the README `Windows Emulator` / driver-analysis lane next to WHP user-mode PE guests such as [[winvisor]] and hybrid emulators such as [[kdemu]] — KACE targets ring-0 driver binaries in RING3 rather than hypervisor-hosted usermode PE.

## Links

- Repo: https://github.com/waryas/KACE (README: Emulate Drivers in RING3 with self context mapping or unicorn)
- Fork: https://github.com/Qfrost911/KACE (kernel AC emulation framework; learning/experimentation platform)

## Related

[[winvisor]] · [[kdemu]] · [[kubera]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[waryasswhe]]
