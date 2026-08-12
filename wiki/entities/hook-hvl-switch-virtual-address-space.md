---
title: Hook HvlSwitchVirtualAddressSpace
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Hook-HvlSwitchVirtualAddressSpace.md
updated: 2026-08-12
confidence: medium
---

# Hook HvlSwitchVirtualAddressSpace

Kernel technique (gmh5225; README `[HvcallCodeVa]`) for **hooking `HvlSwitchVirtualAddressSpace`** — the hypervisor-assisted path Windows uses when switching virtual address spaces. Intercepts CR3 transitions during address-space context switches and manipulates page-table visibility so selected memory pages are hidden from **process memory scanning** performed by anti-cheat during those switches. Useful for studying Hyper-V call (`Hvcall`) address-space hooks, CR3/context-switch evasion, and how kernel AC scanners observe (or miss) pages across address-space boundaries. (source: wiki/sources/descriptions/gmh5225__Hook-HvlSwitchVirtualAddressSpace.md)

## Links

- Repo: https://github.com/gmh5225/Hook-HvlSwitchVirtualAddressSpace

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[hvci]] · [[hook-kdtrap]] · [[eac-cr3-bypass]] · [[windows-kernel-pagehook]] · [[zero-hvci]] · [[hypervisor]]
