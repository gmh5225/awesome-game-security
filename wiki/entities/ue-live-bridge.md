---
title: ue-live-bridge
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Glmour__ue-live-bridge.md
updated: 2026-08-29
confidence: medium
---

# ue-live-bridge

**ue-live-bridge** (Glmour/ue-live-bridge) is a **tooling framework** that lets an **external process** drive a running Unreal Engine game by reading and writing **live UObject state** without modifying engine or game source. A **UE4SS Lua mod** inside the game exposes the world over a pair of **append-only JSONL files**, while a **Python driver** on the outside resolves objects, reads properties, calls **UFunctions**, and issues writes through that file-based channel. The project emphasizes **verified interaction** rather than blind trust: writes are cross-checked with independent re-reads, negative-control poisoning proves checks can fail, and both the CLI and **MCP server** return explicit verdicts such as **CONFIRMED** or **FALSE_SUCCESS** instead of a simple boolean. It ships an MCP interface so AI agents can probe and manipulate game state programmatically, along with off-engine tests that simulate dishonest bridges. Stack: Python + Lua; audience: modders, researchers, and automation authors on Unreal titles they control. (source: wiki/sources/descriptions/Glmour__ue-live-bridge.md)

Sits in the runtime Unreal live-control lane beside in-process [[re-ue4ss]] scripting and editor-facing MCP bridges such as [[unreal-mcp]] and [[unreal-claude]]—differing by driving a **shipping game process** from outside via a verified JSONL IPC channel rather than editor plugins or pure in-game Lua.

## Links

- Repo: https://github.com/glmour/ue-live-bridge [UE4SS Lua bridge with Python MCP driver for live UObject/UFunction control and verified agent write claims]

## Related

[[re-ue4ss]] · [[unreal-mcp]] · [[unreal-claude]] · [[unreal-object-model]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
