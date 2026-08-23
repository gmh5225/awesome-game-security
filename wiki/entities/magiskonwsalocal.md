---
title: MagiskOnWSALocal
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__MagiskOnWSALocal.md
  - wiki/sources/descriptions/LSPosed__MagiskOnWSALocal.md
updated: 2026-08-23
confidence: medium
---

# MagiskOnWSALocal

Python and shell scripts to integrate **Magisk**, **KernelSU**, and **Google Apps (GApps)** into **Windows Subsystem for Android (WSA)** images locally. Extracts WSA packages, patches Magisk and GApps into the system image, and generates installable WSA builds with root access and **LSPosed** support. Targets Android security researchers and developers who need rooted WSA environments for testing and analysis on Windows 11. Sits in the README `WSA` lane beside sideload/APK tooling such as [[win11-apk-installer]], kernel automation such as [[wsa-linux-kernel]], kernel root modules such as [[wsa-kernel-su]], prebuilt distributions such as [[wsa-builds]], and MSIX patchers such as [[wsapatch]] / [[wsa-pacman]]; extends [[magisk]] and [[kernelsu]] onto Android-on-Windows hosts for mobile game-security and modding research. (source: wiki/sources/descriptions/LSPosed__MagiskOnWSALocal.md) (source: wiki/sources/descriptions/gmh5225__MagiskOnWSALocal.md)

## Links

- Repo: https://github.com/LSPosed/MagiskOnWSALocal

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk]] · [[kernelsu]] · [[wsa-kernel-su]] · [[wsa-linux-kernel]] · [[wsa-builds]] · [[wsapatch]] · [[wsa-pacman]] · [[win11-apk-installer]] · [[rootavd]] · [[aeroot]] · [[zygisk]] · [[xposed-module-kit]] · [[mobile-anti-cheat]]
