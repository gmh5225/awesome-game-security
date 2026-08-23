---
title: WSA Linux Kernel
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/WSA-Community__WSA-Linux-Kernel.md
  - wiki/sources/descriptions/LSPosed__WSA-Kernel-SU.md
updated: 2026-08-23
confidence: medium
---

# WSA Linux Kernel

Mirror and build-automation repository for the **Windows Subsystem for Android (WSA)** Linux kernel, including superuser-patched variants. Maintains branch variants for stock source and **KernelSU**-enabled source; provides GitHub Actions pipelines for **x86_64** and **arm64** kernel images. A helper shell script patches required KernelSU configuration entries into WSA kernel trees. Used by Android and platform security researchers who need reproducible WSA kernel builds and customization. Complements runtime kernel root modules such as [[wsa-kernel-su]] (syscall-hook `/system/xbin/su` path with credential/SELinux adjustments for WSA). Sits in the README `WSA` lane beside rooted builds such as [[magiskonwsalocal]] and sideload tooling such as [[wsapatch]] / [[wsa-pacman]]. (source: wiki/sources/descriptions/WSA-Community__WSA-Linux-Kernel.md) (source: wiki/sources/descriptions/LSPosed__WSA-Kernel-SU.md)

## Links

- Repo: https://github.com/WSA-Community/WSA-Linux-Kernel (README tag: WSA)

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[wsa-kernel-su]] · [[magiskonwsalocal]] · [[wsapatch]] · [[wsa-pacman]] · [[win11-apk-installer]]
