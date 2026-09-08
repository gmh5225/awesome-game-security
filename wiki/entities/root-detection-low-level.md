---
title: Root Detection Low level
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/3v1lC0d3__Root_Detection_Low_level.md
updated: 2026-09-08
confidence: medium
---

# Root Detection Low level

**Root_Detection_Low_level** (3v1lC0d3) — Frida-based dynamic analysis script for Android apps that monitors suspicious file-system activity and shell command execution at runtime. (source: wiki/sources/descriptions/3v1lC0d3__Root_Detection_Low_level.md)

## Mechanism

Hooks **`java.io.File`** for path access and **`java.lang.Runtime.exec()`** for shell commands. Filters paths containing keywords such as **`su`**, **`bin`**, and **`apk`**; logs commands executed through the runtime shell. On suspicious file operations, captures **Java stack traces** to trace which code triggered the behavior—mapping root-detection call sites without static patching.

## Use cases

Android security testing, malware analysis, reverse engineering, and investigating how apps perform root detection and other low-level runtime checks. Analysis/tracing tool—not a bypass drop-in; complements [[ssl-bypass]] and signature-driven generators such as [[auto-generate-frida-bypass-scripts-for-ssl-pinning-root-detection-on-android-ios]].

## Links

- Repo: https://github.com/3v1lC0d3/Root_Detection_Low_level [Frida hooks on java.io.File and Runtime.exec for root-detection behavior analysis]

## Related

[[frida]] · [[mobile-anti-cheat]] · [[0xdea-frida-scripts]] · [[ssl-bypass]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
