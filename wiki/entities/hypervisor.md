---
title: hypervisor
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/momo5502__hypervisor.md
updated: 2026-08-01
confidence: medium
---

# hypervisor

Lightweight experimental Intel VT-x Type-2 hypervisor for Windows in C++ (CMake; WDK kernel driver plus user-mode library): uses Extended Page Tables (EPT) and second-level address translation to install stealthy kernel-level memory hooks that intercept code execution while evading conventional memory-integrity checks. Implements EPT page hooks, code watchpoints triggered on EPT violations, and process-lifecycle handling for per-process hook cleanup. Aimed at security researchers studying hardware-assisted virtualization, anti-cheat evasion, and hypervisor-based hooking — not a production AC component. (source: wiki/sources/descriptions/momo5502__hypervisor.md)

Offensive counterpart to the same author's user-mode EPT hook detector [[ept-hook-detection]]; sits beside stealth Type-2 stacks such as [[ophion]] and minimal VT-x learning drivers such as [[hv]] under `Detection: Hacked Hypervisor` / `Detect EPT` research.

## Links

- Repo: https://github.com/momo5502/hypervisor (README tag: Experimental Intel VT-x type-2 hypervisor with EPT hooking for stealth memory interception and integrity-check bypass research)

## Related

[[ept-hook-detection]] · [[ophion]] · [[hv]] · [[hypervisor-detection]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hvci]]
