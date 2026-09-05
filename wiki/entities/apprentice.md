---
title: Apprentice
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/digital-dev__Apprentice.md
updated: 2026-09-05
confidence: medium
---

# Apprentice

**Apprentice** (digital-dev/Apprentice) is a free, open-source **Windows game trainer and offline memory editor** that attaches directly to PC game processes without requiring a server, telemetry, or always-online client. Built with **Electron**, **React**, and **TypeScript** over a **C++ N-API** native addon, it targets offline game modding, memory analysis, and reverse engineering. (source: wiki/sources/descriptions/digital-dev__Apprentice.md)

## Capabilities

- **Cheats:** value freezes, code patches with multiple injection modes, sandboxed **Lua** scripting
- **Cheat Engine interop:** `.CT` table import and export
- **Native layer:** memory scanning, pointer-chain resolution, hardware-breakpoint write watching, **Zydis**-backed disassembly, deep **Mono JIT** introspection for Unity-based games
- **Agent bridge:** bundled read-only **MCP server** exposing the same introspection primitives to AI coding agents for live reverse engineering and cheat development workflows
- **Profiles:** ready-made cheat profiles for titles such as Valheim and Elden Ring

Complements [[cheat-engine]] and CE-table runtimes such as [[freeplay]] as a modern Electron-based offline trainer, and agent-native pipelines such as [[n0xis]] and [[ce-mcp-plugin]] when the workflow needs live process introspection exposed to LLM agents rather than a standalone disassembler host.

## Links

- Repo: https://github.com/digital-dev/Apprentice

## Related

[[cheat-engine]] · [[freeplay]] · [[pointer-lab]] · [[cheatengine-mono-helper]] · [[ce-mcp-plugin]] · [[n0xis]] · [[concepts/il2cpp]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
