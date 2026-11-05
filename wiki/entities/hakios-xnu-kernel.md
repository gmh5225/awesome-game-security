---
title: HakiOS XNU Kernel
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/oosexgang__hakios-xnu-kernel.md
updated: 2026-11-05
confidence: medium
---

# HakiOS XNU Kernel

Independent research project (oosexgang) that ports Apple’s open-source **Darwin / XNU** kernel to **Android phone hardware**, with a custom boot loader, in-tree platform drivers, Linux-style kernel configuration, and dedicated build tooling. Implementation is mainly **C** and **C++**, covering GPU (**Adreno**), Wi‑Fi, cellular, storage, input, and power, plus integrated **hakios-metal** for Metal-style graphics on Qualcomm GPUs. Runs in **QEMU** without Apple hardware, or boots from **RAM** on supported phones and returns to Android after reboot—not a replacement phone ROM. Aimed at kernel developers, mobile security researchers, and anyone studying XNU, driver bring-up, or low-level platform behavior on non-Apple hardware. (source: wiki/sources/descriptions/oosexgang__hakios-xnu-kernel.md)

Related iOS-userland-on-Android work: [[hackios-xnu-kernel]] (earlier oosexgang tree targeting stock iOS 16.5 userspace on POCO X5 Pro / QEMU).

## Links

- Repo: https://github.com/oosexgang/hakios-xnu-kernel

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[hackios-xnu-kernel]] · [[xnu-qemu-arm64]] · [[xnu-1day-practice]] · [[xnuspy]] · [[darwin-vm]] · [[vphone-cli]]
