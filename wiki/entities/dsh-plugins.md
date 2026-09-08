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

Plugin bundle for the **DeepSeek Harness (DSH)** desktop AI assistant. Extends DSH with external tool integration and automation for security researchers and reverse engineers who want an AI-assisted malware, game-binary, and network-forensics workflow without leaving DSH. (source: wiki/sources/descriptions/GalaxyBatMan111__dsh-plugins.md)

**PyGhidra bridge:** Ghidra integration through a PyGhidra server — binary import, function decompilation, and string/xref queries.

**Forensics bridge:** Wraps radare2, RetDec, Wireshark tshark, and mitmproxy for binary analysis and packet capture.

**Agent bridge:** Delegates tasks to local Claude Code, OpenAI Codex, or Tencent Marvis agents with streaming background jobs.

**Implementation:** JavaScript plugins plus Python Ghidra scripts and web-scraping adapters; installs as DSH bundle profiles on Windows.

README category: Cheat / RE Tools.

Complements [[ghidra-bridge]] and [[ghidra-headless-mcp]] agent paths; pairs with [[dsh-cheatengine]] for DSH-side dynamic memory analysis. Pair automated decompile summaries with [[research-rigor]].

## Links

- Repo: https://github.com/GalaxyBatMan111/dsh-plugins

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra-bridge]] · [[ghidra-headless-mcp]] · [[reverify]] · [[dsh-cheatengine]] · [[research-rigor]]
