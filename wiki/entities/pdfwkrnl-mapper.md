---
title: PdFwKrnlMapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__PdFwKrnlMapper.md
updated: 2026-08-11
confidence: medium
---

# PdFwKrnlMapper

Kernel **driver mapper** that exploits the BitLocker **`PdFwKrnl.sys`** signed-driver vulnerability to bypass Driver Signature Enforcement (DSE) and map unsigned drivers into kernel space. Patches **`SeValidateImageData`** / header validation paths rather than only loading arbitrary code via IOCTL — a mapper-focused variant in the same backend lane as [[pdfwkrnl-exploit]]. (source: wiki/sources/descriptions/gmh5225__PdFwKrnlMapper.md)

## Links

- Repo: https://github.com/gmh5225/PdFwKrnlMapper

## Related

[[pdfwkrnl-exploit]] · [[byovd]] · [[known-driver-mappers]] · [[dse-hook]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
