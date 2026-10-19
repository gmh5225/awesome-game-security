---
title: vmlab-win3d
kind: entity
topics: [graphics-api, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/VMLabDev__vmlab-win3d.md
updated: 2026-10-19
confidence: medium
---

# vmlab-win3d

**vmlab-win3d** (VMLabDev) is a build and validation framework for a Windows guest **WDDM/Venus** 3D stack in **QEMU/KVM** with GPU passthrough and virtio/virgl host integration. It assembles signed display drivers, Mesa OpenGL, D3D12, and Vulkan SDK pieces (C/C++, cross-compilation, Docker) and ships automated acceptance evidence on Windows 10/11 for **Direct3D 9–12, OpenGL, and Vulkan**—including fence timing, DMA latency, DWM heap, dmabuf, and Secure Boot pinning experiments—for isolated graphics and anti-cheat research labs. (source: wiki/sources/descriptions/VMLabDev__vmlab-win3d.md)

## Links

- Repo: https://github.com/VMLabDev/vmlab-win3d

## Related

[[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/overview]] · [[frame-observation-boundary]] · [[hvci]]
