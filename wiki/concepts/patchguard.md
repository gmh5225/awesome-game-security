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
  - wiki/sources/descriptions/hfiref0x__UPGDSED.md
  - wiki/sources/descriptions/gmh5225__VulnerablePatchGuardExploit.md
  - wiki/sources/descriptions/gmh5225__QuickPGTrigger.md
  - wiki/sources/descriptions/gmh5225__Patchguard-2023.md
  - wiki/sources/descriptions/emlinhax__tableflipper.md
updated: 2026-08-15
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

[[upgdsed]] combines runtime PatchGuard and DSE disable across Win7–11 using vulnerable signed drivers, CI.dll global manipulation, and KPP context patching — a multi-technique kernel trust-feature bypass reference for researchers. (source: wiki/sources/descriptions/hfiref0x__UPGDSED.md)

[[vulnerablepatchguardexploit]] (gmh5225; C++) implements a vulnerable PatchGuard exploit to disable KPP at runtime for offensive / RE study in the same cheat / PatchGuard-related lane. (source: wiki/sources/descriptions/gmh5225__VulnerablePatchGuardExploit.md)

[[quickpgtrigger]] (gmh5225; C/C++) targets **PatchGuard stress testing** — exercising KPP integrity-check paths under load for researchers in the Anti Cheat Stress Testing / cheat PatchGuard-related lane. (source: wiki/sources/descriptions/gmh5225__QuickPGTrigger.md)

[[patchguard-2023]] (gmh5225) documents 2023-era KPP internals — timer-based verification, context encryption, protected-structure list, recovery routines, trigger mechanisms, and bypass study — for kernel researchers in the cheat / PatchGuard-related lane. (source: wiki/sources/descriptions/gmh5225__Patchguard-2023.md)

[[tableflipper]] (emlinhax; C++) partially disables KPP on builds up to Windows 11 21H2 for offensive / RE study in the same cheat / PatchGuard-related lane. (source: wiki/sources/descriptions/emlinhax__tableflipper.md)

## Related

[[hvci]] · [[kernel-callbacks]] · [[byovd]] · [[pg1903]] · [[upgdsed]] · [[vulnerablepatchguardexploit]] · [[quickpgtrigger]] · [[patchguard-2023]] · [[tableflipper]] · [[demystifying-patchguard]] · [[sushi]] · [[dioprocess-private]] · [[windows-kernel-shadow-stack]] · [[cet-research]] · [[overviews/windows-kernel]]
