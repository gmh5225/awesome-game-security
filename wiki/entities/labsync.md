---
title: LabSync
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cellebrite-labs__LabSync.md
updated: 2026-08-17
confidence: medium
---

# LabSync

IDA Pro plugin (Cellebrite Labs) that **partially synchronizes IDBs** between reverse engineers working on the same binary through a shared **Git** repository. On each save it exports names, types, inlined functions, and other IDB metadata to **YAML**, then commits, pushes, and pulls changes through Git with automatic merge-conflict resolution via **git mergetool**. IDBs are keyed by the **MD5** of the input file so analysts stay aligned across machines. Designed for frequent, non-intrusive syncs when teams need lightweight annotation exchange without sharing full database files. (source: wiki/sources/descriptions/cellebrite-labs__LabSync.md)

Complements real-time co-editing via [[idarling]] and cross-disassembler Git sync via [[binsync]]—LabSync targets IDA-only, Git-versioned partial IDB metadata rather than live multi-user sessions or Ghidra/Binary Ninja hosts.

## Links

- Repo: https://github.com/cellebrite-labs/LabSync

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idarling]] · [[binsync]] · [[ida-migrator]] · [[idarem]] · [[ida-bridge]]
