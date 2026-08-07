---
title: BinExport
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/google__binexport.md
updated: 2026-08-07
confidence: medium
---

# BinExport

**BinExport** is Google's C++ binary-analysis data exporter plugin for **IDA Pro**, **Ghidra**, and **Binary Ninja**. It serializes disassembly into Protocol Buffer format—functions, basic blocks, instructions, cross-references, and call graphs—for consumption by **BinDiff** and other external diffing or automated-analysis tools. The plugin provides a standardized intermediate representation for cross-tool binary comparison workflows aimed at reverse engineers and vulnerability researchers tracking code changes across builds. (source: wiki/sources/descriptions/google__binexport.md)

Upstream export step in the Google BinDiff pipeline; open-source diffing alternatives such as [[diaphora]] and [[turbodiff]] operate inside IDA without the protobuf interchange layer.

## Links

- Repo: https://github.com/google/binexport (README tag: BinDiff)

## Related

[[overviews/reverse-engineering]] · [[diaphora]] · [[turbodiff]] · [[cognitor]] · [[genpatch]]
