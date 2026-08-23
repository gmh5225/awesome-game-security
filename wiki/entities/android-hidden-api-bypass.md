---
title: AndroidHiddenApiBypass
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/LSPosed__AndroidHiddenApiBypass.md
updated: 2026-08-23
confidence: medium
---

# AndroidHiddenApiBypass

**AndroidHiddenApiBypass** (LSPosed) is a **pure-Java library** for bypassing Android **non-SDK (hidden) API restrictions** so restricted framework interfaces can be accessed at runtime. It ships two variants — **HiddenApiBypass** and **LSPass** — with APIs to invoke restricted methods and constructors, read hidden fields, and manage exemption prefixes. The implementation avoids native code and is packaged for modern Android dependency workflows. Commonly used in advanced Android instrumentation, compatibility tooling, and security research. (source: wiki/sources/descriptions/LSPosed__AndroidHiddenApiBypass.md)

Complements JNI-based hidden-API bypass such as [[bypass-hidden-api-restriction]]; pairs with LSPosed/Xposed hook scaffolding such as [[xposed-module-kit]], runtime DEX tooling such as [[dexbuilder]], and ART hook libraries such as [[canyie-pine]] and [[stoic]].

## Links

- Repo: https://github.com/LSPosed/AndroidHiddenApiBypass (Bypass hidden api restriction)

## Related

[[bypass-hidden-api-restriction]] · [[xposed-module-kit]] · [[dexbuilder]] · [[canyie-pine]] · [[stoic]] · [[frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
