---
title: Binary Cartography
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrphrazer__binary-cartography.md
  - wiki/sources/README-categories.md
updated: 2026-09-23
confidence: medium
---

# Binary Cartography

**Binary Cartography** (mrphrazer/binary-cartography) is a curated **webinar series repository** for practical reverse engineering, malware analysis, and software protection on real binaries. (source: wiki/sources/descriptions/mrphrazer__binary-cartography.md)

Each session folder ships slides, sample binaries, references, and a self-contained **Kali-based Docker** lab preconfigured with Ghidra or Binary Ninja, MCP-connected AI coding agents, and common analysis tooling. Sessions progress through increasingly complex **software protection** and obfuscation schemes on real binaries. README category: Cheat / Guide (adjacent RE Tools workflows).

## Session layout

Per-session folders bundle reproducible artifacts: presentation slides, target binaries, bibliography/references, and a Docker compose environment so analysts can replay the full workflow without local toolchain drift.

## Workflow themes

- Agentic workflows automating binary inspection and structure recovery
- Malware triage and heuristic code identification
- Deobfuscation across increasingly complex protection schemes

Primary technologies include Python, Docker, [[ghidra-headless-mcp]], [[binary-ninja-headless-mcp]], and symbolic analysis with **Miasm** plus [[msynth]] for MBA-style simplification during deobfuscation labs.

## Audience

Reverse engineers, malware analysts, and game security researchers who want hands-on, workflow-driven methods for analyzing protected or obfuscated software. Pair with [[static-runtime-evidence]] when separating static inference from lab-backed findings.

## Links

- Repo: https://github.com/mrphrazer/binary-cartography

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binary-ninja-headless-mcp]] · [[ghidra-headless-mcp]] · [[re4f]] · [[static-runtime-evidence]] · [[dynamic-binary-instrumentation]] · [[mixed-boolean-arithmetic]]
