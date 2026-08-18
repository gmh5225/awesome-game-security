---
title: Voyager
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/backengineering__Voyager.md
  - wiki/sources/descriptions/gmh5225__Voyager.md
updated: 2026-08-18
confidence: medium
---

# Voyager

**Hyper-V hacking framework** for Windows 10 x64 on **AMD and Intel** hosts, supporting builds from **1507 through 2004**. Aimed at game-security researchers and reverse engineers studying offensive Hyper-V techniques in the cheat / Windows kernel explorer lane—not a production anti-cheat component. (source: wiki/sources/descriptions/backengineering__Voyager.md)

Upstream maintained by **backengineering**; the same framework appears in the list under gmh5225 as a mirror/fork entry. Ecosystem siblings include **VDM (Voyager Driver Manager)** and [[msrexec]] (MSR write→kernel-exec via `IA32_LSTAR` redirect; VDM backend). Distinct from unrelated cheat samples such as [[fortnite-voyagertf]] (VoyagerTF name only).

Complements Microsoft Hyper-V introspection such as [[hyper-rev]], Type-2 VT-x learning stacks such as [[hv]], hacked-hypervisor detection such as [[hypervisor-detection]] and [[hv-detect]], and Hyper-V stack LPE research such as [[cve-2025-21333]].

## Links

- Repo (upstream): https://github.com/backengineering/Voyager
- Mirror: https://github.com/gmh5225/Voyager

## Related

[[msrexec]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hyper-rev]] · [[hv]] · [[hypervisor-detection]] · [[hv-detect]] · [[hvci]] · [[cve-2025-21333]] · [[fortnite-voyagertf]]
