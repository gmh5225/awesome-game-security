---
title: ida-pro-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__ida-pro-mcp.md
updated: 2026-07-29
confidence: medium
---

# ida-pro-mcp

MCP server for IDA Pro that exposes the full IDAPython API surface to AI agents, enabling automated binary-analysis workflows: function renaming, type annotation, cross-reference queries, decompilation, and struct creation. Ships with comprehensive IDAPython documentation, an installable IDA plugin, and a test framework for validating MCP tool behavior. (source: wiki/sources/descriptions/mrexodia__ida-pro-mcp.md)

Broader agent bridge than curated disasm/decompile/xrefs-only IDA MCP plugins such as [[ida-mcp-server-plugin]]—this path targets whole IDAPython automation rather than a fixed tool subset. Peers with multi-instance IDA MCP servers [[iida-mcp]] and [[ida-multi-mcp]] (parallel routing + BCSD cross-binary similarity), JSON CLI [[idac]] (not MCP), and Ghidra-side agent RE via [[ghidra-headless-mcp]].

## Links

- Repo: https://github.com/mrexodia/ida-pro-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-nexus-docker]] · [[ida-mcp-server-plugin]] · [[iida-mcp]] · [[ida-multi-mcp]] · [[idac]] · [[ghidra-headless-mcp]] · [[aida]] · [[ida-assistant]]
