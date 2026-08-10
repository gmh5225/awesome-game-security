---
title: KernelSU
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/tiann__KernelSU.md
  - wiki/sources/descriptions/msnx__KernelSU-Pixel4XL.md
  - wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md
updated: 2026-08-10
confidence: medium
---

# KernelSU

Kernel-based Android root solution (**kernel su**) listed under Cheat / Android root. Implemented primarily in Kotlin and Rust; grants elevated privileges via kernel-level integration rather than Magisk-style systemless userspace alone. Canonical reference for researchers studying Android root frameworks, module ecosystems (alongside Magisk / APatch), and mobile anti-cheat root-detection tradeoffs. (source: wiki/sources/descriptions/tiann__KernelSU.md)

Adjacent tooling: Magisk modules that also target KernelSU such as [[move-certificate]]; systemless Magisk itself [[magisk]]; Magisk-install paths such as [[cheese]]. Hardened fork [[apex-su]] rewrites userspace in Rust and adds stealth IOCTL over an anonymous `io_uring`-disguised inode (no proc/sys/dev entries) for root-hide research. (source: wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md) Device-specific KernelSU kernel trees such as [[kernelsu-pixel4xl]] (Pixel 4 XL / coral / msm-floral) integrate the same syscall-hook and credential-override model into vendor BSP sources. (source: wiki/sources/descriptions/msnx__KernelSU-Pixel4XL.md)

## Links

- Repo: https://github.com/tiann/KernelSU

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[magisk]] · [[apex-su]] · [[move-certificate]] · [[kernelsu-pixel4xl]] · [[magiskdetector]] · [[frida]] · [[keyattestation]]
