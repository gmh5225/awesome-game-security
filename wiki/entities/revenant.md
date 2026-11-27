---
title: Revenant
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/opacity001__revenant.md
updated: 2026-11-27
confidence: medium
---

# Revenant

**REVENANT** (opacity001/revenant) is a unified reverse-engineering orchestration platform that combines binary lifting, devirtualization, static analysis, and stealth dynamic analysis in one workflow. Implementation is primarily TypeScript on Node.js with CMake-built native C++ and optional N-API bindings that drive external engines such as **revng** (LLVM IR lifting), **NoVmp** (VMProtect devirtualization), and **unthemidator** (Themida / WinLicense unpacking). (source: wiki/sources/descriptions/opacity001__revenant.md)

README category: Cheat / RE Tools.

## Surfaces

The same core engine is exposed through a library, headless **CLI**, **MCP server** for automated agent workflows, and a **VS Code extension** with disassembly, decompilation, control-flow graph, and devirtualization views.

## Static analysis

Loads **PE**, **ELF**, and **Mach-O** binaries; builds control-flow graphs and cross-references for triage of protected clients, packers, and anti-tamper layers.

## Dynamic analysis

Provisions **QEMU**-based analysis VMs hardened against common virtual-machine detection, with instrumented execution via a guest agent—useful when static lift/devirt alone is insufficient.

## Positioning

Sits beside integrated workbenches ([[ceasta]], [[orress]], [[echo-reverse]]) and multi-bridge MCP hubs ([[mcp-reverse]], [[rea-unlock]], [[harness-for-rea]]) by orchestrating lift/devirt/static/dynamic steps in one stack rather than chaining separate GUIs. Complements standalone devirt tools [[novmp]], [[unthemidator]], and agent MCP bridges such as [[x64dbg-mcp]] and [[ghidra-mcp]].

## Links

- Repo: https://github.com/opacity001/revenant

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[novmp]] · [[unthemidator]] · [[vmprotect]] · [[harness-for-rea]] · [[mcp-reverse]] · [[reverify]] · [[ceasta]] · [[research-rigor]]