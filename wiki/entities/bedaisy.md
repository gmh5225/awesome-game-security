---
title: BEDaisy
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Aki2k__BEDaisy.md
updated: 2026-09-03
confidence: medium
---

# BEDaisy

Reverse-engineering proof of concept (Aki2k) focused on BattlEye's **`BEDaisy.sys`** kernel anti-cheat driver. C++ sample demonstrating interception via **image-load callbacks** and **IAT hooking** around **`MmGetSystemRoutineAddress`**, with discussion of taking control over subsequent anti-cheat execution paths and **APC-related** experimentation. Intended for researchers studying kernel anti-cheat behavior, bypass surfaces, and defensive hardening opportunities—not a polished end-user bypass tool. (source: wiki/sources/descriptions/Aki2k__BEDaisy.md)

Complements defensive BEDaisy catalogs such as [[bedaisy-reversal]] and [[battleye-re]] with an offensive interception PoC lane; pairs with [[goodeye]] (APC instrumentation) and [[bedaisy-bypass]] (report-path suppression) for end-to-end BEDaisy kernel study.

## Links

- Repo: https://github.com/Aki2k/BEDaisy

## Related

[[battleye]] · [[bedaisy-reversal]] · [[bedaisy-bypass]] · [[goodeye]] · [[battleye-re]] · [[kernel-callbacks]] · [[apc-research]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
