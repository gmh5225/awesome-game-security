---
title: DSH REA Powerpack
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: high
---

# DSH REA Powerpack

**dsh-rea-powerpack** (Zhishulo/dsh-rea-powerpack) is a **DeepSeek Harness (DSH) plugin** that hardens the **REA** reverse-engineering MCP server on **Windows**: it manages analysis engines, pins `rea-agents` builds, and surfaces capability gaps in a settings dashboard. (source: wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md)

README category: Cheat / RE Tools.

## Architecture

Node.js JavaScript modules expose a **loopback HTTP API**; a **React** client card renders engine matrices, doctor reports, and update policies. Environment variables and PATH entries are composed **only for the MCP child process**, leaving system-wide configuration unchanged. (source: wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md)

## Engine lifecycle

Detects, installs, and verifies bundled or external tooling including **ADB**, **Apktool**, **JADX**, **WABT**, **Frida**, and **Python**, then wires them into REA’s expected layout for agent-driven workflows. (source: wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md)

## Version governance

Pins **rea-agents** to precise builds, **preflights upgrades in a shadow install**, and supports **hot reload** or **rollback on failure**. Missing tool groups are explained in plain language via doctor output. (source: wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md)

## Scope

Targets reverse engineers and security researchers who run REA inside DSH for **native binary**, **mobile**, and **managed-code** analysis on Windows—not a standalone disassembler. (source: wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md)

## Positioning

Complements [[dsh-rea-plugin]] (Chinese REA workbench UI and bundled docs) with **engine lifecycle and REA version pinning**. Pair with [[dsh-plugins]], [[dsh-ghidra]], [[rea]], and [[research-rigor]] when agent-assisted RE conclusions feed anti-cheat or enforcement workflows.

## Links

- Repo: https://github.com/Zhishulo/dsh-rea-powerpack

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dsh-rea-plugin]] · [[dsh-plugins]] · [[rea-atlas]] · [[research-rigor]]
