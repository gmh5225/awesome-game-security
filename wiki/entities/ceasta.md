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

**Ceasta** (ngwg/ceasta) is an all-in-one **binary analysis workbench** combining disassembler, decompiler, and debugger for Windows and Linux. Written in C++17, it loads PE and ELF executables and libraries into a self-contained, vendored environment for reverse engineers and security researchers inspecting game clients, anti-cheat modules, and other protected native code. (source: wiki/sources/descriptions/ngwg__ceasta.md)

README category: Cheat / RE Tools.

## Static analysis

Automated function and cross-reference analysis with an IDA-style listing, C-like pseudocode, and control-flow graphs. Library signature matching helps identify linked components in stripped or partially labeled binaries. (source: wiki/sources/descriptions/ngwg__ceasta.md)

## Debugger

An x64dbg-style debugger with breakpoints, stepping, and live memory inspection bridges static listing and runtime observation in the same session.

## Automation and MCP

Lua scripting, plugins, binary diffing, and a command-line interface support scripted workflows. A built-in **MCP server** lets AI assistants interact with open binaries for decompilation, renaming, and guided debugging. (source: wiki/sources/descriptions/ngwg__ceasta.md)

## Positioning

Complements standalone disassemblers/debuggers and MCP bridges such as [[binary-ninja-headless-mcp]], [[ida-pro-mcp]], [[x64dbg-mcp]], and [[reverify]] with a single vendored stack spanning static listing, decompilation, and live debugging—without chaining separate GUI tools and external MCP plugins.

## Links

- Repo: https://github.com/ngwg/ceasta

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binary-diffing]] · [[binary-ninja-headless-mcp]] · [[reverify]] · [[skid-factory]] · [[sako-restudio]] · [[hikarisystem-hexcore]] · [[x64dbg]]
