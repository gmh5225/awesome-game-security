---
title: frida-ios-dump
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AloneMonkey__frida-ios-dump.md
  - wiki/sources/README-categories.md
updated: 2026-10-14
confidence: high
---

# frida-ios-dump

**frida-ios-dump** (AloneMonkey/frida-ios-dump) is a **host-side Python toolkit** that pulls fully decrypted **IPA** packages from apps running on a **jailbroken** iPhone or iPad. A Python driver attaches with **Frida**, injects a JavaScript agent that uses the **Objective-C bridge** to dump in-memory **Mach-O** binaries and embedded frameworks while **FairPlay** encryption is stripped, then repackages the bundle with parallel **SFTP** transfers over **USB** or **SSH**. (source: wiki/sources/descriptions/AloneMonkey__frida-ios-dump.md)

## Catalog lane

Cheat / IOS App Packaging — jailbroken iOS decrypted IPA acquisition before static RE, patching, or protected-title behavior study. (source: wiki/sources/descriptions/AloneMonkey__frida-ios-dump.md)

## Mechanism

1. **Attach** — Frida injects a JS agent into the target app process on device.
2. **Dump** — ObjC bridge reads decrypted Mach-O and embedded frameworks from memory (FairPlay stripped at runtime).
3. **Transfer** — parallel SFTP pulls modules to the host over USB or SSH (SSH config aliases and keys supported).
4. **Repackage** — host rebuilds an analyzable IPA bundle.

Supports listing installed apps by **display name** or **bundle identifier**; **Frida 17** with bundled **frida-objc-bridge** compilation. Audience: mobile security researchers and reverse engineers who need analyzable iOS binaries for static inspection, patching workflows, or studying how protected games and apps behave on device. (source: wiki/sources/descriptions/AloneMonkey__frida-ios-dump.md)

## Positioning

Active Python alternative beside deprecated Node.js [[bagbak]] in the same jailbroken iOS IPA decrypt/dump lane; pairs with [[frida]] mobile instrumentation and static follow-on in IDA/Ghidra.

## Links

- Repo: https://github.com/AloneMonkey/frida-ios-dump

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[bagbak]] · [[il2cpp-re]]
