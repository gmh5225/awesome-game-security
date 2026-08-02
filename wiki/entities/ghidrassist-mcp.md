---
title: ghidrassist-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jtang613__GhidrAssistMCP.md
updated: 2026-08-02
confidence: medium
---

# ghidrassist-mcp

Ghidra extension implementing the Model Context Protocol (MCP) so external AI assistants, automated analysis tools, and custom scripts can interact with Ghidra's analysis capabilities. Targets game developers, reverse engineers, and tooling builders in the Game Develop / MCP server lane. (source: wiki/sources/descriptions/jtang613__GhidrAssistMCP.md)

Ghidra-side peer to [[ghidra-headless-mcp]] (headless 40+ tool server) and IDA MCP bridges such as [[ida-pro-mcp]] / [[ida-mcp-server-plugin]]—this path exposes Ghidra through MCP for agent-driven RE rather than a standalone headless CLI. Complements in-Ghidra LLM panel [[ghidrassist]] (OpenAI v1-compatible local/cloud providers). Same maintainer as [[gdb-mcp]] and in-IDA [[idassist]].

## Links

- Repo: https://github.com/jtang613/GhidrAssistMCP (README tag: MCP for Ghidra)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidrassist]] · [[ghidra-headless-mcp]] · [[ghidra-bridge]] · [[ida-pro-mcp]] · [[gdb-mcp]] · [[idassist]]
