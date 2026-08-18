---
title: tenrec
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/axelmierczuk__tenrec.md
updated: 2026-08-18
confidence: medium
---

# tenrec

**Headless, extendable, multi-session IDA Pro MCP framework** built with **ida-domain** and **FastMCP**. Supports simultaneous analysis of multiple binaries in separate sessions and ships built-in plugins for functions, cross-references, symbol naming, comments, strings, segments, byte patching, types, and entry points. The Python package accepts custom plugins via entry points and provides auto-generated documentation — aimed at reverse engineers who want AI-integrated, headless IDA Pro analysis through the Model Context Protocol. (source: wiki/sources/descriptions/axelmierczuk__tenrec.md)

Distinct from single-session headless bridges: **multi-session** orchestration plus a **plugin entry-point** extension model. Peers with [[headless-ida-mcp-server]], [[ida-mcp-rs]], [[ida-cli]], [[ida-rpc]], [[ida-pro-mcp]], [[mcp-server-idapro]], [[ida-mcp-server-plugin]], and [[binary-analysis-mcps]] in the Game Develop / MCP server lane.

## Links

- Repo: https://github.com/axelmierczuk/tenrec

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[headless-ida-mcp-server]] · [[ida-mcp-rs]] · [[ida-cli]] · [[ida-rpc]] · [[ida-pro-mcp]] · [[mcp-server-idapro]] · [[binary-analysis-mcps]]
