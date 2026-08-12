---
title: KDP-compatible-driver-loader
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__KDP-compatible-driver-loader.md
updated: 2026-08-12
confidence: medium
---

# KDP-compatible-driver-loader

Kernel unsigned driver loader compatible with **Kernel Data Protection (KDP)** on Windows 10. Leverages Gigabyte **`gdrv.sys`** write primitives from the [[byovd]] lane to bypass Driver Signature Enforcement (DSE) by patching **`SeCiCallbacks`** — initialized by `CiInitialize` and used by `SeValidateImageHeader` to call `CiValidateImageHeader`. (source: wiki/sources/descriptions/gmh5225__KDP-compatible-driver-loader.md)

Complements [[gdrv-loader]] / [[gdrv-loader-v2]] (generic `gdrv.sys` manual-map loaders) and `SeCiCallbacks`-focused DSE research such as [[kernel-research-kit]] and [[kvc]] in the same unsigned-load lane.

## Links

- Repo: https://github.com/gmh5225/KDP-compatible-driver-loader

## Related

[[byovd]] · [[gdrv-loader]] · [[gdrv-loader-v2]] · [[gdriver-lib]] · [[kernel-pool-scanning]] · [[kernel-research-kit]] · [[kvc]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
