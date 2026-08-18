---
title: MAMBO
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/beehive-lab__mambo.md
updated: 2026-08-18
confidence: medium
---

# MAMBO

**MAMBO** is beehive-lab’s **low-overhead dynamic binary instrumentation framework** for **ARM and AArch64 on Linux**. It translates and instruments machine code at runtime through a **software code cache**, supporting instruction-level callbacks, basic-block tracing, function interception, and custom analysis plugins. The C framework runs transparently on unmodified binaries — aimed at security researchers, performance analysts, and tool builders needing lightweight ARM DBI. (source: wiki/sources/descriptions/beehive-lab__mambo.md)

Complements ARM64 RE tooling ([[farm64]] disassembly) and mobile/native hook stacks ([[adbi]], [[qbdi-tracer-android]]) in the Linux ARM instrumentation lane.

## Links

- Repo: https://github.com/beehive-lab/mambo

## Related

[[dynamic-binary-instrumentation]] · [[adbi]] · [[qbdi-tracer-android]] · [[farm64]] · [[frida]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
