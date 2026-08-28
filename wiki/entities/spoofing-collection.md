---
title: SpoofingCollection
kind: entity
topics: [mobile-security, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/mrx7014__SpoofingCollection.md
updated: 2026-08-02
confidence: medium
---

# SpoofingCollection

Curated **Android device-identity spoofing** profiles for rooted phones. Each target ships as a paired **Magisk module** (boot-time system-property rewrite) and **LSPosed Xposed module** (Java hooks on runtime `Build` fields such as `MANUFACTURER`, `MODEL`, `DEVICE`, and `PRODUCT`). Flagship profiles include Samsung Galaxy S26 Ultra, OnePlus 15, Galaxy Tab S10 Ultra, Google Pixel 10 Pro XL, Pixel Tablet, and Xiaomi 17 Pro Max, with attestation-related properties where applicable. (source: wiki/sources/descriptions/mrx7014__SpoofingCollection.md)

Aimed at security researchers studying **mobile anti-cheat**, **Play Integrity**, and **device attestation** on rooted Android, or analyzing how apps fingerprint hardware and how checks can be influenced at both the property and API layers. Sits in the Cheat Magisk / device-fingerprint lane alongside Pixel-only disguise [[easypixel]] and opposite fingerprint SDKs such as [[trustdevice-android]] and attestation probes such as [[keyattestation]].

## Links

- Repo: https://github.com/mrx7014/SpoofingCollection

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[magisk]] · [[xposed-module-kit]] · [[hidemyandroid]] · [[locusmimic]] · [[easypixel]] · [[keyattestation]] · [[trustdevice-android]] · [[magiskdetector]] · [[mobile-anti-cheat]]
