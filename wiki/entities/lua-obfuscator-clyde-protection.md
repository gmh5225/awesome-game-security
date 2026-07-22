---
title: Lua-Obfuscator-Clyde-Protection
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/sfr-development__Lua-Obfuscator-Clyde-Protection.md
updated: 2026-07-22
confidence: medium
---

# Lua-Obfuscator-Clyde-Protection

**Clyde** — from-scratch Luau obfuscator / protection toolkit (TypeScript): full lexer → parser → AST → obfuscator → VM pipeline with full Luau grammar (including type annotations). Multi-pass AST transforms include identifier renaming, string encoding, and control-flow scrambling with opaque predicates. Stronger modes compile to stack-based or register-based VMs with configurable opcode shuffle, constant encoding, polymorphic dispatch, and LZMA-compressed bytecode emitted as a self-contained Luau script. Ships a CLI (batch/CI) and an Express-served browser UI for protecting Luau game/client scripts (Roblox-oriented) against reverse engineering. (source: wiki/sources/descriptions/sfr-development__Lua-Obfuscator-Clyde-Protection.md)

Useful as a script-language VM-obfuscation reference alongside PE/native obfuscation engines—not a commercial AC product or unpacker.

## Links

- Repo: https://github.com/sfr-development/Lua-Obfuscator-Clyde-Protection

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[wprotect]] · [[alcatraz]] · [[kagura]] · [[obfcoder]] · [[opaque-predicates-detective]]
