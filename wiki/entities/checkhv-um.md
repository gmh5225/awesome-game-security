---
title: checkhv_um
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/zer0condition__checkhv_um.md
updated: 2026-07-17
confidence: medium
---

# checkhv_um

User-mode Windows hypervisor detection tool in C: probes Type-1 and Type-2 presence via CPUID hypervisor-present / vendor leaf, RDTSC/RDTSCP timing anomalies, VMCS artifact scanning, and known hypervisor signature matching — no driver required. Aimed at anti-cheat developers and researchers building `Detection: Hacked Hypervisor` capabilities. (source: wiki/sources/descriptions/zer0condition__checkhv_um.md)

Complements HV construction / stealth stacks such as [[hv]] and [[ophion]], and hacked-hypervisor stress tooling such as [[vt-debuuger]].

## Links

- Repo: https://github.com/zer0condition/checkhv_um

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hv]] · [[ophion]] · [[vt-debuuger]] · [[hvci]] · [[overviews/reverse-engineering]]
