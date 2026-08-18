---
title: VDM
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/backengineering__VDM.md
updated: 2026-08-18
confidence: medium
---

# VDM

**VDM (Voyager Driver Manager)** is a C++ library that exploits **vulnerable signed drivers** to obtain arbitrary **physical memory read/write** and **kernel code execution** on Windows. It exposes a clean API over multiple vulnerable-driver backends (**gdrv**, **cpuz**, and others) for physical memory access, virtual-address translation, and kernel-mode shellcode execution. Designed as a modular backend for tools such as [[kdmapper]], [[msrexec]], and bluepill. Aimed at kernel exploitation researchers studying [[byovd]] attack primitives and building kernel-level tooling. (source: wiki/sources/descriptions/backengineering__VDM.md)

Upstream maintained by **backengineering**; ecosystem siblings include [[voyager]] (Hyper-V hacking framework) and [[msrexec]] (MSR write→kernel-exec via `IA32_LSTAR` redirect; uses VDM as a backend).

## Links

- Repo: https://github.com/backengineering/VDM

## Related

[[byovd]] · [[kdmapper]] · [[msrexec]] · [[voyager]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
