---
title: kdmapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/eddeeh__kdmapper.md
updated: 2026-08-16
confidence: medium
---

# kdmapper

Windows kernel **driver mapper** that loads unsigned drivers into kernel memory by exploiting Intel **`iqvw64e.sys`**, a vulnerable signed driver. The tool uses that driver's arbitrary physical memory read/write IOCTL to manually map a custom driver: allocating kernel pool memory, copying PE sections, resolving imports against `ntoskrnl`, processing relocations, and calling the driver entry point. The C++ tool automates the full mapping pipeline including vulnerable-driver deployment and cleanup. Aimed at kernel researchers and cheat developers studying manual driver mapping and **DSE bypass** techniques. (source: wiki/sources/descriptions/eddeeh__kdmapper.md)

Canonical reference implementation in the kdmapper-family lane alongside Rust ports such as [[kdmapper-rs]], Saturn-style mappers such as [[saturn-mapper]], signed-driver section overlay mappers such as [[sinmapper]], multi-provider [[kdu]], and the underlying [[cve-2015-2291]] / [[byovd]] primitive.

## Links

- Repo: https://github.com/eddeeh/kdmapper
- Backend: `iqvw64e.sys`

## Related

[[kdmapper-rs]] · [[saturn-mapper]] · [[sinmapper]] · [[kdu]] · [[cve-2015-2291]] · [[byovd]] · [[known-driver-mappers]] · [[revert-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
