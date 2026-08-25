---
title: android_kernel_gki_common_5.10
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/ExWhyZed9__android_kernel_gki_common_5.10.md
updated: 2026-08-25
confidence: medium
---

# android_kernel_gki_common_5.10

Custom **Android GKI (Generic Kernel Image)** kernel source based on the **common 5.10** branch with **multi-vendor ABI support**. Bundles ABI symbol definitions for major Android OEMs including Samsung, Qualcomm, MediaTek, ASUS, Motorola, OnePlus, and others, plus a **ZenX** build script. Primarily useful for Android kernel developers and mobile security researchers building or analyzing GKI-compliant custom kernels across multiple device platforms. README lists **Redmi Note 11T Pro(+)** / **POCO X4 GT** as a target device. (source: wiki/sources/descriptions/ExWhyZed9__android_kernel_gki_common_5.10.md)

This fork extends the upstream AOSP GKI common base [[kernel-common]] with pre-integrated multi-vendor ABI symbols and build automation, complementing per-device OEM trees such as [[android-kernel-xiaomi-sm8475]] and [[android-kernel-motorola-dubai]], plus out-of-tree driver workflows ([[compile-android-driver]], [[android-kernel-driver-template]], [[kernel-build-scripts]]).

## Links

- Repo: https://github.com/ExWhyZed9/android_kernel_gki_common_5.10

## Related

[[kernel-common]] · [[android-kernel-xiaomi-sm8475]] · [[android-kernel-motorola-dubai]] · [[android-kernel-xiaomi-sweet]] · [[compile-android-driver]] · [[android-kernel-driver-template]] · [[kernel-build-scripts]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
