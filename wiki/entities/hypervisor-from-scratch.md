---
title: Hypervisor From Scratch
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/SinaKarvandi__Hypervisor-From-Scratch.md
updated: 2026-08-21
confidence: medium
---

# Hypervisor From Scratch

Tutorial-driven x86 hypervisor codebase that walks through building a custom Type-2 hypervisor in progressive stages. C, C++, and assembly examples cover VMX setup, VMCS management, Extended Page Table (EPT) translation, and virtualizing a running system, paired with staged learning material on modern hardware virtualization internals. Aimed at low-level systems programmers and security researchers learning hypervisor-based analysis techniques—not a production anti-cheat or stealth hooking stack. (source: wiki/sources/descriptions/SinaKarvandi__Hypervisor-From-Scratch.md)

Educational counterpart to minimal VT-x learning drivers such as [[hv]] and offensive EPT hooking research such as [[hypervisor]]; useful foundation before studying hacked-hypervisor detection ([[hypervisor-detection]], [[ept-hook-detection]]) and VBS/[[hvci]] threat models.

## Links

- Repo: https://github.com/SinaKarvandi/Hypervisor-From-Scratch (README tag: Hypervisor)

## Related

[[hv]] · [[hypervisor]] · [[ophion]] · [[minivisorpkg]] · [[ept-hook-detection]] · [[hypervisor-detection]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
