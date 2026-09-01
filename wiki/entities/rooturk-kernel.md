---
title: ROOTURK Kernel
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/RooTurkk__ROOTURK-Kernel.md
updated: 2026-09-01
confidence: medium
---

# ROOTURK Kernel

Custom **Android GKI** kernel source tree for **POCO X7 Pro**, shipping full Linux kernel sources with **AnyKernel3** flashable packaging, build/install documentation, and a dedicated `rooturk` configuration. Based on **Android 15 GKI 6.6** with **aarch64 ABI** definitions for major SoC vendors (Qualcomm, MediaTek, Xiaomi); built primarily in C with shell-based AnyKernel scripts and **Bazel** build rules. README highlights built-in **KernelSU Next**, **SuSFS** root hiding, and game-oriented idle tuning. Includes Wi-Fi-related docs for compiling and deploying a replacement boot image. Aimed at Android kernel developers and mobile security researchers who need a rooted low-level platform for device modification, reverse engineering, and bypassing mobile game protections that depend on kernel integrity checks. (source: wiki/sources/descriptions/RooTurkk__ROOTURK-Kernel.md)

Sits in the Cheat **Android Kernel Source** lane beside other Xiaomi GKI trees such as [[android-kernel-xiaomi-sm8475]] and [[kernel-xiaomi-sm8250]], and KernelSU-integrated custom kernels such as [[android-kernel-oneplus-sm7250-wksu]]. SuSFS integration aligns with build-automation flows documented in [[kernel-build-scripts]]; KernelSU Next ties to upstream [[kernelsu]] and module ecosystems such as [[zygisk-on-kernelsu]].

## Links

- Repo: https://github.com/RooTurkk/ROOTURK-Kernel

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[kernel-build-scripts]] · [[android-kernel-xiaomi-sm8475]] · [[kernel-xiaomi-sm8250]] · [[mobile-anti-cheat]] · [[zygisk-on-kernelsu]]
