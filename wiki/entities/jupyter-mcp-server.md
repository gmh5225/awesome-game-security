---
title: jupyter-mcp-server
kind: entity
topics: [overview, game-engine]
sources:
  - wiki/sources/descriptions/datalayer__jupyter-mcp-server.md
updated: 2026-08-16
confidence: medium
---

# jupyter-mcp-server

Model Context Protocol (MCP) server that exposes Jupyter notebook operations as MCP tools, enabling AI assistants to create, read, edit, and execute notebooks programmatically. Supports stdio and streamable HTTP transports and connects to local Jupyter servers, JupyterHub, or Google Colab. Fits the Game Develop → MCP server lane for AI-assisted data analysis and notebook-based computation in LLM tool-use pipelines. (source: wiki/sources/descriptions/datalayer__jupyter-mcp-server.md)

Complements generic MCP hosts such as [[zig-mcp-server]] and docs-retrieval bridges such as [[deepwiki-mcp]] by targeting interactive notebook workflows rather than editor or wiki APIs.

## Links

- Repo: https://github.com/datalayer/jupyter-mcp-server

## Related

[[overviews/overview]] · [[overviews/game-engine]] · [[zig-mcp-server]] · [[deepwiki-mcp]] · [[mcp-safety-scanner]]
