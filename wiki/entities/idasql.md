---
title: idasql
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/allthingsida__idasql.md
updated: 2026-08-18
confidence: medium
---

# idasql

**SQL interface to IDA Pro databases** with an AI-assisted natural-language query layer. IDASQL maps IDA analysis data — functions, strings, cross-references, types, and more — to **virtual SQL tables**, enabling query-driven binary analysis without writing IDAPython scripts. Runs as a **standalone CLI** against `.i64` files or as an **in-IDA plugin**, and exposes **remote query** endpoints so external tools or agents can interact with an active analysis session. (source: wiki/sources/descriptions/allthingsida__idasql.md)

Complements SQL-capable agent bridges such as [[ida-bridge]] and JSON CLI paths such as [[idac]] / [[ida-cli]]; consumed by agent harnesses such as [[re-harness]] (read-only IDA 9.3 + IDASQL workflows). Peers with MCP servers ([[ida-pro-mcp]], [[ida-mcp-server-plugin]]) that expose IDA to LLM agents over other transports.

## Links

- Repo: https://github.com/allthingsida/idasql

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-bridge]] · [[ida-cli]] · [[idac]] · [[ida-pro-mcp]] · [[re-harness]]
