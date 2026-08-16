---
title: PEReconstruct
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/diabloidyobane__PEReconstruct.md
updated: 2026-08-16
confidence: medium
---

# PEReconstruct

Python toolkit for **reconstructing manually-mapped PE images** from process memory: deep PE scanning, contiguous memory dumping, headerless PE rebuilding, hook analysis, and export table resolution. Pure-stdlib Python with **no driver or debugger** required—aimed at recovering and statically analyzing manually-mapped DLLs whose PE headers were wiped at runtime. (source: wiki/sources/descriptions/diabloidyobane__PEReconstruct.md)

Sits beside [[pe-sieve]] and [[league-dumper]] in the injection dump/reconstruction lane—headerless manual-map recovery for IDA/Ghidra static RE rather than live detection or title-specific encrypted-module dumps.

## Links

- Repo: https://github.com/diabloidyobane/PEReconstruct

## Related

[[pe-sieve]] · [[xmalhunter]] · [[league-dumper]] · [[patch-finder]] · [[pe-bear]] · [[modexmap]] · [[wizard-loader]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
