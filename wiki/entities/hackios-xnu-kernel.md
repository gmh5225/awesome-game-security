---
title: HackiOS XNU Kernel
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/oosexgang__hackios-xnu-kernel.md
updated: 2026-10-23
confidence: medium
---

# HackiOS XNU Kernel

Research platform (oosexgang) that boots Apple’s open-source **XNU** kernel for iOS 16.5 on **Android phone hardware** (Xiaomi POCO X5 Pro 5G / redwood, Snapdragon 778G) or in **QEMU**, then runs an unmodified iOS 16.5 user space through lock screen, SpringBoard, Safari, and Wi-Fi. Supplies XNU patches, a custom EFI loader, Mu-Silicium UEFI port, in-kernel driver replacements, and Wi-Fi support built around Linux `ath11k` on a compatibility layer, plus build scripts and the `xl` USB control tool. Sessions are **ephemeral RAM fastboot** experiments (no permanent flash); IPSW artifacts are fetched from Apple CDN. Targets researchers studying iOS kernel behavior, platform security, and low-level mobile internals on commodity Qualcomm Android hardware or in a reproducible virtual environment. (source: wiki/sources/descriptions/oosexgang__hackios-xnu-kernel.md) (source: wiki/sources/README-categories.md)

Expands the **IOS Emulator** README lane (~6 links) beside [[darwin-vm]], [[vphone-cli]], and [[qemu-apple-silicon]].

## Links

- Repo: https://github.com/oosexgang/hackios-xnu-kernel

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[darwin-vm]] · [[vphone-cli]] · [[vphone-ws]] · [[xnu-qemu-arm64]]
