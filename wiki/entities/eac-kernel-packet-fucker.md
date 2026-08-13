---
title: EAC-Kernel-Packet-Fucker
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__EAC-Kernel-Packet-Fucker.md
updated: 2026-08-13
confidence: medium
---

# EAC-Kernel-Packet-Fucker

Kernel-mode [[easy-anti-cheat]] bypass research sample (gmh5225; cheat / explore anticheat:eac **[Packet Fucker]**) that **blocks outbound EAC detection telemetry** by sabotaging the driver's pool allocation path for violation reports. The technique hijacks EAC's dynamically imported **`ExAllocatePoolWithTag`** by patching a writable section pointer, causing kernel-mode violation reports (~33 KB) to fail allocation and be discarded before they can be sent to EAC backend servers. Useful for studying how EAC packages and uploads kernel violation telemetry and which allocator hooks can silently drop those packets. (source: wiki/sources/descriptions/gmh5225__EAC-Kernel-Packet-Fucker.md)

## Links

- Repo: https://github.com/gmh5225/EAC-Kernel-Packet-Fucker

## Related

[[easy-anti-cheat]] · [[eac-injector-driver]] · [[eac-bypass]] · [[kernel-pool-scanning]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
