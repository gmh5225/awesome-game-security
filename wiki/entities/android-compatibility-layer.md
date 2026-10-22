---
title: Android Compatibility Layer
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/reveny__Android-Compatibility-Layer.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: medium
---

# Android Compatibility Layer

**Android Compatibility Layer (ACL)** (reveny) runs Android APKs on **x86_64 Linux** without VMs, containers, or full system images. Dex bytecode executes on a host-built **ART** runtime; **arm64-v8a** native libraries are **LLVM AOT**- or **JIT**-translated to x86_64. The stack reimplements framework services with **Wayland**, **Vulkan/OpenGL ES**, fonts, SQLite, and PipeWire, with optional **seccomp**, **Landlock**, and isolated PID/network namespaces. (source: wiki/sources/descriptions/reveny__Android-Compatibility-Layer.md) (source: wiki/sources/README-categories.md)

README **Android Emulator** (~12 links) sample; complements container stacks such as [[anbox]] and hypervisor/QEMU hosts for mobile game RE on Linux.

## Links

- Repo: https://github.com/reveny/Android-Compatibility-Layer

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[anbox]] · [[rooted-android-game-vm]] · [[il2cpp]] · [[mobile-trust-boundaries]]
