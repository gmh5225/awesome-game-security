---
title: LightHook
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/SamuelTulach__LightHook.md
updated: 2026-08-21
confidence: medium
---

# LightHook

**LightHook** (SamuelTulach) is a **single-header, minimalistic hook library** for **x86-64** targets on **Windows, Linux, and EFI**. Written in **pure C** with **no heavy disassembler dependency**, it ships examples for **user mode, kernel mode, and firmware** contexts. Portability comes from platform-specific memory **allocate / protect / free** shims, keeping integration overhead low for low-level instrumentation, reverse engineering, and game-security research where lightweight hooking is preferred. README category: cross-platform hook library. (source: wiki/sources/descriptions/SamuelTulach__LightHook.md)

Sits in the cheat / hook research lane beside [[subhook]], [[renhook]], [[polyhook]], and [[plthook]] as a disassembler-light cross-platform option that also covers **EFI/firmware** hooking beside SamuelTulach's [[efi-memory]] firmware work.

## Links

- Repo: https://github.com/SamuelTulach/LightHook

## Related

[[subhook]] · [[renhook]] · [[polyhook]] · [[polyhook-2-0]] · [[plthook]] · [[efi-memory]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
