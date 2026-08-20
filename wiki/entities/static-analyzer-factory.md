---
title: static-analyzer-factory
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Static-Analyzer-Factory__static-analyzer-factory.md
updated: 2026-08-20
confidence: medium
---

# static-analyzer-factory

Rust-based static analysis framework for vulnerability detection in compiled binaries. Analyzes C/C++ via LLVM IR graphs with pointer/value-flow analysis, taint tracking (IFDS), abstract interpretation, points-to analysis, and call-graph construction. Exposes a Python SDK and CLI and exports SARIF/HTML reports for triage workflows. (source: wiki/sources/descriptions/Static-Analyzer-Factory__static-analyzer-factory.md)

Complements disassembler-integrated SAST such as [[ida-security-scanner]], kernel-driver rule engines such as [[cognitor]], and standalone static workbenches such as [[retract]] when batch LLVM IR–level analysis is needed outside IDA/Ghidra.

## Links

- Repo: https://github.com/Static-Analyzer-Factory/static-analyzer-factory

## Related

[[overviews/reverse-engineering]] · [[ida-security-scanner]] · [[cognitor]] · [[retract]] · [[packpeek]] · [[firmeye]]
