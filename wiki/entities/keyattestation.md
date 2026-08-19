---
title: KeyAttestation
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/vvb2060__KeyAttestation.md
  - wiki/sources/descriptions/VisionR1__KeyAttestation.md
  - wiki/sources/descriptions/quarkslab__android-hardware-attestation-demo.md
  - wiki/sources/descriptions/beakthoven__TrickyStore.md
updated: 2026-08-19
confidence: medium
---

# KeyAttestation

Android app that performs hardware-backed key attestation to verify device integrity and bootloader status. Talks to Android Keymaster / KeyMint HALs via AIDL, retrieves and validates attestation certificates, and checks locked bootloader, verified-boot state, and provisioned key properties. Useful for Android security researchers and mobile anti-cheat engineers studying hardware attestation and device-integrity verification. (source: wiki/sources/descriptions/vvb2060__KeyAttestation.md)

**VisionR1 fork** — Java/Kotlin test application for generating, parsing, and verifying key attestation evidence; save/load certificate chains; local and remote revocation-list handling; RSA attestation support, language/theme options, and privacy-oriented certificate display controls for mobile security validation, device-integrity testing, and attestation research. (source: wiki/sources/descriptions/VisionR1__KeyAttestation.md)

README lane: Cheat / Bootloader. Complements Magisk / root detection samples such as [[magiskdetector]] (same author) with a hardware-attestation view of boot and key trust. Offensive relay bypass PoC that substitutes genuine chains from a clean device: [[android-hardware-attestation-demo]] (Quarkslab; Frida Keystore hook + oracle server). Offensive Keystore-layer trick rewrite [[trickystore]] (beakthoven; Android 10+; cheat / HWID research) studies keystore manipulation opposite these validation probes. Offensive counterpart for Samsung Keymaster TA trust failures: [[keybuster]].

## Links

- Repo (original): https://github.com/vvb2060/KeyAttestation
- Repo (VisionR1 fork): https://github.com/VisionR1/KeyAttestation

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[android-hardware-attestation-demo]] · [[trickystore]] · [[keybuster]] · [[magiskdetector]] · [[cheese]] · [[magiskboot-ndk-on-linux]] · [[ofrp-device-xiaomi-mondrian]]
