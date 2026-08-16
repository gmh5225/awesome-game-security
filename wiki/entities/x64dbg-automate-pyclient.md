---
title: x64dbg-automate-pyclient
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dariushoule__x64dbg-automate-pyclient.md
updated: 2026-08-16
confidence: medium
---

# x64dbg-automate-pyclient

Reference Python client for automating [[x64dbg]] through the x64dbg Automate RPC protocol. Uses ZeroMQ with msgpack serialization for synchronous commands and asynchronous debug events, wrapping low-level RPC calls in higher-level APIs for breakpoints, memory and register access, assembly and disassembly, session control, and GUI operations. Ships an optional Model Context Protocol (MCP) server so LLM-based agents can drive x64dbg sessions. Primary use cases are malware analysis, reverse engineering, and vulnerability hunting where scripted or agent-assisted debugger control is needed. (source: wiki/sources/descriptions/dariushoule__x64dbg-automate-pyclient.md)

External Python RPC + MCP automation rather than an in-debugger plugin: complements [[x64dbg-rippy]] (WebView2 chat panel inside x64dbg) and MCP bridges such as [[ida-pro-mcp]], [[binary-ninja-mcp]], and [[radare2-mcp]] for repeatable, scriptable Windows user-mode attach workflows.

## Links

- Repo: https://github.com/dariushoule/x64dbg-automate-pyclient

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[x64dbg-rippy]] · [[ida-pro-mcp]] · [[binary-ninja-mcp]] · [[radare2-mcp]] · [[chaiscript-plugin]]
