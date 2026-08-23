---
title: KernelSU
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/tiann__KernelSU.md
  - wiki/sources/descriptions/msnx__KernelSU-Pixel4XL.md
  - wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md
  - wiki/sources/descriptions/gmh5225__KernelSU-4.4.md
  - wiki/sources/descriptions/gmh5225__A146B-KSU.md
  - wiki/sources/descriptions/dreamland-blog__KSU-Rust-Frida.md
  - wiki/sources/descriptions/alex193a__Root-My-Pixel.md
  - wiki/sources/descriptions/YuKongA__ghostlock-app.md
  - wiki/sources/descriptions/MlgmXyysd__KernelSU_Debug.md
updated: 2026-08-23
confidence: medium
---

# KernelSU

Kernel-based Android root solution (**kernel su**) listed under Cheat / Android root. Implemented primarily in Kotlin and Rust; grants elevated privileges via kernel-level integration rather than Magisk-style systemless userspace alone. Canonical reference for researchers studying Android root frameworks, module ecosystems (alongside Magisk / APatch), and mobile anti-cheat root-detection tradeoffs. (source: wiki/sources/descriptions/tiann__KernelSU.md)

Adjacent tooling: Magisk modules that also target KernelSU such as [[move-certificate]]; systemless Magisk itself [[magisk]]; Magisk-install paths such as [[cheese]]. Dynamic-instrumentation module [[ksu-rust-frida]] (Rust; Frida gadget into Zygote-forked app processes at startup; attach/spawn/watch-so + HTTP RPC; normal/wxshadow/recomp stealth) combines KernelSU kernel-level app modification with [[frida]] hooking for mobile game/app RE. (source: wiki/sources/descriptions/dreamland-blog__KSU-Rust-Frida.md) Hardened fork [[apex-su]] rewrites userspace in Rust and adds stealth IOCTL over an anonymous `io_uring`-disguised inode (no proc/sys/dev entries) for root-hide research. (source: wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md) Device-specific KernelSU kernel trees such as [[kernelsu-pixel4xl]] (Pixel 4 XL / coral / msm-floral) integrate the same syscall-hook and credential-override model into vendor BSP sources. (source: wiki/sources/descriptions/msnx__KernelSU-Pixel4XL.md) Samsung Galaxy A14 5G (A146B / a14x) KernelSU kernel sources such as [[a146b-ksu]] (gmh5225; modified Samsung kernel tree for custom ROM builders) extend that model to mid-range Exynos/MediTek Samsung BSPs. (source: wiki/sources/descriptions/gmh5225__A146B-KSU.md) Legacy **Linux 4.4** backport [[kernelsu-4.4]] (SELinux policy + APK signature verification; Google GCC 4.9) targets pre-GKI OEM kernels where upstream KernelSU does not ship. (source: wiki/sources/descriptions/gmh5225__KernelSU-4.4.md) One-tap Pixel root installer [[root-my-pixel]] chains CVE-2026-43499 IonStack LPE with ReSukiSU/KernelSU late-load on Pixel 7–10 via Shizuku-elevated shell. (source: wiki/sources/descriptions/alex193a__Root-My-Pixel.md) Multi-vendor one-tap root app [[ghostlock-app]] chains the same CVE via kernel pselect race, then loads KernelSU or ReSukiSU modules after uid 0 on matched kernel builds. (source: wiki/sources/descriptions/YuKongA__ghostlock-app.md) Debug-oriented fork [[kernelsu-debug]] (MlgmXyysd; relaxed manager checks, permissive SELinux options, init scripts; kernel C + Android app/build assets; profile control; Android security research / system debugging) trades production hardening for lab convenience. (source: wiki/sources/descriptions/MlgmXyysd__KernelSU_Debug.md)

## Links

- Repo: https://github.com/tiann/KernelSU

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[magisk]] · [[apex-su]] · [[kernelsu-debug]] · [[move-certificate]] · [[ksu-rust-frida]] · [[kernelsu-pixel4xl]] · [[a146b-ksu]] · [[kernelsu-4.4]] · [[root-my-pixel]] · [[ghostlock-app]] · [[magiskdetector]] · [[frida]] · [[keyattestation]]
