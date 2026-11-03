---
title: Harness for REA
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/protonspy__harness-for-rea.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# Harness for REA

**harness-for-rea** ([protonspy/harness-for-rea](https://github.com/protonspy/harness-for-rea)) is a TypeScript **Electron/React** desktop shell and **Bun** terminal UI for **authorized** deep analysis of binaries you may study—reverse engineering, debugging, and legacy codebase comprehension. You state goals in chat; a **planning orchestrator** (OpenRouter, DeepSeek, or other OpenAI-compatible models) decomposes work into steps; a **Docker-sandboxed Claude Code specialist** executes analysis with the **REA** reverse-engineering MCP server and a root shell. Targets are copied **read-only** into containers; **SQLite** event logging, **validated analysis contracts** with test vectors, and an optional **read-only Cheat Engine** memory bridge for live Windows processes keep findings evidence-backed without exposing full binaries on the host. (source: wiki/sources/descriptions/protonspy__harness-for-rea.md)

Listed under README **Cheat → RE Tools** beside MCP orchestrators such as [[skid-factory]], [[cheat-agent]], and [[rea-mytechnotalent]].

## Architecture

| Layer | Role |
|-------|------|
| **Desktop / TUI** | Electron + shadcn/ui; Bun-based terminal UI |
| **Planning orchestrator** | OpenAI-compatible models break chat goals into steps |
| **Specialist sandbox** | Claude Code in Docker with REA MCP + root shell |
| **Evidence** | Read-only target copies, SQLite logs, analysis contracts + test vectors |
| **Optional CE bridge** | Read-only live Windows process memory via Cheat Engine |

## Positioning

Full-stack **orchestrator** (UI + planner + containerized specialist) rather than a single MCP bridge: contrasts with [[re-harness]] (OpenCode + IDA/IDASQL static PE lane) and complements [[skid-factory]] / [[cheat-agent]] CE–x64dbg–Ghidra MCP stacks and [[rea-mytechnotalent]] offline one-shot inventory + local RAG. Pair [[research-rigor]] when acting on agent summaries. (source: wiki/sources/descriptions/protonspy__harness-for-rea.md)

## Links

- Repo: https://github.com/protonspy/harness-for-rea

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[re-harness]] · [[skid-factory]] · [[cheat-agent]] · [[rea-mytechnotalent]] · [[rea]] · [[aitools]] · [[ceasta]]
