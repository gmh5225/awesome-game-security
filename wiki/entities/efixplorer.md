---
title: efiXplorer
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__efiXplorer.md
updated: 2026-08-26
confidence: medium
---

# efiXplorer

IDA Pro plugin for automated analysis of UEFI firmware binaries. Identifies EFI protocols by GUID matching, annotates Boot Services and Runtime Services table calls, resolves protocol interface usage, and reconstructs PEI/DXE driver dependencies—reducing manual effort in UEFI firmware reverse engineering. Aimed at firmware security researchers analyzing UEFI BIOS implementations, bootkits, and EFI-level malware. (source: wiki/sources/descriptions/gmh5225__efiXplorer.md)

Not a bootkit or mapper—scoped to IDA-side UEFI/EFI structure and service annotation (`[UEFI firmware]` lane). Complements Ghidra annotator [[efiseek]], Python annotator [[ida-efiutils]], flash-image tooling such as [[fiano]], and pre-OS cheat/EFI research samples such as [[efitool]], [[uefi-bootloader]], and [[xigmapper]].

## Links

- Repo: https://github.com/gmh5225/efiXplorer

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[efiseek]] · [[ida-efiutils]] · [[fiano]] · [[efitool]] · [[uefi-bootloader]] · [[xigmapper]] · [[minivisorpkg]] · [[idaplugins]]
