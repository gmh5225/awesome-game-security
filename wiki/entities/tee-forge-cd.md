---
title: TeeForge-CD
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/mcxiaochenn__TeeForge-CD.md
  - wiki/sources/README-categories.md
updated: 2026-11-01
confidence: high
---

# TeeForge-CD

**TeeForge-CD** (mcxiaochenn) is a rooted **Magisk**, **KernelSU**, and **APatch** module that automates upkeep of Android **TEE-related attestation backends**, optional **bootloader/verified-boot** property masking, and user-triggered **Keybox** synchronization for **Play Integrity**–style client checks. Targets researchers and power users who need a maintained **multi-ABI** workflow around hardware attestation and integrity evasion. (source: wiki/sources/descriptions/mcxiaochenn__TeeForge-CD.md)

## Backends and boot behavior

On boot, refreshes compatible backends—**Tricky Store**, **TEESimulator**, **TEESimulator-RS**, and **Oh My Keymint** app scopes—and runs categorized **resetprop** hardening via a dedicated hide helper. **Keybox** updates are explicit (Action, on-device WebUI, or CLI), not automatic at boot. (source: wiki/sources/descriptions/mcxiaochenn__TeeForge-CD.md)

## Keybox and RKP

Keybox material can come from a remote **public key pool** or from locally issued **Remote Key Provisioning (RKP)** chains on supported **Qualcomm arm64** devices. The CLI exposes RKP issuance, target listing, and self-update tooling. (source: wiki/sources/descriptions/mcxiaochenn__TeeForge-CD.md)

## Implementation

Implemented mainly in **Rust** with companion **C** native code, shell-based module installers, and a **Vue/TypeScript WebUI** for on-device control. (source: wiki/sources/descriptions/mcxiaochenn__TeeForge-CD.md)

Listed in the README under **Cheat → Magisk** beside orchestration modules such as [[jerrymanager]] and catalogs such as [[zamr]] and [[android-mods]].

## Links

- Repo: https://github.com/mcxiaochenn/TeeForge-CD

## Related

[[magisk-hub]] · [[android-mods]] · [[jerrymanager]] · [[pif-config-generator]] · [[zamr]] · [[mobile-anti-cheat]] · [[mobile-trust-boundaries]] · [[kernelsu]] · [[magisk]] · [[trickystore]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
