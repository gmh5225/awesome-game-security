---
title: GhostLock OnePlus
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/JoinChang__ghostlock-oneplus.md
  - wiki/sources/README-categories.md
updated: 2026-09-02
confidence: medium
---

# GhostLock OnePlus

Native Android kernel exploit that gains root and installs **KernelSU** on **OnePlus**, **OPPO**, **realme**, and **Xiaomi** devices without unlocking the bootloader or patching the boot image. Targets **CVE-2026-43499** — a futex priority-inheritance use-after-free — combining **pselect6** stack overlay with controlled rb-tree writes for precise kernel memory corruption. Implemented in C with the Android NDK; Python tooling extracts kernel symbols, validates stack layouts, and ships per-device offset tables for multiple SoCs and GKI versions. Dual exploitation paths: UMH injection via ashmem miscdevice redirection or direct credential patching. Research focus: locked-bootloader bypass, kernel exploitation, and post-exploit root persistence on hardened Android builds. (source: wiki/sources/descriptions/JoinChang__ghostlock-oneplus.md)

Vendor-specific native toolkit complementing the multi-vendor one-tap UI in [[ghostlock-app]]; same CVE family as [[cve-2026-43499-popsicle]], [[root-my-pixel]], [[duchamp-root]], and [[root-my-galaxy]].

## Links

- Repo: https://github.com/JoinChang/ghostlock-oneplus
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[ghostlock-app]] · [[cve-2026-43499-popsicle]] · [[root-my-pixel]] · [[duchamp-root]] · [[root-my-galaxy]] · [[mobile-anti-cheat]] · [[android-native-root-detector]]
