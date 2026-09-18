---
title: skid_factory
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/wrong-commit__skid_factory.md
  - wiki/sources/README-categories.md
updated: 2026-09-18
confidence: medium
---

# skid_factory

**skid_factory** (wrong-commit/skid_factory) is a **Node.js orchestration framework** that connects large language models to low-level game-debugging tools through the Model Context Protocol. Written primarily in TypeScript with Lua and Python bridge scripts, it integrates **Cheat Engine**, **x64dbg**, and **Ghidra** for memory scanning, hardware write-breakpoint monitoring, pointer-chain tracing to static bases, and in-game value patching. (source: wiki/sources/descriptions/wrong-commit__skid_factory.md)

## Capabilities

- **Interactive REPL:** value scanning and base-address resolution workflows
- **Advise command:** Cursor CLI–driven iterative memory discovery and patching guidance
- **MCP bridges:** orchestrates CE/x64dbg/Ghidra instead of manual one-off scripts
- **Target use:** offline game memory analysis, pointer-chain reconstruction, and cheat prototyping for authorized RE

Sits beside agent-native labs such as [[open-reverselab]], verification-gated MCP hosts such as [[reverify]], and cross-platform pipelines such as [[n0xis]]—emphasizing **tool orchestration** across CE/x64dbg/Ghidra rather than a single static analyzer.

## Role in the README map

Listed under **Cheat → RE Tools** as a Node.js MCP orchestrator for game RE and cheat-development automation.

## Links

- Repo: https://github.com/wrong-commit/skid_factory

## Related

[[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[open-reverselab]] · [[reverify]] · [[n0xis]] · [[x64dbg-mcp]] · [[binary-ninja-headless-mcp]] · [[cheat-engine]]
