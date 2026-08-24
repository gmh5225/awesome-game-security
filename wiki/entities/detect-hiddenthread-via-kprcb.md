---
title: Detect-HiddenThread-via-KPRCB
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/KANKOSHEV__Detect-HiddenThread-via-KPRCB.md
updated: 2026-08-24
confidence: medium
---

# Detect-HiddenThread-via-KPRCB

Windows **kernel proof of concept** for detecting **hidden threads** removed from the process/thread ID table (KANKOSHEV). Walks thread information through **KPRCB-related structures** and verifies thread presence with **thread lookup checks**. Implemented as a **Visual Studio kernel driver** project in C and C++. Primarily useful for **anti-cheat integrity monitoring** and **low-level forensic research**—not a production enforcement stack. (source: wiki/sources/descriptions/KANKOSHEV__Detect-HiddenThread-via-KPRCB.md)

Complements KTHREAD field-tamper experiments in [[hidden-thread-finder]], multi-path enumeration in [[unkover]] and [[system-thread-finder]], and offensive PspCidTable hide samples such as [[driver-systemthread-from-pspcidtable-src]] when studying threads concealed from standard API views.

## Links

- Repo: https://github.com/KANKOSHEV/Detect-HiddenThread-via-KPRCB

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hidden-thread-finder]] · [[unkover]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[kernel-anti-cheat]] · [[covert-thread]] · [[detect-keattachprocess]]
