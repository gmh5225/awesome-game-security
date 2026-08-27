---
title: android-kernel-inline-hook-framework
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ChwnWang0__Android-kernel-inline-hook-framework.md
updated: 2026-08-27
confidence: medium
---

# android-kernel-inline-hook-framework

Lightweight **ARM64 Android kernel inline hook framework** (ChwnWang0) for intercepting kernel functions from loadable kernel modules. Supports **full instruction relocation** for AArch64 control-flow and literal forms—including **B/BL**, **ADRP**, **LDR literal**, **CBZ**, and **TBZ**—plus **64-bit long jumps** via trampolines. Handles **automatic write-protect and memory-permission bypass** so patches can be applied without manual page-attribute juggling. Primary use case: rooted Android kernel RE, driver/syscall hook prototyping, and low-level mobile security research on GKI/vendor kernels. (source: wiki/sources/descriptions/ChwnWang0__Android-kernel-inline-hook-framework.md)

Complements userspace ARM64 inline hook libraries such as [[and64-inline-hook]] and [[android-inline-hook-arm64]], multi-arch Linux kernel hook scaffolds such as [[kernel-hook-framework]], and integrated Android LKM + Zygisk stacks such as [[integrated-kernel-module]].

## Links

- Repo: https://github.com/ChwnWang0/Android-kernel-inline-hook-framework (ARM64 Android kernel inline hook framework with instruction relocation)

## Related

[[and64-inline-hook]] · [[android-inline-hook-arm64]] · [[kernel-hook-framework]] · [[integrated-kernel-module]] · [[kernelpatch]] · [[hardware-breakpoint]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
