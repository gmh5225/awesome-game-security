---
title: ida-multi-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MeroZemory__ida-multi-mcp.md
updated: 2026-08-23
confidence: medium
---

# ida-multi-mcp

Python MCP server for IDA Pro 8.5+ that routes AI agent requests to multiple running disassembler instances from one connection—auto-discovering GUI and idalib sessions, dispatching analysis calls in parallel, and exposing MCP tools for decompilation, memory reads, patching, and binary survey. Standout **BCSD** cross-binary function similarity search combines instruction MinHash, import/string anchors, control-flow structure, and optional local jTrans neural embeddings to match stripped or recompiled code across related samples. Integrates with Claude Code, Cursor, and other MCP clients for malware and game-security workflows comparing droppers, payloads, patches, and variants. (source: wiki/sources/descriptions/MeroZemory__ida-multi-mcp.md)

Multi-instance peer to [[iida-mcp]] and [[tenrec]]; broader single-instance IDAPython automation via [[ida-pro-mcp]]; collection-oriented IDA MCP tooling via [[binary-analysis-mcps]].

## Links

- Repo: https://github.com/MeroZemory/ida-multi-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[iida-mcp]] · [[ida-pro-mcp]] · [[tenrec]] · [[binary-analysis-mcps]] · [[mcrit-plugin]] · [[diaphora]]
