---
title: KDemu
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/ShallowFeather__KDemu.md
updated: 2026-08-21
confidence: medium
---

# KDemu

**KDemu** is a hybrid **Windows kernel driver emulator** that combines **emulated and native execution paths** for difficult analysis targets. The C++ codebase includes PE loading, exception handling, kernel dump integration, anti-detection logic, and execution monitoring — aimed at improving visibility into **rootkit and anti-cheat style drivers** that resist conventional debugging environments. (source: wiki/sources/descriptions/ShallowFeather__KDemu.md)

Sits in the README `Windows Emulator` lane beside RING3 sandboxes such as [[kace]] and platform-independent [[kubera]], and WHP-hosted usermode guests such as [[winvisor]] — KDemu targets hybrid semi-emulated/semi-native kernel-driver stacks rather than pure usermode PE or full RING3-only emulation.

## Links

- Repo: https://github.com/ShallowFeather/KDemu (README: hybrid semi-emulated, semi-native Windows kernel driver emulator for advanced rootkit and anti-cheat analysis)

## Related

[[kace]] · [[kubera]] · [[winvisor]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
