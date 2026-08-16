---
title: radare2-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dnakov__radare2-mcp.md
updated: 2026-08-16
confidence: medium
---

# radare2-mcp

Model Context Protocol (MCP) server written in C that exposes radare2 binary analysis to AI agents via r2pipe — disassembly, decompilation, cross-references, and general binary analysis. Supports CLI and plugin modes with stdin/stdout communication; configurable sandboxing, readonly mode, and fine-grained tool restrictions for security researchers integrating radare2 into AI-assisted reverse-engineering workflows. (source: wiki/sources/descriptions/dnakov__radare2-mcp.md)

Peers with IDA-side agent RE via [[ida-pro-mcp]] / [[iida-mcp]] / [[ida-mcp-server-plugin]], Ghidra MCP via [[ghidra-headless-mcp]] / [[ghidrassist-mcp]], and Binary Ninja MCP via [[binary-ninja-mcp]]. Complements in-r2 LLM assistants such as [[r2ai]] and the official GUI [[iaito]].

## Links

- Repo: https://github.com/dnakov/radare2-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[r2ai]] · [[iaito]] · [[binary-ninja-mcp]] · [[ida-pro-mcp]] · [[ghidra-headless-mcp]]
