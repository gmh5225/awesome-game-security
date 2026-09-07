---
title: linux-anticheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/mikio815__linux-anticheat.md
updated: 2026-09-07
confidence: medium
---

# linux-anticheat

**linux-anticheat** (mikio815) — **work-in-progress kernel-level anti-cheat** designed for **Linux gaming consoles** such as the **Steam Deck**. A four-layer architecture combines a Rust userspace daemon (game launch + security events), **LSM eBPF** programs for core detection, a thin C kernel module that guards eBPF program integrity outside the sandbox, and a planned **BitVisor** hypervisor layer for Intel VMX/EPT write-protection of static kernel regions. Targets locked-down console environments where Secure Boot, kernel lockdown, and TPM attestation make deep kernel protection practical for game-security research. (source: wiki/sources/descriptions/mikio815__linux-anticheat.md)

Sits in the native Linux open-source AC lane beside [[vigil]], [[tlac-modern-local-anti-cheat-reunioned]], and GNU/Linux compatibility references such as [[are-we-anti-cheat-yet]] and [[aclist-github-io]].

## Architecture

1. **Userspace daemon** (Rust) — launches games and consumes security events.
2. **LSM eBPF** — ptrace blocking, W^X memory enforcement, bpf() monitoring.
3. **Kernel module** (C) — guards eBPF program integrity from outside the eBPF sandbox.
4. **Hypervisor** (planned, BitVisor) — EPT write-protect static kernel regions via Intel VMX/EPT.

## Stack

Built primarily in **Rust** and **C** with the **Aya** eBPF framework. Requires Linux **5.17+** with BTF debug info and **BPF LSM** enabled.

## Status

Early WIP — research and development reference for Linux-native AC architecture, not production-ready enforcement.

## Links

- Repo: https://github.com/mikio815/linux-anticheat [WIP kernel-level Linux console anti-cheat using LSM BPF, a thin kernel module, and BitVisor hypervisor EPT write-protection]

## Related

[[vigil]] · [[tlac-modern-local-anti-cheat-reunioned]] · [[are-we-anti-cheat-yet]] · [[aclist-github-io]] · [[tracee]] · [[hvci]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
