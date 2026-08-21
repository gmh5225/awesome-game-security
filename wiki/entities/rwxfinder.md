---
title: RWXFinder
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/S12cybersecurity__RWXFinder.md
updated: 2026-08-21
confidence: medium
---

# RWXFinder

Windows utility that scans a **target process** for **RWX (Read-Write-Execute)** memory pages suitable for **code injection**. Walks virtual memory regions with **`VirtualQueryEx`**, filters by size, and returns addresses of exploitable RWX regions for shellcode staging or injection research. (source: wiki/sources/descriptions/S12cybersecurity__RWXFinder.md)

README lane: find Windows RWX memory regions in a target process by size via VirtualQueryEx.

Complements injection tradecraft collections such as [[windows-process-injection]] and defensive RWX scanners such as [[ghost]] and [[rasd]].

## Links

- Repo: https://github.com/S12cybersecurity/RWXFinder

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[ghost]] · [[injectors]]
