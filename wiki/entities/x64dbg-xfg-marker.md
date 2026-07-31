---
title: x64dbg XFG Marker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/m417z__x64dbg-xfg-marker.md
updated: 2026-07-31
confidence: medium
---

# x64dbg XFG Marker

[[x64dbg]] plugin that marks **XFG call signatures as data** in the disassembly view. Each signature is **8 bytes** and sits immediately **before** the target function—making forward-edge control-flow guard metadata visible during live debugging. Useful for game-security researchers and reverse engineers studying XFG-protected binaries and offensive x64dbg plugin workflows. (source: wiki/sources/descriptions/m417z__x64dbg-xfg-marker.md)

Pairs with broader CET / shadow-stack hardening research such as [[cet-research]] and [[windows-kernel-shadow-stack]] when modeling how hardware-enforced control-flow integrity affects exploit and hook analysis.

## Links

- Repo: https://github.com/m417z/x64dbg-xfg-marker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[xfindout]] · [[manytypes]] · [[classroom]]
