---
title: iida-mcp
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/saileaxh__iida-mcp.md
updated: 2026-07-23
confidence: medium
---

# iida-mcp

Faster IDA Pro MCP plugin aimed at AI-agent reverse engineering: large tool surface (77 tools), multi-instance routing, and an optional Windows kernel companion driver (`iida-mcp-ioctl`) for live kernel memory/module access—so agents can combine static IDB analysis with dynamic kernel inspection over one MCP protocol. (source: wiki/sources/descriptions/saileaxh__iida-mcp.md)

Peers with other IDA agent bridges such as [[ida-mcp-server-plugin]] (MCP without a kernel driver), [[idac]] (JSON CLI; not MCP), and LLM assistants like [[aida]] / [[ida-assistant]]. The ioctl-driven kernel path also sits next to kernel debug MCP such as [[mcp-windbg]].

## Links

- Repo: https://github.com/saileaxh/iida-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ida-mcp-server-plugin]] · [[idac]] · [[aida]] · [[ida-assistant]] · [[mcp-windbg]] · [[ida-kmdf]]
