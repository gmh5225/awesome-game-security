---
title: PatchGuard
kind: concept
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zzhouhe__PG1903.md
  - wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md
  - wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md
  - wiki/sources/descriptions/tandasat__Sushi.md
  - wiki/sources/descriptions/synacktiv__windows_kernel_shadow_stack.md
updated: 2026-07-21
confidence: high
---

# PatchGuard

Windows Kernel Patch Protection: periodic integrity checks over critical kernel structures; tampering can trigger a BSOD. Constrains SSDT/global hook styles and pushes hostile code toward less-monitored or below-OS techniques. (source: wiki/sources/skills/windows-kernel.md)

## Interaction with anti-cheat

AC kernel components coexist with PatchGuard rather than replacing it. Research often studies timing/context/hypervisor evasions of PG alongside AC callback integrity and [[hvci]].

## Research examples

[[pg1903]] demonstrates a Win10 1903-era approach: locate PatchGuard context pages, clear NX, and neutralize checks in real time (Demo NX). (source: wiki/sources/descriptions/zzhouhe__PG1903.md)

[[demystifying-patchguard]] is a C/C++ educational walkthrough of PatchGuard for researchers in the cheat / PG-related lane. (source: wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md)

[[sushi]] focuses on monitoring PG for offensive/RE study in the same cheat / PatchGuard-related area. (source: wiki/sources/descriptions/tandasat__Sushi.md)

UEFI bootkit research stacks such as [[dioprocess-private]] frame DSE / KPP bypass as a pre-kernel path alongside live process/kernel monitoring (Win10 22H2). (source: wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md)

Kernel CET / shadow-stack work such as [[windows-kernel-shadow-stack]] studies how Windows KM shadow stacks interact with PatchGuard (and potential bypass/weakening scenarios) under Intel CET. (source: wiki/sources/descriptions/synacktiv__windows_kernel_shadow_stack.md)

## Related

[[hvci]] · [[kernel-callbacks]] · [[byovd]] · [[pg1903]] · [[demystifying-patchguard]] · [[sushi]] · [[dioprocess-private]] · [[windows-kernel-shadow-stack]] · [[cet-research]] · [[overviews/windows-kernel]]
