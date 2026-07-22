---
title: KeyAttestation
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/vvb2060__KeyAttestation.md
updated: 2026-07-22
confidence: medium
---

# KeyAttestation

Android app that performs hardware-backed key attestation to verify device integrity and bootloader status. Talks to Android Keymaster / KeyMint HALs via AIDL, retrieves and validates attestation certificates, and checks locked bootloader, verified-boot state, and provisioned key properties. Useful for Android security researchers and mobile anti-cheat engineers studying hardware attestation and device-integrity verification. (source: wiki/sources/descriptions/vvb2060__KeyAttestation.md)

README lane: Cheat / Bootloader. Complements Magisk / root detection samples such as [[magiskdetector]] (same author) with a hardware-attestation view of boot and key trust. Offensive counterpart for Samsung Keymaster TA trust failures: [[keybuster]].

## Links

- Repo: https://github.com/vvb2060/KeyAttestation

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[keybuster]] · [[magiskdetector]] · [[cheese]] · [[magiskboot-ndk-on-linux]] · [[ofrp-device-xiaomi-mondrian]]
