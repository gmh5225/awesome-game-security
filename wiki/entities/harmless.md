---
title: hARMless
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/litemars__hARMless.md
updated: 2026-07-31
confidence: medium
---

# hARMless

ARM64/AArch64 ELF packer and in-memory loader for Linux that encrypts executables, generates custom stub code, and performs fileless execution via `memfd_create` for evasion. Aimed at anti-cheat engineers and defensive researchers studying packed Linux/ARM64 clients under Anti Cheat → Binary Packer / `[ELF]`, rather than shipping as an AC product. (source: wiki/sources/descriptions/litemars__hARMless.md)

Useful as an ARM64 Linux packer reference alongside [[elfpacker]], [[woody-woodpacker]], and [[m0dern-p4cker]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/litemars/hARMless

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[elfpacker]] · [[woody-woodpacker]] · [[m0dern-p4cker]] · [[elfuck]] · [[embuche]]
