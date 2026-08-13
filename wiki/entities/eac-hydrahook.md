---
title: EAC-HydraHook
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__EAC-HydraHook.md
updated: 2026-08-13
confidence: medium
---

# EAC-HydraHook

Hooking framework targeting [[easy-anti-cheat]]'s **Hydra** kernel-to-usermode communication channel (gmh5225; cheat / explore anticheat:eac **[Packet Fucker]**). Intercepts and suppresses EAC detection reports carried over the Hydra protocol so violation/ban telemetry never reaches the anti-cheat backend—complementary to allocator-path packet drops such as [[eac-kernel-packet-fucker]] but focused on the Hydra KM↔UM transport instead of pool allocation. (source: wiki/sources/descriptions/gmh5225__EAC-HydraHook.md)

## Links

- Repo: https://github.com/gmh5225/EAC-HydraHook

## Related

[[easy-anti-cheat]] · [[eac-kernel-packet-fucker]] · [[eac-injector-driver]] · [[eac-bypass]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
