---
title: ShitJumpingVM (NEXTVM)
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/woand__ShitJumpingVM.md
updated: 2026-10-27
confidence: high
---

# ShitJumpingVM (NEXTVM)

**NEXTVM** (woand/ShitJumpingVM) is a lightweight Android **application virtualization** engine: third-party APKs run in **isolated sandbox processes** on a physical device **without root** and without a hardware emulator. (source: wiki/sources/descriptions/woand__ShitJumpingVM.md)

README category: **Cheat → VirtualMachine** (no-root app sandbox lane beside full guest VMs such as [[virtualmachine]]).

## Architecture

- **Java/Kotlin layer** — virtual `Context`, system-service proxies, Jetpack Compose UI; multi-module Gradle project with Hilt and Clean Architecture.
- **Launch intercept** — **Binder IPC** and **ActivityThread** paths are hooked so guest apps start inside the sandbox.
- **Native layer** — C++ **GOT/PLT** patches redirect filesystem and system-property queries seen by the guest.
- **Multi-instance** — parallel clones with per-instance storage and **device identity spoofing**.
- **Anti-detection** — mitigations aimed at common root, emulator, Xposed, and virtual-environment probes; optional **Google Play Services** bridging for auth and push. (source: wiki/sources/descriptions/woand__ShitJumpingVM.md)

## Use cases

Privacy isolation, mobile security research, app compatibility testing, and observing how **protected apps** behave inside a controlled guest environment. (source: wiki/sources/descriptions/woand__ShitJumpingVM.md)

## Links

- Repo: https://github.com/woand/ShitJumpingVM

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[virtualmachine]] · [[virtual-app]] · [[zn-toolbox]] · [[mobile-anti-cheat]] · [[android-emulator-detection]]
