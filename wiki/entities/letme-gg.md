---
title: LetMeGG
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__LetMeGG.md
updated: 2026-08-11
confidence: medium
---

# LetMeGG

C++ proof-of-concept demonstrating techniques to **prevent WinDbg from breaking** into a target — i.e. block or interfere with kernel/user-mode debugger break-in and breakpoint delivery so WinDbg attach or break requests fail or stall. Aimed at low-level Windows, Linux, and mobile researchers studying **Some Tricks / Windows Ring0** anti-debug and anti-kernel-debug surfaces. (source: wiki/sources/descriptions/gmh5225__LetMeGG.md)

Complements offensive debugger-hiding drivers such as [[titanhide]] and stealth KD protocol tooling such as [[nokd]] on the anti-analysis side; pairs with defensive debugger-integrity checks such as [[wubbaboomark]] and anti-debug catalogs such as [[makin]].

## Links

- Repo: https://github.com/gmh5225/LetMeGG

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[titanhide]] · [[nokd]] · [[windbg-scripts]] · [[mcp-windbg]] · [[wubbaboomark]] · [[makin]]
