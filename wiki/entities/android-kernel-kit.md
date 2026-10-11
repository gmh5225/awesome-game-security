---
title: Android Kernel Kit
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/orhpel__android-kernel-kit.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: high
---

# Android Kernel Kit

**android-kernel-kit** (orhpel; AKK) is a **pure Bash** workflow toolkit for Android custom-kernel work: source checkout through compile, `boot.img` repack, ADB flash, and post-boot verification. Listed under README **Cheat** beside other kernel-build automation (not a game cheat artifact). (source: wiki/sources/descriptions/orhpel__android-kernel-kit.md)

## Workflow

Automates clean builds, boot-image repacking via Android Image Kitchen or `magiskboot`, device flashing, log capture, and debug-bundle collection, with automatic DTB handling and schema-driven per-project configuration. Toolchain setup, tmux build streaming, and guided dependency checks aim to keep repeated kernel iterations predictable without manual AVB signing or full boot-image rebuilds for every tweak. (source: wiki/sources/descriptions/orhpel__android-kernel-kit.md)

## Audience

Targets developers and security researchers doing custom Android kernels for bring-up, low-level debugging, and mobile platform work where kernel changes support reverse engineering or security research—complements [[compile-android-driver]], [[kernel-build-scripts]], and [[kernel-build-action]] in the same lane. (source: wiki/sources/descriptions/orhpel__android-kernel-kit.md)

## Links

- Repo: https://github.com/orhpel/android-kernel-kit

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[compile-android-driver]] · [[kernel-build-scripts]] · [[kernel-build-action]] · [[magiskboot]]
