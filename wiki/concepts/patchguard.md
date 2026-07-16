---
title: PatchGuard
kind: concept
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zzhouhe__PG1903.md
updated: 2026-07-16
confidence: high
---

# PatchGuard

Windows Kernel Patch Protection: periodic integrity checks over critical kernel structures; tampering can trigger a BSOD. Constrains SSDT/global hook styles and pushes hostile code toward less-monitored or below-OS techniques. (source: wiki/sources/skills/windows-kernel.md)

## Interaction with anti-cheat

AC kernel components coexist with PatchGuard rather than replacing it. Research often studies timing/context/hypervisor evasions of PG alongside AC callback integrity and [[hvci]].

## Research examples

[[pg1903]] demonstrates a Win10 1903-era approach: locate PatchGuard context pages, clear NX, and neutralize checks in real time (Demo NX). (source: wiki/sources/descriptions/zzhouhe__PG1903.md)

## Related

[[hvci]] · [[kernel-callbacks]] · [[byovd]] · [[pg1903]] · [[overviews/windows-kernel]]
