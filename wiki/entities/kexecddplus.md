---
title: KexecDDPlus
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__KexecDDPlus.md
updated: 2026-08-12
confidence: medium
---

# KexecDDPlus

Enhanced fork of [[kexecdd]] that extends LSASS-based kernel code execution. Builds on **`KSecDD.sys` IOCTL exploitation** with added **DSE bypass** and **arbitrary kernel memory manipulation** — a signed Microsoft crypto/LSA helper path rather than a classic [[byovd]] vulnerable-driver load. (source: wiki/sources/descriptions/gmh5225__KexecDDPlus.md)

Sits in the trusted-process / LSASS research lane beside address-space extend mappers such as [[lsass-extend-mapper]] and PP/PPL→LSASS controllers such as [[kvc]], but here the primitive is abusing **`KSecDD.sys`** IOCTLs from an LSASS context for ring-0 execution and memory writes.

## Links

- Repo: https://github.com/gmh5225/KexecDDPlus

## Related

[[kexecdd]] · [[lsass-extend-mapper]] · [[kvc]] · [[dse-hook]] · [[pastdse]] · [[kslkatz]] · [[lsass-dump-that-lsass]] · [[byovd]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
