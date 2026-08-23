---
title: ksentinel
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/MatheuZSecurity__ksentinel.md
updated: 2026-08-23
confidence: medium
---

# ksentinel

**Linux kernel integrity monitor** (MatheuZSecurity) implemented as a loadable kernel module in C. Watches **syscall and critical function hooks** for signs of **rootkit tampering** using **function prologue hashing**, **syscall table validation**, and **LSTAR checks** to detect unauthorized modifications. Supports configurable monitoring intervals, extra symbol targets, and an **anti-unload mechanism** with an unlock-key workflow. Primary audience: kernel security researchers and defenders evaluating rootkit detection strategies on Linux systems. (source: wiki/sources/descriptions/MatheuZSecurity__ksentinel.md)

Complements offensive Linux rootkit sample collections such as [[rootkit]], io_uring post-exploitation agents such as [[ring-reaper]], LKM hook frameworks such as [[kernel-hook-framework]] and [[venom]], hidden-module discovery such as [[modreveal]], eBPF timing-anomaly rootkit research such as [[rootkit-detection-ebpf-time-trace]], and broader Linux runtime-security platforms such as [[tracee]].

## Links

- Repo: https://github.com/MatheuZSecurity/ksentinel [Kernel integrity monitor for detecting syscall hooking]

## Related

[[rootkit]] · [[ring-reaper]] · [[modreveal]] · [[rootkit-detection-ebpf-time-trace]] · [[kernel-hook-framework]] · [[venom]] · [[tracee]] · [[vigil]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
