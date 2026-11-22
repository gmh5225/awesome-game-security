---
title: ghidra-re
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Yultas__ghidra-re.md
updated: 2026-11-22
confidence: medium
---

# ghidra-re

Ghidra RE Workbench is a self-contained local reverse engineering plugin for Antigravity Desktop. A loopback Java daemon runs headless Ghidra on demand; a Node.js MCP server and workbench sidecar expose analysis to interactive Aux Pane UI and MCP agents. A per-binary offline SQLite index with FTS5 supports symbol, string, call-graph, and cached pseudocode search even when the JVM is stopped. Live sessions use a priority decompiler pool, CFG visualization, synchronized C and assembly views, and batch rename, retype, and comment operations. Requires Ghidra 12.2+, JDK 25+, and Node.js 26+; configurable RAM tiers control idle auto-unload and worker counts. (source: wiki/sources/descriptions/Yultas__ghidra-re.md)

Complements other Ghidra MCP bridges such as [[ghidra-headless-mcp]], [[ghidra-mcp]], and [[ghidramcp]] with an IDE-integrated workbench, offline FTS-backed index, and on-demand JVM lifecycle instead of a permanently resident Ghidra process.

## Links

- Repo: https://github.com/Yultas/ghidra-re

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-headless-mcp]] · [[ghidra-mcp]] · [[ghidramcp]] · [[ghidrassist-mcp]] · [[dsh-ghidra]] · [[ghidra-manager]]