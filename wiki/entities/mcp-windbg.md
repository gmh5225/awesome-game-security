---
title: mcp-windbg
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/svnscha__mcp-windbg.md
updated: 2026-07-21
confidence: medium
---

# mcp-windbg

Python MCP (Model Context Protocol) server that wraps CDB/WinDbg sessions so AI models can triage Windows crash dumps and attach to remote debugging sessions. Includes dump-triage prompts and sample crash programs (null deref, heap overflow, divide-by-zero) for exercising agent-driven debugging workflows. Useful for reverse engineers and kernel developers seeking AI-augmented dump analysis alongside classic WinDbg automation. (source: wiki/sources/descriptions/svnscha__mcp-windbg.md)

Complements JS WinDbg scripting such as [[windbg-scripts]], offline WinDbg-flavored dump tools such as [[ephemera]], and other agent MCP bridges such as [[ida-mcp-server-plugin]] / [[memmcp]] by targeting live CDB/WinDbg rather than IDA or CE-style memory UIs.

## Links

- Repo: https://github.com/svnscha/mcp-windbg (README tag: MCP for WinDBG)

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[windbg-scripts]] · [[ephemera]] · [[minidumpreader]] · [[ida-mcp-server-plugin]] · [[memmcp]]
