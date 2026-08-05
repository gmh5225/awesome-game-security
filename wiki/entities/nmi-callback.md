---
title: NMI Callback
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/helloobaby__Nmi-Callback.md
updated: 2026-08-05
confidence: medium
---

# NMI Callback

C/C++ kernel driver research project focused on **NMI (Non-Maskable Interrupt) callbacks** — the `KeRegisterNmiCallback` / per-CPU NMI handler surface used for debugger detection, cross-processor integrity checks, and other Ring0 monitoring that can intersect hacked-hypervisor stress testing. Aimed at anti-cheat engineers and defensive researchers in the `Detection: Hacked Hypervisor` lane. (source: wiki/sources/descriptions/helloobaby__Nmi-Callback.md)

Sits beside broader [[kernel-callbacks]] research (process/image/Ob notify) and complements hacked-hypervisor detectors such as [[hypervisor-detection]], benchmark suites such as [[nohv]], and AMD SVM stress tooling such as [[baresvm]].

## Links

- Repo: https://github.com/helloobaby/Nmi-Callback (README tag: NMI Callback)

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[kernel-callbacks]] · [[hypervisor-detection]] · [[nohv]] · [[baresvm]] · [[checkhv-um]] · [[hvci]]
