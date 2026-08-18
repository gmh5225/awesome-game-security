---
title: Glass
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/azw413__Glass.md
updated: 2026-08-18
confidence: medium
---

# Glass

Rust-based multi-architecture binary analysis toolkit supporting ARM64, x86-64, ELF, Mach-O, DEX, and PE formats. Provides disassembly, control-flow graph construction, cross-references, pattern matching, and binary patching through a CLI and a built-in MCP server for mobile RE workflows. (source: wiki/sources/descriptions/azw413__Glass.md)

CLI verbs include `disasm`, `search`, `cfg-of`, `dex-callers`, `bin-search`, and `insn-search`; `glass mcp` exposes the same operations as MCP tools on APK, IPA, and AArch64 binaries for LLM agents. Complements decode-oriented MCP servers such as [[apktool-mcp-server]] and [[delamain]] with native disassembly and CFG/xref analysis; peers with multi-format static tools such as [[garlic]] and [[farm64]] in the Rust/mobile static-analysis lane.

## Links

- Repo: https://github.com/azw413/Glass

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[apktool-mcp-server]] · [[delamain]] · [[garlic]] · [[farm64]] · [[mobile-re-skill]] · [[binary-analysis-mcps]]
