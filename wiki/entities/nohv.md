---
title: nohv
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/jonomango__nohv.md
updated: 2026-08-03
confidence: medium
---

# nohv

C/C++ kernel-level project for **benchmarking a custom hypervisor against common VM-detection checks**. Centers on driver development and debugging for anti-cheat engineers and defensive researchers working the `Detection: Hacked Hypervisor` lane — useful for measuring how well a Type-2 or research HV evades guest-side virtualization probes before shipping stealth features. (source: wiki/sources/descriptions/jonomango__nohv.md)

Complements multi-technique detectors such as [[hypervisor-detection]], cross-platform VM artifact libraries such as [[vmaware]], user-mode HV probes such as [[checkhv-um]], and hacked-hypervisor stress tooling such as [[vt-debuuger]] / [[baresvm]].

## Links

- Repo: https://github.com/jonomango/nohv

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hypervisor-detection]] · [[vmaware]] · [[checkhv-um]] · [[vt-debuuger]] · [[baresvm]] · [[hv]] · [[hypervisor]] · [[hvci]]
