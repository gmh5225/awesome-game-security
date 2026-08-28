---
title: xnu-qemu-arm64
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/alephsecurity__xnu-qemu-arm64.md
updated: 2026-08-18
confidence: medium
---

# xnu-qemu-arm64

QEMU fork by Aleph Security that boots a functional iOS system under ARM64 emulation—launchd services, interactive bash, read/write secondary disk devices, unsigned binary execution, and SSH over TCP tunneling, with optional KVM acceleration. Extends QEMU with iOS-specific machine and device models for XNU kernel emulation on ARM64. (source: wiki/sources/descriptions/alephsecurity__xnu-qemu-arm64.md)

Primarily for iOS security researchers and kernel exploit developers studying XNU internals and iOS runtime behavior in an emulated lab, without relying on physical hardware for every experiment. README tag: `[xnu]`.

## Links

- Repo: https://github.com/alephsecurity/xnu-qemu-arm64

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[qemu-apple-silicon]] · [[vphone-cli]] · [[xnu-1day-practice]] · [[xnuspy]] · [[kfd]] · [[kfd-explorer]] · [[cve-2026-xnu-aio-kevent-uaf]] · [[utm]] · [[qemu-gvm]]
