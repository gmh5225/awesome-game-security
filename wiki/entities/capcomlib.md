---
title: CapcomLib
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__CapcomLib.md
updated: 2026-08-14
confidence: medium
---

# CapcomLib

Reflexive kernel driver loader that bypasses Windows Driver Signature Enforcement (DSE) using a custom PE loader. Exploits the historically abused **`Capcom.sys`** rootkit by default to load unsigned drivers, with a modular architecture supporting other known exploitable signed drivers as alternate [[byovd]] backends. (source: wiki/sources/descriptions/gmh5225__CapcomLib.md)

Sits in the same unsigned-driver mapper lane as multi-provider tooling such as [[kdu]] and [[kdp-compatible-driver-loader]], and complements Capcom-specific arbitrary-kernel-execution PoCs such as [[dolboeb-executor]]. Downstream cheat stacks such as [[fortnite-external-4]] illustrate legacy Capcom-mapper + kernel-comm external patterns.

## Links

- Repo: https://github.com/gmh5225/CapcomLib

## Related

[[byovd]] · [[dolboeb-executor]] · [[kdu]] · [[kdp-compatible-driver-loader]] · [[pdfwkrnl-mapper]] · [[dse-hook]] · [[dse-patcher-2]] · [[disabledse]] · [[fortnite-external-4]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
