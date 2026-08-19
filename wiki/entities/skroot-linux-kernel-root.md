---
title: SKRoot-linuxKernelRoot
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/abcz316__SKRoot-linuxKernelRoot.md
updated: 2026-08-19
confidence: medium
---

# SKRoot-linuxKernelRoot

Android-focused **Linux kernel root patching toolkit** for deeply hidden root on stock kernels. Combines C/C++ kernel patch components with Java/JNI app tooling for permission management and deployment. Advertises root command execution, `su` installation and injection, and compatibility across many kernel versions without rebuilding the kernel from source. Used in mobile game and app security research for root detection, bypass behavior, and kernel-level privilege control. (source: wiki/sources/descriptions/abcz316__SKRoot-linuxKernelRoot.md)

Sits in the same Android kernel-root lane as [[kernelsu]], [[apatch]], and [[kernelpatch]] boot-image patching, but emphasizes patch-based privilege on existing vendor kernels rather than module frameworks alone. Same maintainer ecosystem as ARM64 kernel memory driver [[rw-proc-mem33]] (abcz316).

## Links

- Repo: https://github.com/abcz316/SKRoot-linuxKernelRoot

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[apatch]] · [[kernelpatch]] · [[rw-proc-mem33]] · [[magiskdetector]] · [[detection]] · [[mobile-anti-cheat]]
