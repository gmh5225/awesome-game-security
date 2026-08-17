---
title: SENinja
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/borzacchiello__seninja.md
updated: 2026-08-17
confidence: medium
---

# SENinja

Binary Ninja symbolic execution plugin. Implements a symbolic execution engine that explores program paths through Binary Ninja's IL, tracking constraints on input values, detecting unreachable code, and identifying conditions required to reach specific program locations. The Python plugin provides an interactive UI for controlling symbolic exploration. Aimed at vulnerability researchers and reverse engineers using symbolic execution for path analysis and constraint solving in binary analysis. (source: wiki/sources/descriptions/borzacchiello__seninja.md)

BN-side symbolic-exec peer to Triton scaffolding via [[triton-bn]] and in-IDA [[ponce]]; complements radare2-backed [[radius2]] and function-level Unicorn harnesses via [[ripr]] rather than replacing them.

## Links

- Repo: https://github.com/borzacchiello/seninja

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[triton-bn]] · [[ponce]] · [[radius2]] · [[ripr]] · [[binary-ninja-mcp]]
