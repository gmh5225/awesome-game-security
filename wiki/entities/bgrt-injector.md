---
title: BGRTInjector
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/Jamesits__BGRTInjector.md
updated: 2026-08-24
confidence: medium
---

# BGRTInjector

**BGRTInjector** (Jamesits) is a **UEFI utility** that replaces the **boot logo** shown on systems using the ACPI **BGRT** (Boot Graphics Resource Table) mechanism. Written in **C**, it runs as an **EFI loader or driver** and accepts custom **24-bit BMP** assets. The project ships build assets and integration notes for common boot workflows such as **rEFInd** and default EFI paths. Primary use case: **low-level firmware customization** and **boot-chain experimentation** on Windows-capable UEFI machines. (source: wiki/sources/descriptions/Jamesits__BGRTInjector.md)

Complements pre-boot UEFI dev scaffolds such as [[simpleuefi]], [[easyuefi]], and [[uefi-graphic]] when customizing the visible boot surface before OS load—not a bootkit or kernel bypass tool.

## Links

- Repo: https://github.com/Jamesits/BGRTInjector

## Related

[[simpleuefi]] · [[easyuefi]] · [[uefi-graphic]] · [[uefi-bootloader]] · [[eficmake]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
