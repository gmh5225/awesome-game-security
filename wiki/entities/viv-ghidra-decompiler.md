---
title: viv-ghidra-decompiler
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/atlas0fd00m__viv-ghidra-decompiler.md
updated: 2026-08-18
confidence: medium
---

# viv-ghidra-decompiler

Vivisect extension that bridges Vivisect **symbolik** symbolic analysis with Ghidra's decompiler. The Python side extracts symbols, function signatures, and analysis from Vivisect and shows decompiled C pseudocode in a Qt dock widget; a Java Ghidra plugin applies enriched symbols and optionally injects custom p-code before decompilation. A headless Ghidra backend communicates over JSON-RPC/TCP. Primary mode sends Vivisect-derived symbol names, types, and signatures to Ghidra for improved decompilation; an experimental fallback translates symbolik effects into Ghidra p-code when Vivisect analysis disagrees with Ghidra Sleigh lifting. (source: wiki/sources/descriptions/atlas0fd00m__viv-ghidra-decompiler.md)

Targets reverse engineers and binary analysts who want Vivisect's symbolic reasoning combined with Ghidra's high-quality decompilation—useful for game security, anti-cheat, and malware RE workflows. Complements in-IDA Ghidra decompilation via [[blc]] and headless Ghidra peers such as [[ghiradec]] and [[ghidra-bridge]].

## Links

- Repo: https://github.com/atlas0fd00m/viv-ghidra-decompiler

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-bridge]] · [[blc]] · [[ghiradec]] · [[ghidra-decompiler-plugins]]
