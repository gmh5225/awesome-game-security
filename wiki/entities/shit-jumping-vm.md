---
title: ShitJumpingVM (NEXTVM)
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/woand__ShitJumpingVM.md
updated: 2026-10-27
confidence: medium
---

# ShitJumpingVM (NEXTVM)

**NEXTVM** is a lightweight Android **application virtualization** engine: third-party APKs run in **isolated sandbox processes** on a physical device **without root** and without a hardware emulator. A Kotlin virtual context and system-service proxies sit above a **C++ native hook layer** (GOT/PLT patches) that redirects filesystem and property queries; **Binder IPC** and **ActivityThread** launch paths are intercepted. Supports **multiple parallel instances** with per-clone storage and **device identity spoofing**, plus an anti-detection stack for common root, emulator, Xposed, and virtual-environment probes; optional **Google Play Services** bridging for auth and push. (source: wiki/sources/descriptions/woand__ShitJumpingVM.md)

Multi-module Gradle project (Jetpack Compose, Hilt, Clean Architecture). README lists under **Cheat → VirtualMachine** beside full guest VMs such as [[virtualmachine]] and desktop workbenches such as [[rooted-android-game-vm]]. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/woand/ShitJumpingVM

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[virtualmachine]] · [[virtual-app]] · [[zn-toolbox]] · [[mobile-anti-cheat]] · [[android-emulator-detection]]
