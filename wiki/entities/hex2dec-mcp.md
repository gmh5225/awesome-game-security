---
title: hex2dec-mcp
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__hex2dec-mcp.md
updated: 2026-08-08
confidence: medium
---

# hex2dec-mcp

MCP (Model Context Protocol) server that converts between hexadecimal and decimal numbers for AI agent workflows. Written in JavaScript and TypeScript; fits the Game Develop → MCP server lane. Useful for game developers, reverse engineers, and tooling builders who need agents to normalize numeric literals during memory-offset, pointer, and protocol-field work without manual calculator steps. (source: wiki/sources/descriptions/gmh5225__hex2dec-mcp.md)

Complements domain-specific MCP bridges such as [[memmcp]] (CE-like memory tooling) and [[ida-pro-mcp]] (IDA automation) by providing a small numeric-conversion utility rather than live RE or editor integration.

## Links

- Repo: https://github.com/gmh5225/hex2dec-mcp

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[zig-mcp-server]] · [[deepwiki-mcp]] · [[mcpup]]
