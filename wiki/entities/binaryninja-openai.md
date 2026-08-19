---
title: binaryninja-openai
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/WhatTheFuzz__binaryninja-openai.md
updated: 2026-08-19
confidence: medium
---

# binaryninja-openai

Binary Ninja plugin that connects decompiler views to OpenAI models for interactive analysis assistance. Python implementation reads selected functions from HLIL or pseudo-C, summarizes what they do, and can propose variable renames directly in the analysis view. Integrates with Binary Ninja plugin settings and API key management for cloud-model triage and annotation during binary security research. (source: wiki/sources/descriptions/WhatTheFuzz__binaryninja-openai.md)

Cloud OpenAI counterpart to local rename workflows via [[binaryninja-ollama]]; BN-side peer to [[ghidra-openai]] and in-disassembler agents such as [[rikugan]]. For agent transports rather than in-UI assistants, see [[binary-ninja-mcp]] and [[bn]]. Verify model output against disassembly/decompilation per [[research-rigor]].

## Links

- Repo: https://github.com/WhatTheFuzz/binaryninja-openai

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binaryninja-ollama]] · [[ghidra-openai]] · [[binary-ninja-mcp]] · [[bn]] · [[rikugan]] · [[ida-gepetto]] · [[research-rigor]]
