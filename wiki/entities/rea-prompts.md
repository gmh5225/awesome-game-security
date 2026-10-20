---
title: REA Prompts
kind: entity
topics: [reverse-engineering, game-hacking, anti-cheat, dma-attack, mobile-security, windows-kernel]
sources:
  - wiki/sources/descriptions/JoasASantos__REA-Prompts.md
updated: 2026-10-20
confidence: medium
---

# REA Prompts

**REA Investigation Prompts** (JoasASantos/REA-Prompts) is a **documentation-only** library of copy-paste prompt templates for driving **AI coding agents** through **REA (Reverse Engineer Anything)** workflows. Targets reverse engineers and game-security researchers who want structured agent instructions instead of ad hoc chat questions. (source: wiki/sources/descriptions/JoasASantos__REA-Prompts.md)

## Scope

Prompt families cover binaries, firmware, games, mobile apps, and web clients, including:

- Feature tracing, native binary triage, and clean-room behavioral cloning
- Game logic and engine mapping, WASM portability
- Kernel and firmware analysis, vulnerability research
- Electron and JavaScript inspection
- Defensive **anti-cheat**, **DMA**, and broader protection research

## Methodology

Templates emphasize **evidence-backed answers**: separate confirmed facts from hypotheses, prefer **static analysis first**, and scope **responsible use** for security research, interoperability, CTFs, and hardening your own software. (source: wiki/sources/descriptions/JoasASantos__REA-Prompts.md)

## Positioning

Markdown prompt corpus beside MCP bridges and catalogs in the AI-assisted RE lane—[[awesome-ai-reverse-engineering]] (tool index), [[rea]] / [[rea-unlock]] / [[rea-mytechnotalent]] (agent platforms), and rigor tooling such as [[reverify]] and [[re-harness]]. Pair agent output with [[research-rigor]] and [[static-runtime-evidence]] when converting prompts into conclusions.

## Links

- Repo: https://github.com/joasasantos/rea-prompts

## Related

[[research-rigor]] · [[static-runtime-evidence]] · [[awesome-ai-reverse-engineering]] · [[rea]] · [[rea-unlock]] · [[rea-mytechnotalent]] · [[re-harness]] · [[reverify]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/dma-attack]]
