---
title: ANGRYORCHARD
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__ANGRYORCHARD.md
updated: 2026-08-15
confidence: medium
---

# ANGRYORCHARD

Windows kernel exploit PoC that abuses **NtUserHardErrorControl** in the win32k GUI-subsystem syscall surface. The chain elevates a calling thread to **KernelMode** and yields arbitrary kernel read/write primitives—an offensive path that bypasses normal driver load and [[byovd]] blocklists when the underlying win32k flaw is reachable. Primarily C/C++; aimed at low-level Windows researchers in the Some Tricks / Windows Ring3 lane. (source: wiki/sources/descriptions/gmh5225__ANGRYORCHARD.md)

Complements win32k attack-surface corpora such as [[win32k-file-collection]] and [[win32k-file-collection2]] for patch diffing, and session-driver loaders such as [[callmewin32kdriver]] that abuse other win32k load paths rather than syscall privilege escalation.

## Links

- Repo: https://github.com/gmh5225/ANGRYORCHARD

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[win32k-file-collection]] · [[callmewin32kdriver]] · [[windows-kernel-exploits]] · [[byovd]]
