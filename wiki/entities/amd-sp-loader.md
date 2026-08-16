---
title: AMD-SP-Loader
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/dayzerosec__AMD-SP-Loader.md
updated: 2026-08-16
confidence: medium
---

# AMD-SP-Loader

Binary Ninja **loader plugin** for AMD Secure Processor (SP) / Platform Security Processor (PSP) firmware binaries. Sets correct load addresses for **AGESA Bootloader (ABL)** and **PSP bootloader** blobs, optionally annotates **PSP syscalls** from a bundled dictionary, and is designed for binaries extracted via **PSPTool**. Aimed at firmware security researchers reverse engineering AMD PSP firmware and analyzing the AMD Secure Processor bootloader chain. (source: wiki/sources/descriptions/dayzerosec__AMD-SP-Loader.md)

Not a flash extractor or bootkit — scoped to Binary Ninja-side PSP/ABL load mapping and syscall naming (`[AMD-SP or PSP firmware]` lane). Complements UEFI firmware tooling such as [[efixplorer]], [[ida-efiutils]], and [[fiano]], and other Binary Ninja plugin work such as [[binary-ninja-mcp]] and [[triton-bn]].

## Links

- Repo: https://github.com/dayzerosec/AMD-SP-Loader

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[efixplorer]] · [[fiano]] · [[binary-ninja-mcp]] · [[triton-bn]] · [[amd-ibs-toolkit]] · [[embedded-hacking]]
