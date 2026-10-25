---
title: O3 Root
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/zsw125__o3root.md
updated: 2026-10-25
confidence: medium
---

# O3 Root

**Shizuku-driven** Android application that chains a kernel exploit for **CVE-2026-98260** into **temporary root** on select **Xiaomi HyperOS** devices (yingtian / lhasa codenames; HyperOS 4; **Linux 6.18**, e.g. kernel 6.18.21). A native **C** payload drives a **use-after-free** trigger, **page reclaim**, and a **two-stage red-black tree write primitive** with **KASLR sliding**, then elevates credentials and loads an embedded **KernelSU-family** loadable kernel module (**LKM**) for the **current boot only** (not boot-persistent root). The companion **Java** app orchestrates permission checks, firmware gating, payload execution via **Shizuku shell mode**, and automatic selection among bundled **KernelSU**, **KernelSU-Next**, or **SukiSU** modules using runtime **kallsyms** resolution or symbol relinking. Supporting **Python** and shell tooling covers payload/APK builds, OTA and boot-image analysis, and kernel **BTF** verification. Targets mobile kernel exploit research, Android rooting workflows, and analysts studying privilege escalation, **SELinux** interaction, and ephemeral versus persistent root on hardened consumer firmware. (source: wiki/sources/descriptions/zsw125__o3root.md)

Distinct CVE lane from **CVE-2026-43499** packaged roots ([[ghostlock-app]], [[root-my-pixel]], [[ghostlock-oneplus]], [[cve-2026-43499-popsicle]]): **CVE-2026-98260** UAF + rb-tree primitive on HyperOS 6.18. Same Shizuku-orchestrated pattern as [[root-my-pixel]] but Xiaomi yingtian/lhasa–scoped with multi-variant KernelSU-family LKM loading.

## Architecture

| Layer | Role |
|-------|------|
| Java UI | Shizuku permission, firmware/device gating, exploit orchestration |
| Native C | UAF trigger → page reclaim → two-stage rb-tree writes → cred elevation |
| LKM loader | Boot-scoped KernelSU / KernelSU-Next / SukiSU pick via kallsyms or relink |
| Build/analysis | Python/shell: payload/APK build, OTA/boot.img, BTF checks |

## Links

- Repo: https://github.com/zsw125/o3root
- CVE: CVE-2026-98260

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[ghostlock-app]] · [[ghostlock-oneplus]] · [[root-my-pixel]] · [[android-kernel-exploitation]] · [[mobile-anti-cheat]]
