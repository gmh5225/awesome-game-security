---
title: SlopStation
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/NetVar1337__SlopStation.md
  - wiki/sources/README-categories.md
updated: 2026-11-14
confidence: medium
---

# SlopStation

**SlopStation** (NetVar1337/SlopStation) is a Windows desktop workbench for PlayStation 4 reverse engineering and game security research that unifies console and local process analysis in one environment. (source: wiki/sources/descriptions/NetVar1337__SlopStation.md)

README category: **PlayStation** (authorized console debugging and live memory RE).

## Architecture

A **C++ analysis engine** drives core workflows; the shipped **Tauri v2** and **React** front end exposes the same capabilities through **Lua 5.4** scripting and a built-in **MCP server** for automation. (source: wiki/sources/descriptions/NetVar1337__SlopStation.md)

## Capabilities

- **Live console RE:** memory inspection, Cheat Engine–style scanning, and debugging over the **ps4debug-NG** protocol; optional **PS5** support via **ps5debug-NG**.
- **Static analysis:** ELF, PE, and related binaries; **Hyperion**-based decompilation.
- **Emulation:** **Unicorn**-based x86-64 emulation for devirtualization and slicing.
- **Host tooling:** host-side packet capture and an HTTP payload host for on-console tooling. (source: wiki/sources/descriptions/NetVar1337__SlopStation.md)

## Audience

Researchers and analysts who need authorized console debugging, module dumping, patching workflows, and scripted or agent-driven RE on PS4 and related targets—not online anti-cheat bypass research. (source: wiki/sources/descriptions/NetVar1337__SlopStation.md)

## Links

- Repo: https://github.com/NetVar1337/SlopStation

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[reaperpy]] · [[echo-reverse]] · [[ida-ps4-helper]] · [[ghidra-orbis]] · [[cheat-engine]]