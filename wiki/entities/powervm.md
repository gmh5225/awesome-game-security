---
title: PowerVM
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/not1cyyy__PowerVM.md
updated: 2026-08-07
confidence: medium
---

# PowerVM

Kernel-mode process protection and transparent debugging framework that installs an AMD SVM-based Type-1 hypervisor beneath the Windows kernel to hide and analyze protected processes from anti-cheat software. Uses Nested Page Tables (NPT) for hardware-level function hooks, stealth memory reads via CPUID hypercalls, and shadow debugging that keeps DebugPort queries invisible to Ring 0 and Ring 3 observers. The codebase includes a kernel driver, a Qt-based controller launcher, and a fork of Cheat Engine for memory scanning and live game debugging (Delphi/Pascal debug engine; optional CUDA-accelerated pointer scanning). Targets Windows 10/11 on AMD CPUs with SVM support — aimed at researchers studying VMProtect- and ACE-protected processes, hypervisor-based AC evasion, and stealth debugging. (source: wiki/sources/descriptions/not1cyyy__PowerVM.md)

Sits in the AMD hacked-hypervisor lane beside [[baresvm]] and Intel VT-x/EPT stacks such as [[hypervisor]] and [[ophion]]; defensive counterparts include [[hypervisor-detection]], [[checkhv-um]], and [[ept-hook-detection]].

## Links

- Repo: https://github.com/not1cyyy/powervm (README tag: Stealth AMD-SVM Type-1 hypervisor with NPT hooks and a customized Cheat Engine debug engine for inspecting VMProtect- and ACE-protected processes)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[baresvm]] · [[hypervisor]] · [[ophion]] · [[unreal-vtdbg]] · [[hypervisor-detection]] · [[anti-cheat-amateur]] · [[hvci]]
