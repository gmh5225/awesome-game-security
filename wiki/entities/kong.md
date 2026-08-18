---
title: Kong
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/amruth-sn__kong.md
updated: 2026-08-18
confidence: medium
---

# Kong

**Agentic reverse engineer** — LLM-orchestrated binary RE via **in-process [[ghidra]]**, **call-graph analysis**, and **agentic deobfuscation**. Targets obfuscated binaries and expressions (including mixed boolean-arithmetic / MBA-style transforms) using algebraic simplification, pattern matching, or symbolic execution to recover simpler original forms. Aimed at reverse engineers and deobfuscation researchers working protected or MBA-obfuscated code. (source: wiki/sources/descriptions/amruth-sn__kong.md)

Complements Ghidra MCP bridges such as [[ghidra-mcp]] and [[ghidrassist-mcp]] by embedding LLM orchestration directly in Ghidra, and in-disassembler agent plugins such as [[rikugan]] by focusing on Ghidra-native call-graph–driven deobfuscation. For dedicated MBA simplifiers, see [[promba]], [[cobra]], and [[mbased]].

## Links

- Repo: https://github.com/amruth-sn/kong

## Related

[[overviews/reverse-engineering]] · [[mixed-boolean-arithmetic]] · [[ghidra]] · [[ghidra-mcp]] · [[ghidrassist]] · [[rikugan]] · [[promba]] · [[cobra]] · [[mbased]] · [[qsynthesis]]
