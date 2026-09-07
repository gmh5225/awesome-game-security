---
title: DLSS Unlocked
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/ShyVortex__dlss-unlocked.md
updated: 2026-09-07
confidence: medium
---

# DLSS Unlocked

**DirectX 12 game mod and installer** (ShyVortex) that enables NVIDIA **DLSS 3** frame generation, multi-frame generation, and neural rendering in supported DX12 titles on GeForce RTX **20xx–40xx** GPUs on Windows and Linux via Proton. Injects proxy DLLs and intercepts NVIDIA NGX and Streamline calls, optionally bridging frame generation to OptiScaler and FSR 3.1 backends. (source: wiki/sources/descriptions/ShyVortex__dlss-unlocked.md)

## Mechanism

Registry patches or bundled library replacements bypass NVIDIA driver signature checks. Ships Inno Setup installer, standalone packages, ASI and DXGI loader variants, and PowerShell build scripts packaging upstream OptiScaler and DLSS-NR components.

## Research relevance

Illustrates **DLL injection**, Detours-style API hooking, and vendor graphics-library interception — relevant to graphics-integrity analysis and mod security study.

## Links

- Repo: https://github.com/ShyVortex/dlss-unlocked

## Related

[[dxwrapper]] · [[shader-injector]] · [[present-hook]] · [[overviews/graphics-api]]
