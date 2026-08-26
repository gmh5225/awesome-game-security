---
title: CleanCheat
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/CorrM__CleanCheat.md
updated: 2026-08-26
confidence: medium
---

# CleanCheat

**C++ game cheat foundation** (CorrM) that favors a **clean, modular architecture** over monolithic feature code. Structured examples separate **data providers**, **feature modules**, **runners**, and **shared state** so large object-processing logic stays maintainable as prototypes grow. Sample projects—including an **Unreal-focused internal example**—demonstrate extension patterns in practice. Primary audience: developers and researchers building maintainable cheat prototypes for experimentation. Listed under cheat / Game cheat base. (source: wiki/sources/descriptions/CorrM__CleanCheat.md)

Sits in the general-purpose cheat-foundation lane beside modular frameworks such as [[blacksun-framework]] and [[omegaware-framework]], and educational internal scaffolds such as [[nullhooks]]—with an emphasis on layered data/feature/runner separation rather than title-specific gameplay modules.

## Architecture highlights

| Component | Role |
|-----------|------|
| Data providers | Isolate game-state reads and object enumeration from feature logic |
| Feature modules | Encapsulate individual cheat capabilities behind clear interfaces |
| Runners | Orchestrate tick/update loops and module lifecycle |
| Shared state | Central coordination for cross-module object-processing data |

The bundled Unreal internal sample pairs naturally with CorrM's SDK tooling such as [[unreal-finder-tool]] when prototyping UE internals workflows.

## Links

- Repo: https://github.com/CorrM/CleanCheat

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[unreal-finder-tool]] · [[blacksun-framework]] · [[omegaware-framework]] · [[ue4-base]] · [[nullhooks]] · [[intro-to-gamehacking]]
