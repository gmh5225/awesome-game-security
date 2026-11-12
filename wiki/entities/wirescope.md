---
title: WireScope
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel, anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/wesmar__WireScope.md
updated: 2026-11-12
confidence: medium
---

# WireScope

Native Windows application (modern **C++23**, single self-contained executable) that unifies Layer 2 packet capture, per-process traffic accounting, kernel-level firewall enforcement, and network impairment simulation on one **NDIS** data plane. It talks to a lightweight **NDIS 6.x** filter driver (`wsddntf.sys`) over a custom IOCTL protocol—without **Npcap** or other third-party capture libraries. A signed driver package is embedded in the binary as a compressed resource and installed on demand via SetupAPI and INetCfg. Listed under Cheat → **Packet Sniffer&Filter** for security research, anti-cheat and game-traffic analysis, and hands-on RE of how applications use the network. (source: wiki/sources/descriptions/wesmar__WireScope.md) (source: wiki/sources/README-categories.md)

## Capabilities

- **Capture:** Layer 2 sniffing; Wireshark-compatible **PCAP** export.
- **Accounting:** Per-process traffic metering on the shared NDIS path.
- **Enforcement:** Kernel-level firewall with a directional **rule language** (addresses, ports, protocols, per-application matching).
- **Impairment:** Optional bandwidth shaping, delay, and loss simulation for protocol or AC-behavior testing.
- **Interfaces:** **Direct2D** GUI or scriptable **CLI**.

## Platform

Targets **Windows 11 x64**. Contrasts with library-first stacks such as [[ndisapi]] (user-mode API over Windows Packet Filter) or [[npcap]]-dependent sniffers—WireScope ships its own filter driver and avoids external capture runtimes.

## Links

- Repo: https://github.com/wesmar/WireScope

## Related

[[ndisapi]] · [[npcap]] · [[divert]] · [[packet-sniffer]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
