---
title: Hide ACE Kernel
kind: entity
topics: [mobile-security, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/stuffed-cat__hide-ace-kernel.md
updated: 2026-10-15
confidence: medium
---

# Hide ACE Kernel

**KernelSU module** for rooted Android that conceals user-space **`/proc/inte_*`** nodes exposed by **Tencent** and **Oplus** kernel-level anti-cheat on supported OEM builds. Implementation is primarily a **shell service script** that creates empty placeholder files and **bind-mounts** them over integrity interfaces such as `/proc/inte_ko`, `/proc/inte_systbl`, and `/proc/inte_status`, so readers see blank output instead of KO load and syscall-table integrity reports. Targets the kernel security check module associated with **ACE-style** enforcement where user-space clients poll these proc nodes for telemetry. (source: wiki/sources/descriptions/stuffed-cat__hide-ace-kernel.md)

Research focus: mobile game anti-cheat, kernel-assisted enforcement, and how user-space ACE clients consume kernel-exposed integrity signals—without injecting hooks into game processes.

## Links

- Repo: https://github.com/stuffed-cat/hide-ace-kernel

## Related

[[kernelsu]] · [[mobile-anti-cheat]] · [[honor-of-kings-re-research]] · [[pubgm1.6-deadgame]] · [[dfm-android-unicorn]] · [[kpm-memreader]] · [[oppo-oplus-realme-sm8750]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
