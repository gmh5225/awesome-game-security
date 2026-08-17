---
title: Self-Remapping Code
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/changeofpace__Self-Remapping-Code.md
updated: 2026-08-17
confidence: medium
---

# Self-Remapping Code

Windows proof-of-concept demonstrating **self-remapping code** as an **anti-tampering** technique. Creates multiple **virtual mappings** of the same **physical pages**, executing code from one mapping while **integrity-checking** another—making it difficult for debuggers and patching tools to modify running code without detection. The C implementation shows how **section-backed file mappings** can create **aliased views**. Aimed at software protection researchers studying **anti-patching** and **anti-debugging** through **memory aliasing**. (source: wiki/sources/descriptions/changeofpace__Self-Remapping-Code.md)

## Links

- Repo: https://github.com/changeofpace/Self-Remapping-Code

## Related

[[force-page-protection]] · [[memory-guard]] · [[pointer-guard]] · [[no-access-protection]] · [[voidmaw]] · [[integrity-experiments]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
