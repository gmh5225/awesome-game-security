---
title: AIMachDec
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/s3rg0x__AIMachDec.md
updated: 2026-07-23
confidence: medium
---

# AIMachDec

IDA plugin for Apple AARCH64/ARM64 binaries that uses LLMs to translate assembly functions into readable pseudo-code in C, Objective-C, or Swift. Targets Mach-O analysis—including iOS apps, kernelcaches, and dyld_shared_cache libraries—for game-security researchers and RE practitioners in the cheat / IDA Plugins lane. (source: wiki/sources/descriptions/s3rg0x__AIMachDec.md)

Complements Apple/iOS IDA helpers such as [[ida-ios-helper]] and other LLM/agent IDA paths ([[aida]], [[ida-assistant]], [[ida-mcp-server-plugin]])—this project focuses on ARM64 Mach-O decompilation via LLMs rather than Windows C++ RE chat or MCP bridges.

## Links

- Repo: https://github.com/s3rg0x/AIMachDec

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[ida-ios-helper]] · [[aida]] · [[ida-assistant]] · [[ida-mcp-server-plugin]] · [[idaplugins]]
