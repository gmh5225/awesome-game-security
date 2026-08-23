---
title: rootkit
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/MatheuZSecurity__Rootkit.md
updated: 2026-08-23
confidence: medium
---

# rootkit

**Educational Linux rootkit sample collection** (MatheuZSecurity) spanning **kernel space, user space, and eBPF**. Most implementations are in C and demonstrate techniques such as **file and connection hiding**, **syscall and ftrace hooking**, **privilege escalation**, **persistence**, and **anti-forensic behavior**. The repository is organized into many focused subprojects with build scripts and small write-ups that explain each mechanism. Primary use case: **offensive and defensive research**, including **anti-rootkit detection testing** and kernel security experimentation. (source: wiki/sources/descriptions/MatheuZSecurity__Rootkit.md)

Complements defensive Linux LKM integrity monitors such as [[ksentinel]], io_uring post-exploitation agents such as [[ring-reaper]], hidden-module discovery such as [[modreveal]], eBPF timing-anomaly rootkit research such as [[rootkit-detection-ebpf-time-trace]], and offensive LKM hook samples such as [[venom]] and [[kernel-hook-framework]].

## Links

- Repo: https://github.com/MatheuZSecurity/Rootkit [Collection of codes focused on Linux rootkits]

## Related

[[ksentinel]] · [[ring-reaper]] · [[modreveal]] · [[rootkit-detection-ebpf-time-trace]] · [[venom]] · [[kernel-hook-framework]] · [[tracee]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
