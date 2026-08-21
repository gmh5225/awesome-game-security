---
title: EAC_Emu
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Rat431__EAC_Emu.md
updated: 2026-08-21
confidence: medium
---

# EAC_Emu

Simple **x64 EasyAntiCheat emulator stub** (Rat431) implemented as a Windows DLL. Exports a large set of expected anti-cheat API functions and provides placeholder interface implementations so client code that links against EAC components can load and call through without the real module. Primarily C++ with a small assembly helper for low-level patch routines. Intended as a proof of concept for reverse engineering and compatibility testing of software that depends on EAC user-mode interfaces—not a full anti-cheat replacement. (source: wiki/sources/descriptions/Rat431__EAC_Emu.md)

Complements static RE artifacts such as [[eac-reversal]] and [[eac-easyanticheat-src-1]] by offering a runnable stub surface for studying expected export tables and client integration contracts. Analogous in role to VAC-side module emulators such as [[vac-emulator]] and [[vacation3-emu]], but scoped to EAC's x64 DLL API boundary.

## Links

- Repo: https://github.com/Rat431/EAC_Emu

## Related

[[easy-anti-cheat]] · [[eac-reversal]] · [[eac-easyanticheat-src-1]] · [[vac-emulator]] · [[vacation3-emu]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
