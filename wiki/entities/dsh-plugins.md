---
title: DSH Plugins
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/GalaxyBatMan111__dsh-plugins.md
  - wiki/sources/README-categories.md
updated: 2026-09-08
confidence: medium
---

# DSH Plugins

Plugin bundle for the **DeepSeek Harness (DSH)** desktop AI assistant. Extends DSH with external tool integration: a **PyGhidra** bridge for binary import, function decompilation, and string/xref queries; a forensics bridge wrapping radare2, RetDec, Wireshark tshark, and mitmproxy; and an agent bridge delegating tasks to local Claude Code, OpenAI Codex, or Tencent Marvis agents with streaming background jobs. JavaScript plugins plus Python Ghidra scripts install as DSH bundle profiles on Windows. Targets security researchers and reverse engineers who want an AI-assisted malware, game-binary, and network-forensics workflow without leaving DSH. (source: wiki/sources/descriptions/GalaxyBatMan111__dsh-plugins.md)

Complements [[ghidra-bridge]] and [[ghidra-headless-mcp]] agent paths; pair automated decompile summaries with [[research-rigor]].

## Links

- Repo: https://github.com/GalaxyBatMan111/dsh-plugins

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra-bridge]] · [[ghidra-headless-mcp]] · [[reverify]] · [[dsh-cheatengine]] · [[research-rigor]]
