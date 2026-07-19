---
title: UTM
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/utmapp__UTM.md
updated: 2026-07-19
confidence: medium
---

# UTM

Full-featured QEMU-based virtual machine host for iOS and macOS: runs Windows, Linux, and other guests on Apple devices via hardware virtualization (Apple Hypervisor.framework on Apple Silicon) or JIT-powered emulation for x86, ARM, RISC-V, and related architectures. Swift/Objective-C native UI covers VM create/config, USB passthrough, and shared directories—aimed at developers and researchers who need alternate OSes on Apple hardware. (source: wiki/sources/descriptions/utmapp__UTM.md)

Sits in the README `IOS Emulator` / Apple-host VM lane next to QEMU console stacks such as [[xqemu]] / [[xemu]] and macOS research hosts such as [[x260-lenovo-opencore]] / [[xenia-mac]], when the lab target is a guest OS on iPhone/iPad/Mac rather than console title HLE.

## Links

- Repo: https://github.com/utmapp/UTM (README tag: Virtual machines for iOS and macOS)

## Related

[[xqemu]] · [[xemu]] · [[xenia-mac]] · [[x260-lenovo-opencore]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
