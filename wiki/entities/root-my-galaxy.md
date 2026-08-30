---
title: Root My Galaxy
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/BuSung-dev__Root-My-Galaxy.md
updated: 2026-08-30
confidence: medium
---

# Root My Galaxy

Android application that provides one-click rooting for explicitly supported **Samsung Galaxy** firmware builds. Written primarily in **Kotlin** with a **Jetpack Compose** UI and native **C** components through the Android NDK. Automatically matches devices by kernel release, build ID, SDK level, ABI, and page size before downloading and applying device-specific exploit payloads and **KernelSU** artifacts from an external feed. The installer is kept separate from sensitive exploit code, memory offsets, and root payloads, and includes native probes for kernel surface enumeration, KASLR timing analysis, and privilege-escalation validation. Advanced mode allows manual profile selection with separate warnings for kernel-release and build mismatches. Intended for security researchers and authorized testers working on Android kernel exploitation, rooting workflows, and related mobile security research. (source: wiki/sources/descriptions/BuSung-dev__Root-My-Galaxy.md)

Samsung Galaxy counterpart to Pixel-only [[root-my-pixel]] and multi-vendor [[ghostlock-app]] in the CVE-2026-43499 packaged-root lane; same CVE family as [[cve-2026-43499-popsicle]] and Xiaomi siblings [[duchamp-root]]. External feed architecture separates consumer installer from exploit offsets and payloads—similar separation goals to other one-tap CVE-2026-43499 installers. Complements Samsung KernelSU kernel trees such as [[a146b-ksu]] and [[android-kernel-samsung-sm7150]] for custom-ROM builders versus stock-firmware one-tap workflows.

## Links

- Repo: https://github.com/BuSung-dev/Root-My-Galaxy
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[cve-2026-43499-popsicle]] · [[root-my-pixel]] · [[ghostlock-app]] · [[duchamp-root]] · [[a146b-ksu]] · [[android-kernel-samsung-sm7150]] · [[mobile-anti-cheat]] · [[android-native-root-detector]]
