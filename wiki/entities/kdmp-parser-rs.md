---
title: kdmp-parser-rs
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/0vercl0k__kdmp-parser-rs.md
updated: 2026-11-06
confidence: medium
---

# kdmp-parser-rs

**kdmp-parser-rs** (0vercl0k) is a **dependency-free Rust library** for parsing Windows **kernel crash dumps** produced by the OS and WinDbg. It provides cross-platform, read-only access to dump contents: physical memory pages, CPU register and exception context, and loaded user and kernel module lists. **Virtual addresses** are resolved by walking page tables through dedicated physical and virtual memory readers, with optional strict errors when pages were not captured in the dump. A bundled **example CLI** can dump headers, context records, modules, and memory via memory-mapped or file-based I/O—useful for **kernel debugging**, **crash forensics**, and **reverse engineering** workflows that inspect dumps outside the Windows debugger stack. (source: wiki/sources/descriptions/0vercl0k__kdmp-parser-rs.md)

Rust counterpart to the C++ [[kdmp-parser]] crate; complements user-mode [[udmp-parser]], trace symbolization via [[symbolizer]], WinDbg snapshot capture via [[snapshot]], and sibling fuzzing tooling [[wtf]].

## Links

- Repo: https://github.com/0vercl0k/kdmp-parser-rs

## Related

[[kdmp-parser]] · [[udmp-parser]] · [[symbolizer]] · [[snapshot]] · [[wtf]] · [[windbg-tool]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
