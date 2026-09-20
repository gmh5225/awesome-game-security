---
title: Kernemul
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/noahware__kernemul.md
updated: 2026-09-20
confidence: medium
---

# Kernemul

**Kernemul** is a cross-platform C++ emulator that runs Windows x86-64 and ARM64 **kernel drivers and usermode applications** by reimplementing kernel APIs and redirecting guest execution to host-side handlers. (source: wiki/sources/descriptions/noahware__kernemul.md)

**Implementation:** over 380 kernel functions including roughly 120 syscalls; Windows type layouts derived from ntoskrnl PDB symbols for kernel version 26100. Two execution backends: **Unicorn** for portable instruction emulation with multithreaded vCPU support on Linux and Windows, and the **Windows Hypervisor Platform** for faster native execution on x64 Windows hosts. Premade guest filesystems are provided for both architectures so binaries can be emulated without manually extracting kernel components.

**Audience:** reverse engineering, kernel driver analysis, and game security research — studying anti-cheat and other kernel-mode software in a controlled sandbox without loading drivers on the host.

Sits in the README `Windows Emulator` lane (~8 links) beside WHP usermode guests such as [[winvisor]], hybrid kernel-driver stacks such as [[kdemu]], and RING3 sandboxes such as [[kace]] — Kernemul targets full kernel+usermode driver analysis in a controlled sandbox rather than pure usermode PE replay alone.

## Links

- Repo: https://github.com/noahware/kernemul (Windows kernel driver and usermode app emulator for x86-64 and ARM64 with WHP and Unicorn backends)

## Related

[[kdemu]] · [[kace]] · [[winvisor]] · [[kubera]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
