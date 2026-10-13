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

**mobile-harness** (oldboysonnt/mobile-harness) is an **AI-oriented** Python automation framework for **authorized** Android application security testing. It provisions rooted emulators or physical devices (Magisk, rootAVD), hides instrumentation, bypasses SSL pinning via [[frida]], routes HTTP(S) through Burp Suite, and decompiles targets with JADX with indexed code for analysis. Security researchers, bug-bounty testers, and lab or CTF workflows use it for repeatable mobile reverse engineering and assessment, including checks around Play Integrity and common client-side protections on hardened apps and games. (source: wiki/sources/descriptions/oldboysonnt__mobile-harness.md)

## Surfaces

| Component | Role |
|-----------|------|
| **One-click lab setup** | Rooted emulator/device bootstrap; root/SSL/Play Integrity bypass helpers |
| **Traffic** | Burp routing; SSL pinning bypass via Frida |
| **Static RE** | JADX decompilation and code indexing |
| **MCP server** | Device and audit capabilities exposed for agent-driven workflows |
| **Screen / dynamic** | Coordinate-based screen control |
| **Audit pipeline** | Static audit sweeps with verification and reporting |
| **Agent orchestration** | Multi-pass AI agents for surface mapping, static review, traffic analysis, and bounded dynamic probes |

Listed under README **Cheat → Frida** (offensive instrumentation lane).

## Links

- Repo: https://github.com/oldboysonnt/mobile-harness

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[rootraven]] · [[moabille]] · [[lamda]] · [[mobile-re-skill]] · [[android-proxy-mcp]]
