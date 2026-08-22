---
title: DecBench
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/Noelo-Lab__decbench.md
updated: 2026-08-22
confidence: medium
---

# DecBench

**Python benchmarking suite** for measuring how well **decompilers** recover source from compiled **C binaries**. Runs a three-stage pipeline: compile projects at multiple optimization levels, decompile with pluggable backends, then score output. Supports traditional backends including angr, [[ghidra]], IDA, Binary Ninja, r2dec, and dewolf, plus optional **LLM or coding-agent** backends. Core metrics: **CFG graph-edit distance** (structural correctness), **type matching** against DWARF ground truth, and **recompilation byte-match** (assembly similarity). Corpora span Debian-style packages, cross-compiled embedded and RTOS firmware, and carefully sandboxed malware samples. Targets reverse engineers, binary-analysis researchers, and anyone comparing or improving decompiler quality—including game-security RE where lifted pseudocode quality affects AC module analysis. (source: wiki/sources/descriptions/Noelo-Lab__decbench.md)

Complements agent backdoor benchmarks such as [[binaryaudit]] with quantitative decompiler recovery scores, and pairs naturally with LLM-native decompilers like [[kuna]] when evaluating iterative agent refinement.

## Links

- Repo: https://github.com/Noelo-Lab/decbench
- Site: https://decbench.com

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[kuna]] · [[binaryaudit]] · [[retdec]] · [[kong]] · [[ghidra-mcp]] · [[angrop]]
