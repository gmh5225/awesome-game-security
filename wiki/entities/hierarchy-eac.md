---
title: hierarchy-eac
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Sinclairq__hierarchy-eac.md
updated: 2026-08-21
confidence: medium
---

# hierarchy-eac

Proof-of-concept **Windows kernel driver** that demonstrates bypassing **EasyAntiCheat.sys self-integrity checks** by abusing **call-hierarchy behavior**. Mostly **C++** with supporting **x64 assembly**; includes **PE parsing**, **section-bound checks**, and custom **VM-style control logic**. Ships Visual Studio project files and references a companion technical write-up explaining the approach. Primary use case is anti-cheat reverse engineering and research into kernel-level integrity mechanisms. Listed under cheat / explore anticheat:eac `[Bypassing self-integrity]`. (source: wiki/sources/descriptions/Sinclairq__hierarchy-eac.md)

Complements callback-driven section-compare analysis such as [[bypassing-easyanticheat-integrity-check]] and historical integrity PoCs such as [[cveac-2020]] by focusing on how EAC's integrity validation depends on call-stack / hierarchy semantics rather than only static image comparison.

## Links

- Repo: https://github.com/Sinclairq/hierarchy-eac

## Related

[[easy-anti-cheat]] · [[bypassing-easyanticheat-integrity-check]] · [[cveac-2020]] · [[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
