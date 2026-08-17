---
title: unity-mcp
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/wondeks__unity-mcp.md
  - wiki/sources/descriptions/justinpbarnett__unity-mcp.md
updated: 2026-08-02
confidence: medium
---

# unity-mcp

MCP (Model Context Protocol) server for Unity aimed at streamlining editor/workflow automation for AI assistants and tooling. Fits the Game Develop → MCP server lane; useful for game developers, reverse engineers, and tooling builders wiring agents into Unity projects rather than reversing shipped IL2CPP/Mono binaries. (source: wiki/sources/descriptions/wondeks__unity-mcp.md) (source: wiki/sources/descriptions/justinpbarnett__unity-mcp.md)

The README lists two independent implementations under the same label:

- **justinpbarnett/unity-mcp** — C# and Python; shader, rendering, and graphics-oriented MCP surface (source: wiki/sources/descriptions/justinpbarnett__unity-mcp.md)
- **wondeks/unity-mcp** — editor + C# scripting interaction (source: wiki/sources/descriptions/wondeks__unity-mcp.md)

Complements editor-side Unity automation such as [[unicli]] (terminal CLI) and [[com-unity-ide-cursor]] (Cursor external editor integration) by exposing Unity via MCP instead of a command-line or IDE-launch surface.

## Links

- Repo (justinpbarnett): https://github.com/justinpbarnett/unity-mcp
- Repo (wondeks): https://github.com/wondeks/unity-mcp

## Related

[[unicli]] · [[com-unity-ide-cursor]] · [[il2cpp]] · [[overviews/game-engine]] · [[overviews/overview]]
