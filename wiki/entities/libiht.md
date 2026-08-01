---
title: libiht
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/libiht__libiht.md
updated: 2026-08-01
confidence: medium
---

# libiht

**Intel Hardware Trace Library** from Tencent Security Xuanwu Lab (Tencent Spark Talent Program). A library for working with Intel hardware-assisted execution tracing — the same CPU trace lane used in control-flow and integrity research without patching `.text`. Aimed at game security researchers and reverse engineers in the cheat / Windows kernel explorer area. (source: wiki/sources/descriptions/libiht__libiht.md)

Sits beside LBR/BTS branch-recording drivers such as [[branch-monitoring-project]] and Intel-PT hypervisor fuzzing stacks such as [[qemu-nyx]] as a programmatic hardware-trace option.

## Links

- Repo: https://github.com/libiht/libiht

## Related

[[branch-monitoring-project]] · [[qemu-nyx]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
