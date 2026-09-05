---
title: vphone-aio
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/34306__vphone-aio.md
updated: 2026-09-05
confidence: medium
---

# vphone-aio

**All-in-one** macOS setup bundle — shell script plus compressed archives — that provisions a **pre-jailbroken vphone iOS emulator** with **full bootstrap** installed. Automates downloading, merging, and extracting the [[vphone-cli]] environment on **Apple Silicon Macs**, requiring **SIP disabled** and **AMFI bypassed**. Targets **iOS security researchers** and emulator users who need a ready-to-use jailbroken iOS lab for **app analysis and testing** without manual firmware assembly. (source: wiki/sources/descriptions/34306__vphone-aio.md)

Sits on the README `IOS Emulator` lane as a turnkey wrapper around Lakr233's Virtualization.framework vphone stack — complements lower-level [[vphone-cli]] patch/build workflows, QEMU full-system labs such as [[xnu-qemu-arm64]] and [[darwin-vm]], and Apple-host VM tooling such as [[utm]].

## Links

- Repo: https://github.com/34306/vphone-aio (README: 1 script run the vphone)

## Related

[[vphone-cli]] · [[xnu-qemu-arm64]] · [[darwin-vm]] · [[qemu-apple-silicon]] · [[utm]] · [[malimite]] · [[ida-ios-helper]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
