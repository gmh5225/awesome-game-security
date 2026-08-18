---
title: eac-spoofer-meme
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/zensenzay__eac-spoofer-meme.md
updated: 2026-08-18
confidence: medium
---

# eac-spoofer-meme

**eac-spoofer-meme** is an open-source Windows **hardware and system identifier (HWID) spoofer** aimed at bypassing [[easy-anti-cheat]] and similar anti-cheat fingerprinting. A kernel-mode C driver pairs with a user-mode C++ controller over custom IOCTLs to rewrite identifiers across SMBIOS/WMI, disk and NVMe serials, network MAC addresses, GPU and PCI IDs, CPUID values, EFI variables, ACPI tables, and numerous Windows registry machine IDs. (source: wiki/sources/descriptions/zensenzay__eac-spoofer-meme.md)

Advanced techniques include disk I/O completion hooking, registry notification callbacks for transparent PCI and USB alias redirection, VT-x and AMD SVM mini-hypervisors to intercept CPUID queries, and optional artifact cleanup plus process memory injection primitives. The project is positioned as a reference for researchers studying how anti-cheat systems collect hardware fingerprints and how kernel-level spoofing can evade those checks.

Sits in the `Cheat > HWID` lane beside comprehensive kernel spoofers such as [[hwid-kernel-spoofer]], [[easy-hwid-spoofer]], [[full-hwid-spoofer-v6]], and [[hwid-spoofer-eac-be]], and upstream [[hwid]] / [[driver-hwid-btbd-modified]] storage-stack research.

## Links

- Repo: https://github.com/zensenzay/eac-spoofer-meme

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[easy-anti-cheat]] · [[hwid-kernel-spoofer]] · [[easy-hwid-spoofer]] · [[hwid-spoofer-eac-be]] · [[full-hwid-spoofer-v6]] · [[hwid]] · [[driver-hwid-btbd-modified]] · [[hwid-checker-mg]]
