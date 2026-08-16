---
title: x64dbg-rippy
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dariushoule__x64dbg-rippy.md
updated: 2026-08-16
confidence: medium
---

# x64dbg-rippy

AI-powered reverse engineering assistant plugin for [[x64dbg]] that embeds a WebView2 chat panel directly in the debugger. Connects to Anthropic or OpenAI-compatible LLM APIs and exposes tool-use so the agent can read memory, disassemble code, set breakpoints, single-step, and drive the debugger programmatically through a conversational interface — aimed at interactive AI-assisted debugging and automated analysis inside x64dbg. (source: wiki/sources/descriptions/dariushoule__x64dbg-rippy.md)

In-debugger LLM panel rather than an external MCP server: complements MCP bridges such as [[ida-pro-mcp]], [[binary-ninja-mcp]], and [[radare2-mcp]] by keeping live Windows user-mode attach workflows inside the x64dbg UI.

## Links

- Repo: https://github.com/dariushoule/x64dbg-rippy

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[ida-pro-mcp]] · [[binary-ninja-mcp]] · [[radare2-mcp]] · [[rev-tools-setup]]
