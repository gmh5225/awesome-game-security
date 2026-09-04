---
title: dse_pg_bypass
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/4l3x777__dse_pg_bypass.md
updated: 2026-09-04
confidence: medium
---

# dse_pg_bypass

Windows kernel research **proof of concept** (4l3x777) for bypassing **Driver Signature Enforcement (DSE)** and **[[patchguard|PatchGuard]]** through a [[concepts/byovd|BYOVD]] attack model. Combines C++ implementation with detailed reversing notes that trace signature validation callbacks and integrity-check execution paths in modern Windows kernels. Highlights how vulnerable signed drivers can be leveraged to interfere with code integrity decisions and patch-protection behavior. Intended for educational kernel security analysis and for defenders studying realistic BYOVD attack surfaces and mitigations. (source: wiki/sources/descriptions/4l3x777__dse_pg_bypass.md)

Sits in the cheat / DSE + PatchGuard research lane beside multi-technique runtime disable tooling such as [[upgdsed]], RTCore64 DSE-nullify demos such as [[cybersec2023-byovd-demo]], CI/`g_CiOptions` controllers such as [[kvc]], and PG-focused toolkits such as [[shark]].

## Links

- Repo: https://github.com/4l3x777/dse_pg_bypass

## Related

[[byovd]] · [[patchguard]] · [[upgdsed]] · [[cybersec2023-byovd-demo]] · [[kvc]] · [[dse-hook]] · [[dse-patcher-2]] · [[shark]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
