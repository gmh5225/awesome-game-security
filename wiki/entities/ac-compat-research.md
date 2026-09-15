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

**ac-compat-research** (IZxMD) is an independent systems-security research project documenting a vendor-agnostic feasibility study for a **Linux compatibility layer** capable of hosting **kernel anti-cheat components** with security equivalence to Windows—**without virtualization as the primary approach**. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

Complements runtime compatibility tracking such as [[are-we-anti-cheat-yet]] and native Linux AC implementation research such as [[linux-anticheat]] in the platform-architecture lane.

## Scope

The study analyzes what kernel anti-cheats require from a Windows kernel using **public sources**, evaluates Linux capabilities and limitations (**LSM**, kernel modules, signing, isolation, ABI constraints), and explores **non-virtualized** design options subject to rigorous falsification. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

## Deliverables

Produces a **dossier** and **knowledge graph** intended as an engineering specification rather than shipping code. Targets researchers and engineers working on anti-cheat architecture and Linux game security. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

## Exclusions

Explicitly excludes reverse-engineering closed binaries, bypass techniques, and game-specific exploits. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

## Status

Early setup phase — no implementation yet. (source: wiki/sources/descriptions/IZxMD__ac-compat-research.md)

## Links

- Repo: https://github.com/IZxMD/ac-compat-research

## Related

[[are-we-anti-cheat-yet]] · [[linux-anticheat]] · [[aclist-github-io]] · [[concepts/easy-anti-cheat]] · [[concepts/research-rigor]] · [[overviews/anti-cheat]]
