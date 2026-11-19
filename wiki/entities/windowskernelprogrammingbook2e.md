---
title: Windows Kernel Programming Book 2e
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/zodiacon__windowskernelprogrammingbook2e.md
updated: 2026-11-19
confidence: high
---

# Windows Kernel Programming Book 2e

**windowskernelprogrammingbook2e** (zodiacon/windowskernelprogrammingbook2e) is the official companion source code for the second edition of *Windows Kernel Programming*, shipped as chapter-aligned Visual Studio solutions that walk through hands-on WDK driver development. (source: wiki/sources/descriptions/zodiacon__windowskernelprogrammingbook2e.md)

## Capabilities

- Per-chapter **WDM** sample drivers in C/C++ built with the Windows Driver Kit, plus user-mode clients that exercise devices, **IOCTLs**, and shared buffers (patterns such as Boost and Booster).
- Progression from **`DriverEntry`**, unload, and IRP dispatch through synchronization, process enumeration, monitoring/protection components, **kernel callbacks** and timers, file-system **minifilters** (backup and delete protection), **Windows Filtering Platform** examples, and device-monitoring drivers.
- Shared **ktl** kernel template library: reusable helpers for locks, memory, strings, and collections reused across labs.

## Use cases

Driver authors and security researchers use these labs as a structured baseline for kernel monitoring, filtering, and access-control primitives—the same foundations anti-cheat and low-level endpoint security stacks build on. Complements GUI tooling from the same author family ([[infstudio]], [[dbgprint]], [[poolmonxv3]]) and starter scaffolds such as [[driver-base]].

## Links

- Repo: https://github.com/zodiacon/windowskernelprogrammingbook2e (README: official WDK chapter sample projects for *Windows Kernel Programming*, 2nd ed.—minifilters, callbacks, and related kernel-mode labs)

## Related

[[kernel-callbacks]] · [[driver-trust-boundaries]] · [[driver-base]] · [[infstudio]] · [[dbgprint]] · [[poolmonxv3]] · [[object-explorer]] · [[overviews/windows-kernel]] · [[research-rigor]]