---
title: Anbox
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/anbox__anbox.md
updated: 2026-08-18
confidence: medium
---

# Anbox

Container-based runtime that runs a **full Android system on Linux** without relying on heavyweight virtualization. Uses **Linux namespaces** and a host-side daemon to broker hardware access, including **OpenGL ES** rendering paths adapted from Android emulator components. C++ / CMake codebase integrating **LXC**, **D-Bus**, and **protobuf**; targets desktop and cloud-style Android application workloads. Maintenance is archived but the project remains a useful reference for containerized Android hosts and emulator-adjacent RE. (source: wiki/sources/descriptions/anbox__anbox.md)

Sits in the README `Android Emulator` lane beside QEMU/KVM stacks such as [[qemu-gvm]] and [[android-emulator-hypervisor-driver]], runtime emulator root via [[aeroot]], and AVD Magisk/root via [[rootavd]]. Container fingerprinting probes such as [[conbeerlib]] and classic emulator heuristics ([[anti-emulator]], [[android-emulator-detection]]) apply when APKs run inside Anbox rather than on bare metal.

## Links

- Repo: https://github.com/anbox/anbox

## Related

[[android-emulator]] · [[aeroot]] · [[rootavd]] · [[conbeerlib]] · [[anti-emulator]] · [[android-emulator-detection]] · [[qemu-gvm]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
