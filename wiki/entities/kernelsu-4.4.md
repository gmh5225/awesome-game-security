---
title: KernelSU-4.4
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__KernelSU-4.4.md
updated: 2026-08-12
confidence: medium
---

# KernelSU-4.4

Backport of [[kernelsu]] to **Android Linux kernel 4.4** for kernel-based root access management on legacy devices. Provides `su` and root access control at the kernel level, integrating SELinux policy modification and APK signature verification; built with **Google GCC 4.9**. Listed under Cheat / Android root as adapted for Linux Kernel 4.4 + Google GCC 4.9. (source: wiki/sources/descriptions/gmh5225__KernelSU-4.4.md)

Legacy-kernel KernelSU ports like this extend the same kernel-level credential-override and root-management model to pre-GKI BSPs where upstream KernelSU targets newer kernels—relevant for researchers studying root on older OEM trees and mobile anti-cheat root-detection on legacy Android builds.

## Links

- Repo: https://github.com/gmh5225/KernelSU-4.4

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[kernelsu-pixel4xl]] · [[pc-ginkgo]] · [[android-kernel-huawei-hi6250-8-exp]] · [[magiskdetector]]
