---
title: FakeEye
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/mexploitui__FakeEye.md
  - wiki/sources/descriptions/Hypercall__FakeEye.md
updated: 2026-08-24
confidence: medium
---

# FakeEye

Lightweight **BattlEye-style launcher emulator**: compact C++ (Visual Studio project files + helper headers) that reproduces launcher-side startup behavior for controlled anti-cheat research and compatibility testing in isolated lab setups—not a kernel bypass. (source: wiki/sources/descriptions/Hypercall__FakeEye.md)

The Hypercall tree focuses on mimicking a BattlEye-style game-launcher environment without the real [[battleye]] stack. An earlier mexploitui fork documents the same lane in more detail: SCM-managed `BEService`, external config, and BE-style game process creation so protected titles start as if BattlEye were present. (source: wiki/sources/descriptions/mexploitui__FakeEye.md)

Complements client-protocol emulators such as [[be-emulator]] and in-process client-interface PoCs such as [[beclient]] by covering service/install/launch contracts rather than runtime BEClient DLL protocol handling.

## Links

- Repo (Hypercall): https://github.com/Hypercall/FakeEye
- Repo (mexploitui): https://github.com/mexploitui/FakeEye

## Related

[[battleye]] · [[be-emulator]] · [[beclient]] · [[noeye]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
