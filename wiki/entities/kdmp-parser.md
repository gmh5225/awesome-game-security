---
title: kdmp-parser
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/0vercl0k__kdmp-parser.md
updated: 2026-09-06
confidence: medium
---

# kdmp-parser

**kdmp-parser** (0vercl0k) is a **C++ parsing library and toolset** for Windows **kernel crash dumps**. It supports **full** and **active** dump formats and exposes context records, exception information, bugcheck parameters, and physical memory views through library APIs and a standalone parser CLI. The repository ships CMake build scripts, automated tests, and optional **Python bindings** for scripting workflows—aimed at low-level **crash forensics**, **kernel debugging automation**, and **exploitation research**. (source: wiki/sources/descriptions/0vercl0k__kdmp-parser.md)

Rust reimplementation: [[kdmp-parser-rs]] (dependency-free crate; phys/virt readers and page-table walks; example CLI). Complements sibling user-mode minidump tooling [[udmp-parser]], execution-trace symbolization via [[symbolizer]], WinDbg snapshot capture via [[snapshot]], and sibling 0vercl0k fuzzing tooling [[wtf]].

## Links

- Repo: https://github.com/0vercl0k/kdmp-parser

## Related

[[kdmp-parser-rs]] · [[udmp-parser]] · [[symbolizer]] · [[snapshot]] · [[wtf]] · [[windbg-tool]] · [[windbg-js-scripts]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
