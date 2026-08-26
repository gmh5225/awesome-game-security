---
title: Ghidra Obfuscation Detection
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Deatty__Ghidra-Obfuscation-Detection.md
updated: 2026-08-26
confidence: medium
---

# Ghidra Obfuscation Detection

Ghidra script that spots potentially obfuscated or unusually complex functions by applying heuristic feature extraction to function bodies. Analysts can quickly prioritize suspicious code regions during reverse engineering sessions. Implemented in Java for direct use inside the Ghidra scripting environment; lightweight to integrate into existing analysis workflows. Primarily aimed at malware and game binary researchers who need faster triage of protected code. (source: wiki/sources/descriptions/Deatty__Ghidra-Obfuscation-Detection.md)

Ghidra-native obfuscation triage—complements Binary Ninja heuristics in [[obfuscation-detection]] and complexity metrics from [[ghidrametrics]] before manual deobfuscation work.

## Links

- Repo: https://github.com/Deatty/Ghidra-Obfuscation-Detection

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[obfuscation-detection]] · [[obfuscation-analysis]] · [[control-flow-flattening]] · [[ghidra]] · [[ghidrametrics]] · [[xrefgen]]
