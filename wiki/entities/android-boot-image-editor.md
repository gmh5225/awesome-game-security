---
title: Android Boot Image Editor
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cfig__Android_boot_image_editor.md
updated: 2026-08-17
confidence: medium
---

# Android Boot Image Editor

Kotlin/Java Gradle tool for reverse engineering Android ROM partition images — `boot.img`, recovery, `vendor_boot`, and related boot partitions. Provides unpack/repack workflows that extract kernels, ramdisks, DTBs, and VBMeta images with AVB signing, LZ4/XZ/GZIP compression, and EROFS/sparse image handling. Runs on Linux, macOS, and Windows with JDK 11+ and supports Android boot image formats v0–v4 plus vendor boot images. (source: wiki/sources/descriptions/cfig__Android_boot_image_editor.md)

Aimed at Android security researchers and ROM developers performing boot-image analysis, modification, and repacking — the same boot-partition lane as Magisk-style root and custom recovery work that mobile anti-cheat often treats as integrity signals.

Adjacent: Magisk-derived boot tooling [[magiskboot]], [[magiskboot-linux]], [[magiskboot-ndk-on-linux]], and [[magiskboot-build]]; OTA partition dumps via [[payload-dumper]] and [[payload-dumper-go]]; root frameworks [[magisk]] and [[kernelsu]].

## Links

- Repo: https://github.com/cfig/Android_boot_image_editor

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[magiskboot]] · [[magiskboot-linux]] · [[magiskboot-ndk-on-linux]] · [[magiskboot-build]] · [[payload-dumper]] · [[payload-dumper-go]] · [[magisk]] · [[kernelsu]]
