---
title: HookHvcallCodeVa
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/1401199262__HookHvcallCodeVa.md
updated: 2026-09-05
confidence: medium
---

# HookHvcallCodeVa

**HookHvcallCodeVa** (1401199262) is a Windows kernel **proof of concept** that hooks the **hypercall code callback** invoked during **address-space switching**. It **pattern-scans** internal routines, installs a **custom callback**, and adjusts **enlightenment-related flags** at runtime. Implemented in C++ with low-level **CR3 handling** and **per-processor hypercall page setup** logic. Primary use case: advanced **kernel internals** and **hypervisor-behavior research** in game-security contexts. README category: `[HvcallCodeVa]`. (source: wiki/sources/descriptions/1401199262__HookHvcallCodeVa.md)

Complements sibling 1401199262 kernel PoCs [[hook-swap-context]], [[nmi-stack-walk]], and [[remote-call]], and the broader **HvcallCodeVa** research lane: [[driver-hypercall-page-hook]], [[hook-hvl-switch-virtual-address-space]], [[hyperdeceit]], and context-switch–scoped memory concealment such as [[yumekage]].

## Links

- Repo: https://github.com/1401199262/HookHvcallCodeVa [HvcallCodeVa]

## Related

[[hook-swap-context]] · [[driver-hypercall-page-hook]] · [[hook-hvl-switch-virtual-address-space]] · [[hyperdeceit]] · [[yumekage]] · [[nmi-stack-walk]] · [[remote-call]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
