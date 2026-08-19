---
title: lpmapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/VollRagm__lpmapper.md
updated: 2026-08-19
confidence: medium
---

# lpmapper

**lpmapper** (VollRagm/lpmapper) is a Windows **kernel mapper** in C++ that places shellcode into **already loaded large-page drivers** without allocating fresh kernel memory. It follows a workflow inspired by known manual mappers but requires specific **registry configuration** for large-page drivers. The technique is framed as a way to reduce visibility to common kernel anti-cheat detection paths — especially pool-allocation and Big Pool telemetry that pool-alloc mappers such as [[kdmapper]] trigger. Primary use case is advanced kernel security research and anti-cheat bypass experimentation. (source: wiki/sources/descriptions/VollRagm__lpmapper.md)

README tags the project under **Manual Map To Large Page Driver**. Complements section-overlay mappers such as [[sinmapper]] and pool-alloc BYOVD mappers such as [[umap]] and [[kdmapper]].

## Links

- Repo: https://github.com/VollRagm/lpmapper

## Related

[[sinmapper]] · [[kdmapper]] · [[umap]] · [[known-driver-mappers]] · [[kernel-pool-scanning]] · [[nullmap]] · [[revert-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
