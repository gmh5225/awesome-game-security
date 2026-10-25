---
title: Unthemidator
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/x86rc__unthemidator.md
updated: 2026-10-25
confidence: medium
---

# Unthemidator

C++20 **static unpacker** for Windows PE modules protected with **Themida**, **Code Virtualizer**, and **WinLicense** (README: v3–v4). Unpacks through **CPU emulation** with Unicorn and Zydis so the protected binary is **not executed on the host** and its APIs are not invoked directly; the tool then **rebuilds a runnable, debuggable PE** with restored imports, resources, and decompressed virtual-machine code. Covers **32-bit and 64-bit** executables, DLLs, drivers, and related modules; can identify Themida/Code Virtualizer VM versions and protection entry points. Targets reverse engineers and security researchers analyzing commercially packed software, including games and other Oreans-shielded applications. (source: wiki/sources/descriptions/x86rc__unthemidator.md)

Complements dynamic Cheat → Fix Themida tooling ([[unlicense]] Frida strip, [[magicmida-rs]] Win32 Debug API unpack, [[bobalkkagi]] Unicorn API-hook emulation): **emulation-first static unpack + full PE rebuild** without running the protected sample, beside post-unpack deobfuscation ([[themida-unmutate]], [[ghidr-orean]]) and attach helpers ([[themidie]]).

## Links

- Repo: https://github.com/x86rc/unthemidator

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unlicense]] · [[bobalkkagi]] · [[magicmida-rs]] · [[themida-unmutate]] · [[themida-research]] · [[ghidr-orean]] · [[unicorn-pe]]
