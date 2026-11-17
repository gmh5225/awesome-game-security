---
title: OPPO K3 Root Research
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/kipcloud120__oppo-k3-root-research.md
updated: 2026-11-17
confidence: medium
---

# OPPO K3 Root Research

Structured **feasibility study** of obtaining temporary root on an **OPPO K3** (Qualcomm **SDM710**, Android 11, Linux **4.9.227**) with a **locked bootloader**, **shell-only ADB**, and no shipped working exploit. The repository evaluates kernel and userspace attack surfaces systematically and records **why each path fails at a specific, verifiable gap** rather than presenting a privilege-escalation chain. (source: wiki/sources/descriptions/kipcloud120__oppo-k3-root-research.md)

## Attack surfaces reviewed

| Surface | Notes |
|---------|--------|
| **KGSL** | Adreno GPU kernel driver attack surface |
| **GhostLock-style races** | Futex / `rtmutex` race classes related to the GhostLock family |
| **Binder CVEs** | Historical Binder driver vulnerability paths |
| **FastRPC** | Qualcomm userspace–DSP RPC boundary |

## Tooling

Python and C deliver **offline analyzers** (vmlinux symbols, syscall stack geometry, Linux 4.9 structure layouts) and **on-device probe and race programs**, plus handover notes, ADB artifacts, and kernel source references for reproducible negative-result analysis.

## Positioning

**Cheat / Android Root** — complements working locked-bootloader exploits such as [[ghostlock-oneplus]] and training labs such as [[android-kernel-exploitation-lab]] by documenting vendor hardening limits on a mid-tier OPPO handset. Pair methodology with [[research-rigor]] when generalizing from documented gaps to other SDM710 builds.

## Links

- Repo: https://github.com/kipcloud120/oppo-k3-root-research

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[ghostlock-oneplus]] · [[android-kernel-exploitation-lab]] · [[android-kernel-exploitation]] · [[cve-2019-2215]] · [[cve-2020-0041]] · [[research-rigor]]