---
title: LADD
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/BarakAharoni__LADD.md
updated: 2026-08-31
confidence: medium
---

# LADD

Linux **anti-debugging detection** tool implemented in C. Checks multiple indicators including **ptrace behavior**, **LD_PRELOAD tampering**, and **TracerPid** values in `/proc/self/status`. Detection logic is designed to execute early and report likely debugging conditions with simple runtime checks. Primary use case is anti-analysis research and defensive hardening experiments for Linux binaries. (source: wiki/sources/descriptions/BarakAharoni__LADD.md)

Complements the broader Linux anti-debug technique catalog [[adbg]], Windows integratable libraries such as [[cpp-anti-debug]], and educational packers such as [[kiteshield]] that also use ptrace-based anti-debug on Linux.

## Links

- Repo: https://github.com/BarakAharoni/LADD

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[adbg]] · [[cpp-anti-debug]] · [[anti-debugging]] · [[kiteshield]] · [[pince]] · [[edb-debugger]]
