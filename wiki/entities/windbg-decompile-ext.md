---
title: windbg-decompile-ext
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/kernullist__windbg-decompile-ext.md
updated: 2026-08-02
confidence: medium
---

# windbg-decompile-ext

WinDbg x64 extension that disassembles live functions and uses an LLM to produce verified pseudocode. Fastest integration path is to vendor the header and import library into the project. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / WinDbg Plugins lane. (source: wiki/sources/descriptions/kernullist__windbg-decompile-ext.md)

Complements agent-facing WinDbg MCP such as [[mcp-windbg]], JS automation via [[windbg-scripts]], and IDA-side LLM decompiler assistants such as [[daila]] — but targets live attach/decompile inside WinDbg rather than dump triage or static IDA workflows. Verify model output against disassembly per [[research-rigor]].

## Links

- Repo: https://github.com/kernullist/windbg-decompile-ext (README tag: WinDbg x64 extension that disassembles live functions and uses an LLM to produce verified pseudocode)

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[mcp-windbg]] · [[windbg-scripts]] · [[daila]] · [[research-rigor]]
