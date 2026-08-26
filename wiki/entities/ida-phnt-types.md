---
title: IDA PHNT Types
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Dump-GUY__IDA_PHNT_TYPES.md
updated: 2026-08-26
confidence: medium
---

# IDA PHNT Types

Converts **PHNT** (Process Hacker Native API) headers into **IDA Pro**-compatible type resources for reverse engineering. Ships generated **IDC** scripts and **TIL** type libraries for both **32-bit** and **64-bit** workflows, derived from modern **Windows SDK** and PHNT definitions. Built around C/C++ header processing with Hex-Rays tooling such as **idaclang** and **tilib**. Used by reverse engineers who need richer Windows internal types and function prototypes when analyzing system binaries, drivers, or anti-cheat components. (source: wiki/sources/descriptions/Dump-GUY__IDA_PHNT_TYPES.md)

Type-import lane—not live struct browsing ([[bb]], [[bb-viewer]]) or Hex-Rays annotation plugins ([[ntrays]], [[ida-kmdf]]). Complements PHNT-aware debuggers/plugins such as [[disable-parallel-loader]] and offline SDK introspection via [[bb]].

## Links

- Repo: https://github.com/Dump-GUY/IDA_PHNT_TYPES

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[apply-callee-type-ex]] · [[bb]] · [[bb-viewer]] · [[ntrays]] · [[ida-kmdf]]
