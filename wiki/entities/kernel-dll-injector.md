---
title: Kernel-dll-injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/alexkrnl__Kernel-dll-injector.md
updated: 2026-08-18
confidence: medium
---

# Kernel-dll-injector

Windows **kernel-mode DLL injector** (C/C++; Visual Studio + WDK) that injects a chosen DLL into **newly created processes** when **kernel32** loads. Includes both a kernel driver and a sample payload DLL. The technique is based on analysis of the **Sirifef (Max++)** rootkit injection path and is documented as **x86-focused**. Useful for studying kernel-assisted process injection and for defensive research on detecting or mitigating early-startup APC-style loads. (source: wiki/sources/descriptions/alexkrnl__Kernel-dll-injector.md)

README lane: APC.

## Links

- Repo: https://github.com/alexkrnl/Kernel-dll-injector

## Related

[[injdrv]] · [[kinject]] · [[apc-research]] · [[stealthy-kernelmode-injector]] · [[windows-process-injection]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
