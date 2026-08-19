---
title: pafish
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/a0rtega__pafish.md
updated: 2026-08-19
confidence: medium
---

# pafish

Open-source **anti-analysis testing tool** that emulates detection techniques used by real malware. Written in C with modular checks for virtual machines, sandboxes, debuggers, hooks, and environment artifacts across VMware, VirtualBox, QEMU, and Wine. Intended for reproducible testing; builds with MinGW-w64 and make-based workflows. Used by security researchers to evaluate analysis environments and study evasion behavior. (source: wiki/sources/descriptions/a0rtega__pafish.md)

Complements sandbox / virtual-environment detection demos such as [[anticuckoo]], anti-debug technique catalogs such as [[makin]], and broader VM / hypervisor fingerprint probes such as [[vmaware]] and [[hypervisor-detection]].

## Links

- Repo: https://github.com/a0rtega/pafish

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[anticuckoo]] · [[makin]] · [[vmaware]] · [[hypervisor-detection]] · [[awesome-anti-virtualization]]
