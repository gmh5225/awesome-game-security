---
title: Ophion
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/zer0condition__Ophion.md
updated: 2026-07-17
confidence: medium
---

# Ophion

Stealth Intel VT-x Type-2 hypervisor for Windows x64 as a WDM kernel driver in C: VMX + EPT, multi-core broadcast, VM exits for CPUID / control-register access, plus anti-detection (CPUID result caching, CR4.VMXE hide, TSC offset compensation, private host CR3). Aimed at researchers studying lightweight HV construction and common hypervisor-detection bypass vs EAC/BE/AVs—not a production anti-cheat component. (source: wiki/sources/descriptions/zer0condition__Ophion.md)

Pairs with the minimal learning stack [[hv]] and hacked-hypervisor stress tooling such as [[vt-debuuger]] under `Detection: Hacked Hypervisor`.

## Links

- Repo: https://github.com/zer0condition/Ophion (README tag: Hacked Hypervisor Testing)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hv]] · [[vt-debuuger]] · [[hvci]] · [[overviews/reverse-engineering]]
