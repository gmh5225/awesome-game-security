---
title: ida-mcp-server-plugin
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/taida957789__ida-mcp-server-plugin.md
updated: 2026-07-20
confidence: medium
---

# ida-mcp-server-plugin

IDA Pro Python plugin that runs a Model Context Protocol (MCP) server, exposing IDA analysis to AI assistants and MCP clients. Clients can query disassembly, decompilation, cross-references, function info, and type data from a live IDB remotely—bridging IDA with LLM-assisted reverse-engineering workflows. (source: wiki/sources/descriptions/taida957789__ida-mcp-server-plugin.md)

Complements agent-facing IDA CLIs such as [[idac]] (JSON over Unix socket; not MCP) and remote IDB UIs such as [[idarem]]; this path is the MCP-protocol bridge into IDA itself.

## Links

- Repo: https://github.com/taida957789/ida-mcp-server-plugin

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idac]] · [[idarem]] · [[symbridge]] · [[memmcp]] · [[apktool-mcp-server]]
