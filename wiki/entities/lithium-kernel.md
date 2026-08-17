---
title: lithium-kernel
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/bootmgfw__lithium-kernel.md
updated: 2026-08-17
confidence: medium
---

# lithium-kernel

**lithium-kernel** (bootmgfw/lithium-kernel) is a Windows x64 **kernel-mode driver framework** paired with a user-mode client that communicate through a **custom IOCTL interface**. Written primarily in C++ with supporting assembly, it exposes physical and virtual memory read/write, directory table base (DTB) resolution, page-table walking, and IDA-style pattern scanning. It also supports cross-process memory allocation and protection changes, **MouClass** callback-based kernel mouse emulation, thread hiding, NMI callback suppression, and kernel pool tracker cleaning. Aimed at low-level Windows research, reverse engineering, and game-security work that needs kernel primitives for memory access and anti-analysis evasion. (source: wiki/sources/descriptions/bootmgfw__lithium-kernel.md)

Sits in the standalone KM+UM driver-primitives lane beside memory-access libraries such as [[ntmemory]] and [[readphys]], MouClass input research such as [[kernel-mouse]] and [[mouseclassservicecallbacktrick]], thread-evasion PoCs such as [[covert-thread]] and [[zero-thread-kernel]], NMI suppression samples such as [[nmi]] and [[disable-nmi-callbacks]], and pool-forensics context under [[kernel-pool-scanning]]. End-to-end Apex Legends external consumer [[apex-external-cheat]] from the same author illustrates driver-backed cross-process reads in a DX11 ImGui overlay stack.

## Links

- Repo: https://github.com/bootmgfw/lithium-kernel (README: Windows kernel driver + usermode client — physical/virtual memory R/W, page-table walk, pattern scan, MouClass mouse IOCTL)

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[apex-external-cheat]] · [[ntmemory]] · [[readphys]] · [[kernel-mouse]] · [[mouseclassservicecallbacktrick]] · [[covert-thread]] · [[zero-thread-kernel]] · [[nmi]] · [[disable-nmi-callbacks]] · [[kernel-pool-scanning]]
