---
title: qemu-apple-silicon
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/ChefKissInc__qemu-apple-silicon.md
updated: 2026-08-28
confidence: medium
---

# qemu-apple-silicon

QEMU fork by ChefKissInc with platform-specific modifications for **Apple Silicon virtualization** and **iOS device emulation**. Carries the full upstream QEMU emulator codebase plus ARM-focused changes for running hardware-accelerated ARM virtual machines on Apple Silicon Macs. (source: wiki/sources/descriptions/ChefKissInc__qemu-apple-silicon.md)

Primarily for **iOS security researchers** and **emulator developers** who need accelerated ARM virtualization on macOS for app testing and analysis—complements full-system iOS/XNU QEMU labs such as [[xnu-qemu-arm64]], Virtualization.framework workflows such as [[vphone-cli]], and general Apple-host VM tooling such as [[utm]] on the README `IOS Emulator` lane.

## Links

- Repo: https://github.com/ChefKissInc/qemu-apple-silicon

## Related

[[xnu-qemu-arm64]] · [[vphone-cli]] · [[utm]] · [[xnu-1day-practice]] · [[malimite]] · [[ida-ios-helper]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
