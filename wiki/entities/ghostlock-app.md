---
title: GhostLock App
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/YuKongA__ghostlock-app.md
updated: 2026-08-19
confidence: medium
---

# GhostLock App

Android one-tap root application that exploits a kernel **pselect race condition** (**CVE-2026-43499**) on supported modern smartphones. Combines a native C exploit core (Android NDK), Java UI for one-tap execution, and a Rust offset extractor that derives kernel structure offsets from boot images and OTA packages. Devices are matched by exact kernel release strings with per-build offset tables and runtime JSON import so new kernels can be supported without rebuilding the app. Post-exploitation integrates with **KernelSU** or **ReSukiSU** for module loading after uid 0. Intended for Android security researchers and reverse engineers studying kernel vulnerabilities, root bypass techniques, and game anti-cheat environments on locked-down hardware. (source: wiki/sources/descriptions/YuKongA__ghostlock-app.md)

Broader multi-vendor coverage than Pixel-only [[root-my-pixel]] (IonStack delivery on Pixel 7–10); same CVE family as [[cve-2026-43499-popsicle]] LD_PRELOAD PoC and other packaged root installers. Rust offset extraction complements boot-image tooling such as [[android-boot-image-editor]] and [[payload-dumper-go]].

## Links

- Repo: https://github.com/YuKongA/ghostlock-app
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[cve-2026-43499-popsicle]] · [[root-my-pixel]] · [[android-boot-image-editor]] · [[mobile-anti-cheat]] · [[android-native-root-detector]]
