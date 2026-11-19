---
title: Accel-virt
kind: entity
topics: [graphics-api, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/acceleration3__accel-virt.md
updated: 2026-11-19
confidence: medium
---

# Accel-virt

**accel-virt** ([acceleration3/accel-virt](https://github.com/acceleration3/accel-virt)) is a **paravirtualized graphics acceleration stack** for **Windows 11 QEMU/KVM** guests: a guest Windows rendering environment paired with a **host-side GPU executor** over an extended **virtio-gpu** device (**virtio-gpu-av-pci**) integrated with QEMU. The codebase is **C/C++** (CMake) and implements **kernel-mode DXGI/DXGK** plumbing via **avgpu.sys** plus user-mode shims for **Direct3D 9/11/12**, **Vulkan**, **OpenGL**, and **OpenCL**. (source: wiki/sources/descriptions/acceleration3__accel-virt.md)

## Capabilities

- **Guest RAM lending**, **session recording and replay**, trace/inspect tooling, and dedicated probe modules for Direct3D, OpenGL, Vulkan, and **overlay-style presentation** paths.
- Large **fuzz corpora** and conformance tests targeting virtio command streams, paging, and API record layouts.

Targets game security researchers who need an **isolated VM graphics lab** to study driver behavior, capture and replay GPU API traffic, or analyze **overlay and layered-device** interactions relevant to anti-cheat design. README category: Windows Emulator / paravirtual GPU. (source: wiki/sources/descriptions/acceleration3__accel-virt.md)

## Links

- Repo: https://github.com/acceleration3/accel-virt

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[vmlab-win3d]] · [[frame-observation-boundary]] · [[present-hook]] · [[gpu-inspector]]