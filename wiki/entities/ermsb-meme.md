---
title: ermsb-meme
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/everdox__ermsb-meme.md
updated: 2026-08-15
confidence: medium
---

# ermsb-meme

C proof-of-concept for **REP MOV–based EPT detection** — a defensive side-channel aimed at hypervisors that use **EPT (Extended Page Tables)** for stealth hooking or access watchpoints. Targets the README `Detection: Hacked Hypervisor` lane for anti-cheat engineers and kernel security researchers who need guest-visible signals that EPT policy is intercepting memory-backed code execution, complementing timing and write-and-compare EPT probes. (source: wiki/sources/descriptions/everdox__ermsb-meme.md)

Sits beside user-mode EPT hook detectors such as [[ept-hook-detection]] and multi-heuristic hypervisor probes such as [[hypervisor-detection]]; opposite stealth Type-2 research stacks such as [[ophion]] and [[hypervisor]] that depend on EPT for hooking without guest-kernel patches.

## Links

- Repo: https://github.com/everdox/ermsb-meme

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[ept-hook-detection]] · [[hypervisor-detection]] · [[checkhv-um]] · [[ophion]] · [[hypervisor]] · [[hvci]]
