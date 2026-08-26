---
title: DroidVM
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Droid-VM__DroidVM.md
updated: 2026-08-26
confidence: medium
---

# DroidVM

Android application for running **virtual machines on-device** using **QEMU/KVM** and the **Qualcomm Gunyah** hypervisor. Supports **ARM64** and **x86_64** guest OS images with **VNC** display and console management. README highlights UEFI Linux/Windows guests, **crosvm/QEMU** backends, **VirGL/GfxStream** GPU passthrough, **VirtFS** sharing, and **root required**. (source: wiki/sources/descriptions/Droid-VM__DroidVM.md)

Sits in the README `Android Emulator` lane beside the Gunyah reference stack [[gunyah-hypervisor]], QEMU research hosts such as [[qemu-gvm]], and Google/Android Studio emulator tooling ([[android-emulator]], [[android-emulator-hypervisor-driver]])—oriented toward Snapdragon on-phone hypervisor labs rather than anti-emulator fingerprint checks ([[anti-emulator]], [[android-emulator-detection]]).

## Links

- Repo: https://github.com/Droid-VM/DroidVM (README: Android VM manager on Snapdragon)

## Related

[[gunyah-hypervisor]] · [[qemu-gvm]] · [[android-emulator]] · [[aeroot]] · [[rootavd]] · [[winlator]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
