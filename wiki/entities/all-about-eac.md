---
title: all-about-eac
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/BishopTopG__all-about-eac.md
  - wiki/sources/README-categories.md
updated: 2026-09-14
confidence: medium
---

# all-about-eac

Memflow-only reverse-engineering **dossier** documenting one captured **EasyAntiCheat_EOS.sys** build (Fortnite) from **outside a Windows VM** via passive physical-memory acquisitions matched to Windows kernel PDB layouts. Maps EAC's registered kernel surfaces: process/thread/image callbacks, Object Manager handle policy, registry callbacks, Filter Manager minifilter, device IPC, and private per-thread callback contexts. Packages narrative deep dives, technical appendices, evidence-labeled claims, Python validation tooling, and reproducible derivation rules—explicitly excluding bypass or exploit material. (source: wiki/sources/descriptions/BishopTopG__all-about-eac.md)

Complements disk-based driver dumps ([[easyanticheat-reversing]], [[eac-extractor-utility]]) and Linux userland VM reconstruction ([[eac-analysis]]) with an **external VM memory-forensics** lane for studying live EAC kernel registration and minifilter policy.

## Links

- Repo: https://github.com/BishopTopG/all-about-eac

## Related

[[easy-anti-cheat]] · [[eac-reversal]] · [[eac-analysis]] · [[easyanticheat-reversing]] · [[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
