---
title: uefi-bootkit
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/ajkhoury__UEFI-Bootkit.md
updated: 2026-08-18
confidence: medium
---

# uefi-bootkit

Compact proof-of-concept **UEFI bootkit** that targets the UEFI boot chain with mostly C code and minimal assembly. The codebase includes a UEFI application and runtime driver components intended to persist beyond **`ExitBootServices`** and continue execution into the OS boot process. It demonstrates practical EFI build setup, image loading logic, and runtime protocol handling in a firmware context. (source: wiki/sources/descriptions/ajkhoury__UEFI-Bootkit.md)

Aimed at low-level boot security research—studies of **pre-OS persistence** and **detection challenges**—adjacent to generic bootkit PoCs such as [[bootlicker]] and staged EFI→kernel implants such as [[driver-efi-bootkit]], but focused on a compact C-centric UEFI app + runtime driver scaffold rather than Boot Manager patching or Python EFI inject tooling.

## Links

- Repo: https://github.com/ajkhoury/UEFI-Bootkit

## Related

[[bootlicker]] · [[driver-efi-bootkit]] · [[uefi-bootloader]] · [[efixplorer]] · [[efidump]] · [[pubg-internal]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
