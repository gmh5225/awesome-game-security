---
title: REA (Reverse Engineer Anything)
kind: entity
topics: [reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/morluto__rea.md
  - wiki/sources/README-categories.md
updated: 2026-10-09
confidence: medium
---

# REA (Reverse Engineer Anything)

**REA** (morluto/rea) is a local **CLI and Model Context Protocol server** that connects AI coding agents to a unified reverse-engineering toolkit for software without source code. Implemented primarily in TypeScript on Node.js, it bridges external analyzers (Hopper, Ghidra, IDA Pro, JADX, pwntools, mitmproxy, and others) and supports native binaries, JavaScript/Electron apps, .NET assemblies, websites and network captures, Android APKs, firmware, and related offline diagnostics. Analysis runs on the host and returns findings with explicit **evidence provenance and stated limitations** so agents can trace behavior without treating model output as ground truth. Deep native work still requires separately installed disassemblers/decompilers. (source: wiki/sources/descriptions/morluto__rea.md)

Sits in the README **Game Develop → MCP server** lane beside editor bridges such as [[binary-ninja-headless-mcp]] and [[ghidra-headless-mcp]], but targets **cross-format agent-assisted RE** rather than a single IDE plugin.

## Links

- Repo: https://github.com/morluto/rea

## Related

[[binary-ninja-headless-mcp]] · [[ghidra-headless-mcp]] · [[ida-pro-mcp]] · [[reverify]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
