---
title: ida-efiutils
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/snare__ida-efiutils.md
updated: 2026-07-22
confidence: medium
---

# ida-efiutils

IDA Pro Python plugin for analyzing UEFI firmware binaries. Identifies and annotates EFI protocol GUIDs, Boot Services and Runtime Services table references, protocol installations and lookups, and PEI/DXE module entry points; applies automatic symbol annotation and type information to enrich UEFI binary analysis. Aimed at firmware security researchers reverse engineering UEFI BIOS implementations and boot-level malware. (source: wiki/sources/descriptions/snare__ida-efiutils.md)

Not a bootkit or mapper—scoped to IDA-side UEFI/EFI structure and service annotation (`[EFI binaries]` lane). Complements KMDF/WDF annotation such as [[ida-kmdf]] and EFI payload/research samples such as [[efitool]], [[xigmapper]], and [[minivisorpkg]].

## Links

- Repo: https://github.com/snare/ida-efiutils

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ida-kmdf]] · [[efitool]] · [[xigmapper]] · [[minivisorpkg]] · [[idaplugins]]
