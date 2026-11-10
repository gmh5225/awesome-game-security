---
title: smo-harmony
kind: entity
topics: [reverse-engineering, mobile-security, graphics-api]
sources:
  - wiki/sources/descriptions/zpp1103__smo-harmony.md
  - wiki/sources/README-categories.md
updated: 2026-11-10
confidence: medium
---

# smo-harmony

HarmonyOS NEXT research workspace for rehosting *Super Mario Odyssey* (Switch firmware **1.4.1**) via a **high-level emulation (HLE)** host: translated ARM64 game modules run inside a DevEco **HAP** while Horizon `nn::*` system services are implemented in native C/C++—not a retail-ready port. (source: wiki/sources/descriptions/zpp1103__smo-harmony.md)

## Stack

- **Host:** C/C++ runtime layers, ArkTS shell, NAPI bridge; OpenHarmony/HarmonyOS NEXT packaging.
- **Guest:** NSO extraction, patching, and assembly embed workflows for bring-up and forensics.
- **Graphics:** NVN API replay translated to **Vulkan** on OpenHarmony.
- **Automation:** Python and shell boot, analysis, and build pipelines for iterative research.

## Research notes

The tree documents a parallel *Tears of the Kingdom* effort and derived metadata conventions—useful for comparing Switch binary translation and console GPU shim layers across titles on a non-Windows ARM64 host. Contrast Windows static-recomp ports such as [[smo-recomp]] (AOT lift→native x64) where the split is lifted guest code vs reimplemented services on a different host ABI. (source: wiki/sources/descriptions/zpp1103__smo-harmony.md)

## Audience

Reverse engineers and platform porters studying Switch runtime rehosting, NVN→Vulkan shims, and cross-platform game bring-up—not players seeking a shipped build. Users must supply their own **dump**; the repository is a source-only snapshot.

## Links

- Repo: https://github.com/zpp1103/smo-harmony

## Related

[[smo-recomp]] · [[totk-pc-recomp]] · [[letsgo-recomp]] · [[static-runtime-evidence]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
