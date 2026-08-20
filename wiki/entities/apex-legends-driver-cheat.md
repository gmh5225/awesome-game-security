---
title: Apex Legends Driver Cheat
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/TheCruZ__Apex_Legends_Driver_Cheat.md
updated: 2026-08-20
confidence: medium
---

# Apex Legends Driver Cheat

**Apex_Legends_Driver_Cheat** (TheCruZ) is a **kernel-assisted external cheat framework** for **Apex Legends**. It combines a **Windows kernel driver** for cross-process memory read and write, a **C++ user-mode controller**, and a **transparent overlay** for ESP-style visuals and aiming logic. The kernel component is loaded via **vulnerable-driver mapping** techniques rather than conventional signed-driver installation. Primary intent is **cheat development and anti-cheat bypass research** on [[easy-anti-cheat]]-protected Apex clients. (source: wiki/sources/descriptions/TheCruZ__Apex_Legends_Driver_Cheat.md)

Same author as BYOVD mapper [[kdmapper]] and firmware-assisted Apex samples [[direct-efi-apex-cheat]] and [[efi-driver-access]]. Sits in the kernel-assisted external lane beside [[apex-external-cheat]] and [[apex-dma-cheat-updated]] rather than below-OS DMA or EFI paths.

## Links

- Repo: https://github.com/TheCruZ/Apex_Legends_Driver_Cheat

## Related

[[kdmapper]] · [[byovd]] · [[direct-efi-apex-cheat]] · [[efi-driver-access]] · [[apex-external-cheat]] · [[apex-dma-cheat-updated]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
