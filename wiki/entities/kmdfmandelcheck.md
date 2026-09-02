---
title: KmdfMandelcheck
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/AnalogFeelings__KmdfMandelcheck.md
updated: 2026-09-02
confidence: medium
---

# KmdfMandelcheck

Compact **Windows kernel driver** (KMDF) that renders a **bitmap on screen after a BSOD**. Written in C; integrates with **boot video routines** through a **modified BOOTVID interface**. Minimal codebase demonstrating **low-level kernel graphics output** and **crash-time display handling**. (source: wiki/sources/descriptions/AnalogFeelings__KmdfMandelcheck.md)

Research lane: **Windows internals** study of **BOOTVID crash-screen output** and **post-bugcheck rendering behavior**—useful for driver developers and reverse engineers exploring boot-time and crash-time display paths. Sits beside legacy BOOTVID animation PoCs such as [[bad-bugcheck-old]] and framebuffer-based successors such as [[bad-bugcheck]].

## Links

- Repo: https://github.com/AnalogFeelings/KmdfMandelcheck

## Related

[[bad-bugcheck-old]] · [[bad-bugcheck]] · [[bugcheck2linux]] · [[bugcheckhack]] · [[overviews/windows-kernel]]
