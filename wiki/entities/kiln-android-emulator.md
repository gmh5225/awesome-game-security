---
title: kiln-android-emulator
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/NKS1608__kiln-android-emulator.md
updated: 2026-10-20
confidence: medium
---

# kiln-android-emulator

**Kiln** is an Android emulator for **Apple Silicon Macs** that runs full phone-like **Android 16** instances in a window, aimed at apps and mobile games. It builds on a customized **QEMU** stack with **Apple Hypervisor Framework** acceleration, custom Linux kernel modules, and GPU-backed **OpenGL ES 3.1** and **Vulkan** rendering through **gfxstream** and **MoltenVK**. Each instance can mimic many retail phone models with separate **SIM**, **IMEI**, and hardware profiles; the launcher adds per-game key mapping, controllers, **adb**, shells, and a **`kilnctl`** CLI for automation. The open-source portion is mostly C kernel and QEMU device code plus build scripts, alongside a **LineageOS**-based guest image. (source: wiki/sources/descriptions/NKS1608__kiln-android-emulator.md)

Useful for game security and reverse-engineering workflows that need a controllable Android environment on macOS—studying **emulator detection**, **Play Integrity** limits, and app behavior outside certified hardware—alongside QEMU research hosts such as [[qemu-gvm]] and detection libraries such as [[android-emulator-detection]].

## Links

- Repo: https://github.com/NKS1608/kiln-android-emulator

## Related

[[qemu-gvm]] · [[android-emulator]] · [[genymotion-kernel]] · [[anti-emulator]] · [[android-emulator-detection]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
