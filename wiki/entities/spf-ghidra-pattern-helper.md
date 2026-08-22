---
title: spf-ghidra-pattern-helper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/TrackAndTruckDevs__SPF_GhidraPatternHelper.md
updated: 2026-08-22
confidence: medium
---

# spf-ghidra-pattern-helper

Java-based Ghidra script with a graphical **Pattern Generator** and **Pattern Finder** interface for generating and searching byte signatures inside a loaded binary. Selected instruction sequences become SPF-style template patterns, masked hex signatures, extended range-based patterns, and raw bytes compatible with the C++ **PatternFinder** in SPF-Framework. (source: wiki/sources/descriptions/TrackAndTruckDevs__SPF_GhidraPatternHelper.md)

The built-in **PatternEngine** supports wildcards, byte ranges, optional bytes, alternation, and automatic displacement masking, with optional auto-verification to check signature uniqueness. Targeted at reverse engineers and game mod developers prototyping signatures during plugin work for **American Truck Simulator** and **Euro Truck Simulator 2**.

Unlike [[binja-sigmaker]] or [[ida-pro-sigmaker]], which emit IDA-style wildcard patterns from disassembled functions, this tool integrates signature authoring and in-binary search inside Ghidra and aligns output with SPF-Framework runtime scanning syntax.

## Links

- Repo: https://github.com/TrackAndTruckDevs/SPF_GhidraPatternHelper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-scripts]] · [[binja-sigmaker]] · [[ida-pro-sigmaker]] · [[sigmakerex]] · [[hyara]] · [[patternsleuth]]
