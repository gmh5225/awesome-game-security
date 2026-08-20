---
title: EFI Driver Access
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/TheCruZ__EFI_Driver_Access.md
updated: 2026-08-20
confidence: medium
---

# EFI Driver Access

**EFI_Driver_Access** (TheCruZ) demonstrates loading an **EFI runtime driver during boot** to obtain **privileged memory access** from Windows user mode after the OS starts. The project pairs an **EFI-side runtime module** with a **Visual Studio usermode client** that issues **read**, **write**, and **process-base** requests. Implementation mixes **C/C++**, **GNU-EFI**, and Visual Studio components, with documented **build and boot workflow** steps. It is primarily intended for **kernel and anti-cheat bypass research** that relies on **pre-OS execution paths** rather than conventional signed-driver load telemetry. (source: wiki/sources/descriptions/TheCruZ__EFI_Driver_Access.md)

Sits in the **EFI RPM** lane beside runtime process-memory PoCs such as [[efidump]], GetVariable-backed samples such as [[sub-get-variable]], and integrated below-OS stacks such as [[efi-monitor]] and [[sumap]]. Same author as canonical BYOVD mapper [[kdmapper]].

## Links

- Repo: https://github.com/TheCruZ/EFI_Driver_Access

## Related

[[kdmapper]] · [[direct-efi-apex-cheat]] · [[efidump]] · [[sub-get-variable]] · [[efi-monitor]] · [[sumap]] · [[uefi-bootloader]] · [[fortnite-efi-external]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
