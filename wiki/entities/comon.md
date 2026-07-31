---
title: comon
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/lowleveldesign__comon.md
updated: 2026-07-31
confidence: medium
---

# comon

WinDbg extension for tracing COM interactions — class creations and interface querying — during live debugging. Useful for game-security researchers and reverse engineers studying offensive techniques in the cheat / WinDbg Plugins lane. (source: wiki/sources/descriptions/lowleveldesign__comon.md)

Complements JS WinDbg automation such as [[windbg-scripts]] and agent-facing CDB/WinDbg MCP tooling such as [[mcp-windbg]] by focusing specifically on COM factory and `QueryInterface` call paths rather than general kernel scripting or dump triage.

## Links

- Repo: https://github.com/lowleveldesign/comon (README tag: Trace COM)

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[windbg-scripts]] · [[mcp-windbg]] · [[ephemera]]
