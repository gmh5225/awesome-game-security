---
title: Direct EFI Apex Cheat
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/TheCruZ__Direct-EFI-Apex-Cheat.md
updated: 2026-08-20
confidence: medium
---

# Direct EFI Apex Cheat

**Direct-EFI-Apex-Cheat** (TheCruZ) combines a **user-mode Apex Legends cheat client** with a **UEFI runtime component** that reaches kernel memory paths from an EFI context. The **C/C++** stack implements **command-based memory operations**, **process-base resolution**, and gameplay features such as **glow** and **aim assistance**. Communication uses **runtime variable hooks** and **low-level Windows kernel function pointers** bridged from the EFI side. Primary intent is **firmware-assisted cheat and anti-cheat bypass experimentation** on [[easy-anti-cheat]]-protected Apex clients without conventional Windows kernel-driver load telemetry. (source: wiki/sources/descriptions/TheCruZ__Direct-EFI-Apex-Cheat.md)

Same author as generic EFI RPM sample [[efi-driver-access]] and BYOVD mapper [[kdmapper]]. Sits in the title-integrated below-OS external lane beside [[fortnite-efi-external]], GetVariable-backed RPM such as [[sub-get-variable]], and integrated EFI stacks such as [[efi-monitor]] and [[sumap]].

## Links

- Repo: https://github.com/TheCruZ/Direct-EFI-Apex-Cheat

## Related

[[efi-driver-access]] · [[kdmapper]] · [[apex-legends-driver-cheat]] · [[fortnite-efi-external]] · [[sub-get-variable]] · [[efi-monitor]] · [[sumap]] · [[easy-anti-cheat]] · [[apex-external-cheat]] · [[apex-dma-cheat-updated]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
