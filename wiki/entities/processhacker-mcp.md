---
title: processhacker-mcp
kind: entity
topics: [reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/illegal-instruction-co__processhacker-mcp.md
updated: 2026-08-04
confidence: medium
---

# processhacker-mcp

C/C++ MCP (Model Context Protocol) server that exposes Process Hacker–style runtime process analysis and process-hacking workflows to AI agents. Extensible via DLL plugins for asset pipelines, editor tooling, and custom plugin development. Fits the Game Develop → MCP server lane while targeting live host/process inspection rather than static disassembly or CE-style memory scanning alone. (source: wiki/sources/descriptions/illegal-instruction-co__processhacker-mcp.md)

Complements the Process Hacker lineage in [[systeminformer]] (successor GUI explorer) and agent-facing live-memory MCP bridges such as [[cheatengine-mcp-bridge]] / [[memmcp]] by wiring Process Hacker–oriented runtime analysis into LLM agent workflows.

## Links

- Repo: https://github.com/illegal-instruction-co/processhacker-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[systeminformer]] · [[cheatengine-mcp-bridge]] · [[memmcp]] · [[mcp-windbg]] · [[openprocmon]]
