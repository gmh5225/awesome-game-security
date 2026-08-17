---
title: ghidriff
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/clearbluejar__ghidriff.md
updated: 2026-08-17
confidence: medium
---

# ghidriff

Python-based Ghidra binary diffing framework that automates headless analysis of two binaries, correlates functions using multiple strategies (structural graph matching, version tracking, BSim similarity), and produces detailed Markdown reports with decompiled diffs, call-graph changes, and metadata deltas. Supports PE, Mach-O, and ELF across Windows, macOS, and Linux; includes Docker packaging for CI pipelines and a Docusaurus documentation site with guides for diffing **ntoskrnl**, **afd.sys** CVEs, and iOS dylibs. Aimed at vulnerability researchers, patch analysts, and reverse engineers comparing binary updates to identify security fixes and behavioral changes—including anti-cheat driver rebuilds and obfuscated client patches. (source: wiki/sources/descriptions/clearbluejar__ghidriff.md)

Ghidra-native complement to IDA-centric diffing via [[diaphora]], [[turbodiff]], and BinDiff/[[binexport]] pipelines; pairs with headless Ghidra automation such as [[ghidra-headless-mcp]] and the upstream [[ghidra]] framework.

## Links

- Repo: https://github.com/clearbluejar/ghidriff

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[diaphora]] · [[turbodiff]] · [[binexport]] · [[cognitor]] · [[windiff]]
