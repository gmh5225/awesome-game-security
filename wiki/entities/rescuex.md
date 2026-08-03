---
title: RescueX
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/jiayuxuan123__RescueX.md
updated: 2026-08-03
confidence: medium
---

# RescueX

Android root module for **Magisk**, **KernelSU**, and **APatch** that monitors boot behavior and automatically recovers the device when repeated reboots or startup timeouts indicate a **boot loop**. Tiered rescue actions include disabling suspect modules, full module disable with whitelist support, module snapshots and rollback, and a one-time safe mode with precise restoration. Built mainly with shell scripts and a JavaScript WebUI; optionally includes an arm64 native C watchdog. Also provides adaptive boot timeouts, OTA and patch detection, local SHA-256 integrity checks, and sanitized diagnostic export. Intended for rooted Android users and module developers who need reliable, offline recovery when experimental or faulty modules prevent successful boot. (source: wiki/sources/descriptions/jiayuxuan123__RescueX.md)

## Links

- Repo: https://github.com/jiayuxuan123/RescueX

## Related

[[overviews/mobile-security]] · [[magisk]] · [[kernelsu]] · [[move-certificate]] · [[florida-zygisk]] · [[root-socket-kit]]
