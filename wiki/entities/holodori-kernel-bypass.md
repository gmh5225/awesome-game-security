---
title: Holodori-Kernel-Bypass
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/redecorate__Holodori-Kernel-Bypass.md
updated: 2026-07-25
confidence: medium
---

# Holodori-Kernel-Bypass

Holodori Kernel Bypass (holo-emu): userspace emulator for the `usrdrv017964.sys` kernel-driver interface used by the hololive Dreams client. Mainly C with MinHook-based API hooking; a loader injects an emulator DLL that fakes device protocol, service state, registry keys, symbolic links, and loaded-driver metadata without installing or loading the real kernel driver. The `.sys` image is used only as read-only PE data for integrity transforms. Includes a test client and launch helpers for native Windows, Wine, and Proton — aimed at game-security / RE work on anti-tamper kernel drivers without exposing a vulnerable kernel component. (source: wiki/sources/descriptions/redecorate__Holodori-Kernel-Bypass.md)

Complements RING3 driver-analysis stacks such as [[kace]] (full kernel-API emulation) and WHP guests such as [[winvisor]]: Holodori targets a title-specific AC driver *protocol* in userspace rather than loading the `.sys` under an emulator.

## Links

- Repo: https://github.com/redecorate/Holodori-Kernel-Bypass (README: Userspace emulation of Hololive Dreams usrdrv017964 kernel anti-cheat for Wine/Proton)

## Related

[[kace]] · [[winvisor]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
