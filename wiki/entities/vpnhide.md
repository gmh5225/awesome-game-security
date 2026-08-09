---
title: vpnhide
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/okhsunrog__vpnhide.md
updated: 2026-08-09
confidence: medium
---

# vpnhide

Android **VPN-hide** tool for rooted devices that conceals an active VPN connection from user-selected apps via a multi-layered filtering architecture—without injecting hooks into target processes. (source: wiki/sources/descriptions/okhsunrog__vpnhide.md)

**Java/Binder lane:** LSPosed module filters VPN-related data at the `system_server` Binder level.

**Native backends (pick one):** GKI kernel module using kretprobes, KernelPatch Module for non-GKI kernels, or Zygisk fallback—each intercepts ioctl, netlink, and `/proc/net` detection paths before results reach target processes.

**Optional ports module:** blocks localhost probing used to detect local VPN/proxy daemons (e.g. Clash, sing-box).

The companion app (Kotlin + Rust/C native) exposes per-app **Java**, **Native**, **Apps**, and **Ports** role configuration, built-in diagnostics, and statistics on how apps attempt VPN detection.

Research focus: bypass client-side VPN fingerprinting in banking, government, retail, and similarly hardened Android apps. Contrasts with multi-check collectors such as [[detection]] and RASP SDKs that flag VPN/proxy use (e.g. [[rs-native-kit-security]]).

## Links

- Repo: https://github.com/okhsunrog/vpnhide

## Related

[[magisk]] · [[kernelsu]] · [[apatch-kpm]] · [[zygisk]] · [[detection]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
