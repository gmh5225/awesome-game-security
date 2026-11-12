---
title: idasignwriter
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/crackinglandia__idasignwriter.md
updated: 2026-11-12
confidence: medium
---

# idasignwriter

IDA Pro **SigWriter** plugin (IDAPython; PyQt5 on IDA 8.2, PySide6 on IDA 9.3+) that builds byte-level code patterns from the analyst’s selection in a dockable GUI with fine-grained wildcard control. It can automatically wildcard jumps, calls, global and RIP-relative references, immediates, fixups, and ambiguous operands on ARM, MIPS, and other ISAs. Patterns export as IDA or x64dbg/Cheat Engine strings, C/C++ arrays with masks, YARA rules, raw hex, or masked binary blobs; the plugin can search the IDB for matches. A companion **.NET** variant generates CIL patterns from managed binaries with the same export options. (source: wiki/sources/descriptions/crackinglandia__idasignwriter.md)

Targets reverse engineers and game-security researchers who need durable cross-build signatures—not just IDA-native strings but portable formats for scanners and cheat offset pipelines. Complements [[ida-sigmaker]], [[sigmakerex]], [[ida-pro-sigmaker]], and [[binja-sigmaker]]; YARA output sits beside [[yarka]] and [[hyara]].

## Links

- Repo: https://github.com/crackinglandia/idasignwriter

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-sigmaker]] · [[sigmakerex]] · [[ida-pro-sigmaker]] · [[binja-sigmaker]] · [[signature-forge]] · [[yarka]]
