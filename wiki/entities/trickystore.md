---
title: TrickyStore
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/5ec1cff__TrickyStore.md
  - wiki/sources/descriptions/beakthoven__TrickyStore.md
updated: 2026-09-04
confidence: medium
---

# TrickyStore

**TrickyStore** (5ec1cff/TrickyStore) is an Android module that modifies the **certificate chain** returned by Android **key attestation**. Targets **Android 10+** (README notes **Android 12+**). Supports **per-app targeting** through configuration files—package lists and optional hardware **keybox** data—and can switch between **leaf-certificate patching** and **generated-certificate** modes to accommodate devices with different TEE behavior. Also supports **security patch level (SPL) spoofing** in attestation results. Primary use case: mobile security research around integrity checks, attestation flows, and anti-tamper validation. (source: wiki/sources/descriptions/5ec1cff__TrickyStore.md)

**beakthoven rewrite** — complete rewrite of the Android **Keystore trick** that manipulates how apps interact with hardware-backed key APIs. Requires **Android 10+**. Aimed at game-security researchers studying offensive techniques in the **cheat / HWID** lane beside Play Integrity and hardware Key Attestation checks. (source: wiki/sources/descriptions/beakthoven__TrickyStore.md)

README lane: Cheat / Keystore. Sits in the Android attestation-evasion lane beside relay PoCs such as [[android-hardware-attestation-demo]], property/profile spoofing such as [[spoofing-collection]], and defensive attestation probes such as [[keyattestation]].

## Links

- Repo (upstream): https://github.com/5ec1cff/TrickyStore
- Repo (beakthoven rewrite): https://github.com/beakthoven/TrickyStore

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[keyattestation]] · [[android-hardware-attestation-demo]] · [[spoofing-collection]] · [[knoxpatch]] · [[mobile-anti-cheat]]
