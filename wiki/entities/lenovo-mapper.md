---
title: lenovo-mapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__lenovo_mapper.md
updated: 2026-08-08
confidence: medium
---

# lenovo-mapper

Driver mapper that loads unsigned kernel drivers via Lenovo's vulnerable **`LenovoDiagnosticsDriver.sys`**. The manual-mapping pipeline abuses the signed driver's memory-access IOCTLs to obtain kernel R/W primitives needed for PE section mapping without the normal signed-driver install path. Aimed at kernel researchers studying [[byovd]]-based driver mapping through Lenovo driver exploitation. (source: wiki/sources/descriptions/gmh5225__lenovo_mapper.md)

Complements other Lenovo OEM-driver research such as [[lenovo-exec]] (same **`LenovoDiagnosticsDriver.sys`**; IOCTL → arbitrary kernel code execution), [[phantomkiller]] (`BootRepair.sys` process kill), and [[lenovo-cve-2025-8061]] (`LnvMSRIO.sys` LPE); sits in the same driver-mapper lane as [[saturn-mapper]], [[kdu]], and [[nullmap]].

## Links

- Repo: https://github.com/gmh5225/lenovo_mapper

## Related

[[byovd]] · [[lenovo-exec]] · [[phantomkiller]] · [[lenovo-cve-2025-8061]] · [[saturn-mapper]] · [[kdu]] · [[nullmap]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
