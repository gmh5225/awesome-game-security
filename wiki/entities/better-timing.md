---
title: BetterTiming
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/SamuelTulach__BetterTiming.md
updated: 2026-08-21
confidence: medium
---

# BetterTiming

**BetterTiming** (SamuelTulach) is a **Linux KVM patch** that improves **virtual CPU timing behavior** to bypass **timing-based anti-VM checks**. Delivered as a kernel patch with documentation and demonstration artifacts showing **reduced detection by common VM-check tools**. The approach **records VM-exit timing characteristics** and **offsets the guest TSC** so execution timing appears closer to bare metal. Primarily aimed at **virtualization security research** and testing **anti-cheat or anti-analysis timing heuristics**. README category: Bypass CPU Timing. (source: wiki/sources/descriptions/SamuelTulach__BetterTiming.md)

Complements RDTSC-focused KVM handler patches such as [[rdtsc-kvm-handler]] and sits in the QEMU/KVM anti-detection research-host lane beside [[hypervisor-phantom]] and [[kvm-performance]]. Same maintainer as other SamuelTulach projects such as [[light-hook]], [[efi-memory]], and [[hook-guard]].

## Links

- Repo: https://github.com/SamuelTulach/BetterTiming (README tag: Bypass CPU Timing)

## Related

[[rdtsc-kvm-handler]] · [[hypervisor-phantom]] · [[kvm-performance]] · [[checkhv-um]] · [[ophion]] · [[vmaware]] · [[awesome-anti-virtualization]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
