---
title: vphone-cli
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Lakr233__vphone-cli.md
updated: 2026-08-23
confidence: medium
---

# vphone-cli

CLI tool and **firmware patching framework** for building and running **virtualized iPhones (vphone)** on **Apple Silicon Macs**. Combines Swift CLI source with Python patchers for **iBoot**, **kernel**, and **TXM** components, plus jailbreak patch sets, ramdisk builders, and research notes on kernel binary patches and keyboard event pipelines. Boots virtual iOS via **Virtualization.framework** using a **PCC research VM** with **SIP/AMFI disabled**, supporting **DFU**, **restore**, **ramdisk**, and **custom firmware (CFW)** workflows. (source: wiki/sources/descriptions/Lakr233__vphone-cli.md)

Primarily for **iOS security researchers** and **emulator developers** building custom firmware for virtualized iOS environments—complements QEMU full-system iOS/XNU labs such as [[xnu-qemu-arm64]] and Apple-host VM tooling such as [[utm]] on the README `IOS Emulator` lane.

## Links

- Repo: https://github.com/Lakr233/vphone-cli (README: Boot virtual iPhone on macOS via Virtualization.framework)

## Related

[[xnu-qemu-arm64]] · [[utm]] · [[xnu-1day-practice]] · [[malimite]] · [[ida-ios-helper]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
