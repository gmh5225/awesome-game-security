---
title: kernel-callback-removal
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/V-i-x-x__kernel-callback-removal.md
updated: 2026-08-20
confidence: medium
---

# kernel-callback-removal

Documents and implements an **ETW-TI kernel bypass** that toggles provider state from kernel memory. Explains locating relevant Windows kernel structures, discovering offsets, and modifying enable flags using an existing read/write primitive. Combines C++ implementation with detailed WinDbg and IDA-based reverse-engineering notes for advanced pentesters and defenders studying EDR bypass methods. (source: wiki/sources/descriptions/V-i-x-x__kernel-callback-removal.md)

Sits in the same blind-telemetry lane as [[edrsandblast]] and [[disable-threat-tracing]] on [[etw-threat-intelligence]], and callback-removal research such as [[bustercall]] on [[kernel-callbacks]].

## Links

- Repo: https://github.com/V-i-x-x/kernel-callback-removal [Removing kernel callbacks]

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[kernel-callbacks]] · [[edrsandblast]] · [[bustercall]] · [[disable-threat-tracing]] · [[etwti-fluctuation-monitor]]
