---
title: dk
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/long123king__dk.md
updated: 2026-07-31
confidence: medium
---

# dk

Refactored WinDbg extension based on **tokenext** for visualizing token-related pointer relationships during live kernel debugging. SVG overlays color-code local-buffer pointers (green), symbol pointers (red), and heap-allocation pointers (blue); heap allocation change history renders as clickable blue rectangles for tracing allocation churn. Useful for game-security researchers and reverse engineers in the Cheat → WinDbg Plugins lane. (source: wiki/sources/descriptions/long123king__dk.md)

Complements general WinDbg scripting such as [[windbg-scripts]], COM tracing via [[comon]], and agent-facing dump triage via [[mcp-windbg]] by focusing on interactive token/heap pointer visualization rather than automation scripts or COM factory paths.

## Links

- Repo: https://github.com/long123king/dk (README tag: Refactored version of tokenext)

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[windbg-scripts]] · [[comon]] · [[mcp-windbg]] · [[ephemera]]
