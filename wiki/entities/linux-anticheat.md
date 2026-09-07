---
title: linux-anticheat
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/mikio815__linux-anticheat.md
updated: 2026-09-07
confidence: low
---

# linux-anticheat

**Work-in-progress kernel-level anti-cheat** (mikio815) targeting Linux gaming consoles such as the **Steam Deck**. Four-layer architecture: Rust userspace daemon (game launch + security events), **LSM eBPF** detection (ptrace block, W^X memory, bpf() monitoring), thin C kernel module guarding eBPF program integrity, and planned **BitVisor** hypervisor EPT write-protection for static kernel regions. (source: wiki/sources/descriptions/mikio815__linux-anticheat.md)

## Stack

Built primarily in Rust and C with the **Aya** eBPF framework. Requires Linux **5.17+** with BTF debug info and BPF LSM enabled. Targets locked-down console environments where Secure Boot, kernel lockdown, and TPM attestation make deep kernel protection practical.

## Status

Early WIP — research and development reference for Linux-native AC architecture, not production-ready enforcement.

## Links

- Repo: https://github.com/mikio815/linux-anticheat

## Related

[[vigil]] · [[tlac-modern-local-anti-cheat-reunioned]] · [[hvci]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
