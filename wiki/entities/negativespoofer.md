---
title: negativespoofer
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/SamuelTulach__negativespoofer.md
updated: 2026-08-21
confidence: medium
---

# negativespoofer

Boot-time **SMBIOS spoofing** project that modifies firmware tables before the operating system starts. Implementation follows a **Clover-style patching** approach with C and EFI-oriented code plus separate build and usage guidance. By changing SMBIOS data pre-boot, it targets hardware identity signals consumed later by system and security software. Historical resource for pre-OS hardware fingerprint manipulation research in anti-cheat and platform security contexts. README category: cheat / [HWID]. (source: wiki/sources/descriptions/SamuelTulach__negativespoofer.md)

Distinct from kernel-mode SMBIOS hook spoofers such as [[easy-hwid-spoofer]] and UEFI bootkit loader chains such as [[rainbow-efi]] / [[rainbow]] — operates at firmware-table patch time before OS boot rather than via driver dispatch hooks or loader-stage implants.

## Links

- Repo: https://github.com/SamuelTulach/negativespoofer

## Related

[[rainbow]] · [[rainbow-efi]] · [[spoofer-amidewin]] · [[hwid-checker-mg]] · [[windows-spoofer]] · [[tpm-spoofer]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
