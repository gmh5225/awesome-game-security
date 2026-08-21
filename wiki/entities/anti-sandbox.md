---
title: anti-sandbox
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/SaadAhla__Anti-Sandbox.md
updated: 2026-08-21
confidence: medium
---

# anti-sandbox

Small Windows **proof of concept** for detecting Any.Run-like sandbox environments through host artifact checks. Written in C++, it combines folder presence probes, process enumeration, user-profile heuristics, and service or driver lookup logic. Detection fires only when **multiple indicators** align with expected sandbox traits—a layered scoring approach typical of sandbox-aware malware evasion. Intended for malware-analysis research and for understanding how automated inspection can be bypassed. (source: wiki/sources/descriptions/SaadAhla__Anti-Sandbox.md)

Complements broader anti-analysis testers such as [[pafish]], Cuckoo-oriented demos such as [[anticuckoo]], and VM / hypervisor fingerprint probes such as [[vmaware]] and [[hypervisor-detection]].

## Links

- Repo: https://github.com/SaadAhla/Anti-Sandbox (README tag: Detecting AnyRun sandbox)

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pafish]] · [[anticuckoo]] · [[vmaware]] · [[hypervisor-detection]] · [[awesome-anti-virtualization]]
