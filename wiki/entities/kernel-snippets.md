---
title: KernelSnippets
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__KernelSnippets.md
updated: 2026-08-12
confidence: medium
---

# KernelSnippets

Curated **Windows kernel-mode code snippets** from gmh5225 — reusable header-sized patterns for common driver development tasks rather than a turnkey driver or framework. Coverage spans callback registration, memory operations, process manipulation, and related Ring0 techniques useful when prototyping anti-cheat bypass or defensive driver research. (source: wiki/sources/descriptions/gmh5225__KernelSnippets.md)

Notable indexed sample: **VGK's SwapContextHk** — a Vanguard (`vgk.sys`) context-swap hook reference in the Some Tricks / anti-cheat research lane.

## Links

- Repo: https://github.com/gmh5225/KernelSnippets
- Sample: https://github.com/gmh5225/KernelSnippets/blob/main/VGK_SwapContextHk.h

## Related

[[kernel-callback-functions-list]] · [[kernel-callbacks]] · [[vanguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
