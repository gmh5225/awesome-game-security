---
title: rtl8852au-userspace
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/damanoreshkan-beep__rtl8852au-userspace.md
  - wiki/sources/README-categories.md
updated: 2026-08-25
confidence: medium
---

# rtl8852au-userspace

**rtl8852au-userspace** (damanoreshkan-beep) is a userspace, no-root driver for the Realtek RTL8852AU Wi-Fi 6 USB adapter (ASUS USB-AX56) that controls the radio entirely over libusb and usbfs without a kernel module. Written primarily in C with Kotlin and TypeScript tooling, it performs cold power-on, firmware download, and monitor-mode reception into radiotap pcap files with channel hopping across 2.4 and 5 GHz, plus live RF calibration and raw 802.11 frame injection by porting register sequences from the Linux rtw89 kernel driver. (source: wiki/sources/descriptions/damanoreshkan-beep__rtl8852au-userspace.md)

Targets wireless security researchers who need packet capture, RF analysis, and interoperability testing on owned hardware without root privileges. Listed under Cheat → Android Network Explorer beside [[pcapdroid]] VPN capture stacks.

## Capabilities

| Feature | Role |
|---------|------|
| libusb/usbfs control | No kernel module; no root on Android |
| Monitor mode + radiotap pcap | Raw 802.11 capture with channel hopping |
| Frame injection | Over-the-air 802.11 transmit for RF testing |
| rtw89 port | Register/calibration logic from Linux kernel driver |

## Links

- Repo: https://github.com/damanoreshkan-beep/rtl8852au-userspace

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[pcapdroid]] · [[android-proxy-mcp]] · [[lamda]] · [[peetch]]
