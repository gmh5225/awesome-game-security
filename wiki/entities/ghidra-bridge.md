---
title: ghidra-bridge
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/justfoxing__ghidra_bridge.md
updated: 2026-08-02
confidence: medium
---

# ghidra-bridge

Python 3 bridge to Ghidra's Python scripting API. Ghidra's built-in scripting runs on Jython, which is aging and limits modern Python tooling; this project exposes Ghidra automation to CPython 3 clients so game-security researchers and reverse engineers can drive decompilation, symbols, and scripts from external workflows. (source: wiki/sources/descriptions/justfoxing__ghidra_bridge.md)

Foundation layer for Ghidra plugin and LLM pipelines such as [[gpt-wpre]] (decomp/call-graph extract) and complements agent-facing paths like [[ghidra-headless-mcp]]; pair scripted output with [[research-rigor]] when acting on automated summaries.

## Links

- Repo: https://github.com/justfoxing/ghidra_bridge

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[gpt-wpre]] · [[ghidra-headless-mcp]] · [[ghidrametrics]] · [[threatresearch]] · [[gba-ghidra-loader]] · [[research-rigor]]
