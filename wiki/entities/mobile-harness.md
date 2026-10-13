---
title: Mobile Pentest Harness (mph)
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/oldboysonnt__mobile-harness.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: high
---

# Mobile Pentest Harness (mph)

**mobile-harness** (oldboysonnt/mobile-harness) is a Python-oriented automation framework for **authorized** Android application security testing. It provisions rooted emulators or devices (Magisk, rootAVD), hides instrumentation, bypasses SSL pinning via Frida, routes HTTP(S) through Burp Suite, and decompiles targets with JADX with indexed code for analysis. (source: wiki/sources/descriptions/oldboysonnt__mobile-harness.md)

## Surfaces

| Component | Role |
|-----------|------|
| **One-click lab setup** | Rooted emulator/device bootstrap with common bypass helpers |
| **Traffic** | Burp routing; SSL pinning bypass via Frida |
| **Static RE** | JADX decompilation and code indexing |
| **MCP server** | Device and audit capabilities for agent-driven workflows |
| **Dynamic probes** | Coordinate-based screen control; static audit sweeps; multi-pass agent orchestration |

Play Integrity and typical client-side hardening checks appear in lab workflows for hardened apps and games. Listed under README **Cheat → Frida** (offensive instrumentation lane).

## Links

- Repo: https://github.com/oldboysonnt/mobile-harness

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[rootraven]] · [[moabille]] · [[lamda]] · [[mobile-re-skill]]
