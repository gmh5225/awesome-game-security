---
title: KDU
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/hfiref0x__KDU.md
updated: 2026-08-05
confidence: medium
---

# KDU

**Kernel Driver Utility** — a Windows C tool for loading unsigned kernel drivers via [[byovd]]. An extensible **provider system** supports dozens of known vulnerable signed drivers (Intel, ASUS, MSI, Gigabyte, and others) to obtain arbitrary kernel read/write or code execution, then maps a custom unsigned driver into kernel memory. The codebase automates **DSE bypass**, driver mapping, and cleanup. Aimed at security researchers studying driver signature enforcement bypass and the BYOVD attack surface. (source: wiki/sources/descriptions/hfiref0x__KDU.md)

Canonical multi-provider mapper in the same lane as [[saturn-mapper]], [[kdmapper-rs]], and [[known-driver-mappers]]; downstream tools such as [[ksdumper-11]] load custom drivers through KDU’s vulnerable-driver chain. Same author ecosystem as [[upgdsed]] (runtime PatchGuard + DSE disable).

## Links

- Repo: https://github.com/hfiref0x/KDU

## Related

[[byovd]] · [[saturn-mapper]] · [[kdmapper-rs]] · [[known-driver-mappers]] · [[gdrv-loader-v2]] · [[ksdumper-11]] · [[upgdsed]] · [[loldrivers]] · [[msft-driverblocklist]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
