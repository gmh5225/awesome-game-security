---
title: Ceasta
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ngwg__ceasta.md
  - wiki/sources/README-categories.md
updated: 2026-09-25
confidence: medium
---

# Ceasta

**Ceasta** (ngwg/ceasta) is an integrated **disassembler, decompiler, and debugger** for Windows and Linux PE/ELF binaries. Written in C++17, it provides IDA-style listings with C-like pseudocode, control-flow graphs, and an x64dbg-style debugger with breakpoints, stepping, and live memory inspection. Lua scripting, plugins, binary diffing, library signature matching, CLI automation, and a built-in **MCP server** support AI-assisted decompilation, renaming, and guided debugging on game clients, anti-cheat modules, and other protected native code. (source: wiki/sources/descriptions/ngwg__ceasta.md)

README category: Cheat / RE Tools.

## Capabilities

- PE/ELF load, automated function and cross-reference analysis
- Debugger with breakpoints, stepping, and memory inspection
- Lua plugins, binary diffing, library signature matching, CLI automation
- Built-in MCP server for AI-assisted RE workflows

## Positioning

Complements standalone disassemblers/debuggers and MCP bridges such as [[binary-ninja-headless-mcp]], [[ida-pro-mcp]], and [[reverify]] with a self-contained vendored analysis environment spanning static listing, decompilation, and live debugging.

## Links

- Repo: https://github.com/ngwg/ceasta

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binary-ninja-headless-mcp]] · [[reverify]] · [[skid-factory]] · [[sako-restudio]] · [[hikarisystem-hexcore]]
