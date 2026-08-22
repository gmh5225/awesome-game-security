---
title: ATDCM64a-LPE
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/MrAle98__ATDCM64a-LPE.md
updated: 2026-08-22
confidence: medium
---

# ATDCM64a-LPE

Local privilege escalation proof of concept targeting a vulnerable AMD Windows driver **`atdcm64a.sys`**. C++ implementation with Visual Studio project files plus PowerShell and batch scripts for deployment and execution; the exploit template demonstrates driver interaction and lab-oriented workflow preparation for Windows kernel exploitation research, including studies relevant to anti-cheat and driver security hardening. (source: wiki/sources/descriptions/MrAle98__ATDCM64a-LPE.md)

Sits in the AMD signed-driver [[byovd]] lane beside [[hitcon-2023-demo-cve-2023-20562]] and [[amd-ryzen-master-driver-v17-exploit]]; complements other MrAle98 kernel LPE PoCs such as [[cve-2024-49138-poc]].

## Links

- Repo: https://github.com/MrAle98/ATDCM64a-LPE
- Driver: `atdcm64a.sys`
- Research: [Exploiting AMD atdcm64a.sys arbitrary pointer dereference (part 1)](https://security.humanativaspa.it/exploiting-amd-atdcm64a.sys-arbitrary-pointer-dereference-part-1/)

## Related

[[byovd]] · [[hitcon-2023-demo-cve-2023-20562]] · [[amd-ryzen-master-driver-v17-exploit]] · [[windows-kernel-exploits]] · [[cve-2024-49138-poc]] · [[eneio64-driver-exploit]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
