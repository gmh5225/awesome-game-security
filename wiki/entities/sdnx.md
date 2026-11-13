---
title: SDNX
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/exp0t__SDNX.md
updated: 2026-11-13
confidence: medium
---

# SDNX

**SDNX** ([exp0t/SDNX](https://github.com/exp0t/SDNX)) is an **early work-in-progress research port** that statically recompiles the **Xbox 360 retail build** of *Sleeping Dogs* into **native C++** and runs it on **Nintendo Switch homebrew** with a **custom Vulkan** graphics stack—not a full Xbox 360 emulator wrapper. (source: wiki/sources/descriptions/exp0t__SDNX.md)

## Lift pipeline

The retail **`default.xex`** is lifted to **AArch64** with **ReXGlue**-based binary translation. **CMake** drives **Switch** and **desktop bench** targets using **devkitA64**, **libnx**, and **Mesa NVK**. (source: wiki/sources/descriptions/exp0t__SDNX.md)

## Graphics

A **native renderer** interprets **Xenos GPU command streams** directly instead of emulating the original GPU. **Shader microcode** is translated ahead of time with **XenosRecomp** and **DXC** into **HLSL** and **SPIR-V**. (source: wiki/sources/descriptions/exp0t__SDNX.md)

## Tooling

**Python** and **C++** utilities parse **archives**, **textures**, and **shader containers**, and automate bench and Switch builds—supporting study of **UE3-era proprietary assets** and low-level graphics replacement on constrained hardware. (source: wiki/sources/descriptions/exp0t__SDNX.md)

## Audience and scope

Aimed at **reverse engineers** and **advanced porting researchers** studying Xbox 360 executables and console static recompilation. **No copyrighted game data** in-repo; users bring their own retail assets. Not an anti-cheat or live-service analysis surface. (source: wiki/sources/descriptions/exp0t__SDNX.md)

## Links

- Repo: https://github.com/exp0t/SDNX

## Related

[[cod6-nx]] · [[nhl-legacy-remaster]] · [[ng2recomp]] · [[mcla-pc]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
