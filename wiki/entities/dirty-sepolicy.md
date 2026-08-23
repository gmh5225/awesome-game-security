---
title: DirtySepolicy
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/LSPosed__DirtySepolicy.md
updated: 2026-08-23
confidence: medium
---

# DirtySepolicy

**DirtySepolicy** (LSPosed) is an **Android app** that demonstrates runtime **SEPolicy / SELinux** manipulation without **root** or **kernel** modifications. It binds to **App Zygote** services via **AIDL** and injects permissive SELinux policy rules at runtime—showing how zygote-scoped policy changes can be achieved from userspace. The same technique supports **detecting userspace `su` solutions** by running **SELinux access checks** from the App Zygote process context. (source: wiki/sources/descriptions/LSPosed__DirtySepolicy.md)

Sits in the **Detection:Android root** lane as an App-Zygote–scoped SELinux probe, complementing multi-check inspectors such as [[advanced-root-checker]] and [[root-app-detector]] and contrasting with Zygote hook/injection frameworks like [[android-super-inject]].

## Links

- Repo: https://github.com/LSPosed/DirtySepolicy (README tag: Detect userspace su solutions via SELinux access checks from the App Zygote process)

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[advanced-root-checker]] · [[root-app-detector]] · [[android-super-inject]] · [[magisk]] · [[kernelsu]]
