---
title: SwishDbgExt
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/comaeio__SwishDbgExt.md
updated: 2026-08-16
confidence: medium
---

# SwishDbgExt

Microsoft WinDbg debugging extension that expands the available command set and fixes or improves existing built-in WinDbg commands. Developed by Matt Suiche (@msuiche) at Comae. Useful for game-security researchers and reverse engineers studying offensive techniques in the cheat / WinDbg Plugins lane. (source: wiki/sources/descriptions/comaeio__SwishDbgExt.md)

Complements JS WinDbg automation such as [[windbg-scripts]], specialized trace extensions such as [[comon]] and [[dk]], agent-facing CDB/WinDbg MCP such as [[mcp-windbg]], and LLM decompiler extension [[windbg-decompile-ext]] — but focuses on richer native WinDbg commands rather than scripting, COM tracing, or agent triage.

Related Comae tooling includes [[dumpit-mirror]] for live physical-memory capture feeding Volatility / WinDbg offline analysis.

## Links

- Repo: https://github.com/comaeio/SwishDbgExt

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[windbg-scripts]] · [[comon]] · [[dk]] · [[mcp-windbg]] · [[windbg-decompile-ext]] · [[dumpit-mirror]]
