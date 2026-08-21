---
title: mutante
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/SamuelTulach__mutante.md
updated: 2026-08-21
confidence: medium
---

# mutante

**mutante** (SamuelTulach) is a Windows **kernel-mode HWID spoofer** that alters several hardware identity sources. The C/C++ driver targets **disk serial information**, **S.M.A.R.T. behavior**, and **SMBIOS table fields** while avoiding permanent hook dependencies. It ships as a Visual Studio driver project and reflects an older generation of anti-cheat evasion tooling. Today it is most useful as an **archival reference** for low-level SMBIOS and storage identifier manipulation techniques in game security research. README category: cheat / [HWID]. (source: wiki/sources/descriptions/SamuelTulach__mutante.md)

Distinct from boot-time firmware-table spoofers such as [[negativespoofer]] and UEFI bootkit chains such as [[rainbow]] / [[rainbow-efi]] — operates at kernel runtime on storage and SMBIOS surfaces rather than pre-OS firmware patching or loader-stage implants. Overlaps the disk/SMART/SMBIOS lane of educational PoCs such as [[skotschia-hwid-spoofer]] and dispatch-hook stacks such as [[easy-hwid-spoofer]], but emphasizes hook-minimal identifier rewriting in a standalone WDK driver.

## Links

- Repo: https://github.com/SamuelTulach/mutante

## Related

[[negativespoofer]] · [[rainbow]] · [[tpm-spoofer]] · [[skotschia-hwid-spoofer]] · [[hdd-serial-spoofer]] · [[easy-hwid-spoofer]] · [[hwid-checker-mg]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
