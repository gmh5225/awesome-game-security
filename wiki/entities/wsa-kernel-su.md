---
title: WSA Kernel SU
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/LSPosed__WSA-Kernel-SU.md
updated: 2026-08-23
confidence: medium
---

# WSA Kernel SU

Kernel module that exposes a classic `/system/xbin/su` path on Android kernels, with emphasis on **Windows Subsystem for Android (WSA)** setups. Hooks selected syscalls and redirects `su` execution while adjusting credentials and **SELinux** behavior to grant root. Implemented as low-level **C** for modern kernels; includes options to reduce visibility of superuser functionality. Targets Android platform modding and security research where kernel-assisted root behavior is required—complementing broader KernelSU integration paths such as [[wsa-linux-kernel]] and prebuilt WSA distributions like [[wsa-builds]]. (source: wiki/sources/descriptions/LSPosed__WSA-Kernel-SU.md)

## Links

- Repo: https://github.com/LSPosed/WSA-Kernel-SU (README tag: WSA with KernelSU)

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[wsa-linux-kernel]] · [[wsa-builds]] · [[magiskonwsalocal]] · [[wsapatch]] · [[wsa-pacman]]
