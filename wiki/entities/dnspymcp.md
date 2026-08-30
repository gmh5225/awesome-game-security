---
title: DnSpyMCP
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/rabbanyhmm__DnSpyMCP.md
updated: 2026-08-30
confidence: medium
---

# DnSpyMCP

**DnSpyMCP** (rabbanyhmm/DnSpyMCP) is a local **Model Context Protocol** server that exposes AI agents to deep **.NET assembly** inspection, decompilation, and binary patching without requiring [[dnspy]] at runtime. Written in C# on .NET 8, it uses **dnlib** for assembly and IL manipulation and **ICSharpCode.Decompiler** for C# output, offering 31 MCP tools for listing types, decompiling methods, analyzing IL, and applying patches. (source: wiki/sources/descriptions/rabbanyhmm__DnSpyMCP.md)

## Capabilities

- **Core .NET RE:** type/method/field listing, C# decompilation, IL analysis, metadata edits, binary patching
- **Unity / IL2CPP:** offset and RVA lookup, struct layout export, `dump.cs` bridging, cross-reference tracing, multi-DLL workspace search
- **Network / security research:** packet-handler discovery, crypto-usage scans, hardcoded-secret extraction

Communicates over stdio JSON-RPC and integrates with MCP clients such as Claude Code, Codex, Cursor, and OpenCode for game security, reverse engineering, and anti-cheat analysis workflows. Complements interactive [[dnspy]] debugging with headless, agent-driven .NET RE—especially for Unity Mono dummy DLLs and managed tooling around [[concepts/il2cpp]] dump artifacts.

## Links

- Repo: https://github.com/rabbanyhmm/DnSpyMCP

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[dnspy]] · [[ilspy]] · [[dncil]] · [[concepts/il2cpp]] · [[n0xis]] · [[ida-pro-mcp]] · [[x64dbg-mcp]]
