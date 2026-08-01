---
title: Fiano
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/linuxboot__fiano.md
updated: 2026-08-01
confidence: medium
---

# Fiano

Go library and toolset for parsing, creating, and manipulating UEFI firmware images. Handles UEFI Firmware Volumes, FFS files, PE32 sections, compression (LZMA, Tiano), and GUIDed sections in BIOS/UEFI ROM images; CLI commands extract, replace, and remove firmware modules from flash images. Aimed at firmware security researchers, UEFI developers, and boot security analysts. (source: wiki/sources/descriptions/linuxboot__fiano.md)

Complements IDA-side UEFI annotation via [[ida-efiutils]] and pre-OS cheat/EFI research samples such as [[uefi-bootloader]], [[efitool]], and [[xigmapper]] — Fiano operates on whole flash images rather than disassembled modules.

## Links

- Repo: https://github.com/linuxboot/fiano

## Related

[[ida-efiutils]] · [[uefi-bootloader]] · [[efitool]] · [[eficmake]] · [[pesign]] · [[minivisorpkg]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
