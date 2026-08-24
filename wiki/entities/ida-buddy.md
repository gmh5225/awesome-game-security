---
title: ida-buddy
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JustasMasiulis__ida_buddy.md
updated: 2026-08-24
confidence: medium
---

# ida-buddy

**Python CLI companion for IDA Pro** — WinDbg-style **idalib** terminal interface (`idb`) for LLM agents. Connects to running IDA instances through a worker plugin and exposes disassembly, decompilation, cross-references, type queries, memory reads, and annotation from the shell. Uses a **persistent headless worker per database**, **compact stdout**, and supports **DB mutations with undo**. (source: wiki/sources/descriptions/JustasMasiulis__ida_buddy.md)

Sits in the agent-RE lane beside MCP servers ([[ida-cli]], [[headless-ida-mcp-server]], [[ida-mcp-rs]]) and non-MCP CLI bridges ([[idac]], [[ida-bridge]], [[ida-rpc]]), but emphasizes a **terminal-first, WinDbg-style** workflow over MCP protocol transport.

## Links

- Repo: https://github.com/JustasMasiulis/ida_buddy

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-cli]] · [[idac]] · [[ida-bridge]] · [[ida-rpc]] · [[ida-mcp-server-plugin]] · [[headless-ida-mcp-server]] · [[ida-jm-xorstr-decrypt-plugin]]
