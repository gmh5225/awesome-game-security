---
title: mcp-reverse
kind: entity
topics: [reverse-engineering, game-engine, game-hacking, anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/1llu50ry__mcp-reverse.md
updated: 2026-10-29
confidence: medium
---

# mcp-reverse

**mcp-reverse** (1llu50ry/mcp-reverse) is a **TypeScript/Node.js Model Context Protocol server** that exposes **180+ tools** aggregating reverse-engineering and game-debugging workflows for AI assistants (Claude, Cursor, Codex). **Sidecar bridge plugins** drive **Ghidra, IDA Pro, Binary Ninja, x64dbg, Cheat Engine, Frida, dnSpy, ILSpy, and ReClass.NET** from one hub so agents keep familiar disassemblers, debuggers, and live-memory tools instead of replacing them. Built-in **native modules** cover disassembly, **multi-backend decompilation caching**, signature and **YARA** scanning, ROP and memory analysis, **PDB/DWARF** support, game-engine helpers, and Cheat Engine server integration; an **agent mesh** coordinates multi-agent sessions. Shipped **example client configs**, **Docker/systemd** deployment, and cookbooks for decompilation, **VMProtect unpacking**, and mesh collaboration; README positions a bundled **anti-cheat skill corpus** beside the tool surface. Targets security researchers, malware analysts, CTF players, and game-security engineers who want LLM-assisted binary analysis without leaving existing toolchains. (source: wiki/sources/descriptions/1llu50ry__mcp-reverse.md)

Listed in the README under **Game Develop → MCP server** beside focused single-tool MCP servers such as [[binary-ninja-headless-mcp]], [[ida-pro-mcp]], and [[cheat-mcp]].

## Links

- Repo: https://github.com/1llu50ry/mcp-reverse

## Related

[[binary-ninja-headless-mcp]] · [[ghidra-headless-mcp]] · [[ida-pro-mcp]] · [[cheat-mcp]] · [[uc-mcp]] · [[rea]] · [[frida]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[research-rigor]]
