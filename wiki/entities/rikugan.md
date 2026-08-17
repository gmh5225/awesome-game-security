---
title: Rikugan
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/buzzer-re__Rikugan.md
updated: 2026-08-17
confidence: medium
---

# Rikugan

Reverse-engineering AI agent plugin for **IDA Pro** and **Binary Ninja** that embeds multi-provider LLM support directly in the disassembler UI. Python plugin with a generator-based agentic loop (streaming, in-process tool orchestration, automatic error recovery, plan mode for multi-step workflows, and context management) so analysts stay inside the RE environment. Chat opens via **Ctrl+Shift+I**; supports cloud APIs and local **Ollama**. (source: wiki/sources/descriptions/buzzer-re__Rikugan.md)

Unlike external MCP bridges ([[ida-pro-mcp]], [[binary-ninja-mcp]]), Rikugan runs natively in-process with tool use tied to the open database. Complements other in-disassembler LLM assistants such as [[idassist]], [[aida]], and [[daila]], and buzzer-re's offline agent corpus exporter [[tocode]].

## Links

- Repo: https://github.com/buzzer-re/Rikugan

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idassist]] · [[aida]] · [[binary-ninja-mcp]] · [[ida-pro-mcp]] · [[tocode]] · [[research-rigor]]
