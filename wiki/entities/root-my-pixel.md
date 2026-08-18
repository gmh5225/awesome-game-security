---
title: Root My Pixel
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/alex193a__Root-My-Pixel.md
updated: 2026-08-18
confidence: medium
---

# Root My Pixel

Android app that automates **temporary root** on supported **Google Pixel** devices (Pixel 7 through Pixel 10 family) via a one-tap install workflow. Uses the NebuSec **IonStack** kernel exploit (**CVE-2026-43499**) together with **ReSukiSU** and **KernelSU** late-load; **Shizuku** grants elevated shell without prior root while native payloads stage from bundled assets. Kotlin UI with JNI/C device profiling matches firmware and kernel module interface versions to supported build profiles before exploit execution. Features include real-time exploit logging, soft reboot of `system_server`, and log export for debugging. Aimed at mobile security researchers, reverse engineers, and game-security practitioners who need rooted Pixel hardware for app analysis, kernel behavior study, and anti-cheat or root-detection evaluation. (source: wiki/sources/descriptions/alex193a__Root-My-Pixel.md)

Same CVE as the Xiaomi popsicle LPE PoC [[cve-2026-43499-popsicle]] but packaged as a consumer Pixel root installer rather than a standalone exploit repo. Complements Pixel flashing/root tooling such as [[pixel-flasher]] and KernelSU integration paths via [[kernelsu]].

## Links

- Repo: https://github.com/alex193a/Root-My-Pixel
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[cve-2026-43499-popsicle]] · [[pixel-flasher]] · [[easypixel]] · [[mobile-anti-cheat]] · [[android-native-root-detector]]
