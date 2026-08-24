---
title: bndb2pat
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/joren485__bndb2pat.md
updated: 2026-08-14
confidence: medium
---

# bndb2pat

Binary Ninja plugin that exports IDA Pro FLIRT `.pat` pattern files from binaries opened in Binary Ninja. Python implementation walks functions via Binary Ninja low-level IL, emitting byte masks with wildcard masking for variable operands, CRC16 checksums, and public/named symbol references in FLIRT format. Resulting `.pat` files feed FLAIR tools such as `sigmake` to build `.sig` signature libraries for IDA Pro. Inspired by Mandiant FLARE's idb2pat and Kaspersky's [[hrtng]]; bridges signature authoring between Binary Ninja analysis and IDA FLIRT workflows. (source: wiki/sources/descriptions/joren485__bndb2pat.md)

Unlike in-IDA signature makers ([[ida-sigmaker]], [[sigmakerex]], [[ida-pro-sigmaker]]) that emit runtime scan patterns, bndb2pat targets FLIRT library generation for stripped-binary function identification—closer to prebuilt FLIRT packs such as [[sig-database]].

## Workflow

1. Analyze binary in Binary Ninja; run bndb2pat to emit `.pat` patterns per function.
2. Process patterns with FLAIR (`sigmake`) into `.sig` libraries.
3. Load `.sig` libraries in IDA Pro to auto-name matching functions in stripped game clients or malware samples.

## Links

- Repo: https://github.com/joren485/bndb2pat

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-sigmaker]] · [[sigmakerex]] · [[ida-pro-sigmaker]] · [[sig-database]] · [[hyara]] · [[idenlib]]
