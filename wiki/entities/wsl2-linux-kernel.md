---
title: WSL2 Linux Kernel
kind: entity
topics: [windows-kernel, overview]
sources:
  - wiki/sources/descriptions/microsoft__WSL2-Linux-Kernel.md
updated: 2026-07-30
confidence: medium
---

# WSL2 Linux Kernel

Official Microsoft **WSL2 Linux kernel** source tree — the kernel image that runs inside WSL2’s lightweight utility VM. Kernel-level layout (`arch`, drivers, `fs`, networking hooks) for building, patching, or auditing the Linux side of Windows Subsystem for Linux rather than the Windows host or WSL userspace front-end. Mainly useful for Windows-subsystem and developer-environment researchers working in the README **WSL** lane. (source: wiki/sources/descriptions/microsoft__WSL2-Linux-Kernel.md)

Pair with [[windows-subsystem-linux]] (community full-tree reference) and the broader WSL stack (userspace/VM infra lives in the separate `microsoft/WSL` repo).

## Links

- Repo: https://github.com/microsoft/WSL2-Linux-Kernel

## Related

[[overviews/windows-kernel]] · [[windows-subsystem-linux]] · [[winvisor]] · [[kace]] · [[conbeerlib]]
