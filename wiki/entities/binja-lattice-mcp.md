---
title: binja-lattice-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Invoke-RE__binja-lattice-mcp.md
updated: 2026-08-24
confidence: medium
---

# binja-lattice-mcp

**BinjaLattice** — Binary Ninja plugin (**Invoke-RE**) that bridges live analysis sessions to external MCP servers over an authenticated HTTP interface. Python implementation with token-based authentication, optional TLS, and a REST-style API for secure tool communication. Exports disassembly and pseudocode context from open databases and supports controlled edits such as renaming functions and adding comments — aimed at reverse engineers who want AI or automation pipelines to interact with live Binary Ninja databases safely. (source: wiki/sources/descriptions/Invoke-RE__binja-lattice-mcp.md)

HTTP-authenticated BN-side MCP bridge rather than a standalone MCP server: complements [[binary-ninja-mcp]] (fosdickio; Python MCP server exposing BN analysis to LLM clients) and CLI-oriented agent access via [[bn]]. Peers with IDA-side MCP bridges such as [[ida-pro-mcp]] and Ghidra MCP via [[ghidramcp]] / [[ghidra-headless-mcp]].

## Links

- Repo: https://github.com/Invoke-RE/binja-lattice-mcp (README: MCP for Binary_Ninja)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binary-ninja-mcp]] · [[bn]] · [[ida-pro-mcp]] · [[ghidramcp]] · [[binary-analysis-mcps]]
