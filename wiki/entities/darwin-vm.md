---
title: darwin-vm
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jprx__darwin-vm.md
  - wiki/sources/README-categories.md
updated: 2026-08-29
confidence: medium
---

# darwin-vm

QEMU-based environment (jprx) for booting lightweight, debuggable **iOS and macOS (Darwin)** systems to a root shell without jailbreak or kernel patches. Emulates Apple Silicon devices from iPhone 12 through iPhone 17 (A14–A19) and M1 through M5 Macs using a custom `qemu-sptm` fork supporting SPTM, TXM, and MIE-based kernels. Python and shell scripts automate IPSW extraction, filesystem patching, trust-cache signing, and VM launch; GDB or LLDB attach for kernel and userspace debugging. Researchers can compile and run custom root-level programs, swap development kernels from Apple Kernel Debug Kits, and inspect or patch `kernel`, `dyld`, `launchd`, and other low-level Darwin components. Headless by design—no GUI or SpringBoard—targeting security researchers, reverse engineers, and kernel developers who need a fast, reproducible sandbox for Apple platform internals. (source: wiki/sources/descriptions/jprx__darwin-vm.md)

Expands the IOS Emulator README lane (~4 links) beside [[qemu-apple-silicon]] and [[vphone-cli]] for jailbreak-free Darwin kernel and userspace RE.

## Links

- Repo: https://github.com/jprx/darwin-vm

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[qemu-apple-silicon]] · [[vphone-cli]] · [[xnu-qemu-arm64]]
