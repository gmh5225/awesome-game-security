---
title: ida-mcp-server
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MxIris-Reverse-Engineering__ida-mcp-server.md
updated: 2026-08-22
confidence: medium
---

# ida-mcp-server

**MCP for IDA Pro** — Python Model Context Protocol server that bridges LLM tooling with IDA Pro analysis data. Ships as a standalone server package plus an IDA plugin for bidirectional communication, exposing automation-oriented capabilities to query disassembly context, run analysis workflows, and integrate with MCP-compatible clients. Targets reverse engineers who want AI-assisted interaction with live IDA databases. (source: wiki/sources/descriptions/MxIris-Reverse-Engineering__ida-mcp-server.md)

Peers with other IDA MCP bridges such as [[ida-mcp-server-plugin]] (disasm/decompile/xrefs/types plugin), [[ida-pro-mcp]] (full IDAPython MCP), [[headless-ida-mcp-server]] (headless function/variable tools), [[mcp-server-idapro]] (AI-assistant bridge), and [[ida-mcp-rs]] (Rust headless MCP).

## Links

- Repo: https://github.com/MxIris-Reverse-Engineering/ida-mcp-server

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-mcp-server-plugin]] · [[ida-pro-mcp]] · [[headless-ida-mcp-server]] · [[mcp-server-idapro]] · [[ida-mcp-rs]] · [[binary-analysis-mcps]]
