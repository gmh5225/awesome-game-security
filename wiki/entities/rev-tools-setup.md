---
title: rev-tools-setup
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/lilyco-42__rev-tools-setup.md
updated: 2026-08-07
confidence: medium
---

# rev-tools-setup

One-click Windows setup for a reverse-engineering and anti-cheat research toolchain that AI agents can drive through the Model Context Protocol. A PowerShell installer uses Scoop to deploy memory analysis, debugging, binary analysis, network capture, and telemetry tools — Cheat Engine, Ghidra, x64dbg, DynamoRIO, Wireshark, YARA, ReClass.NET — plus Python packages including Frida, Scapy, PyTorch, and OpenCV. It also clones and configures a read-only Cheat Engine MCP server, writes MCP client settings for OpenCode and Claude Desktop, and includes scripts and documentation to verify connectivity and avoid common installation pitfalls. Targets security researchers and AI-assisted workflows for offline debugging, process analysis, cheat-table parsing, and MMO anti-cheat lab work on Windows 10 and 11. (source: wiki/sources/descriptions/lilyco-42__rev-tools-setup.md)

Complements bundled RE installers such as [[retoolkit]] and link catalogs such as [[retools]], but optimizes for agent-driven MCP workflows rather than a static tool bundle alone. Pairs with live CE MCP bridges such as [[cheatengine-mcp-bridge]] and standalone memory MCP servers such as [[memmcp]].

## Links

- Repo: https://github.com/lilyco-42/rev-tools-setup

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[retoolkit]] · [[retools]] · [[cheatengine-mcp-bridge]] · [[memmcp]] · [[x64dbg]] · [[frida]]
