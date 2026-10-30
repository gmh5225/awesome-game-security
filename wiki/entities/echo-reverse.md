---
title: Echo Reverse
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/NetVar1337__echo-reverse.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: medium
---

# Echo Reverse

**echo-reverse** (NetVar1337/echo-reverse) is a Windows desktop reverse-engineering workbench that connects to live game and application targets through the Echo backend. The UI is Tauri + React; AngelScript agents run over a local WebSocket relay. (source: wiki/sources/descriptions/NetVar1337__echo-reverse.md)

## Architecture

Front end: **Tauri + React**. Analysis agents: **AngelScript** over a local **WebSocket** relay to the **Echo** backend, which attaches to live game and application processes for memory and code views. (source: wiki/sources/descriptions/NetVar1337__echo-reverse.md)

## Capabilities

- **Live analysis:** disassembly, PE and string analysis, memory scanning and watches, function emulation via Echo-backed memory access.
- **Engine tooling:** Unreal, Unity IL2CPP, and Source 2 inspection helpers in one workspace.
- **Automation:** AngelScript templates (stock templates), overlay design, Frida integration, deobfuscation helpers, and an **MCP endpoint** for external agent-driven workflows.
- **Extended lanes:** kernel and network tooling alongside user-mode RE in the same workbench. (source: wiki/sources/descriptions/NetVar1337__echo-reverse.md)

## Audience

Researchers who want a single live-target workspace for code exploration, memory triage, and script-driven automation during game security and RE work — adjacent to integrated suites such as [[orress]], [[ceasta]], and MCP bridges like [[dsh-ghidra]]. (source: wiki/sources/descriptions/NetVar1337__echo-reverse.md)

## Links

- Repo: https://github.com/NetVar1337/echo-reverse [Windows Tauri/React live RE workbench on Echo: memory and disassembly, game-engine inspection, Frida, kernel/network tooling, and MCP for agents]

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[il2cpp]] · [[unreal-object-model]] · [[source-netvars]]
