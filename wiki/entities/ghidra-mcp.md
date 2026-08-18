---
title: ghidra-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bethington__ghidra-mcp.md
updated: 2026-08-18
confidence: medium
---

# ghidra-mcp

Model Context Protocol server and Ghidra extension that bridges Ghidra reverse engineering with AI coding agents for programmatic binary analysis and annotation. Combines a Java Ghidra extension (GUI plugin and headless HTTP server) with a Python MCP bridge exposing 200+ tools for decompilation, function and data-type editing, comments, cross-references, and related RE workflows. Notable capabilities include BSim and optional knowledge-database integration, headless parity with the GUI, streamable HTTP or stdio transports, a Windows-oriented debugger path for live analysis, and Maven/Gradle or Docker deployment. (source: wiki/sources/descriptions/bethington__ghidra-mcp.md)

Broader Ghidra MCP surface than [[ghidra-headless-mcp]] (40+ headless tools with fake backend) and complementary to in-Ghidra [[ghidrassist-mcp]] / [[ghidrassist]] LLM panels—this path targets agent-driven documentation and analysis inside Ghidra for reverse engineers and game-security researchers.

## Links

- Repo: https://github.com/bethington/ghidra-mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-headless-mcp]] · [[ghidrassist-mcp]] · [[ghidrassist]] · [[ghidra-bridge]] · [[binary-ninja-mcp]] · [[ida-pro-mcp]]
