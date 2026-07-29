---
title: ghidra-headless-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrphrazer__ghidra-headless-mcp.md
updated: 2026-07-29
confidence: medium
---

# ghidra-headless-mcp

MCP server that drives headless Ghidra instances for AI-assisted reverse engineering. Exposes 40+ tools across disassembly, decompilation, cross-references, symbol/type management, and scripting categories. Includes a fake backend for offline testing, a standalone CLI for non-MCP usage, fuzz-testing support, and JSON-RPC over stdio integration with Claude, Cursor, and Copilot agents. (source: wiki/sources/descriptions/mrphrazer__ghidra-headless-mcp.md)

Ghidra-side peer to IDA MCP bridges such as [[ida-mcp-server-plugin]] and [[iida-mcp]]—this path targets headless Ghidra rather than a live IDA GUI/IDB. Also complements Ghidra batch/metrics tooling like [[ghidrametrics]] and agent PoC workflows such as [[pocsmith]] that cite Ghidra MCP hooks.

## Links

- Repo: https://github.com/mrphrazer/ghidra-headless-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-mcp-server-plugin]] · [[iida-mcp]] · [[ghidrametrics]] · [[binaryninja-pcode]] · [[obfuscation-detection]] · [[obfuscation-analysis]] · [[pocsmith]]
