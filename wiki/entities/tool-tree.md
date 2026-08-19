---
title: Tool-Tree
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Zenlua__Tool-Tree.md
updated: 2026-08-19
confidence: medium
---

# Tool-Tree

Android **ROM and APK toolkit app** for unpacking, packing, and editing firmware images and application packages on **ARM64** devices. Supports boot, dtbo, ext4, erofs, f2fs, payload, super, zip, APK, APKS, APEX, CAPEX, squashfs, and Amlogic image formats, plus built-in shell utilities including **apktool-style** APK decode/build, signing, and BusyBox. Implemented mainly in Kotlin and Java with Bash scripts and a KRScript-style UI for tool workflows; works with or without root. Extensible **Addon** and **Apkon** modules let users add ROM and APK editing capabilities. Aimed at Android reverse engineers, ROM modders, and APK analysts who need on-device firmware and package manipulation. (source: wiki/sources/descriptions/Zenlua__Tool-Tree.md)

Complements desktop decode→patch→sign lanes such as [[apktool]] and [[apk-sh]] when analysts need ROM/APK tooling directly on hardware; sits beside on-device shells such as [[termux-app]] and curated modding collections such as [[android-modding]].

## Links

- Repo: https://github.com/Zenlua/Tool-Tree (README tag: Android ROM/APK unpack-repack toolkit)

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apktool]] · [[apk-sh]] · [[android-modding]] · [[termux-app]]
