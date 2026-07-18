---
title: xign_poc_april_2026
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/waryas__xign_poc_april_2026.md
updated: 2026-07-18
confidence: medium
---

# xign_poc_april_2026

Public disclosure PoC for multiple vulnerabilities in the XIGNCODE3 / xhunter anti-cheat kernel driver (`xhunter64.sys`). Demonstrates arbitrary physical memory read/write, kernel address leak, and arbitrary process termination via `IRP_MJ_WRITE` command handling—useful for studying AC driver IOCTL/IRP attack surface and how a signed game-protection driver can become a kernel-primitive source. (source: wiki/sources/descriptions/waryas__xign_poc_april_2026.md)

## Links

- Repo: https://github.com/waryas/xign_poc_april_2026

## Related

[[byovd]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[av-edr-killer]] · [[windows-kernel-exploits]]
