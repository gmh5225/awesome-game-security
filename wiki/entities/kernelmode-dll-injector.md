---
title: Kernelmode-DLL-Injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/YouNeverKnow00__Kernelmode-DLL-Injector.md
updated: 2026-08-19
confidence: medium
---

# Kernelmode-DLL-Injector

Windows **kernel-mode DLL injector** (C++) that loads a custom kernel driver through **[[kdmapper]]** and an Intel **[[byovd]]** vulnerable driver, then performs **manual DLL mapping** into target processes from kernel space. The codebase covers PE section mapping, import resolution, TLS callback handling, and user-kernel communication through **IOCTL** operations. Mainly useful for game security researchers studying kernel-assisted DLL injection, manual mapping techniques, and vulnerable-driver exploitation for process manipulation. (source: wiki/sources/descriptions/YouNeverKnow00__Kernelmode-DLL-Injector.md)

README lane: Manual Map.

## Links

- Repo: https://github.com/YouNeverKnow00/Kernelmode-DLL-Injector

## Related

[[kdmapper]] · [[byovd]] · [[kernel-dll-injector]] · [[stealthy-kernelmode-injector]] · [[kernel-vad-injector]] · [[kernelmode-manual-mapping-through-iat]] · [[windows-process-injection]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
