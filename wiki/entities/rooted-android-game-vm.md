---
title: Rooted Android Game VM
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Iviesever__rooted-android-game-vm.md
  - wiki/sources/README-categories.md
updated: 2026-09-20
confidence: medium
---

# Rooted Android Game VM

Windows 11 desktop application that delivers a **rooted Android emulator** and integrated debugging workbench for running, testing, and inspecting Android games and apps without relying on the command line. Built in **C# / .NET** with a **WPF** launcher, **JSON CLI**, and **Inno Setup** installer. (source: wiki/sources/descriptions/Iviesever__rooted-android-game-vm.md)

**Capabilities:** automated download and verification of the Android SDK, emulator, system image, and **Magisk** root tooling inside an isolated virtual device; APK install/update, browsing and exporting application private directories, root diagnostics, checkpoints, file transfers, and automation-friendly debug operations through a shared GUI/CLI service layer.

**Audience:** Android reverse engineering, game security research, and authorized app analysis on Windows. Does not promise compatibility with Play Integrity, anti-emulator, or anti-root protections.

Sits in the desktop-hosted Android emulator lane beside on-device guest VMs such as [[virtualmachine]] (VM Studio) and container sandboxes such as [[zn-toolbox]] — host-side isolation with explicit root/Magisk tooling rather than phone-local syscall translation.

## Links

- Repo: https://github.com/Iviesever/rooted-android-game-vm

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[virtualmachine]] · [[zn-toolbox]] · [[rootavd]] · [[scrcpy]] · [[mobile-anti-cheat]] · [[android-emulator-detection]]
