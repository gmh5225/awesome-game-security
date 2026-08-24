---
title: HyperDbg
kind: entity
topics: [reverse-engineering, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/HyperDbg__HyperDbg.md
updated: 2026-08-24
confidence: medium
---

# HyperDbg

**HyperDbg** is an open-source **hypervisor-assisted debugger** for Windows **user-mode and kernel-mode** analysis. Implemented mainly in **C and C++**, it relies on hardware virtualization — **Intel VT-x** and **Extended Page Tables (EPT)** — to provide stealthy debugging primitives that sit below conventional usermode debuggers. Key capabilities include **stealth breakpoints**, **hidden hooks**, **memory-access monitoring**, and **extensible debugging workflows**. Intended for **reverse engineering**, **fuzzing**, **malware analysis**, and **anti-cheat or anti-debug research**. (source: wiki/sources/descriptions/HyperDbg__HyperDbg.md)

Complements conventional Windows debuggers such as [[x64dbg]] and WinDbg; sits in the same VT-x/EPT lane as [[vt-debuger]], [[unreal-vtdbg]], and [[hypervisor-from-scratch]], and opposite defensive stacks such as [[novahypervisor]] and [[hypervisor-detection]].

## Links

- Repo: https://github.com/HyperDbg/HyperDbg [VT debuger]

## Related

[[x64dbg]] · [[vt-debuger]] · [[unreal-vtdbg]] · [[hypervisor-from-scratch]] · [[hypervisor]] · [[novahypervisor]] · [[retoolkit]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
