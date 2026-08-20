---
title: dsh-cheatengine
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/TindalosKorone__dsh-cheatengine.md
updated: 2026-08-20
confidence: medium
---

# dsh-cheatengine

**dsh-cheatengine** (TindalosKorone/dsh-cheatengine) is a **DeepSeek Harness** plugin that lets AI agents remotely control Cheat Engine on Windows through a local TCP bridge. Written in TypeScript as a Node.js plugin, it exposes dozens of `ce_*` tools for process attachment, memory scanning and read/write, disassembly, hardware and data breakpoints, register inspection, pointer chains, AOB patterns, and Lua or Auto Assembler scripts. (source: wiki/sources/descriptions/TindalosKorone__dsh-cheatengine.md)

Game-oriented helpers include anti-cheat detection, module dumping, speedhack, and cheat table save/load. Session tracking adds hypothesis, evidence, audit, undo, and snapshot support. Tools unlock on demand to keep agent context small; dangerous write and script operations require explicit unlock. Aimed at authorized game security research, reverse engineering, and dynamic memory analysis—not standalone cheating or static analysis.

Unlike [[cheatengine-mcp-bridge]] (MCP + CE Lua worker + FastMCP over named pipes), this path uses DeepSeek Harness plugin semantics with a TCP bridge and `ce_*` tool namespace. Pairs with canonical [[cheat-engine]] and standalone [[memmcp]].

## Links

- Repo: https://github.com/TindalosKorone/dsh-cheatengine

## Related

[[cheat-engine]] · [[cheatengine-mcp-bridge]] · [[memmcp]] · [[cedetector]] · [[detection-cheat-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
