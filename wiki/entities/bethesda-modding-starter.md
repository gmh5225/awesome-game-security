---
title: Bethesda Modding Starter
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/rollingrock__bethesda-modding-starter.md
updated: 2026-08-15
confidence: medium
---

# Bethesda Modding Starter

One-stop Windows bootstrap for Bethesda **Creation Engine** script-extender plugin development and engine-level reverse engineering on **Fallout 4**, **Skyrim**, and **Starfield**. Ships idempotent PowerShell setup, a CMake/vcpkg plugin scaffolder, C++ **F4SE** and **SFSE** templates wired to **CommonLib**, address-library import tooling, and **devbench** for in-game memory and render-target instrumentation over localhost. Integrates **Ghidra** and **x64dbg** workflows bridged via MCP for AI-assisted decompilation and live debugging; primary languages are C++ (plugins), PowerShell (automation), and Python (Ghidra scripts). (source: wiki/sources/descriptions/rollingrock__bethesda-modding-starter.md)

Reproducible mod-dev + binary-analysis toolchain lane—complements generic RE MCP servers ([[ghidra-headless-mcp]], [[x64dbg]]) with title-specific CommonLib scaffolding and address-library tooling.

## Links

- Repo: https://github.com/rollingrock/bethesda-modding-starter

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[x64dbg]] · [[ghidra-headless-mcp]] · [[research-rigor]]
