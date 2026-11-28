---
title: magisk-frida
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ViRb3__magisk-frida.md
updated: 2026-11-28
confidence: medium
---

# magisk-frida

Magisk/KernelSU/APatch root module that auto-starts official **`frida-server` at boot**, so hosts can attach Frida for dynamic instrumentation without manual server push or lifecycle scripts. Ships multi-arch binaries (arm, arm64, x86, x86_64); module config can override the default local listen port. A Python build pipeline downloads upstream Frida releases and packages installable ZIPs, keeping server versions aligned with official builds. Targets reverse engineers, security researchers, and developers who need reliable on-device Frida for mobile app and game analysis, hooking, and runtime inspection. (source: wiki/sources/descriptions/ViRb3__magisk-frida.md)

Baseline stock-server boot module—contrast anti-detection forks such as [[florida-zygisk]] (Florida-patched server; magisk-frida-derived) and [[magisk-hluda]], Zygisk gadget inject via [[zygisk-frida]], and bundled server+Gadget stacks such as [[frida-magisk]]. Framework home: [[magisk]] · [[kernelsu]] · [[frida]].

## Links

- Repo: https://github.com/ViRb3/magisk-frida (Magisk/KernelSU/APatch module; auto-starts up-to-date frida-server on boot; multi-arch; configurable listen port)

## Related

[[frida]] · [[magisk]] · [[kernelsu]] · [[florida-zygisk]] · [[magisk-hluda]] · [[frida-magisk]] · [[frida-rs]] · [[zygisk-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[antifrida]] · [[frida-detection]]