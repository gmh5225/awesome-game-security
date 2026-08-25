---
title: cheatengine-mcp-bridge
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/miscusi-peek__cheatengine-mcp-bridge.md
  - wiki/sources/descriptions/beamstar__cheatengine-mcp-bridge.md
updated: 2026-08-18
confidence: medium
---

# cheatengine-mcp-bridge

MCP bridge that connects AI agents to a live Cheat Engine instance. The README lists two independent repos under the same label in the Game Develop → MCP server lane—useful for game developers, reverse engineers, and tooling builders wiring LLM agents into live CE workflows rather than reimplementing memory tooling from scratch.

## miscusi-peek/cheatengine-mcp-bridge

Named-pipe IPC path: a Lua worker thread inside CE stays synchronized with a Python FastMCP server, targeting sub-2ms command latency. Exposes 40+ tools for memory reads, AOB scanning, pointer-chain traversal, structure dissection, RTTI class identification, hardware breakpoints (DR0–DR3), and DBVM hypervisor-level tracing. (source: wiki/sources/descriptions/miscusi-peek__cheatengine-mcp-bridge.md)

## beamstar/cheatengine-mcp-bridge

Alternate README listing for MCP integration with Cheat Engine in the Game Develop / MCP server area. (source: wiki/sources/descriptions/beamstar__cheatengine-mcp-bridge.md)

Unlike standalone Python memory MCP servers such as [[memmcp]], this path drives the full CE runtime (Lua engine, scanner, debugger, DBVM) rather than reimplementing CE-like primitives. Alternate in-process CE MCP plugin [[ce-mcp-plugin]] (Eruditi; C + Lua; async TCP command channel for memory R/W, freeze, disasm/asm, process control, and DLL injection) targets the same AI-assisted live-CE lane via native plugin IPC rather than named pipes. (source: wiki/sources/descriptions/Eruditi__CE-MCP-Plugin.md) Alternate agent bridge [[dsh-cheatengine]] uses DeepSeek Harness + TCP `ce_*` tools instead of MCP/FastMCP. Pairs with CE Lua plugins such as [[gddumper]] and AC-facing CE detection research such as [[cedetector]].

## Links

- Repo (miscusi-peek): https://github.com/miscusi-peek/cheatengine-mcp-bridge
- Repo (beamstar): https://github.com/beamstar/cheatengine-mcp-bridge

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[ce-mcp-plugin]] · [[dsh-cheatengine]] · [[memmcp]] · [[gddumper]] · [[cedetector]] · [[dma-cheat-engine-loader]] · [[ghidra-headless-mcp]] · [[ida-pro-mcp]] · [[mcp-windbg]]
