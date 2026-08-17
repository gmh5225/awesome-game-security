---
title: MouHidInputHook (changeofpace)
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/changeofpace__MouHidInputHook.md
updated: 2026-08-17
confidence: medium
---

# MouHidInputHook (changeofpace)

Windows kernel driver that hooks the **CONNECT_DATA** object inside **MouHid** device objects to **filter, modify, and inject** mouse input packets without attaching filter devices or altering the USB HID mouse device stack. Emulates the **Moufiltr** strategy by intercepting the **ClassService** callback that transfers mouse data into class data queues; supports **safe unhooking** without unloading stacks and **PnP notification** for device changes. Described as **PatchGuard-safe** and relatively stealthy because it avoids filter-device attachment and resolves undocumented **CONNECT_DATA** field offsets via heuristics. Aimed at anti-cheat researchers and input-security analysts studying kernel-level mouse interception and input-simulation detection. (source: wiki/sources/descriptions/changeofpace__MouHidInputHook.md)

Complements MouClass **ServiceCallback** PoCs such as [[mouseclassservicecallbacktrick]] and [[mouseclassservicecallbackmeme]], MouClass filter-driver samples such as [[kernel-mouse]], and user-mode win32k reference [[ntuserinjectmouseinput-syscall]] when threat-modeling ring-0 mouse input paths.

## Links

- Repo: https://github.com/changeofpace/MouHidInputHook

## Related

[[mouseclassservicecallbacktrick]] · [[mouseclassservicecallbackmeme]] · [[kernel-mouse]] · [[ntuserinjectmouseinput-syscall]] · [[hardware-input-injection]] · [[self-remapping-code]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
