---
title: ida-no-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/P4nda0s__IDA-NO-MCP.md
updated: 2026-08-22
confidence: medium
---

# ida-no-mcp

**IDA NO MCP** exports IDA Pro decompilation and analysis artifacts as plain source files so AI coding tools can reverse-engineer binaries **without an MCP bridge**. Dual-track delivery: a Python IDA plugin for interactive GUI exports and a Rust CLI binary (`inp`) powered by **idalib** for large binaries, batch jobs, and skipping hung auto-analysis. (source: wiki/sources/descriptions/P4nda0s__IDA-NO-MCP.md)

Exports include decompiled C (or disassembly fallback), caller/callee metadata, strings, imports/exports, optional memory hexdumps, call graphs, and an `AGENTS.md` guide for AI IDEs. Layout modes switch between per-function files and a consolidated tree for databases with tens of thousands of functions. Targets reverse engineers who want fast, low-friction AI-assisted binary analysis in tools like Cursor or Claude Code.

Contrasts with live MCP servers such as [[ida-pro-mcp]], [[headless-ida-mcp-server]], and [[ida-cli]] by materializing a file corpus agents read directly rather than calling IDA over MCP. Complements whole-program export pipelines such as [[tocode]] and read-only harnesses such as [[re-harness]].

## Links

- Repo: https://github.com/P4nda0s/IDA-NO-MCP

## Related

[[overviews/reverse-engineering]] · [[research-rigor]] · [[ida-cli]] · [[ida-pro-mcp]] · [[headless-ida-mcp-server]] · [[ida-nexus-docker]] · [[tocode]] · [[re-harness]]
