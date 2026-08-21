---
title: pwnedboot
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/SamuelTulach__PwnedBoot.md
updated: 2026-08-21
confidence: medium
---

# pwnedboot

Proof-of-concept **boot payload** that replaces the Windows **microcode update DLL** to run custom code very early in the boot chain. Implemented in C and C++ with EFI-focused code, Visual Studio project files, and bundled gnu-efi components. The core technique shows how the bootloader can execute the replacement module under specific boot options, then **remap execution** to continue the normal boot flow — using Windows' own bootloader as a shim to bypass **Secure Boot**. Primarily useful for boot security research, early-boot attack surface analysis, and anti-cheat threat modeling around pre-OS execution. (source: wiki/sources/descriptions/SamuelTulach__PwnedBoot.md)

Distinct from full UEFI bootkit frameworks such as [[rainbow]] and [[bootlicker]] but sits in the same pre-kernel Windows boot-chain lane as [[uefi-bootkit]] and [[driver-efi-bootkit]].

## Links

- Repo: https://github.com/SamuelTulach/PwnedBoot

## Related

[[bootlicker]] · [[rainbow]] · [[uefi-bootkit]] · [[driver-efi-bootkit]] · [[negativespoofer]] · [[simpleuefi]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
