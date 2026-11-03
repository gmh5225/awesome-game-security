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

**harness-for-rea** (protonspy/harness-for-rea) is a desktop Electron/React shell and Bun terminal UI that orchestrates **authorized** binary reverse engineering for security researchers and developers. A planning orchestrator (OpenRouter, DeepSeek, or other OpenAI-compatible models) decomposes goals into steps; a Docker-sandboxed **Claude Code** specialist performs analysis with the REA reverse-engineering MCP server and a root shell inside isolated containers. Targets are copied read-only into sandboxes; SQLite event logging, validated analysis contracts with test vectors, and optional read-only **Cheat Engine** memory bridges for live Windows processes keep evidence structured without exposing full binaries on the host. (source: wiki/sources/descriptions/protonspy__harness-for-rea.md)

Listed under README **Cheat → RE Tools** beside MCP orchestrators such as [[skid-factory]], [[cheat-agent]], and [[rea-mytechnotalent]].

## Surfaces

| Component | Role |
|-----------|------|
| **Desktop / TUI** | Electron + shadcn/ui desktop; Bun-based terminal UI |
| **Planning orchestrator** | OpenAI-compatible models break work into steps |
| **Specialist sandbox** | Claude Code in Docker with REA MCP + root shell |
| **Evidence** | Read-only target copies, SQLite logs, analysis contracts |
| **Optional CE bridge** | Read-only live Windows process memory via Cheat Engine |

## Links

- Repo: https://github.com/protonspy/harness-for-rea

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[skid-factory]] · [[cheat-agent]] · [[rea-mytechnotalent]] · [[aitools]] · [[ceasta]]
