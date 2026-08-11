---
title: KnoxPatch
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/salvogiangri__KnoxPatch.md
updated: 2026-08-11
confidence: medium
---

# KnoxPatch

**LSPosed Xposed module** (Kotlin) that restores Samsung apps and Knox-protected features on rooted Samsung Galaxy devices. Hooks target Samsung applications to bypass root detection, spoof critical system properties, disable Knox SDK and Samsung Attestation Key checks, and patch Samsung Keystore and Knox Matrix APIs. A companion **KnoxPatch Enhancer** Magisk or [[kernelsu]] module adds system-level patches for features runtime hooks alone cannot fix—such as Secure Folder on legacy One UI devices. Supports One UI from Android 9 through 16; enables apps including Samsung Health, Secure Folder, SmartThings, and Samsung Cloud. Aimed at mobile security research, reverse engineering Samsung Knox integrity mechanisms, and studying how OEM root and attestation checks behave on modified devices. (source: wiki/sources/descriptions/salvogiangri__KnoxPatch.md)

Sits in the Samsung OEM integrity lane beside device-identity spoofing [[spoofing-collection]], attestation probes [[keyattestation]], and TrustZone key-extraction research [[keybuster]].

## Links

- Repo: https://github.com/salvogiangri/KnoxPatch

## Related

[[magisk]] · [[kernelsu]] · [[xposed-module-kit]] · [[spoofing-collection]] · [[keyattestation]] · [[keybuster]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
