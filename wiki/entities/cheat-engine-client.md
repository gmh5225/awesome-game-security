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

**CheatEngine.Client** (CheatEngineNet/CheatEngine.Client) is the official high-level, **lifecycle-safe** C# library for building **in-process** plugins that run inside [[cheat-engine]] on **Windows x64**. It wraps **CheatEngine.SDK** with activation-scoped dependency injection, typed memory access, AOB and value scanning, process selection, address tables, assembly and Auto Assembler helpers, and generated Lua bindings—without exposing raw host handles to plugin code. (source: wiki/sources/descriptions/CheatEngineNet__CheatEngine.Client.md)

Distinct from external orchestrators ([[harness-for-rea]], [[cheatengine-mcp-bridge]]) that drive CE from outside the process, and from hand-rolled SDK glue: this stack targets **maintainable, testable** plugin code for memory inspection, game modification, and reverse-engineering workflows.

## Architecture

| Layer | Role |
|-------|------|
| **Cheat Engine host** | Loads in-process .NET plugins on Windows x64 |
| **CheatEngine.SDK** | Low-level host interop and native CE surfaces |
| **CheatEngine.Client** | Fluent APIs, activation-scoped DI, typed memory and scan helpers |
| **Plugin project** | NuGet packages, module lifecycle, lease-based resource cleanup |
| **Tooling** | `dotnet new ceplugin` template; targets **.NET 10** and **Cheat Engine 7.7** |

## Capabilities

- NuGet-packaged fluent APIs with hosting/module lifecycle and lease-based cleanup
- Process selection, address tables, Auto Assembler and assembly helpers
- Generated Lua bindings for scriptable workflows beside C# plugin logic
- Official README placement under **Cheat → RE Tools** next to extensions such as [[aitools]] and [[ce-decky]]

## Audience

**C#/.NET developers** building CE plugins who want structured DI and resource safety instead of leaking raw SDK handles—listed under **Cheat** in the README map.

## Links

- Repo: https://github.com/CheatEngineNet/CheatEngine.Client

## Related

[[cheat-engine]] · [[aitools]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[harness-for-rea]] · [[skid-factory]] · [[cheatengine-mcp-bridge]]
