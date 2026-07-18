---
title: SystemThreadFinder
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/weak1337__SystemThreadFinder.md
updated: 2026-07-18
confidence: medium
---

# SystemThreadFinder

Tool that flags **hidden / manually mapped system threads** by enumerating threads via `NtQuerySystemInformation`, then checking each kernel thread’s start address against loaded driver image ranges—threads whose start address falls outside any legitimate module are suspicious. Built by reverse-engineering [[battleye]]’s thread-detection logic; useful for AC researchers studying kernel thread heuristics and stealthy driver-based cheats that spawn threads from unmapped memory. (source: wiki/sources/descriptions/weak1337__SystemThreadFinder.md)

Complements evasion PoCs such as [[zero-thread-kernel]] that avoid creating visible system threads.

## Links

- Repo: https://github.com/weak1337/SystemThreadFinder

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[battleye]] · [[zero-thread-kernel]] · [[revert-mapper]] · [[kernel-callbacks]]
