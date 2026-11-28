---
title: apple-silicon-port-factory
kind: entity
topics: [mobile-security, graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mweinbach__apple-silicon-port-factory.md
updated: 2026-11-28
confidence: medium
---

# apple-silicon-port-factory

Experimental research framework (Rust) that loads user-supplied Windows x86-64 PE executables and DLLs and runs them natively on Apple Silicon macOS and iOS without Wine, CrossOver, or D3DMetal at runtime. Combines an iced-x86 x86-64 interpreter, block JIT, and disk-backed AOT cache with a clean-room Win32 layer; routes Direct3D 11/12 and Vulkan through Metal 4 and MetalFX with DXIL-to-Metal shader tooling. A factory CLI and ops database support PE scanning, Win32 import and instruction coverage audits, runtime hazard checks, anti-cheat compatibility reporting, offline AOT prewarming, and differential x86 verification for porting workflows—aimed at developers and researchers bringing legitimately owned Windows games to Apple Silicon (optional per-game manifests; deep targets such as Overwatch and Alan Wake 2). (source: wiki/sources/descriptions/mweinbach__apple-silicon-port-factory.md)

Sits in the README **Windows Emulator** lane as a cross-API Metal translation + x86 hosting stack beside [[qemu-apple-silicon]] virtualization labs and [[nfsu2recomp]]-style Win32 lifts—not a shipping game port or anti-cheat bypass product.

## Links

- Repo: https://github.com/mweinbach/apple-silicon-port-factory

## Related

[[qemu-apple-silicon]] · [[darwin-vm]] · [[nfsu2recomp]] · [[winvisor]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]