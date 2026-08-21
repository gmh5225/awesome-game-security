---
title: RDTSC-KVM-Handler
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/WCharacter__RDTSC-KVM-Handler.md
updated: 2026-08-19
confidence: medium
---

# RDTSC-KVM-Handler

Modified **Linux KVM handler** sources that intercept and alter **RDTSC** timing behavior on both **Intel VMX** and **AMD SVM** paths. The project explains how to patch kernel virtualization code, adjust fake timestamp deltas, and configure QEMU CPU flags such as disabling **RDTSCP** — low-level hypervisor timing control in Linux kernel C. Primary use case is virtualization and anti-detection research, including experiments around timing-based anti-cheat checks. (source: wiki/sources/descriptions/WCharacter__RDTSC-KVM-Handler.md)

Complements user-mode RDTSC hypervisor probes such as [[checkhv-um]] and stealth Type-2 stacks with TSC compensation such as [[ophion]], VM-exit timing compensation such as [[better-timing]], and sits beside QEMU/KVM guest hardening such as [[qemu-patched]] and [[hardened-qemu]] in the below-OS research-host lane.

## Links

- Repo: https://github.com/WCharacter/RDTSC-KVM-Handler (README tag: Bypass RDTSC)

## Related

[[better-timing]] · [[checkhv-um]] · [[ophion]] · [[qemu-patched]] · [[hardened-qemu]] · [[vmaware]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
