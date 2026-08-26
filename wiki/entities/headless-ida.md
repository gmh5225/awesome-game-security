---
title: headless-ida
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/DennyDai__headless-ida.md
updated: 2026-08-26
confidence: medium
---

# headless-ida

**Python toolkit for running IDA Pro in headless workflows** — usable as a module or command-line utility to execute **IDAPython scripts**, run **one-liners**, and open **interactive sessions** without the GUI. Supports a **remote server mode** through **RPyC** and can work with **idat64** or **idalib** backends. Primary use case is scalable reverse engineering automation for malware analysis, binary research, and game security investigations. (source: wiki/sources/descriptions/DennyDai__headless-ida.md)

Sits in the headless IDA automation lane beneath MCP/agent bridges ([[ida-cli]], [[headless-ida-mcp-server]], [[ida-mcp-rs]]) and beside terminal-oriented idalib tools ([[ida-buddy]], [[idac]], [[ida-bridge]], [[ida-rpc]]). Emphasizes **scriptable IDAPython execution** and **RPyC remote sessions** rather than MCP protocol transport.

## Links

- Repo: https://github.com/DennyDai/headless-ida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-buddy]] · [[ida-cli]] · [[headless-ida-mcp-server]] · [[idac]] · [[ida-bridge]] · [[ida-rpc]]
