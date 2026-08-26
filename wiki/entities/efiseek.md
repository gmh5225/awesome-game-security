---
title: efiSeek
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/DSecurity__efiSeek.md
updated: 2026-08-26
confidence: medium
---

# efiSeek

Ghidra analyzer plugin that automates reverse engineering tasks for EFI binaries. Implemented in Java; identifies known EFI GUIDs, protocol usage patterns, and callback relationships such as `LOCATE_PROTOCOL`, `NOTIFY`, and `INSTALL_PROTOCOL_INTERFACE` flows. Includes helper scripts and GUID data to speed headless workflows and structured firmware analysis. Aimed at firmware security researchers investigating UEFI internals, attack surface, and low-level behavior. (source: wiki/sources/descriptions/DSecurity__efiSeek.md)

Ghidra-side UEFI annotation—complements IDA annotators [[efixplorer]] and [[ida-efiutils]] when analyzing bootkits, EFI malware, or pre-OS cheat research samples.

## Links

- Repo: https://github.com/DSecurity/efiSeek

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ghidra]] · [[efixplorer]] · [[ida-efiutils]] · [[fiano]] · [[visualuefi-2-0]] · [[ghidra-decompiler-plugins]]
