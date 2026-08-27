---
title: Duchamp Root
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Colorful-glassblock__duchamp-root.md
updated: 2026-08-27
confidence: medium
---

# Duchamp Root

One-click Android root tool for **Xiaomi K70e** (codename **duchamp**) that chains the **IonStack** kernel exploit (**CVE-2026-43499**) and installs an embedded **KernelSU** `ksud` daemon. Written in C for aarch64 Android, built with NDK/clang, and delivered as an **LD_PRELOAD** shared library (`preload.so`). The exploit chain leaks KASLR via a **pselect** side channel, hijacks file-operation tables through a **futex PI race**, forges pipe buffer ops for arbitrary kernel physical read/write, then patches process credentials for uid 0. Includes per-device target offsets for duchamp and related Android 16 builds. Intended for security researchers studying Android kernel privilege escalation, root persistence, and reverse-engineering techniques. (source: wiki/sources/descriptions/Colorful-glassblock__duchamp-root.md)

Same CVE family as [[cve-2026-43499-popsicle]] (Xiaomi popsicle LD_PRELOAD PoC) and packaged installers [[root-my-pixel]] (Pixel IonStack + KernelSU late-load) and [[ghostlock-app]] (multi-vendor pselect race + offset extraction). Xiaomi K70e-specific sibling to popsicle with embedded [[kernelsu]] post-exploit management rather than standalone PoC sources alone.

## Links

- Repo: https://github.com/Colorful-glassblock/duchamp-root
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[cve-2026-43499-popsicle]] · [[root-my-pixel]] · [[ghostlock-app]] · [[mobile-anti-cheat]] · [[android-native-root-detector]]
