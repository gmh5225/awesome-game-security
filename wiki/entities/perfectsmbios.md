---
title: PerfectSMBios
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Th3Spl__PerfectSMBios.md
  - wiki/sources/README-categories.md
updated: 2026-08-29
confidence: medium
---

# PerfectSMBios

Lightweight **UEFI library** (Th3Spl) for reading and **spoofing SMBIOS firmware tables** before the operating system loads. Written in C and built with **VisualUefi** or **EDK2**, it locates SMBIOS 2.0 and 3.0 entry points through the EFI configuration table and provides helpers to find specific structure types, read string fields, and overwrite them with randomized ASCII values. Unlike many SMBIOS spoofing tools, it avoids Windows kernel dependencies such as `ntoskrnl.exe` or `winload.efi` and works cleanly on both Windows and Linux. The included example modifies the system manufacturer string; reusable headers can be dropped into custom UEFI projects for hardware fingerprint evasion, anti-cheat research, and low-level reverse engineering. README category: cheat / EFI Driver + HWID. (source: wiki/sources/descriptions/Th3Spl__PerfectSMBios.md)

Distinct from Clover-style boot-time table patches such as [[negativespoofer]] and loader-chain HWID spoofers such as [[rainbow-efi]] — operates as a drop-in pre-OS SMBIOS helper library rather than a full bootkit or kernel driver hook stack. Complements Th3Spl's [[simpleuefi]] Visual Studio UEFI scaffold for firmware-stage prototyping.

## Links

- Repo: https://github.com/Th3Spl/PerfectSMBios

## Related

[[simpleuefi]] · [[negativespoofer]] · [[rainbow-efi]] · [[mutante]] · [[easy-hwid-spoofer]] · [[hwid-checker-mg]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
