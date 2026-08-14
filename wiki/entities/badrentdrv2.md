---
title: BadRentdrv2
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__BadRentdrv2.md
updated: 2026-08-14
confidence: medium
---

# BadRentdrv2

Exploits the signed vulnerable driver **`Rentdrv2.sys`** for kernel memory access on Windows. The project's user-mode code abuses Rentdrv2's insecure IOCTL interface to achieve arbitrary physical memory read/write—typical [[byovd]] primitives for unsigned driver mapping, kernel patching, or anti-cheat bypass. Aimed at BYOVD researchers studying Rentdrv2 driver exploitation. (source: wiki/sources/descriptions/gmh5225__BadRentdrv2.md)

## Links

- Repo: https://github.com/gmh5225/BadRentdrv2

## Related

[[byovd]] · [[physmem-drivers]] · [[qiomem]] · [[amd-ryzen-master-driver-v17-exploit]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
