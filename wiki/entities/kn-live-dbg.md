---
title: kn-live-dbg
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/kernullist__kn-live-dbg.md
updated: 2026-08-02
confidence: medium
---

# kn-live-dbg

Windows kernel-level **live debugging toolkit**: a kernel driver exposes memory inspection, module enumeration, and Zydis-based disassembly; a user-mode CLI TUI handles symbols, types, and interactive UX in a LiveKD-style workflow without requiring a traditional kernel debugger (KD) setup. Aimed at game-security researchers and reverse engineers studying offensive kernel inspection in the cheat / WinDbg Plugins lane. (source: wiki/sources/descriptions/kernullist__kn-live-dbg.md)

Complements WinDbg attach automation such as [[windbg-scripts]], agent-facing [[mcp-windbg]], and in-WinDbg LLM decompile via [[windbg-decompile-ext]] from the same maintainer — but targets driver-backed live kernel memory access and CLI exploration rather than CDB scripting or pseudocode generation. Pair with [[windows-kernel-debugging-guide]] for remote KD setup reference and [[research-rigor]] when generalizing structure offsets across builds.

## Links

- Repo: https://github.com/kernullist/kn-live-dbg (README tag: Windows kernel live debugging — driver exposes memory primitives, user-mode TUI handles symbols, types, and UX (LiveKD-style))

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[windbg-decompile-ext]] · [[windbg-scripts]] · [[mcp-windbg]] · [[windows-kernel-debugging-guide]] · [[research-rigor]]
