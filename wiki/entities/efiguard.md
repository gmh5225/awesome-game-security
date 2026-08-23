---
title: EfiGuard
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Mattiwatti__EfiGuard.md
updated: 2026-08-23
confidence: medium
---

# EfiGuard

**EfiGuard** (Mattiwatti) is a portable **x64 UEFI bootkit** that patches the **Windows boot chain** to disable **PatchGuard** and **Driver Signature Enforcement (DSE)** during startup. The codebase is primarily **C and C++** with **EDK2 UEFI** components, a loader application, and helper tooling such as **EfiDSEFix**. It supports a wide range of **Windows x64** versions, uses **runtime disassembly** for robust patching, and provides multiple **boot-time patch modes** including **SetVariable-based control paths**. README category: **[EFI]**. Aimed at low-level Windows security researchers studying **boot integrity**, **kernel protections**, and **anti-cheat or driver-loading bypass** behavior. (source: wiki/sources/descriptions/Mattiwatti__EfiGuard.md)

Sits in the **pre-kernel bootkit** lane beside [[bootlicker]], [[driver-efi-bootkit]], and [[uefi-bootkit]], but focused on **KPP + DSE neutralization at boot** rather than runtime EFI RPM or staged driver implants alone. The SetVariable communication pattern inspired follow-on samples such as [[efi-memory]].

## Links

- Repo: https://github.com/Mattiwatti/EfiGuard

## Related

[[bootlicker]] · [[driver-efi-bootkit]] · [[uefi-bootkit]] · [[efi-memory]] · [[upgdsed]] · [[dse-hook]] · [[patchguard]] · [[efixplorer]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
