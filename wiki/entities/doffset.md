---
title: dOffset
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dNop90__dOffset.md
updated: 2026-08-16
confidence: medium
---

# dOffset

IDA Pro and Cheat Engine tooling to resolve the **offset of the current module**—bridging static disassembly addresses in IDA with live runtime module bases from Cheat Engine and other debuggers. Useful when performing static analysis of a binary while simultaneously debugging with multiple tools, including IDA Pro, Cheat Engine, x64dbg, and similar stacks. (source: wiki/sources/descriptions/dNop90__dOffset.md)

Targets game-security researchers and reverse engineers studying offensive techniques in the cheat / IDA Plugins lane—especially workflows that correlate IDA database addresses with in-process module RVAs during patch-sensitive RE.

## Links

- Repo: https://github.com/dNop90/dOffset

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ce-tracer-ida]] · [[ida-pro-loadmap]] · [[x64dbg]] · [[idaplugins]]
