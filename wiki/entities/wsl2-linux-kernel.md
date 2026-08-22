---
title: WSL2 Linux Kernel
kind: entity
topics: [windows-kernel, overview]
sources:
  - wiki/sources/descriptions/microsoft__WSL2-Linux-Kernel.md
  - wiki/sources/descriptions/microsoft__WSL.md
updated: 2026-07-30
confidence: medium
---

# WSL2 Linux Kernel

Official Microsoft **WSL2 Linux kernel** source tree — the kernel image that runs inside WSL2’s lightweight utility VM. Kernel-level layout (`arch`, drivers, `fs`, networking hooks) for building, patching, or auditing the Linux side of Windows Subsystem for Linux rather than the Windows host or WSL userspace front-end. Mainly useful for Windows-subsystem and developer-environment researchers working in the README **WSL** lane. (source: wiki/sources/descriptions/microsoft__WSL2-Linux-Kernel.md)

Pair with [[wsl]] (Windows-side `wsl.exe`, Lxss Manager, DrvFS, GNS, init/VM infra), [[wsl2-linux-kernel-rolling]] (Nevuly; CI-driven rolling stable kernel builds for WSL2 x86/ARM64), and [[windows-subsystem-linux]] (community full-tree reference).

## Links

- Repo: https://github.com/microsoft/WSL2-Linux-Kernel

## Related

[[wsl]] · [[wsl2-linux-kernel-rolling]] · [[overviews/windows-kernel]] · [[windows-subsystem-linux]] · [[winvisor]] · [[kace]] · [[conbeerlib]]
