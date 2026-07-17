---
title: hv
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/zer0condition__hv.md
updated: 2026-07-17
confidence: medium
---

# hv

Minimal Intel VT-x Type-2 hypervisor for Windows in C: enters VMX root, configures VMCS, handles VM exits for CPUID / MSR / control-register access, and virtualizes the running OS. Aimed at kernel researchers learning VT-x internals—not a production anti-cheat component. (source: wiki/sources/descriptions/zer0condition__hv.md)

Useful alongside hacked-hypervisor detection research (e.g. [[vt-debuuger]]) and VBS/[[hvci]] threat models under `Detection: Hacked Hypervisor`.

## Links

- Repo: https://github.com/zer0condition/hv (README tag: Hacked Hypervisor Testing)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hvci]] · [[vt-debuuger]] · [[overviews/reverse-engineering]]
