---
title: ida-codex-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Iamgublin__ida-codex-mcp.md
updated: 2026-08-24
confidence: medium
---

# ida-codex-mcp

Python bridge that connects IDA Pro to MCP clients: an IDA plugin serves TCP JSON requests, and a local MCP stdio server re-exports tools and resources for LLM agents. Exposes function listing, call graphs, pseudocode and disassembly retrieval, xrefs, strings, memory reads, and renaming or typing helpers—targeting analysts who want to automate reverse engineering workflows from AI-assisted tooling. (source: wiki/sources/descriptions/Iamgublin__ida-codex-mcp.md)

Peers with other IDA MCP bridges such as [[ida-pro-mcp]] (full IDAPython surface), [[iida-mcp]] (large tool set + optional kernel driver), [[ida-mcp-server-plugin]] / [[ida-mcp-server]] (standalone MCP + IDA plugin), and headless [[ida-cli]] (idalib Rust/C++ MCP).

## Links

- Repo: https://github.com/Iamgublin/ida-codex-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-mcp]] · [[iida-mcp]] · [[ida-mcp-server-plugin]] · [[ida-mcp-server]] · [[ida-cli]] · [[ida-buddy]] · [[ghidra-mcp]]
