---
title: open-reverselab
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/LING71671__open-reverselab.md
updated: 2026-08-23
confidence: medium
---

# open-reverselab

**ReverseLab** — open-source reverse engineering laboratory combining a large executable knowledge base with automated tooling for hands-on security analysis. Ships 180+ technique articles and 100+ MCP automation tools organized into boards for web CTF, Android APK/DEX analysis, Windows PE binaries, cryptography, and game cheating or anti-cheat research. Agent-native workflow: detect signals, route through a knowledge router to relevant attack chains, and execute mapped steps via integrated tools such as [[ghidra]], [[frida]], [[x64dbg]], and [[jadx]]. Primary implementation is Python for scripts and MCP servers, with PowerShell, JavaScript, and shell automation for cross-platform setup. Targets reverse engineers, security researchers, CTF players, and AI agents performing authorized binary analysis, vulnerability research, and malware or game-protection investigation. (source: wiki/sources/descriptions/LING71671__open-reverselab.md)

Integrated multi-tool lab rather than a single-host MCP bridge — complements per-tool servers such as [[ghidramcp]], [[x64dbg-mcp]], and [[apktool-mcp-server]], and multi-format static MCP via [[glass]].

## Links

- Repo: https://github.com/ling71671/open-reverselab (README: agent-native RE lab with knowledge base, 100+ MCP tools, and APK/PE/game-cheating analysis workflows)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidramcp]] · [[x64dbg]] · [[x64dbg-mcp]] · [[frida]] · [[jadx]] · [[apktool-mcp-server]] · [[glass]]
