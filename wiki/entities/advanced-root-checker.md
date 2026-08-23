---
title: Advanced Root Checker
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Laert-Android__Advanced-Root-Checker.md
updated: 2026-08-23
confidence: medium
---

# Advanced Root Checker

**Advanced Root Checker** (Laert-Android) is a free, open-source **Android app** that scans a device for **root indicators** and related **security risks** entirely **offline**. Written in **Java** for **Android 5.0+**, it runs dozens of checks covering `su` binaries, BusyBox, **Magisk**, **KernelSU**, **APatch**, **Zygisk**, **Xposed/LSPosed**, root-cloaking apps, **SELinux** state, and dangerous system properties. An **anti-tamper** section probes **Frida**, Xposed hooks, debuggers, suspicious libraries, and APK signature or package-name changes; device security info and a **risk score** summary round out the report. Primary use case: local Android security assessment and root detection for users, developers, and anyone evaluating anti-root or anti-cheat-style checks without network access. (source: wiki/sources/descriptions/Laert-Android__Advanced-Root-Checker.md)

Complements multi-check inspectors such as [[duck-detector-refactoring]], native root detector [[android-native-root-detector]], Frida probes [[detect-frida]], and memory-integrity demo [[memdetection]]—opposite root frameworks [[magisk]], [[kernelsu]], and [[apatch]].

## Links

- Repo: https://github.com/Laert-Android/Advanced-Root-Checker

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[duck-detector-refactoring]] · [[android-native-root-detector]] · [[detect-frida]] · [[memdetection]] · [[root-app-detector]] · [[magisk]] · [[kernelsu]] · [[apatch]]
