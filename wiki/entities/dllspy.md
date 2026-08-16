---
title: DLLSpy
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/cyberark__DLLSpy.md
updated: 2026-08-16
confidence: medium
---

# DLLSpy

**DLLSpy** is a CyberArk Windows tool for detecting **DLL hijacking vulnerabilities** in installed applications. It scans running processes and installed programs for missing DLL dependencies, writable DLL directories, and unsafe search-path configurations that could enable code execution, then generates reports identifying specific hijacking opportunities. Aimed at security auditors and system administrators assessing DLL hijacking risk across Windows environments. (source: wiki/sources/descriptions/cyberark__DLLSpy.md)

Defensive audit counterpart in the Cheat → DLL Hijack lane beside catalog DBs [[windows-dll-hijacking]] and [[hijacklibs]] and offensive discovery tooling [[dllirant]] / [[impulsive-dll-hijack]] (not a game-specific cheat); useful for AC/EDR researchers mapping image-load / search-order abuse on managed hosts.

## Links

- Repo: https://github.com/cyberark/DLLSpy (README: DLL Hijacking Detection Tool)

## Related

[[windows-dll-hijacking]] · [[hijacklibs]] · [[dllirant]] · [[impulsive-dll-hijack]] · [[pipeviewer]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
