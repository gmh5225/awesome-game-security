---
title: kernel-common
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/aosp-mirror__kernel_common.md
updated: 2026-08-18
confidence: medium
---

# kernel-common

Official **AOSP Generic Kernel Image (GKI) common kernel** mirror — the shared upstream base all Android device vendors build upon. Contains core Linux kernel sources with Android-specific patches, **Bazel** build integration, and **Rust** toolchain support. Primary reference for studying kernel attack surfaces and defense mechanisms across the Android ecosystem rather than a single OEM BSP tree. Listed under Cheat `[GKI]`. (source: wiki/sources/descriptions/aosp-mirror__kernel_common.md)

Complements per-device OEM kernel sources (e.g. [[android-kernel-xiaomi-pipa]], [[kernelsu-pixel4xl]]) and out-of-tree driver workflows such as [[compile-android-driver]], [[android-kernel-driver-template]], and [[kernel-build-action]]. Root frameworks that target stock GKI kernels — [[kernelsu]], [[kernelpatch]] / [[apatch]] — and CVE research such as [[android-kernel-exploitation]] often trace back to this common upstream.

## Links

- Repo: https://github.com/aosp-mirror/kernel_common

## Related

[[compile-android-driver]] · [[android-kernel-driver-template]] · [[kernel-build-action]] · [[kernelsu]] · [[kernelpatch]] · [[apatch]] · [[android-kernel-exploitation]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
