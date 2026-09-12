---
title: ida-pro-agent
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ackwrap__ida-pro-agent.md
updated: 2026-09-12
confidence: medium
---

# ida-pro-agent

IDA Pro 9.4 Windows plugin that brings AI-assisted binary analysis into disassembly workflows through a built-in AI Console and an MCP Gateway for external AI clients. Exposes IDA capabilities including function and cross-reference inspection, Hex-Rays pseudocode, bounded argument tracing across direct callers, guard-evidence extraction, and previewable IDB edits through ChangeSets (preview/apply/rollback). The x64 stack combines a C++ IDA plugin with Go and Python tooling, Qt 6.8.2, and support for OpenAI, Anthropic, and custom API providers over MCP. Aimed at reverse engineers and security researchers who want LLM-driven analysis inside IDA for malware review, anti-cheat research, and deep binary inspection. (source: wiki/sources/descriptions/ackwrap__ida-pro-agent.md)

Combines in-IDA LLM chat with an MCP bridge—similar lane to [[ida-pro-mcp]] and [[ida-codex-mcp]] (external agent automation) but with built-in console, bounded caller tracing, guard-evidence extraction, and ChangeSet-gated IDB edits rather than raw IDAPython exposure. Peers with rename/explain copilots [[binarylens]], [[aether]], and [[idassist]]; complements verification-focused [[reverify]] and export-without-MCP [[ida-no-mcp]] for agent-native RE pipelines.

## Links

- Repo: https://github.com/ackwrap/ida-pro-agent

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-mcp]] · [[ida-codex-mcp]] · [[binarylens]] · [[aether]] · [[idassist]] · [[reverify]] · [[ida-no-mcp]] · [[idaplugins]]
