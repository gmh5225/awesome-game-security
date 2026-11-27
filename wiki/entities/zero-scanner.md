---
title: Zero Scanner
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/highho__zero-scanner.md
updated: 2026-11-27
confidence: medium
---

# Zero Scanner

**Zero** (highho/zero-scanner) is a modern, lightweight **Windows x64** memory workbench that reimplements a Cheat Engine–style **scan → locate → watch → modify** workflow in a single **offline** desktop application. It is built with **Rust** and **egui**, ships as a portable executable, and targets reverse engineers, game memory analysts, and security researchers who want full local control without cloud services or telemetry. (source: wiki/sources/descriptions/highho__zero-scanner.md)

## Capabilities

- Typed **value scans**, **AOB** pattern search, and **pointer chains**
- Built-in **x86-64 disassembly**, **reversible code patches**, and **speed control**
- **Lua scripting** and import/export of Cheat Engine **`.CT` tables**
- On-device **triage and observation** pipeline that ranks address candidates with explainable scoring and optional feedback learning
- **MCP HTTP server** on localhost to expose the scan engine to local AI assistants

## Positioning

Listed under **Cheat → memory scanner** beside native CE-style tools such as [[cheatos]], [[enesmem]], [[pointer-lab]], and [[pymemory-editor]]. Compared to attaching external MCP bridges to full Cheat Engine, Zero bundles the workbench and agent endpoint in one Rust/egui stack with an explicit offline, no-telemetry stance. Complements bridges such as [[cheatengine-mcp-bridge]], [[memmcp]], and cross-platform [[pymemory-editor]] when analysts prefer a self-contained Windows x64 scanner with built-in agent integration.

## Links

- Repo: https://github.com/highho/zero-scanner

## Related

[[cheat-engine]] · [[cheatos]] · [[enesmem]] · [[pointer-lab]] · [[pymemory-editor]] · [[cheatengine-mcp-bridge]] · [[memmcp]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]