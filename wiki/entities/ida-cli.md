---
title: ida-cli
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cpkt9762__ida-cli.md
updated: 2026-08-16
confidence: medium
---

# ida-cli

**Headless IDA Pro MCP server** for AI-assisted binary analysis, powered by **idalib**. Implemented primarily in Rust and C/C++, it targets reverse engineering, plugin development, and modding workflows where LLM agents drive static analysis without a live IDA GUI session. (source: wiki/sources/descriptions/cpkt9762__ida-cli.md)

Sits in the same agent-RE lane as plugin-based IDA MCP servers ([[ida-pro-mcp]], [[iida-mcp]], [[ida-mcp-server-plugin]]) and headless MCP servers such as [[headless-ida-mcp-server]] and [[ida-mcp-rs]] (blacktop; Rust) but emphasizes a **headless idalib** deployment rather than in-UI plugins. Complements JSON CLI bridges such as [[idac]] and [[ida-bridge]] that expose IDAPython/SQL to agents over other transports.

## Links

- Repo: https://github.com/cpkt9762/ida-cli

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[headless-ida-mcp-server]] · [[ida-pro-mcp]] · [[iida-mcp]] · [[ida-mcp-server-plugin]] · [[idac]] · [[ida-bridge]] · [[solana-sbpf-rlib]]
