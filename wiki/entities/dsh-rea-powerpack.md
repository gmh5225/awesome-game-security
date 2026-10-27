---
title: DSH REA Powerpack
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: medium
---

# DSH REA Powerpack

**dsh-rea-powerpack** (Zhishulo/dsh-rea-powerpack) is a **DeepSeek Harness (DSH) plugin** that hardens the REA reverse-engineering MCP server on Windows: it detects, installs, and verifies analysis engines (ADB, Apktool, JADX, WABT, Frida, Python), composes REA-specific environment variables and PATH for the MCP child process without changing system-wide config, and exposes engine matrices, doctor reports, and update policies in a React settings card over a loopback HTTP API. Version governance pins `rea-agents` builds, preflights upgrades in a shadow install, and supports hot reload or rollback on failure while explaining missing tool groups in plain language. (source: wiki/sources/descriptions/Zhishulo__dsh-rea-powerpack.md)

README category: Cheat / RE Tools.

## Positioning

Complements [[dsh-rea-plugin]] (Chinese REA workbench UI and bundled docs) with **engine lifecycle and REA version pinning** for Windows DSH users. Pair with [[dsh-plugins]], [[dsh-ghidra]], and [[research-rigor]] when agent-assisted RE conclusions feed anti-cheat or enforcement workflows.

## Links

- Repo: https://github.com/Zhishulo/dsh-rea-powerpack

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dsh-rea-plugin]] · [[dsh-plugins]] · [[rea-atlas]] · [[research-rigor]]
