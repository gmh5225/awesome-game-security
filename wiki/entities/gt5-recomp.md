---
title: GT5 Recomp
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/MormonFTP-hub__gt5-recomp.md
updated: 2026-11-24
confidence: medium
---

# GT5 Recomp

**gt5-recomp** (MormonFTP-hub/gt5-recomp) is a native **Windows and Linux** recompilation port of PlayStation 3 *Gran Turismo 5* that statically translates **PPU and SPU** PowerPC guest code to host-native binaries instead of running the retail build under RPCS3-style full-system emulation. Users supply their own disc or install image; the project documents decryption, lifting, patching, and mod installation as an end-to-end AAA static-port reference. (source: wiki/sources/descriptions/MormonFTP-hub__gt5-recomp.md)

## Static translation pipeline

Built on the **ps3recomp** toolchain: **CMake** orchestration, large **C/C++** runtime glue, and extensive **Python** and **PowerShell** automation for lift jobs, native patches, RSX and audio debugging, and update/mod installs. Retail keys, binaries, and generated lift artifacts remain **local** to the researcher. (source: wiki/sources/descriptions/MormonFTP-hub__gt5-recomp.md)

## Host runtime

**High-level emulation** of PS3 system services complements translated PPU/SPU code; **hand-written native replacements** cover hot SPU workloads. Graphics route through **DirectX 12** or **Vulkan** RSX runtimes with optional **NVIDIA DLSS** and **AMD FSR** upscaling. Distribution includes a graphical installer and **C#** launcher for setup and updates. (source: wiki/sources/descriptions/MormonFTP-hub__gt5-recomp.md)

## Audience

Targets **preservationists** and porting researchers studying PS3 executable decryption, static recompilation at AAA scale, and performance-oriented reverse engineering—not live multiplayer anti-cheat bypass. (source: wiki/sources/descriptions/MormonFTP-hub__gt5-recomp.md)

## Positioning

Sits in the PS3 **ps3recomp** cluster beside [[motorstorm-mv-recomp]] (WIP *MotorStorm* translation) and general Cell analysis tooling such as [[spu2c]]. Pair with [[static-runtime-evidence]] when labeling which guest subsystems are lifted vs HLE-stubbed. (source: wiki/sources/descriptions/MormonFTP-hub__gt5-recomp.md)

## Links

- Repo: https://github.com/MormonFTP-hub/gt5-recomp [Gran Turismo 5 (PS3) static recompilation to native Windows/Linux via ps3recomp: PPC/SPU lift, D3D12/Vulkan RSX runtime, launcher installer, and documented modding pipeline (BYO disc)]

## Related

[[motorstorm-mv-recomp]] · [[spu2c]] · [[gow-pc-port]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]