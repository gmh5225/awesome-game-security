---
title: android-hardware-attestation-demo
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/quarkslab__android-hardware-attestation-demo.md
updated: 2026-08-12
confidence: medium
---

# android-hardware-attestation-demo

Quarkslab end-to-end proof of concept that bypasses backend Android hardware Key Attestation by relaying genuine attestation certificate chains from a clean, bootloader-locked device to a rooted analysis phone. The bypass does not forge cryptography—it substitutes a legitimate TEE/StrongBox hardware-backed chain bound to the backend challenge so verified-boot and hardware-backed checks pass on a compromised device. (source: wiki/sources/descriptions/quarkslab__android-hardware-attestation-demo.md)

Stack: two Kotlin Android apps (demo client + attestation oracle server), a Python backend that issues nonces and validates chains against Google root CAs and revocation lists, and TypeScript [[frida]] hooks on `KeystoreAttestation.generateAttestedKey` to forward the backend nonce to the clean device and return its chain. Educational material for mobile security researchers studying anti-tamper and anti-cheat mechanisms that rely on Android hardware attestation.

Complements defensive attestation tooling such as [[keyattestation]] and Samsung TA research such as [[keybuster]] with an offensive relay model—server-side validation alone cannot distinguish a locally generated chain from one proxied from another device unless binding extends beyond the attestation nonce.

## Links

- Repo: https://github.com/quarkslab/android-hardware-attestation-demo

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[keyattestation]] · [[keybuster]] · [[frida]] · [[knoxpatch]] · [[spoofing-collection]]
