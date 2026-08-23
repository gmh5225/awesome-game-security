---
title: ThreadSpy (KelvinMsft)
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/KelvinMsft__ThreadSpy.md
updated: 2026-08-23
confidence: medium
---

# ThreadSpy (KelvinMsft)

**ThreadSpy** is a **hardware-assisted thread hijacking framework** for Windows (KelvinMsft). It takes over **running threads on the fly** without **patching instruction bytes**, enabling **code injection** or **memory operations** inside target process contexts. Implementation is primarily **C++** with **kernel-oriented components** and build setup for **Visual Studio** and **WDK** toolchains. Aimed at advanced security research into **stealth execution redirection** and **anti-cheat bypass** techniques. (source: wiki/sources/descriptions/KelvinMsft__ThreadSpy.md)

README lane: **PMI Callback** — offensive use of Performance Monitoring Interrupt paths for in-process execution redirection rather than detection-oriented HPC monitoring.

Contrasts with usermode thread-hijack PoCs such as [[thread-hijacking-injector]] (NullTerminatorr; compact remote context manipulation) and complements PMI/HPC security-monitoring samples such as [[pmi-hpc]] and KelvinMsft PMU/PMI research such as [[perfmon]] and [[usbmon]] in the same Windows kernel lane.

## Links

- Repo: https://github.com/KelvinMsft/ThreadSpy

## Related

[[thread-hijacking-injector]] · [[pmi-hpc]] · [[perfmon]] · [[process-injection-techniques]] · [[windows-process-injection]] · [[usbmon]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
