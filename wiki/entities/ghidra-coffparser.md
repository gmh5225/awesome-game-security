---
title: Ghidra COFFParser
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/MEhrn00__Ghidra_COFFParser.md
updated: 2026-08-23
confidence: medium
---

# Ghidra COFFParser

Python **Ghidra analysis script** that performs **comprehensive COFF parsing** beyond Ghidra's default loader behavior. Maps **headers**, **symbol data**, **string tables**, and **relocation entries** with added type information, then **applies relocations** and **cross-references** to improve analysis context inside the disassembler. Primary use case is reverse engineering **COFF object files** (`.obj`) with richer structural visibility in Ghidra—useful when inspecting compiler output, relink/patch workflows, or object-level artifacts from protected binaries. (source: wiki/sources/descriptions/MEhrn00__Ghidra_COFFParser.md)

Complements IDA-side COFF round-tripping via [[ida2obj]] and Authenticode/PE-COFF tooling such as [[unsign]] when the analysis target is an object file rather than a linked PE image.

## Links

- Repo: https://github.com/MEhrn00/Ghidra_COFFParser

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[ida2obj]] · [[ghidra-scripts]] · [[pagalaxylab-ghidra-scripts]]
