---
title: Kernel-Bridge
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/HoShiMin__Kernel-Bridge.md
updated: 2026-08-24
confidence: medium
---

# Kernel-Bridge

**Kernel-Bridge** is a Windows **kernel driver framework and template** for low-level system programming and research. Implemented in modern **C++**, it includes **hypervisor-assisted components** for **Intel VT-x** and **AMD-V** environments. The framework exposes abstractions for **memory operations**, **IOCTL handling**, **hooks**, **CPUID** and **MSR** interactions, and other kernel primitives. Commonly used in advanced debugging, monitoring, and **anti-cheat related kernel security research**. (source: wiki/sources/descriptions/HoShiMin__Kernel-Bridge.md)

Complements hypervisor-assisted debuggers such as [[hyperdbg]] and [[vt-debuger]], driver scaffolding such as [[driver-base]] and [[windows-kernel-rs]], and educational VT-x stacks such as [[hypervisor-from-scratch]].

## Links

- Repo: https://github.com/HoShiMin/Kernel-Bridge

## Related

[[hyperdbg]] · [[vt-debuger]] · [[hypervisor-from-scratch]] · [[driver-base]] · [[windows-kernel-rs]] · [[kernel-research-kit]] · [[kernel-snippets]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
