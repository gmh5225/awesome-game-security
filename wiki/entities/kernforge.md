---
title: kernforge
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/kernullist__kernforge.md
updated: 2026-08-02
confidence: medium
---

# kernforge

Go-based **AI-assisted coding CLI and engineering agent** for Windows security, anti-cheat, driver, telemetry, and Unreal Engine integrity workflows — not a generic coding assistant. Builds reusable **project knowledge packs** via architecture analysis, structural indexing, and security overlays; supports investigate/simulate loops, root-cause analysis, source-level fuzz reasoning, verification plans, evidence/session memory, and **MCP skills**. Includes C++ driver templates, PowerShell build tooling, a VS Code extension, and automated driver POC scaffolding for **WDM**, **minifilter**, **registry filter**, and **WFP callout** styles. (source: wiki/sources/descriptions/kernullist__kernforge.md)

Targets security and anti-cheat engineers analyzing, hardening, and validating kernel and game-security codebases. Complements point tools from the same maintainer — [[kn-live-dbg]] (live kernel inspect), [[kn-diff-pool]] (Big Pool diff), [[windbg-decompile-ext]] (WinDbg LLM decompile) — by orchestrating multi-step analysis, fuzz reasoning, and driver POC generation across a repo. Pair with [[research-rigor]] when acting on agent output and [[wdutf]] when validating driver logic under test.

## Links

- Repo: https://github.com/kernullist/kernforge (README tag: Go workbench for Windows/anti-cheat project analysis, fuzzing, and evidence-backed verification)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kn-live-dbg]] · [[kn-diff-pool]] · [[windbg-decompile-ext]] · [[wdutf]] · [[research-rigor]] · [[kernel-callbacks]]
