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
  - wiki/sources/descriptions/armasm__EasyAntiPatchGuard.md
  - wiki/sources/descriptions/Rythorndoran__PageTableHook.md
  - wiki/sources/descriptions/NeoMaster831__kurasagi.md
  - wiki/sources/descriptions/NSG650__NoMoreBugCheckReloaded.md
  - wiki/sources/descriptions/NSG650__NoMoreBugCheck.md
  - wiki/sources/descriptions/NSG650__BugCheckHack.md
  - wiki/sources/descriptions/Mattiwatti__EfiGuard.md
  - wiki/sources/descriptions/AmitMoshel1__PatchGuardEncryptorDriver.md
  - wiki/sources/descriptions/AdamOron__PatchGuardBypass.md
  - wiki/sources/descriptions/9176324__Shark.md
  - wiki/sources/descriptions/4l3x777__dse_pg_bypass.md
updated: 2026-09-04
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

[[easy-anti-patchguard]] (armasm) is a Win8–Win10-era kernel PoC that uses a driver plus assembly hooks to observe or short-circuit PatchGuard dispatch paths in protected routines, with call-chain analysis from kernel debugging sessions. (source: wiki/sources/descriptions/armasm__EasyAntiPatchGuard.md)

[[page-table-hook]] (Rythorndoran; C++ driver demo) redirects execution by editing page-table mappings instead of patching kernel code—preserving original routine access while avoiding typical PatchGuard-triggering inline hooks; includes `NtCreateFile` interception for advanced kernel / AC bypass study. (source: wiki/sources/descriptions/Rythorndoran__PageTableHook.md)

[[kurasagi]] (NeoMaster831; C/C++ kernel PoC; Win11 24H2–25H2 runtime PatchGuard bypass; manual-map load via [[kdmapper]]; documents crash-prone edge cases and CRITICAL_STRUCTURE_CORRUPTION behavior for advanced kernel security researchers) targets recent-build KPP bypass study in controlled lab environments. (source: wiki/sources/descriptions/NeoMaster831__kurasagi.md)

[[nomore-bugcheck-reloaded]] (NSG650) moves kernel crash-handling patches into a **UEFI boot-stage loader**—altering bugcheck behavior before normal driver-load paths—illustrating below-OS timing that sidesteps runtime PatchGuard pressure on loaded driver images. (source: wiki/sources/descriptions/NSG650__NoMoreBugCheckReloaded.md)

[[efiguard]] (Mattiwatti; portable x64 UEFI bootkit; patches the Windows boot chain at startup to disable PatchGuard and DSE; runtime disassembly; SetVariable-based boot-time patch modes; EfiDSEFix helper; wide Win x64 version support) illustrates **pre-kernel KPP + DSE neutralization** before normal driver-load telemetry exists. (source: wiki/sources/descriptions/Mattiwatti__EfiGuard.md)

[[nomore-bugcheck]] (NSG650) is the earlier **runtime kernel driver** lane: direct **`KeBugCheckEx`** code patching with restore logic to suppress the normal bugcheck path—illustrating PatchGuard-adjacent risk when hostile code overwrites crash-handling entry points from a loaded driver. (source: wiki/sources/descriptions/NSG650__NoMoreBugCheck.md)

[[bugcheckhack]] (NSG650) is a **driver + user-mode controller** that resolves kernel offsets and patches **bugcheck-related routines** to alter BSOD appearance and behavior—another runtime lane showing how crash-path patching research sits adjacent to PatchGuard-monitored kernel integrity. (source: wiki/sources/descriptions/NSG650__BugCheckHack.md)

[[patchguard-encryptor-driver]] (AmitMoshel1; C++ kernel driver) implements a **self-contained PatchGuard-like monitor**—periodic KTIMER/KDPC checks over SSDT, IDT, and selected MSRs plus meta-integrity verification of timer/DPC structures—useful for studying kernel anti-tamper design rather than KPP bypass. (source: wiki/sources/descriptions/AmitMoshel1__PatchGuardEncryptorDriver.md)

[[patchguardbypass]] (AdamOron; in-progress C/C++ research) documents a planned **dynamic modern-build KPP bypass** with goals to disable PG execution, evade runtime integrity checks, and verify PG state — for kernel security and anti-cheat analysts studying defensive attack surface. (source: wiki/sources/descriptions/AdamOron__PatchGuardBypass.md)

[[shark]] (9176324; C/C++/assembly kernel toolkit; driver + loader; x86/x64; runtime PatchGuard disable; Visual Studio/NMAKE workflows; references virtualization-assisted loading) is a kernel research toolkit for low-level PG bypass and kernel-defense study. (source: wiki/sources/descriptions/9176324__Shark.md)

[[dse-pg-bypass]] (4l3x777; C++ kernel research PoC; [[byovd]] attack model; detailed reversing notes on signature validation callbacks and PatchGuard integrity-check execution paths; educational combined DSE + KPP bypass study for defenders) sits in the same cheat / PatchGuard-related lane. (source: wiki/sources/descriptions/4l3x777__dse_pg_bypass.md)

## Related

[[hvci]] · [[kernel-callbacks]] · [[byovd]] · [[page-table-hook]] · [[pg1903]] · [[upgdsed]] · [[vulnerablepatchguardexploit]] · [[quickpgtrigger]] · [[patchguard-2023]] · [[patchguard-encryptor-driver]] · [[patchguardbypass]] · [[shark]] · [[dse-pg-bypass]] · [[tableflipper]] · [[easy-anti-patchguard]] · [[demystifying-patchguard]] · [[sushi]] · [[kurasagi]] · [[nomore-bugcheck]] · [[nomore-bugcheck-reloaded]] · [[bugcheckhack]] · [[efiguard]] · [[dioprocess-private]] · [[windows-kernel-shadow-stack]] · [[cet-research]] · [[overviews/windows-kernel]]
