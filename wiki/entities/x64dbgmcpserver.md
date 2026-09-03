---
title: x64DbgMCPServer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AgentSmithers__x64DbgMCPServer.md
updated: 2026-09-03
confidence: medium
---

# x64DbgMCPServer

C# / .NET Framework plugin for [[x64dbg]] that exposes debugger functionality through an MCP-compatible HTTP interface. Maps debugger actions to remotely callable commands for memory reads, disassembly, register queries, labeling, and automation. Architecture includes a lightweight self-hosted listener and modular command routing for tool integration and rapid extension—aimed at AI-assisted reverse engineering and scripted game security analysis workflows. (source: wiki/sources/descriptions/AgentSmithers__x64DbgMCPServer.md)

Alternative x64dbg MCP bridge to [[x64dbg-mcp]] (TypeScript; 23 mega-tools / 151 REST endpoints; native `.dp64`/`.dp32` REST plugin)—AgentSmithers targets a C# in-process plugin with HTTP MCP rather than an external TypeScript server. Complements [[x64dbg-automate-pyclient]] (Automate ZeroMQ RPC + optional MCP) and [[x64dbg-rippy]] (in-debugger WebView2 LLM panel).

## Links

- Repo: https://github.com/AgentSmithers/x64DbgMCPServer

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[x64dbg-mcp]] · [[x64dbg-automate-pyclient]] · [[x64dbg-rippy]] · [[ida-pro-mcp]]
