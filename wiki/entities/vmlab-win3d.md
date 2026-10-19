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

**vmlab-win3d** (VMLabDev) is a build and validation framework for a Windows guest **kernel- and user-mode 3D graphics stack** in **QEMU/KVM** with hardware-accelerated **GPU passthrough** and **virtio/virgl** host integration. It packages signed **WDDM/Venus** display drivers with **Mesa OpenGL**, **D3D12**, and **Vulkan SDK** pieces using cross-compilation toolchains, shell and Python packaging scripts, and **Docker** build environments (runtime mostly **C/C++**). Automated acceptance and compatibility evidence covers **Windows 10 and 11** on **AMD and NVIDIA** hosts for **Direct3D 9 through 12**, **OpenGL**, and **Vulkan** via probes, benchmarks, and **commercial game workloads**, plus experiments on fence timing, **DMA latency**, **DWM** heap usage, **dmabuf** sharing, and driver pinning under **Secure Boot**. The project targets game security researchers, reverse engineers, and anti-cheat developers who need reproducible, isolated Windows graphics labs to study titles, kernel drivers, and virtualized GPU behavior at scale. (source: wiki/sources/descriptions/VMLabDev__vmlab-win3d.md)

## Links

- Repo: https://github.com/VMLabDev/vmlab-win3d

## Related

[[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[frame-observation-boundary]] · [[hvci]] · [[gpu-inspector]]
