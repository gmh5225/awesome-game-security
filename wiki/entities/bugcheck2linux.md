---
title: BugCheck2Linux
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/NSG650__BugCheck2Linux.md
updated: 2026-08-22
confidence: medium
---

# BugCheck2Linux

Windows **kernel driver** that boots a **RISC-V Linux emulator** inside the **bug check (BSOD) screen**. Uses the **mini-rv32ima** RISC-V emulator, **BOOTVID** for framebuffer rendering during the bugcheck phase, and an embedded **device tree** plus **boot image** to run a minimal Linux system from kernel mode. (source: wiki/sources/descriptions/NSG650__BugCheck2Linux.md)

Research lane: **creative use of the Windows bugcheck environment** and **embedded emulation from kernel mode**—for kernel researchers and enthusiasts exploring crash-screen rendering and in-driver virtualization, not a production stability tool. Part of the NSG650 bugcheck-research family alongside [[bugcheckhack]], [[bad-bugcheck]], [[nomore-bugcheck]], and [[nomore-bugcheck-reloaded]].

## Links

- Repo: https://github.com/NSG650/BugCheck2Linux

## Related

[[bugcheckhack]] · [[bad-bugcheck]] · [[nomore-bugcheck]] · [[nomore-bugcheck-reloaded]] · [[bugcheck-suppressor]] · [[ntdoom]] · [[overviews/windows-kernel]]
