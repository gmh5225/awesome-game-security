---
title: WSA Next
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__wsa-next.md
updated: 2026-11-24
confidence: medium
---

# WSA Next

Community upgrade path for **Windows Subsystem for Android (WSA)** that ships **AOSP Android 15** images for **Microsoft WSA 2407** on **Windows 11** while reusing the stock **Hyper-V** host, HALs, and package identity. The Windows side is a native **C++23** installer and manager with PowerShell/shell tooling; the Android side adds custom device layers (Java/C++) with patches across frameworks, telephony, Bluetooth, and **SELinux** policy. Features include **Google Play** registration, **ARM64** app translation (`ndk_translation`), **virtiofs** storage, host-accelerated video decode, and bridges for **Windows Hello**, Bluetooth, and SIM/SMS/MMS. Optional per-request root uses a documented **uid-0** helper named `0` instead of a traditional `su` binary—aimed at evading common root and anti-cheat fingerprint checks—while gating elevation on **Windows Hello** and keeping signed images. Targets developers, reverse engineers, and security researchers who need current Android apps and games on Windows, including how mobile anti-tamper, **DRM**, and root-detection behave in a desktop WSA environment. Sits in the README `WSA` lane beside prebuilt distributions such as [[wsa-builds]], Magisk integration such as [[magiskonwsalocal]], and kernel root modules such as [[wsa-kernel-su]]. (source: wiki/sources/descriptions/wesmar__wsa-next.md)

## Links

- Repo: https://github.com/wesmar/wsa-next (README tag: WSA)

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[wsa-builds]] · [[magiskonwsalocal]] · [[wsa-kernel-su]] · [[wsa-linux-kernel]] · [[wsapatch]] · [[wsa-pacman]] · [[how-to-download-and-install-wsa]] · [[mobile-anti-cheat]] · [[root-detection-low-level]]