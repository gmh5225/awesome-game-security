---
title: Hidden-Thread-Finder
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Hidden-Thread-Finder.md
updated: 2026-08-12
confidence: medium
---

# Hidden-Thread-Finder

Proof-of-concept **hidden / manipulated system-thread detector** (gmh5225) that compares what **APC** and **NMI callbacks** can still recover after key **KTHREAD** fields are tampered with. The demo creates a system thread, deliberately clears fields such as `SystemThread`, `ApcQueueable`, `StackBase`, and `InitialStack` on a Windows 10 20H2–specific KTHREAD layout, then inspects the thread through both a queued APC callback and a registered NMI callback. Logging shows whether each mechanism can still observe stack metadata or system-thread state—more an experiment in what thread-hiding tricks break simple inspection than a production scanner. (source: wiki/sources/descriptions/gmh5225__Hidden-Thread-Finder.md)

Useful for anti-cheat and kernel researchers studying **hidden-thread detection**, **KTHREAD field spoofing**, and the limits of **APC- versus NMI-based validation**.

Complements enumeration heuristics in [[system-thread-finder]] and [[stealth-sytem-thread-finder-be]], NMI stack-walk research such as [[kernel-anti-cheat]] and [[nmi-nmi-callback]], and evasion PoCs such as [[zero-thread-kernel]] that avoid creating visible system threads.

## Links

- Repo: https://github.com/gmh5225/Hidden-Thread-Finder

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[kernel-anti-cheat]] · [[nmi-nmi-callback]] · [[zero-thread-kernel]] · [[cheat-attack-thread-slemu]]
