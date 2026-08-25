---
title: MAST Orchestrator
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/GliTcHZzZ67__mast-orchestrator.md
updated: 2026-08-25
confidence: medium
---

# MAST Orchestrator

Web-based dashboard for automating mobile application security testing on rooted Android devices via [[frida]]. Python/Flask backend uses ADB to discover connected devices, verify root access, and deploy architecture-matched `frida-server` binaries with one click. (source: wiki/sources/descriptions/GliTcHZzZ67__mast-orchestrator.md)

Ships with ready-made Frida hooks for SSL pinning bypass, root detection bypass, and cryptographic API monitoring. Can fetch additional scripts from approved remote sources such as GitHub Raw or Frida Codeshare. Browser UI streams hook output in real time; API endpoints are protected with token-based authentication.

Targets security researchers and penetration testers performing authorized dynamic analysis of Android applications — including game clients with SSL pinning, root checks, and crypto-protected traffic.

## Links

- Repo: https://github.com/GliTcHZzZ67/mast-orchestrator

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[rootraven]] · [[frida-ide]] · [[mobile-anti-cheat]] · [[auto-generate-frida-bypass-scripts-for-ssl-pinning-root-detection-on-android-ios]]
