---
title: PoCsmith
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/originsec__pocsmith.md
updated: 2026-07-26
confidence: medium
---

# PoCsmith

AI-driven Windows PoC exploit generation framework: LLM agents with MCP tools analyze CVEs / patchwatch diff reports, then iteratively write, compile, and verify working exploits with budget tracking and reporting. README positions a Claude agent plus MCP bridges (Hyper-V, kd, Ghidra) that develop and validate PoCs on pre-patch VMs—useful for agent-augmented Windows vuln RE alongside dump/debug MCP peers such as [[mcp-windbg]]. (source: wiki/sources/descriptions/originsec__pocsmith.md)

## Links

- Repo: https://github.com/originsec/pocsmith

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[mcp-windbg]] · [[windows-kernel-exploits]] · [[cve-2026-40369-exploit]]
