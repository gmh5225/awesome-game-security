---
title: EfiDump
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__EfiDump.md
updated: 2026-08-13
confidence: medium
---

# EfiDump

Proof-of-concept **EFI runtime driver** plus a Windows **usermode client** for direct **process memory read and write** after the OS has booted. The repo is a minimal EFI-based process dumper: a `driver` runtime component (build `driver.efi` with **gnu-efi**) and a separate `client` that communicates with it once Windows is running. Typical flow: compile the runtime driver, load it from an **EDK2 shell** on a FAT32 USB device, then use the client post-boot. The author explicitly notes **no hardening or memory-safety checks**—research-only. (source: wiki/sources/descriptions/gmh5225__EfiDump.md)

Useful for studying how **runtime EFI drivers survive into the OS** and expose cross-process memory primitives to a companion tool without a conventional Windows kernel driver load—adjacent to OS-runtime UEFI cheat stacks such as [[fortnite-efi-external]] and runtime mappers such as [[uefi-bootloader]], but focused on generic process dump/R/W rather than a title-specific external.

## Links

- Repo: https://github.com/gmh5225/EfiDump

## Related

[[fortnite-efi-external]] · [[uefi-bootloader]] · [[bootlicker]] · [[efitool]] · [[offline-crash-dump-uefi]] · [[tool-diy-system-memory-dump]] · [[eficmake]] · [[efixplorer]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
