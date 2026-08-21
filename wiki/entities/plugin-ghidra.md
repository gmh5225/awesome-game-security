---
title: plugin-ghidra
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/RevEngAI__plugin-ghidra.md
updated: 2026-08-21
confidence: medium
---

# plugin-ghidra

Ghidra extension that connects the disassembler to the **RevEng.AI** AI-assisted reverse engineering platform. Written in Java as a Gradle-built Ghidra plugin (targets Ghidra 11.4+ and Java 21), it uploads the currently open binary for remote analysis. Supports binary code similarity, individual and batch function matching/renaming against known similar functions, and AI-powered decompilation views. Aimed at reverse engineers working on stripped or otherwise hard-to-analyze binaries who want ML-assisted function identification and decompilation inside Ghidra. (source: wiki/sources/descriptions/RevEngAI__plugin-ghidra.md)

Ghidra-native counterpart to [[reai-ida]] on IDA Pro; complements local signature renaming ([[renamaida]]), cloud function recognition ([[finger]]), OpenAI Ghidra assistants ([[ghidra-openai]], [[ghidrassist]]), and MCP bridges ([[ghidra-mcp]])—verify platform-suggested names and decompilation against disassembly per [[research-rigor]].

## Links

- Repo: https://github.com/RevEngAI/plugin-ghidra

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[reai-ida]] · [[ghidra]] · [[ghidra-openai]] · [[ghidrassist]] · [[ghidra-mcp]] · [[renamaida]] · [[finger]] · [[research-rigor]]
