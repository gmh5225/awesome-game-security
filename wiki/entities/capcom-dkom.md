---
title: CapcomDKOM
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__CapcomDKOM.md
updated: 2026-08-14
confidence: medium
---

# CapcomDKOM

Direct Kernel Object Manipulation (DKOM) tool that leverages the historically abused **`Capcom.sys`** driver for ring-0 code execution. Abuses the Capcom IOCTL **`0xAA013044`** to run kernel shellcode payloads, resolving kernel APIs via **`MmGetSystemRoutineAddress`**. (source: wiki/sources/descriptions/gmh5225__CapcomDKOM.md)

Sits in the same **`Capcom.sys`** BYOVD lane as arbitrary kernel-execution PoCs such as [[dolboeb-executor]] and unsigned-driver loaders such as [[capcomlib]], but focuses on **DKOM** (kernel object manipulation) rather than generic shellcode dispatch or PE manual mapping.

## Links

- Repo: https://github.com/gmh5225/CapcomDKOM

## Related

[[byovd]] · [[dolboeb-executor]] · [[capcomlib]] · [[fortnite-external-4]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
