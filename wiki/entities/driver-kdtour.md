---
title: Driver-KDtour
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-KDtour.md
updated: 2026-08-13
confidence: medium
---

# Driver-KDtour

Small, dependency-free Windows kernel detour library for patching exported kernel routines inline. The `c_detour` class saves stolen bytes, builds a custom absolute jump stub, and writes patches through MDL-backed writable mappings—keeping install and removal self-contained without page-guard style tricks. (source: wiki/sources/descriptions/gmh5225__Driver-KDtour.md)

The archived README positions it as a simple hooking library for targets such as `MmCopyMemory` and `MmCopyVirtualMemory`; the sample entry point hooks `KeAttachProcess`. Mainly useful for kernel researchers wanting a compact reference for inline detours, custom trampoline stubs, and low-friction kernel hook experiments.

## Links

- Repo: https://github.com/gmh5225/Driver-KDtour (README tag: Easy Kernel Detour)

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[windows-kernel-pagehook]] · [[hook-kdtrap]] · [[subhook]] · [[detoursnt]] · [[ntmemory]]
