---
title: SmmInfect
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Oliver-1-1__SmmInfect.md
updated: 2026-08-22
confidence: medium
---

# SmmInfect

**SmmInfect** (Oliver-1-1) is an **SMM backdoor research framework** that pairs a firmware-level **SMI handler** with **user-mode clients**. It ships **UEFI** and **EDK2** components plus **Windows** and **Linux** code to trigger SMIs and exchange data with privileged **System Management Mode** logic. The repository documents build workflows, **BIOS patching** steps, hardware requirements, and **Secure Boot** / firmware constraints. It targets advanced platform security research on **firmware trust boundaries** and **high-privilege persistence** below the OS. (source: wiki/sources/descriptions/Oliver-1-1__SmmInfect.md)

Complements other Ring -2 SMM research such as [[smm]], Cr4sh UEFI backdoor work such as [[smm-backdoor-ng]], and Oliver-1-1 UEFI tooling such as [[uefi-graphic]] when studying below-OS offensive lanes beside EFI bootkits.

## Links

- Repo: https://github.com/Oliver-1-1/SmmInfect

## Related

[[smm]] · [[smm-backdoor-ng]] · [[uefi-graphic]] · [[simpleuefi]] · [[visualuefi-2-0]] · [[uefi-bootkit]] · [[rainbow]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
