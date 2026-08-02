---
title: GhidrAssist
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jtang613__GhidrAssist.md
updated: 2026-08-02
confidence: medium
---

# GhidrAssist

LLM extension for Ghidra that adds in-IDE AI assistance for reverse engineering. Connects to any OpenAI v1-compatible API—local models (Ollama, LM-Studio, Open-WebUI) or cloud providers (OpenAI, Anthropic, Azure). Targets game-security researchers and reverse engineers studying offensive techniques in the cheat / Ghidra Plugins lane. (source: wiki/sources/descriptions/jtang613__GhidrAssist.md)

Ghidra-side peer to in-IDA [[idassist]] and agent bridges like [[ghidrassist-mcp]] / [[ghidra-headless-mcp]]—this path embeds LLM chat/explain workflows inside Ghidra rather than exposing analysis through an external MCP server. Same maintainer as [[ghidrassist-mcp]], [[gdb-mcp]], and [[idassist]].

## Links

- Repo: https://github.com/jtang613/GhidrAssist
- Related MCP variant: [[ghidrassist-mcp]] (https://github.com/jtang613/GhidrAssistMCP)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidrassist-mcp]] · [[ghidra-headless-mcp]] · [[ghidra-bridge]] · [[idassist]] · [[ida-assistant]] · [[research-rigor]]
