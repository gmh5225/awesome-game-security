---
title: angrop
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/angr__angrop.md
updated: 2026-08-18
confidence: medium
---

# angrop

**angrop** is an automatic **ROP gadget finder and chain builder** built on the **angr** framework. It uses symbolic execution, constraint solving, and graph search to model gadget effects and synthesize exploit chains programmatically. Implemented in Python with both CLI and API, and architecture-agnostic across multiple targets. Primarily useful for exploit development, binary research, and offensive security workflows that overlap with game client vulnerability analysis. (source: wiki/sources/descriptions/angr__angrop.md)

Complements gadget scanners such as [[ropgadget-rs]] and [[agafi]], constraint-driven chain builders such as [[exrop]], and other angr-based RE tools such as [[idadeflat]] and [[oxidizer]].

## Links

- Repo: https://github.com/angr/angrop

## Related

[[ropgadget-rs]] · [[agafi]] · [[exrop]] · [[idadeflat]] · [[oxidizer]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
