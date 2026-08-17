---
title: ida-rpc
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bkerler__ida_rpc.md
updated: 2026-08-17
confidence: medium
---

# ida-rpc

**IDA Pro JSON-RPC daemon** — an IDA plugin/server that exposes IDA's analysis capabilities (disassembly, decompilation, cross-references, patching, type system) over a network protocol for remote scripting and LLM/agent-assisted RE. Supports headless and GUI IDA sessions; ships a **ghidra-rpc-compatible CLI** for cross-disassembler agent workflows. (source: wiki/sources/descriptions/bkerler__ida_rpc.md)

Sits in the agent-facing IDA automation lane beside MCP bridges ([[ida-mcp-rs]], [[headless-ida-mcp-server]], [[ida-pro-mcp]], [[mcp-server-idapro]]) and JSON-RPC Ghidra peers such as [[ghidra-headless-mcp]].

## Links

- Repo: https://github.com/bkerler/ida_rpc

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-mcp-rs]] · [[headless-ida-mcp-server]] · [[ida-pro-mcp]] · [[mcp-server-idapro]] · [[binary-analysis-mcps]] · [[ghidra-headless-mcp]]
