---
title: valthrun-uefi-mapper
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Valthrun__valthrun-uefi-mapper.md
updated: 2026-08-20
confidence: medium
---

# valthrun-uefi-mapper

**valthrun-uefi-mapper** is a **UEFI-based mapper** that loads an unsigned game driver during the boot path, before normal operating-system driver initialization. It is written in **Rust** for the **x86_64 UEFI** target and ships scripts to build **bootable ISO images** for USB deployment. The loader runs early enough to experiment with boot-time driver mapping and stealth-oriented Windows security workflows that skip standard kernel driver-load telemetry. (source: wiki/sources/descriptions/Valthrun__valthrun-uefi-mapper.md)

README category: `[EFI Manual Map]`.

## Links

- Repo: https://github.com/Valthrun/valthrun-uefi-mapper

## Related

[[sumap]] · [[xigmapper]] · [[uefi-bootloader]] · [[luaboot]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
