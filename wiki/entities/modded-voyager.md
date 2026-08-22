---
title: Modded Voyager
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/NurdAlert__modded-voyager.md
updated: 2026-08-22
confidence: medium
---

# Modded Voyager

**Modded Voyager** (NurdAlert) is a modified **Voyager-style UEFI hypervisor loader and payload framework** for **Intel and AMD** systems. It provides separate **VM-exit handlers** and memory primitives for guest physical and virtual address translation, read/write operations, and page-table initialization. UEFI components hook Windows boot stages such as **`bootmgfw`** and **`winload`**, patching **Hyper-V–related paths before OS startup**. Aimed at advanced low-level research into **boot-time virtualization**, **kernel control**, and **anti-cheat bypass** techniques. (source: wiki/sources/descriptions/NurdAlert__modded-voyager.md)

Extends the [[voyager]] Hyper-V offensive-research lineage with a **pre-OS UEFI loader** path rather than relying solely on in-guest Hyper-V exploitation. Complements boot-chain research such as [[bootlicker]], [[pwnedboot]], [[driver-efi-bootkit]], and [[uefi-bootkit]], and defensive **hacked-hypervisor** probes such as [[hypervisor-detection]] and [[detect-hypervisor-detect-ring-0]].

## Links

- Repo: https://github.com/NurdAlert/modded-voyager

## Related

[[voyager]] · [[vdm]] · [[msrexec]] · [[hyper-rev]] · [[minivisorpkg]] · [[bootlicker]] · [[pwnedboot]] · [[driver-efi-bootkit]] · [[hypervisor-detection]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
