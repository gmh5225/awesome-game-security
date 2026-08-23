---
title: WSA Kernel Build
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/KiruyaMomochi__wsa-kernel-build.md
updated: 2026-08-23
confidence: medium
---

# WSA Kernel Build

Docker-based environment for building the **Windows Subsystem for Android (WSA)** Linux kernel. Packages required build tools and cross-compilation dependencies for **x86_64** and **arm64** targets. Workflow targets reproducible local builds and **CI** pipelines using Docker and standard Linux kernel build tooling. Aimed at developers and security researchers who need custom WSA kernels for testing or instrumentation. Complements kernel mirror/automation repos such as [[wsa-linux-kernel]] and prebuilt distributions such as [[wsa-builds]]; sits in the README `WSA` lane beside sideload/patch tooling such as [[wsapatch]] and [[wsa-pacman]]. (source: wiki/sources/descriptions/KiruyaMomochi__wsa-kernel-build.md)

## Links

- Repo: https://github.com/KiruyaMomochi/wsa-kernel-build (README tag: Build WSA Kernel with Docker)

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[wsa-linux-kernel]] · [[wsa-builds]] · [[wsa-kernel-su]] · [[magiskonwsalocal]] · [[wsapatch]] · [[wsa-pacman]]
