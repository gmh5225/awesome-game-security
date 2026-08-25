---
title: SEH Helper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/EliseZeroTwo__SEH-Helper.md
updated: 2026-08-25
confidence: medium
---

# SEH Helper

Binary Ninja plugin (Python) for inspecting **Structured Exception Handler (SEH)** chains in PE binaries. UI actions list SEH entries, inspect the handler at the cursor, or continuously follow cursor context — aimed at improving visibility into exception metadata during static analysis of Windows x86/x64 images, including malware and game-security investigations. (source: wiki/sources/descriptions/EliseZeroTwo__SEH-Helper.md)

Complements IDA-side SEH decompiler utilities such as [[happyida]] (Hex-Rays try/catch reconstruction) with BN-native PE exception-chain navigation. Pairs with other Binary Ninja analysis plugins such as [[tanto]], [[opaque-predicate-patcher]], and [[binary-ninja-mcp]] in protected-binary RE workflows.

## Links

- Repo: https://github.com/EliseZeroTwo/SEH-Helper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[happyida]] · [[bn]] · [[binary-ninja-mcp]] · [[tanto]] · [[gh-anti-debug-bypass-practice-tool]]
