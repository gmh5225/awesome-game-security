---
title: papaw
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/dimkr__papaw.md
updated: 2026-08-16
confidence: medium
---

# papaw

Permissively-licensed Linux executable packer that compresses statically-linked ELF binaries with LZMA, zstd, or miniz, supports self-replacement on disk, and optionally adds basic anti-debugging. Targets smaller executables on resource-constrained devices via a simple `papawify` / `unpapawify` workflow. Mainly useful for security researchers studying ELF packing, anti-debugging techniques, and binary protection mechanisms on Linux under Anti Cheat → Binary Packer / `[ELF]` LZMA. (source: wiki/sources/descriptions/dimkr__papaw.md)

Useful as a Linux/ELF compression packer reference alongside [[elfuck]], [[elfpacker]], and [[elfcrypt]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/dimkr/papaw

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[elfuck]] · [[elfpacker]] · [[elfcrypt]] · [[woody-woodpacker]] · [[awesome-executable-packing]] · [[anti-debugging]]
