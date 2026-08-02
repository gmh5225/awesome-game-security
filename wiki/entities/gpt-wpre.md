---
title: gpt-wpre
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/moyix__gpt-wpre.md
updated: 2026-07-29
confidence: medium
---

# gpt-wpre

Python whole-program reverse-engineering pipeline: pulls Ghidra decompilation and call graphs through [[ghidra-bridge]], then recursively summarizes functions bottom-up with GPT-3 (`text-davinci-003`). Callee functions are summarized first; those natural-language dependency summaries become context when summarizing callers—compressing cross-function detail to fit LLM context limits and yield readable program-level analysis. (source: wiki/sources/descriptions/moyix__gpt-wpre.md)

Early ChatGPT-era Ghidra+LLM batch workflow—complements interactive agent bridges such as [[ghidra-headless-mcp]] and in-IDA LLM assistants like [[ida-llm-explainer]]; verify summaries against disassembly/decompilation per [[research-rigor]].

## Links

- Repo: https://github.com/moyix/gpt-wpre

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra-bridge]] · [[ghidra-headless-mcp]] · [[ghidrametrics]] · [[ida-llm-explainer]] · [[aida]] · [[r2ai]] · [[research-rigor]]
