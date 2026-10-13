---
title: kiln-ida
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/TechMecca__kiln-ida.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: medium
---

# kiln-ida

Native **IDA Pro 9.1** plugin that exposes the open database to AI assistants over the **Model Context Protocol** via **Streamable HTTP** on localhost. Implemented as a single Python **IDAPython** module with no pip dependencies; dozens of tools inspect and navigate functions, pseudocode, assembly, cross-references, strings, types, memory, and the debugger, with optional **Hex-Rays** decompilation and guarded write operations (renames, comments, patches, breakpoints, IDAPython execution). Work is marshaled onto IDA’s main thread; live targets support hardware-only breakpoints and non-suspending trace modes, with long-poll debugger stops so clients can review sessions interactively. Aimed at reverse engineers and game security analysts who want MCP-capable clients (including Kiln’s chat integration) to work against a live IDB rather than static exports. (source: wiki/sources/descriptions/TechMecca__kiln-ida.md)

Curated-tool surface and debugger/MCP ergonomics rather than full IDAPython exposure—peers with [[ida-pro-mcp]], [[iida-mcp]], and [[ida-multi-mcp]] in the agent-assisted RE lane; pair with [[research-rigor]] when trusting automated edits.

## Links

- Repo: https://github.com/TechMecca/kiln-ida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-mcp]] · [[iida-mcp]] · [[ida-multi-mcp]] · [[research-rigor]]
