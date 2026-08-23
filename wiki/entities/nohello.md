---
title: NoHello
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/MhmRdd__NoHello.md
updated: 2026-08-23
confidence: medium
---

# NoHello

**Zygisk-based Android module** that hides **root** and **Zygisk-related artifacts** from target apps. Native code plus Android build tooling implements **blacklist or whitelist** targeting modes and **mount-rule-driven unmount** logic so per-app concealment can follow configurable policies. Documentation covers setup on **Magisk**, **KernelSU**, **APatch**, and related Zygisk variants. Aimed at mobile security and anti-cheat bypass researchers testing root-detection resistance in app environments. (source: wiki/sources/descriptions/MhmRdd__NoHello.md)

Sits in the Cheat / Magisk root-hide lane beside [[zygisk-magiskhide]], [[magiskhide]], [[hideroot]], and [[riru-momo-hider]]; opposite detectors such as [[magiskdetector]], [[detect-zygisk]], [[meowna-detector]], and [[mobile-anti-cheat]]. Requires a Zygisk-compatible root stack ([[magisk]], [[kernelsu]], [[apatch]], or [[rezygisk]]) with the [[zygisk]] specialization hook path enabled.

## Links

- Repo: https://github.com/MhmRdd/NoHello

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[magisk]] · [[kernelsu]] · [[apatch]] · [[rezygisk]] · [[zygisk]] · [[zygisk-magiskhide]] · [[magiskhide]] · [[mobile-anti-cheat]]
