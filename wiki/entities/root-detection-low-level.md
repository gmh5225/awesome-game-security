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

**Root_Detection_Low_level** (3v1lC0d3) — Frida-based dynamic analysis script for Android apps that monitors suspicious file-system activity and shell command execution. Hooks `java.io.File` and `java.lang.Runtime.exec()` to log paths containing keywords such as `su`, `bin`, and `apk`, and captures Java stack traces when suspicious file operations occur. JavaScript Frida script for Android security testing, malware analysis, RE, and studying how apps perform root detection and low-level runtime checks. (source: wiki/sources/descriptions/3v1lC0d3__Root_Detection_Low_level.md)

## Links

- Repo: https://github.com/3v1lC0d3/Root_Detection_Low_level [Frida hooks on java.io.File and Runtime.exec for root-detection behavior analysis]

## Related

[[frida]] · [[mobile-anti-cheat]] · [[0xdea-frida-scripts]] · [[ssl-bypass]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
