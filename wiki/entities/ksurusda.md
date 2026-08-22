---
title: ksurusda
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/zensu357__ksurusda.md
updated: 2026-08-22
confidence: medium
---

# ksurusda

**KsuRusda** is an Android **Zygisk** module that injects a stealth, anti-detection **Frida gadget** into selected apps on rooted devices running **KernelSU**, **Magisk**, or **APatch**. It bundles the **Rusda** patched Frida kernel, stripping common Frida fingerprints (thread names, RPC identifiers, memfd mappings) while remaining compatible with standard Frida clients and scripts. (source: wiki/sources/descriptions/zensu357__ksurusda.md)

Injection occurs at Zygisk **`postAppSpecialize`** without APK signature changes. **Library remapping** hides mapped gadget paths; optional startup delays and child-process gating help evade ptrace-based and startup anti-debug checks. Operators configure targets via responsive **WebUI** or JSON. **TCP listen mode** supports PC-side dynamic debugging; **offline script mode** loads local JavaScript without network permissions. (source: wiki/sources/descriptions/zensu357__ksurusda.md)

Targets mobile security researchers, reverse engineers, and auditors hooking protected Android applications—including games with anti-Frida defenses. Contrasts with boot-persistent server modules such as [[florida-zygisk]] and complements gadget injectors such as [[zygisk-frida]] and [[ksu-rust-frida]]. Framework home: [[magisk]] · [[kernelsu]] · [[zygisk]] · [[frida]].

## Links

- Repo: https://github.com/zensu357/ksurusda (Zygisk module injecting Rusda anti-detection Frida gadget on KernelSU, Magisk, or APatch)

## Related

[[frida]] · [[zygisk]] · [[magisk]] · [[kernelsu]] · [[florida-zygisk]] · [[zygisk-frida]] · [[ksu-rust-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[antifrida]] · [[frida-detection]]
