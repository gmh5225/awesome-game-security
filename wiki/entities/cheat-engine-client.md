---
title: CheatEngine.Client
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/CheatEngineNet__CheatEngine.Client.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# CheatEngine.Client

**CheatEngine.Client** (CheatEngineNet/CheatEngine.Client) is the official high-level C# library for building in-process Cheat Engine plugins on Windows x64. It wraps **CheatEngine.SDK** with activation-scoped dependency injection, typed memory access, AOB and value scanning, process selection, address tables, assembly and Auto Assembler helpers, and generated Lua bindings while avoiding leaked raw host handles. (source: wiki/sources/descriptions/CheatEngineNet__CheatEngine.Client.md)

## Capabilities

- NuGet-packaged fluent APIs with module lifecycle management and lease-based resource cleanup
- `dotnet new ceplugin` project template targeting .NET 10 and Cheat Engine 7.7
- Maintainable plugin workflows for memory inspection, game modification, and RE beside hand-rolled SDK calls

## Role in the README map

Listed under **Cheat → RE Tools** next to official extensions such as [[aitools]] and [[ce-decky]]. Complements external MCP bridges ([[cheatengine-mcp-bridge]], [[harness-for-rea]]) that orchestrate CE from outside the process.

## Links

- Repo: https://github.com/CheatEngineNet/CheatEngine.Client

## Related

[[cheat-engine]] · [[aitools]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[harness-for-rea]] · [[skid-factory]]
