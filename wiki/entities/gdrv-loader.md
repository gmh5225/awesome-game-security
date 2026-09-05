---
title: gdrv-loader
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__gdrv-loader.md
updated: 2026-08-08
confidence: medium
---

# gdrv-loader

Windows tool that loads unsigned kernel drivers by exploiting Gigabyte's signed vulnerable **`gdrv64.sys`** driver. The manual-mapping pipeline uses gdrv's arbitrary memory read/write IOCTLs to map a custom driver into kernel memory, bypassing Driver Signature Enforcement (DSE) through [[byovd]]. Aimed at kernel researchers studying Gigabyte driver exploitation and DSE bypass. (source: wiki/sources/descriptions/gmh5225__gdrv-loader.md)

Complements [[gdrv-loader-v2]] (alternate `gdrv.sys` loader implementation), [[gdrv-loader-updated]] (Win10/11 updated loader), multi-provider mappers such as [[kdu]], and Gigabyte-family tooling in [[loldrivers]] / [[msft-driverblocklist]] blocklist research.

## Links

- Repo: https://github.com/gmh5225/gdrv-loader/tree/1909_mitigation

## Related

[[byovd]] · [[gdrv-loader-v2]] · [[gdrv-loader-updated]] · [[kdu]] · [[saturn-mapper]] · [[known-driver-mappers]] · [[loldrivers]] · [[msft-driverblocklist]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
