---
title: Binlex
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/c3rb3ru5d3d53c__binlex.md
updated: 2026-08-17
confidence: medium
---

# Binlex

C++ and Rust binary pattern extraction and genetic trait analysis tool. Disassembles PE, ELF, and raw binaries across multiple architectures to extract function-level byte patterns and instruction traits for malware similarity analysis, YARA rule generation, and threat-intelligence correlation. Outputs JSON for integration with analysis pipelines. Aimed at malware analysts, threat-intelligence researchers, and reverse engineers building detection signatures from binary artifacts. (source: wiki/sources/descriptions/c3rb3ru5d3d53c__binlex.md)

Standalone CLI pattern/trait extractor—not a disassembler plugin like [[hyara]] or [[bndb2pat]]. Complements similarity engines ([[mcrit-plugin]]) and static packer fingerprinting ([[packpeek]]) for signature-authoring workflows.

## Links

- Repo: https://github.com/c3rb3ru5d3d53c/binlex

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[hyara]] · [[bndb2pat]] · [[packpeek]] · [[mcrit-plugin]] · [[aho-corasick]]
