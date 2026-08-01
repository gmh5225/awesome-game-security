---
title: KPM-MemReader
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/libtersafe__KPM-MemReader.md
updated: 2026-08-01
confidence: medium
---

# KPM-MemReader

**KernelPatch Module (KPM)** for Android that enables **cross-process memory read** via an **ioctl hook**, loadable through KernelPatch / [[apatch-kpm]] on rooted GKI devices. Written in C/C++; focuses on kernel-level modding and hooking in the cheat / Android kernel driver lane. (source: wiki/sources/descriptions/libtersafe__KPM-MemReader.md)

## What it covers

- Kernel-scope memory read across process boundaries (ioctl-mediated hook path)
- APatch / KernelPatch module integration — same KPM class as collections in [[apatch-kpm]] and title RE such as [[honor-of-kings-re-research]]
- Complements other `libtersafe` ACE research such as [[dfm-android-unicorn]] (userspace emulation) and LKM memory-ops tooling such as [[kernel-hack]] / [[root-socket-kit]]

Audience: game-security researchers and reverse engineers studying offensive Android kernel driver techniques against protected mobile clients.

## Links

- Repo: https://github.com/libtersafe/KPM-MemReader

## Related

[[apatch-kpm]] · [[dfm-android-unicorn]] · [[honor-of-kings-re-research]] · [[kernel-hack]] · [[root-socket-kit]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
