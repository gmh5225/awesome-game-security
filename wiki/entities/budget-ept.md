---
title: BudgetEPT (brew02)
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/brew02__BudgetEPT.md
updated: 2026-08-17
confidence: medium
---

# BudgetEPT (brew02)

**BudgetEPT** (brew02/BudgetEPT) is a proof-of-concept kernel driver that repurposes **SMAP** (Supervisor Mode Access Prevention) and **SMEP** (Supervisor Mode Execution Prevention) to build **inline hooks with split-page-like semantics** similar to **EPT hooks**, without requiring a hypervisor or direct extended page table manipulation. The project demonstrates how CPU access-control features can emulate EPT-style execute/read views on the same virtual address. A limited example shows how **software virtualization** could complement these hooks to better conceal their presence. Aimed at kernel security researchers studying alternative hooking techniques, SMAP/SMEP abuse, and EPT hook emulation outside virtualization. (source: wiki/sources/descriptions/brew02__BudgetEPT.md)

Complements brew02 **#PF page-fault hooks** in [[fast-pf-hook]], per-process **PTE hooks** such as [[windows-kernel-pagehook]], and full **VT-x EPT hook** stacks such as [[hypervisor]] and [[ophion]]. Defensive **EPT hook detectors** such as [[ept-hook-detection]] and [[ermsb-meme]] target hypervisor-backed splits rather than this SMAP/SMEP emulation lane.

## Links

- Repo: https://github.com/brew02/BudgetEPT (README tag: Create stealthy, inline, EPT-like hooks using SMAP and SMEP)

## Related

[[fast-pf-hook]] · [[windows-kernel-pagehook]] · [[smep-bypass]] · [[hypervisor]] · [[ophion]] · [[ept-hook-detection]] · [[hook-kdtrap]] · [[ki-user-exception-dispatcher-hook]] · [[covert-thread]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
