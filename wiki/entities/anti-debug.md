---
title: Anti-Debug
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Metick__Anti-Debug.md
updated: 2026-08-23
confidence: medium
---

# Anti-Debug

Small **Windows C++ proof-of-concept** (Metick) demonstrating debugger detection through **`ResumeThread` suspend-count behavior**. When a debugger attaches and briefly suspends a thread, the elevated suspend count returned from WinAPI calls can reveal the attachment. The sample is intentionally minimal—one anti-debug signal rather than a full protection framework—for Windows security learners experimenting with anti-tamper and anti-analysis techniques. (source: wiki/sources/descriptions/Metick__Anti-Debug.md)

## Technique

- Observes thread suspend count via `ResumeThread` return value after debugger-induced suspension
- Single-signal PoC; not a production anti-cheat component

## Links

- Repo: https://github.com/Metick/Anti-Debug

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[anti-debugging]] · [[makin]] · [[antidbg]] · [[ghostdebug]] · [[dmalibrary]] · [[cheatengine-dma]]
