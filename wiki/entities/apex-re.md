---
title: Apex-RE
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/emrewyt__apex-re.md
  - wiki/sources/README-categories.md
updated: 2026-11-13
confidence: medium
---

# Apex-RE

**Apex-RE** ([emrewyt/apex-re](https://github.com/emrewyt/apex-re)) is an open-source **reverse engineering skill and prompt library** for AI coding agents (Claude Code, Cursor, Codex). It teaches a structured, **verification-oriented** workflow for native and managed binaries: triage, signature scanning, memory diffing, VM trace analysis, and emulation-backed checks—aimed at compilable C++20/C# outputs, Kaitai struct specs, and grounded memory layouts instead of ungrounded pseudocode. (source: wiki/sources/descriptions/emrewyt__apex-re.md)

Ships **zero-dependency Python** helpers alongside extensive reference guides for **Unreal** and **Unity** game binaries, **.NET** and **NativeAOT**, obfuscators (**VMProtect**, **OLLVM**), and integration with **Ghidra**, **IDA Pro**, and **Frida**. Listed under README **Cheat → RE Tools**.

## Methodology

Five-layer task directives emphasize evidence collection, cross-checking, and round-trip verification so agent output stays tied to observable binary behavior. (source: wiki/sources/descriptions/emrewyt__apex-re.md)

## Positioning

Installable **agent skill + scripts** corpus in the game-security RE lane—complements orchestrators such as [[harness-for-rea]] and prompt libraries such as [[rea-prompts]], and sits beside the [[awesome-ai-reverse-engineering]] catalog. Pair agent runs with [[research-rigor]] and [[static-runtime-evidence]]. For protected-game workflows, relate to [[codex-vmprotect-unpack-skill]] and Fix-VMProtect unpack skills.

## Links

- Repo: https://github.com/emrewyt/apex-re

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[harness-for-rea]] · [[rea-prompts]] · [[awesome-ai-reverse-engineering]] · [[research-rigor]] · [[static-runtime-evidence]] · [[codex-vmprotect-unpack-skill]]
