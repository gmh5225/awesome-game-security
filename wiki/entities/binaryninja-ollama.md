---
title: binaryninja-ollama
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ahaggard2013__binaryninja-ollama.md
updated: 2026-08-19
confidence: medium
---

# binaryninja-ollama

Binary Ninja plugin that uses a locally hosted Ollama server to rename functions and variables with LLM assistance. Python implementation integrates directly with HLIL workflows for bulk renaming and targeted renaming actions. Configurable server, port, and model settings let analysts run semantic labeling offline with locally available models — without sending binaries or code context to third-party cloud services. (source: wiki/sources/descriptions/ahaggard2013__binaryninja-ollama.md)

Complements cloud OpenAI triage via [[binaryninja-openai]], broader agent-RE transports such as [[binary-ninja-mcp]] and [[bn]], and in-disassembler LLM assistants such as [[rikugan]]. For IDA-side local rename/explain plugins, see [[ida-gepetto]] and [[ida-llm-explainer]].

## Links

- Repo: https://github.com/ahaggard2013/binaryninja-ollama

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binaryninja-openai]] · [[binary-ninja-mcp]] · [[bn]] · [[rikugan]] · [[ida-gepetto]] · [[ida-llm-explainer]]
