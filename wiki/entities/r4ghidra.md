---
title: r4ghidra
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/radareorg__r4ghidra.md
updated: 2026-10-15
confidence: medium
---

# r4ghidra

**r4ghidra** (radareorg) is a **Ghidra extension** that integrates **Radare2** with Ghidra so analysts can drive Ghidra’s analysis through a **radare2-style command environment**. The plugin is implemented mainly in **Java** and built with **Gradle** as a standard Ghidra module, with supporting **Python** and **Ruby** scripts for headless workflows and legacy tooling. It exposes an embedded **HTTP server** and a full **REPL command shell**, mapping common radare2 operations—seeking, flags, comments, analysis, decompilation, and scripting—to Ghidra’s program database via dedicated command handlers. Older companion scripts export Ghidra decompiler output into radare2 projects and sync symbols and comments between the two tools. The project targets reverse engineers who want Ghidra’s decompiler and UI with radare2 automation, including game and anti-cheat research workflows. (source: wiki/sources/descriptions/radareorg__r4ghidra.md)

Complements other Ghidra bridges such as [[gdbghidra]] (live GDB sync), [[ghidra-bridge]] (external CPython scripting), and agent-facing [[radare2-mcp]] / [[ghidra-headless-mcp]] paths when the goal is **r2pipe/r2web-style automation** against a Ghidra program database rather than a standalone r2 session.

## Links

- Repo: https://github.com/radareorg/r4ghidra (README: Ghidra extension with radare2-style REPL and r2pipe/r2web integration)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[iaito]] · [[radius2]] · [[r2garlic]] · [[radare2-mcp]] · [[gdbghidra]] · [[ghidra-bridge]]
