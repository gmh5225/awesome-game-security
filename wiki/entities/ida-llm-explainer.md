---
title: ida-llm-explainer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/pgarba__ida-llm-explainer.md
updated: 2026-07-26
confidence: medium
---

# ida-llm-explainer

IDA Pro plugin that uses a local llama.cpp server to explain functions and propose renames, types, and comments in Hex-Rays or disassembly—without writing to the IDB until you accept. Streams model output live with human-in-the-loop checkboxes; can rename functions/locals/labels/callees/globals, infer structs, recover packed string tables, and run call-graph-aware batch/recursive workflows across multiple llama-server endpoints. Also exports compiler-verified standalone C (optional Compiler Explorer) and offers CFG recovery/optional patching for obfuscated x86/x64 and AArch64. Aimed at private, offline LLM-assisted RE of protected or game-related binaries (cheat / IDA Plugins). (source: wiki/sources/descriptions/pgarba__ida-llm-explainer.md)

Complements cloud/chat IDA assistants such as [[aida]] and [[ida-assistant]], and agent bridges like [[ida-mcp-server-plugin]] / [[iida-mcp]]—this path keeps inference local via llama.cpp with explicit accept before database writes.

## Links

- Repo: https://github.com/pgarba/ida-llm-explainer

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[aida]] · [[ida-assistant]] · [[ida-mcp-server-plugin]] · [[iida-mcp]] · [[idaplugins]]
