---
title: gui-plugin-template
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/danielplohmann__gui-plugin-template.md
updated: 2026-08-16
confidence: medium
---

# gui-plugin-template

Python plugin template providing a cross-compatible GUI framework for building disassembler plugins that run on **IDA Pro**, **Ghidra**, **Binary Ninja**, and **Cutter** via PyQt/PySide. Abstracts each host's native API behind a harmonized interface layer so developers maintain one GUI codebase instead of separate per-tool implementations. Aimed at reverse engineers and security researchers shipping portable binary-analysis plugins. (source: wiki/sources/descriptions/danielplohmann__gui-plugin-template.md)

Scaffolding for **plugin UI portability**—not analysis logic itself. Complements cross-disassembler annotation sync via [[binsync]], multi-host YARA rule generation via [[hyara]], and IDA-only GUI tooling such as [[classy]] and [[mcrit-plugin]] from the same author lane.

## Links

- Repo: https://github.com/danielplohmann/gui-plugin-template

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[binsync]] · [[hyara]] · [[mcrit-plugin]] · [[classy]] · [[idaplugins]]
