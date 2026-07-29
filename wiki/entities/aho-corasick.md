---
title: aho-corasick
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/mischasan__aho-corasick.md
updated: 2026-07-29
confidence: medium
---

# aho-corasick

High-performance Aho-Corasick multi-pattern string matching library from mischasan. Uses an Interleaved State-transition Matrix (ISM) representation tuned for both minimal memory footprint and maximum search throughput. Supports memory-mapped serialization so compiled automata can be persisted and reused, and exposes a C API to build, query, and dump the compiled state machine. (source: wiki/sources/descriptions/mischasan__aho-corasick.md)

Useful as a building block for AC signature-scan backends, YARA-style rule engines, and RE tooling that must scan files or memory for many fixed strings in one pass—complementary to SIMD byte-pattern scanners such as [[patternsleuth]] and IDA-side signature tooling such as [[ida-fusion]].

## Links

- Repo: https://github.com/mischasan/aho-corasick

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[patternsleuth]] · [[ida-fusion]] · [[apkid]]
