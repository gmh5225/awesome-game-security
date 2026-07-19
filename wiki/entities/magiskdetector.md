---
title: MagiskDetector
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/vvb2060__MagiskDetector.md
updated: 2026-07-19
confidence: medium
---

# MagiskDetector

Archived Android app that detects Magisk root-framework installs. Runs checks in an isolated process via AppZygote and AIDL remote-service IPC (outside the main app sandbox), probing Magisk artifacts and mount-namespace anomalies. Useful for mobile anti-cheat engineers and researchers studying Magisk detection and root-hide / DenyList bypass tradeoffs. (source: wiki/sources/descriptions/vvb2060__MagiskDetector.md)

Sits in the Anti Cheat `Detection:Magisk` / Android-root lane alongside Magisk install and hide tooling such as [[cheese]], [[move-certificate]], and [[magiskboot-ndk-on-linux]].

## Links

- Repo: https://github.com/vvb2060/MagiskDetector

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[cheese]] · [[move-certificate]] · [[magiskboot-ndk-on-linux]]
