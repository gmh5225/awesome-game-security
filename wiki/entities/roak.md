---
title: roak
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/KeServiceDescriptorTable__roak.md
updated: 2026-08-23
confidence: medium
---

# roak

Windows **kernel-mode driver** that exposes read/write memory access through a **custom communication channel** instead of a conventional device IOCTL surface. The driver hooks **HAL timer query functions** for covert user↔kernel messaging, dispatches memory operations via **packet-based request handling**, and bundles **kernel offset resolution** plus system utility modules. Mainly useful for kernel security researchers studying **covert driver communication**, HAL-adjacent syscall channels, and kernel memory access patterns—adjacent to [[r69-driver]] in the `NtQueryAuxiliaryCounterFrequency` lane. (source: wiki/sources/descriptions/KeServiceDescriptorTable__roak.md)

## Links

- Repo: https://github.com/KeServiceDescriptorTable/roak
- README tag: `[NtQueryAuxiliaryCounterFrequency]`

## Related

[[r69-driver]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[driver-read-write]] · [[wnf-driver-meme]] · [[driver-detect-nullshit]]
