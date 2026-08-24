---
title: hrtng
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/KasperskyLab__hrtng.md
updated: 2026-08-24
confidence: medium
---

# hrtng

**hrtng** (KasperskyLab) is a **C++ IDA Pro plugin** that extends the **Hex-Rays decompiler** with a broad set of reverse-engineering helpers for day-to-day analysis. Built against the IDA SDK with supporting scripts, it automates variable renaming and auto-comments, supports interactive pseudocode recasting, string and data decryption, and type or structure building. For obfuscated binaries it adds control-flow unflattening, de-inlining, API-hash scanning, microcode signatures, and virtual or indirect call assistance, plus UI and patching utilities. Primary audience: reverse engineers and malware analysts speeding up IDA and Hex-Rays workflows on complex or protected code. (source: wiki/sources/descriptions/KasperskyLab__hrtng.md)

Complements other Hex-Rays microcode and deobfuscation plugins such as [[hex-rays-deob]], [[d810-ng]], and [[genmc]], and pseudocode polish utilities such as [[ida-wpp-remover]] and [[happyida]]. Referenced as inspiration for FLIRT pattern export in [[bndb2pat]].

## Links

- Repo: https://github.com/KasperskyLab/hrtng

## Related

[[hex-rays-deob]] · [[d810-ng]] · [[genmc]] · [[ida-wpp-remover]] · [[happyida]] · [[bndb2pat]] · [[control-flow-flattening]] · [[obfuscation-analysis]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
