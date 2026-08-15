---
title: binary-ninja-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/fosdickio__binary_ninja_mcp.md
updated: 2026-08-15
confidence: medium
---

# binary-ninja-mcp

Model Context Protocol (MCP) server for Binary Ninja that exposes binary-analysis functionality to AI assistants. Python server lets LLM clients query disassembly, decompilation, cross-references, function lists, and type information from Binary Ninja databases — enabling AI-driven reverse-engineering workflows for MCP-compatible agents. (source: wiki/sources/descriptions/fosdickio__binary_ninja_mcp.md)

Peers with IDA-side agent RE via [[ida-pro-mcp]] / [[ida-mcp-server-plugin]] / [[iida-mcp]] and Ghidra MCP via [[ghidra-headless-mcp]] / [[ghidrassist-mcp]]. Complements Binary Ninja plugin work such as [[binaryninja-pcode]], [[ariadne]], and [[obfuscation-analysis]] inside the same disassembler.

## Links

- Repo: https://github.com/fosdickio/binary_ninja_mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-mcp]] · [[ghidra-headless-mcp]] · [[binaryninja-pcode]] · [[cheatengine-mcp-bridge]] · [[memmcp]]
