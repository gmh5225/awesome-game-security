---
title: KSU-Rust-Frida
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dreamland-blog__KSU-Rust-Frida.md
updated: 2026-08-16
confidence: medium
---

# KSU-Rust-Frida

**KernelSU** module written in Rust that loads the **Frida gadget** into target Android applications at startup. Combines [[kernelsu]] kernel-level app modification with [[frida]] dynamic instrumentation: the Frida shared library is injected into Zygote-forked processes before the app's own code runs, enabling runtime hooking without a separate root-detection bypass step. (source: wiki/sources/descriptions/dreamland-blog__KSU-Rust-Frida.md)

Single-binary ARM64 engine with **attach**, **spawn**, and **watch-so** modes, localhost **HTTP RPC** control plane, and multi-mode stealth tiers (**normal**, **wxshadow**, **recomp**). Also supports Magisk module workflows. Mainly useful for mobile security researchers performing dynamic analysis and instrumentation of Android games and apps on KernelSU/Magisk roots. (source: wiki/sources/descriptions/dreamland-blog__KSU-Rust-Frida.md)

## Links

- Repo: https://github.com/dreamland-blog/KSU-Rust-Frida (Android ARM64 dynamic instrumentation module for KernelSU/Magisk)

## Related

[[kernelsu]] · [[frida]] · [[frida-rs]] · [[magisk]] · [[zygisk-frida]] · [[rust-frida]] · [[mkpms]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
