---
title: ept-hook-detection
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/momo5502__ept-hook-detection.md
updated: 2026-07-29
confidence: medium
---

# ept-hook-detection

User-mode tool that detects **EPT (Extended Page Table)** hooks installed by hypervisors using three independent methods: **timing-based detection** (execution latency discrepancies), **write-and-compare** checks (write to code pages and verify whether the hypervisor silently redirects reads), and **cross-thread consistency** checks (compare code views across CPU cores). Targets the README `Detect EPT` lane for AC engineers validating hypervisor-based code hiding or split views of executable pages. (source: wiki/sources/descriptions/momo5502__ept-hook-detection.md)

Complements broader hacked-hypervisor probes such as [[hypervisor-detection]] and [[checkhv-um]], VPGATHER / vectored-exception EPT probes such as [[bloodhound]], and sits opposite stealth Type-2 stacks such as [[ophion]] that rely on EPT for hooking and anti-detection.

## Links

- Repo: https://github.com/momo5502/ept-hook-detection

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[bloodhound]] · [[hypervisor-detection]] · [[checkhv-um]] · [[ophion]] · [[hvci]] · [[patch-finder]]
