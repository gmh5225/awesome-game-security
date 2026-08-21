---
title: rainbow
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/SamuelTulach__rainbow.md
updated: 2026-08-21
confidence: medium
---

# rainbow

UEFI-based **bootkit** that runs before the Windows kernel loads, built on the **EDK-II** firmware development framework. Includes **OVMF** debugging support for QEMU-based development and testing, plus a **Visual Studio** solution for building UEFI applications. Primarily useful for UEFI security researchers and anti-cheat analysts studying pre-boot attack vectors, bootkit techniques, and firmware-level persistence mechanisms. README category: cheat / [HWID]. (source: wiki/sources/descriptions/SamuelTulach__rainbow.md)

Distinct from the gmh5225 [[rainbow-efi]] fork (detailed `ExitBootServices` → `OslLoaderBlock` → `IopLoadDriver` HWID spoof chain) but sits in the same pre-kernel UEFI bootkit lane as [[driver-efi-bootkit]], [[bootlicker]], and [[uefi-bootkit]].

## Links

- Repo: https://github.com/SamuelTulach/rainbow

## Related

[[rainbow-efi]] · [[driver-efi-bootkit]] · [[bootlicker]] · [[uefi-bootkit]] · [[simpleuefi]] · [[eficmake]] · [[tpm-spoofer]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
