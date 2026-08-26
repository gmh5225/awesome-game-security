---
title: windbg-tool
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Devolutions__windbg-tool.md
updated: 2026-08-26
confidence: medium
---

# windbg-tool

Windows-first CLI and Model Context Protocol server that automates WinDbg-oriented debugging workflows, with a primary focus on Microsoft Time Travel Debugging (TTD) trace replay. Written mainly in Rust with a native C++ bridge to the TTD Replay API, it opens and navigates `.run` traces, inspects registers and memory, disassembles code, resolves symbols, and triages user or kernel crash dumps without manual debugger interaction. It can record new TTD traces, run one-shot live probes such as startup and managed breakpoints, and exposes stable JSON-oriented commands plus an MCP server so AI agents and scripts can drive analysis programmatically. A long-lived local daemon supports replay sessions; DbgEng remote-server helpers and utilities to install, update, and launch WinDbg round out the workflow. Targets reverse engineers, security researchers, and game-security analysts who need repeatable, automatable Windows debugging for crash investigation, behavioral analysis, and anti-cheat or malware research. (source: wiki/sources/descriptions/Devolutions__windbg-tool.md)

Complements Python CDB/WinDbg MCP such as [[mcp-windbg]], in-session LLM assistants such as [[windbg-copilot]], JS data-model automation such as [[windbg-scripts]] and [[windbg-cookbook]], and IDA-side TTD replay such as [[ttddbg]] by focusing on programmatic TTD replay, dump triage, and agent-driven WinDbg workflows from a Rust CLI rather than interactive WinDbg scripting or static IDA replay alone.

## Links

- Repo: https://github.com/Devolutions/windbg-tool (README tag: Windows CLI + MCP for WinDbg/TTD)

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[mcp-windbg]] · [[windbg-copilot]] · [[windbg-scripts]] · [[windbg-cookbook]] · [[ttddbg]]
