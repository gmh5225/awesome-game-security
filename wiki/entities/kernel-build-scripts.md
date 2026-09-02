---
title: kernel build scripts
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/TheWildJames__kernel_build_scripts.md
  - wiki/sources/descriptions/Andrea-lyz__oppo_oplus_realme_sm8750.md
updated: 2026-09-02
confidence: medium
---

# kernel build scripts

Collection of **Bash automation scripts** for building Android kernels across **GKI and non-GKI** targets (TheWildJames). Orchestrates repo sync, patch application, defconfig changes, packaging, and release publishing for multiple device families and kernel branches. Heavily integrates [[kernelsu]] and SUSFS patch flows; includes vendor-specific build variants for Pixel, OnePlus, Xiaomi, and others. Primary audience: advanced Android kernel modders and mobile security researchers—note that some scripts may now be outdated. (source: wiki/sources/descriptions/TheWildJames__kernel_build_scripts.md)

Complements GitHub Actions kernel CI such as [[kernel-build-action]] and out-of-tree driver build automation such as [[compile-android-driver]] when researchers need multi-vendor custom kernel image pipelines via local or hosted Bash workflows. OPPO/OnePlus/Realme SM8750 and MT6991 automation with OKI/GKI modes, f2fs patches, and KernelSU integration via [[oppo-oplus-realme-sm8750]] (Andrea-lyz; cheat / Android Kernel Source). (source: wiki/sources/descriptions/Andrea-lyz__oppo_oplus_realme_sm8750.md)

## Links

- Repo: https://github.com/TheWildJames/kernel_build_scripts

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[kernel-build-action]] · [[compile-android-driver]] · [[oppo-oplus-realme-sm8750]] · [[android-kernel-hacking-toolkit]] · [[kernel-common]]
