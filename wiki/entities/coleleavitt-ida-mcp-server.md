---
title: coleleavitt IDA MCP Server
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/coleleavitt__ida-mcp-server.md
updated: 2026-11-12
confidence: medium
---

# coleleavitt IDA MCP Server

Native **C++17 IDA Pro 9.x plugin** that exposes a live IDA database to MCP clients over local HTTP—built with the official IDA SDK (no separate Python bridge). Ships **249 tools** spanning disassembly, Hex-Rays decompilation, microcode, types, cross-references, control-flow recovery, ObjC/C++ class reconstruction, byte patching, debugging, and IDAPython/IDC scripting. Uses Boost.Asio/Beast and `nlohmann_json`, supports multiple MCP protocol versions, and offers **core** vs **full** tool profiles to trade agent context size against automation depth. Targets reverse engineers and game-security analysts who want LLM-assisted workflows on in-session binary analysis. (source: wiki/sources/descriptions/coleleavitt__ida-mcp-server.md) (source: wiki/sources/README-categories.md)

Distinct from Python MCP bridges such as [[ida-mcp-server]] (MxIris standalone server + plugin), [[ida-pro-mcp]], [[headless-ida-mcp-server]], [[ida-mcp-server-plugin]], and [[kiln-ida]] by running entirely in-process as a C++ plugin rather than an external interpreter bridge.

## Links

- Repo: https://github.com/coleleavitt/ida-mcp-server

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[ida-mcp-server]] · [[ida-pro-mcp]] · [[headless-ida-mcp-server]] · [[binary-ninja-headless-mcp]] · [[mcp-reverse]]
