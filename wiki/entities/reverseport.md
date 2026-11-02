---
title: ReversePort
kind: entity
topics: [reverse-engineering, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/laaielichter__Reverseport.md
updated: 2026-11-02
confidence: medium
---

# ReversePort

**laaielichter/Reverseport** — agent-oriented toolkit that pairs a **game and application porting engine** with a bundled **reverse-engineering analysis stack**, exposed through a CLI and **Model Context Protocol (MCP)** servers. The porting layer scans codebases, builds dependency graphs, compares versions, and applies engine-migration knowledge for targets such as **Godot**, **Unity**, **IL2CPP**, and common game archive formats; bundled agent skill packs guide port planning, Godot migrations, rebuilds, and verification with parity checks. The analysis side integrates disassemblers and decompilers including **Ghidra**, **IDA Pro**, **Hopper**, and **Kuna**, plus mobile and runtime tooling such as **JADX**, **Frida**, **LLDB**, **mitmproxy**, and **pwndbg**, with bridges in TypeScript/JavaScript as well as Java and Python helpers. Aimed at reverse engineers, game security researchers, and developers who want AI coding agents to help port, rebuild, or systematically investigate proprietary game and native binaries. (source: wiki/sources/descriptions/laaielichter__Reverseport.md)

## Links

- Repo: https://github.com/laaielichter/reverseport (README: MCP server and CLI for agent-driven game RE—Godot packs, Unity IL2CPP, native/.NET via Ghidra/IDA/Hopper, build diffing, cross-engine porting with parity checks)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[il2cpp]] · [[ghidra]] · [[reverse-this]] · [[reverify]]
