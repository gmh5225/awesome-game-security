---
title: Anti-Cheat-Amateur
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/not1cyyy__Anti-Cheat-Amateur.md
updated: 2026-08-03
confidence: medium
---

# Anti-Cheat-Amateur

Bundles **MemRE**, an injectable Windows memory editor, with **GothGirlFeet**, a kdmapper-compatible KMDF kernel driver that exposes cross-process memory read, write, region, and module enumeration through IOCTLs on a hooked NUL device. C++17 user-mode GUI plus C driver; adds **DBVM** hypervisor hypercall shims so scans can bypass user-mode anti-cheat protections that block standard `ReadProcessMemory`. MemRE provides Cheat Engine–style first/next scan workflows, pointer scanning, Unreal Engine GWorld and GNames signature resolution, and export to Cheat Engine tables. Aimed at game-security researchers studying anti-cheat bypass, kernel-assisted memory access, and Unreal Engine analysis — README tags Tencent ACE evasion research. (source: wiki/sources/descriptions/not1cyyy__Anti-Cheat-Amateur.md)

Research stack spanning usermode memory tooling, stealth kdmapper-style driver mapping, and hypervisor-assisted RPM — not a commercial anti-cheat product.

## Links

- Repo: https://github.com/not1cyyy/Anti-Cheat-Amateur

## Related

[[kiroshi]] · [[kdmapper-rs]] · [[saturn-mapper]] · [[known-driver-mappers]] · [[cheatengine-mcp-bridge]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
