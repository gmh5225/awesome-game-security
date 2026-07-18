---
title: VaultGuard
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/wesmar__VaultGuard.md
updated: 2026-07-18
confidence: medium
---

# VaultGuard

Windows process and file protection tool written entirely in x64 MASM (zero CRT, ~60 KB) with a kernel driver that monitors and blocks suspicious process access for anti-debugging / anti-tampering, plus folder/file protection via an FSFilter minifilter (hide, lock, read-only, or block execution). Ships a Win11 system-tray GUI (Mica), scriptable CLI, drag-and-drop, and per-process trusted bypass. (source: wiki/sources/descriptions/wesmar__VaultGuard.md)

Useful defensive reference for the same [[kernel-callbacks]] / minifilter (`FltRegisterFilter`) and Ob-handle surfaces that game anti-cheat stacks use to strip or deny process access—adjacent to inspection tools such as [[openark]] and [[systeminformer]], and same-author kernel utilities [[kvc]] / [[windefctl]].

## Links

- Repo: https://github.com/wesmar/VaultGuard

## Related

[[kernel-callbacks]] · [[openark]] · [[systeminformer]] · [[kvc]] · [[windefctl]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
