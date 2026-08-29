---
title: n0xis
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/LargoScript__n0xis.md
updated: 2026-08-29
confidence: medium
---

# n0xis

**n0xis** (LargoScript/n0xis) is a cross-platform **Rust** reverse-engineering toolkit for x64 Windows game binaries that unifies static disassembly/decompilation and live process memory analysis in one deterministic pipeline. It exposes a stable **CLI** and **MCP server** that return versioned **JSON artifacts** for human review or autonomous agent workflows. (source: wiki/sources/descriptions/LargoScript__n0xis.md)

## Capabilities

- **Static analysis:** CFG recovery, SSA optimization, type inference, pseudo-C decompilation, cross-references; PE/ELF on disk via pluggable adapters
- **Dynamic analysis:** value and AOB scanning, pointer-path discovery, struct dissection, code injection, hooks, hardware watchpoints, persistent cheat tables
- **Game-specific:** Unity **IL2CPP** metadata, Lua and LuaJIT bytecode; config-driven **N0xHUD** companion window

Bridges traditional disassembler/decompiler workflows and [[cheat-engine]]-style runtime manipulation with explainable, reproducible outputs—aimed at game-security researchers, reverse engineers, and AI agents. Complements host-specific MCP bridges such as [[ida-pro-mcp]] and [[x64dbg-mcp]] with a standalone unified static+dynamic pipeline rather than wrapping a single GUI RE host.

## Links

- Repo: https://github.com/LargoScript/n0xis

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[cheat-engine]] · [[pointer-lab]] · [[ida-pro-mcp]] · [[concepts/il2cpp]] · [[aether]] · [[neverd]]
