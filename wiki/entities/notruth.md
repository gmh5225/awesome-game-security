---
title: NoTruth (KelvinMsft)
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/KelvinMsft__NoTruth.md
updated: 2026-08-23
confidence: medium
---

# NoTruth (KelvinMsft)

**NoTruth** is an open-source **Windows x64 research implementation** for hiding **user-mode memory** with **VT-x** and **EPT** techniques (KelvinMsft). It demonstrates how **read operations** can be redirected to **fake values** while **execution semantics** remain controlled, enabling experiments around **checksum** and **integrity bypasses**. The codebase is largely **C and C++** kernel-level code with **driver** and **test components** for virtualization-capable environments. Aimed at low-level security researchers investigating **memory deception**, **anti-cheat evasion**, and **hypervisor-assisted instrumentation**. (source: wiki/sources/descriptions/KelvinMsft__NoTruth.md)

README lane: **Hide Memory By VT** — offensive EPT read/view deception rather than defensive hypervisor hardening or EPT hook detection.

Complements full **VT-x EPT hook** stacks such as [[hypervisor]] and [[ophion]], software EPT-emulation hooks such as [[budget-ept]], and defensive **EPT hook detectors** such as [[ept-hook-detection]]. Sits beside other KelvinMsft Windows kernel research such as [[perfmon]], [[thread-spy]], and [[usbmon]] in the same author lane.

## Links

- Repo: https://github.com/KelvinMsft/NoTruth

## Related

[[hypervisor]] · [[ophion]] · [[budget-ept]] · [[ept-hook-detection]] · [[hypervisor-from-scratch]] · [[hypervisor-detection]] · [[perfmon]] · [[thread-spy]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
