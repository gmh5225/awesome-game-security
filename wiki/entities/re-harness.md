---
title: re-harness
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/thatskriptkid__re-harness.md
updated: 2026-08-10
confidence: medium
---

# re-harness

**RE-harness** is a Windows PE static-analysis harness implemented as an OpenCode plugin that gives large language models structured, read-only access to IDA Pro and IDASQL for evidence-driven reverse engineering. (source: wiki/sources/descriptions/thatskriptkid__re-harness.md)

Written primarily in Python with a TypeScript OpenCode plugin, it targets Qwen 27B/35B models and orchestrates IDA database preparation, pseudocode extraction, and controlled analysis workflows without executing untrusted samples. When Hex-Rays decompilation fails or produces oversized output, the harness lifts individual functions through a bundled NeverD and LLVM pipeline, normalizes stack-relative addresses, optimizes with LLVM O3, and redecompiles simplified code back in IDA while preserving verified API and call-site names. FLIRT signature databases, Windows API semantics data, and configurable OpenRouter or llama.cpp provider settings are integrated.

Aimed at reverse engineers and game security researchers who need LLM-assisted static analysis of Windows executables with auditable, tool-grounded outputs rather than speculative guesses. Pair model conclusions with disassembly evidence per [[research-rigor]].

## Links

- Repo: https://github.com/thatskriptkid/re-harness

## Related

[[overviews/reverse-engineering]] · [[ida-bridge]] · [[daila]] · [[aida]] · [[ida-llm-explainer]] · [[ida2llvm]] · [[research-rigor]] · [[rev-tools-setup]]
