---
title: Xiaomi USB Security Bypass
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/CHERWING__xiaomi_usb_security_bypass.md
  - wiki/sources/README-categories.md
updated: 2026-09-08
confidence: medium
---

# Xiaomi USB Security Bypass

**Magisk module** for rooted **Xiaomi/Redmi** phones on **MIUI/HyperOS** that bypasses vendor USB-debugging security gates and fastboot account/SIM requirements. (source: wiki/sources/descriptions/CHERWING__xiaomi_usb_security_bypass.md)

**Mechanism:** At boot, forces `persist.security.adbinput`, `persist.security.adbinstall`, and `persist.fastboot.enable` to `1` via Magisk `resetprop` through `system.prop`, with a `service.sh` fallback that degrades from `setprop` to `resetprop` when SELinux blocks writes.

**Use case:** Enables full USB debugging, USB install, and fastboot flashing without Mi account or SIM verification; unlocks ADB input injection for **scrcpy**, Total Control, `monkey`, and `uiautomator` (fixes `INJECT_EVENTS` permission errors blocking remote mouse/keyboard over USB).

**Implementation:** Shell scripts plus a small Python `build_zip.py` packager for the flashable module zip.

README category: Cheat / Magisk. Intended for mobile developers, reverse engineers, and security researchers who need MIUI USB debugging and input injection on rooted Xiaomi hardware.

## Links

- Repo: https://github.com/CHERWING/xiaomi_usb_security_bypass

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[usb-detection-bypass]] · [[rootavd]] · [[moabille]] · [[xiaomi-hyperos-bootloader-bypass]]
