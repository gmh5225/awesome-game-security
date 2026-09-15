---
title: ac-compat-research
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/IZxMD__ac-compat-research.md
  - wiki/sources/README-categories.md
updated: 2026-09-15
confidence: medium
---

# ac-compat-research

**ac-compat-research** (IZxMD) is an independent systems-security research project documenting a vendor-agnostic feasibility study for a **Linux compatibility layer** capable of hosting **kernel anti-cheat components** with security equivalence to Windows—**without virtualization as the primary approach**. The study analyzes what kernel anti-cheats require from a Windows kernel using public sources, evaluates Linux capabilities and limitations (LSM, kernel modules, signing, isolation, ABI constraints), and explores non-virtualized design options subject to rigorous falsification. It produces a dossier and knowledge graph as an engineering specification rather than shipping code, and explicitly excludes reverse-engineering closed binaries, bypass techniques, or game-specific exploits. The repository is in early setup with no implementation yet. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

Complements runtime compatibility tracking such as [[are-we-anti-cheat-yet]] and native Linux AC research such as [[linux-anticheat]] in the platform-architecture lane.

## Links

- Repo: https://github.com/IZxMD/ac-compat-research

## Related

[[are-we-anti-cheat-yet]] · [[linux-anticheat]] · [[concepts/easy-anti-cheat]] · [[overviews/anti-cheat]]
