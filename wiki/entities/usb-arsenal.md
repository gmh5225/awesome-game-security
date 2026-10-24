---
title: USB Arsenal
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ravindu644__USB-Arsenal.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: medium
---

# USB Arsenal

**Root-required** Android (and Linux) tooling that builds **composite USB gadgets** through kernel **configfs**, so a phone can expose multiple device classes to a host PC at once. (source: wiki/sources/descriptions/ravindu644__USB-Arsenal.md)

**Capabilities:** Writable **mass storage** and ISO/CD-ROM emulation; **RNDIS/NCM tethering** with DHCP/NAT; configurable **HID keyboard and mouse** endpoints. The C core configures gadgets and releases the controller so normal **ADB/MTP** can resume.

**Distribution:** Magisk or **KernelSU** module with kernel patches for common Android gadget bugs, plus a **Jetpack Compose** app for capability probing, identity profiles, and live gadget control.

README category: Cheat / Android Root (adjacent Magisk lane). Useful for security research, reverse engineering, and hardware-adjacent host testing without dedicated BadUSB hardware—pairs with [[hardware-input-injection]] and [[xiaomi-usb-security-bypass]] when USB debugging or host-side input paths matter.

## Links

- Repo: https://github.com/ravindu644/USB-Arsenal

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[usb-detection-bypass]] · [[titanium-macro]] · [[moabille]]
