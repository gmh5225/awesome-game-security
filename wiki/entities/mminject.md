---
title: MMInject
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/SDXT__MMInject.md
updated: 2026-08-21
confidence: medium
---

# MMInject

Windows **kernel DLL injector** (C; native Windows internals headers) that hides execution by manipulating **page permissions** through **NX-bit swapping** and **VAD-related** techniques. The injector allocates writable pages, modifies underlying page-table behavior to gain execute capability, and attempts to reduce obvious memory-protection artifacts. Includes dynamic kernel data handling, I/O, and loader logic. Primarily aimed at advanced game-security and anti-cheat bypass research studying stealthy kernel-assisted injection. (source: wiki/sources/descriptions/SDXT__MMInject.md)

README lane: Using NX Bit Swapping and VAD hide.

## Links

- Repo: https://github.com/SDXT/MMInject

## Related

[[kernel-vad-injector]] · [[stealthy-kernelmode-injector]] · [[page-table-injector]] · [[kernel-dll-injector]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
