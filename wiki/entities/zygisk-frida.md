---
title: zygisk-frida
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/lico-n__ZygiskFrida.md
  - wiki/sources/descriptions/hex91__zygisk-gadget-stealth.md
updated: 2026-11-06
confidence: medium
---

# zygisk-frida

Magisk **Zygisk** module that injects the **Frida gadget** into Android application processes. Zygisk runs module code during app specialization so the gadget loads early in every target process—useful for game-security researchers and reverse engineers working in the cheat / Magisk lane who need in-process dynamic instrumentation without external `frida-server` attach. (source: wiki/sources/descriptions/lico-n__ZygiskFrida.md)

Contrasts with boot-persistent server modules such as [[florida-zygisk]] (Florida anti-detection `frida-server`) and stealth gadget stacks such as [[zygisk-gadget-stealth]] (hex91; artifact-focused gadget inject without APK repack). Framework home: [[magisk]] · [[zygisk]] · [[frida]].

## Links

- Repo: https://github.com/lico-n/ZygiskFrida (Injects Frida gadget using Zygisk)

## Related

[[frida]] · [[zygisk]] · [[magisk]] · [[florida-zygisk]] · [[zygisk-gadget-stealth]] · [[fridare]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[antifrida]] · [[frida-detection]]
