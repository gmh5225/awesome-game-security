---
title: HyperDeceit
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Xyrem__HyperDeceit.md
updated: 2026-08-19
confidence: medium
---

# HyperDeceit

**HyperDeceit** (Xyrem/HyperDeceit) is a C++ library that **impersonates Hyper-V behavior** and **intercepts selected hypercalls** from the Windows kernel. It ships ready-to-hook implementations for low-level paths including **TLB flushing**, **sleep and shutdown handling**, **address-space switching**, and **spinlock behavior**, with emphasis on virtualization internals, kernel compatibility constraints, and integration as a reusable library component. Aimed at advanced kernel and anti-cheat researchers studying **hypervisor-layer interception** and stealth techniques—not a production anti-cheat component. (source: wiki/sources/descriptions/Xyrem__HyperDeceit.md)

Complements Hyper-V hypercall-page hook PoCs such as [[driver-hypercall-page-hook]] and [[hook-hvl-switch-virtual-address-space]] (README `[HvcallCodeVa]` lane), Microsoft Hyper-V introspection such as [[hyper-rev]], offensive Hyper-V frameworks such as [[voyager]], and sibling Xyrem kernel concealment research such as [[yumekage]].

## Links

- Repo: https://github.com/Xyrem/HyperDeceit (README tag: HvcallCodeVa)

## Related

[[driver-hypercall-page-hook]] · [[hook-hvl-switch-virtual-address-space]] · [[hyper-rev]] · [[voyager]] · [[yumekage]] · [[hypervisor-detection]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
