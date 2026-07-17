---
title: ZeroThreadKernel
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md
updated: 2026-07-17
confidence: medium
---

# ZeroThreadKernel

Windows kernel communication PoC (C driver) that runs custom kernel code **without creating visible system threads**. It reuses existing kernel thread contexts or timer callbacks so the work does not show up as a new thread—aimed at studying stealthy Ring0 execution and AC detectors that enumerate system threads to find manually mapped drivers. (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md)

README tag: `NtCreateCompositionSurfaceHandle`.

## Links

- Repo: https://github.com/zer0condition/ZeroThreadKernel

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[ntmemory]] · [[revert-mapper]] · [[kernel-callbacks]]
