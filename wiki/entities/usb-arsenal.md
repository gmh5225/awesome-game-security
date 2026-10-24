---
title: USB Arsenal
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ravindu644__USB-Arsenal.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: high
---

# USB Arsenal

**USB Arsenal** (ravindu644/USB-Arsenal) is **root-required** tooling for **Android and Linux** that assembles **composite USB gadgets** through kernel **configfs**, so a phone or container can present several device classes to a host PC at once. (source: wiki/sources/descriptions/ravindu644__USB-Arsenal.md)

README category: Cheat / Android Root.

## Capabilities

- **Mass storage:** writable volumes plus **ISO or CD-ROM** emulation.
- **USB tethering:** **NCM or RNDIS** with **DHCP and NAT**.
- **HID:** configurable **keyboard and mouse** endpoints for host boot and input tooling.
- **Handoff:** the **C core** configures gadgets, then releases the controller so normal **ADB/MTP** can resume. (source: wiki/sources/descriptions/ravindu644__USB-Arsenal.md)

## Architecture

- **Magisk or KernelSU module** with kernel patches for common Android USB gadget bugs.
- **Kotlin Jetpack Compose app** for setup, capability probing, USB **identity profiles**, and live gadget control. (source: wiki/sources/descriptions/ravindu644__USB-Arsenal.md)

## Positioning

Suited to security research, reverse engineering, and hardware-adjacent host testing where you emulate custom or multi-function USB peripherals and observe host behavior **without dedicated BadUSB hardware**—adjacent to [[hardware-input-injection]] and [[xiaomi-usb-security-bypass]] when USB debugging or host-side input paths matter. (source: wiki/sources/descriptions/ravindu644__USB-Arsenal.md)

## Links

- Repo: https://github.com/ravindu644/USB-Arsenal

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[usb-detection-bypass]] · [[titanium-macro]] · [[moabille]] · [[magisk]]
