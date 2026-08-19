---
title: rw_socket_driver
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/adrianyy__rw_socket_driver.md
updated: 2026-08-19
confidence: medium
---

# rw_socket_driver

Windows **kernel driver** (C/C++) that exposes **protected-process memory read and write** over **network sockets**. A remote client exchanges commands with the driver via kernel socket communication—external memory control without in-process hooks. The codebase is adapted for **manual mapping** scenarios and is used in low-level game-security research for cheat-development experiments and anti-cheat robustness evaluation. (source: wiki/sources/descriptions/adrianyy__rw_socket_driver.md)

Contrasts with WSK transport libraries such as [[ksocket]] (BSD-style TCP/UDP from ring 0) by layering a full RPM/WPM command protocol on top of kernel networking. Complements IOCTL, shared-memory, and data-pointer KM↔UM channels such as [[kernel-payload-comms]] and [[km-um-communication]].

## Links

- Repo: https://github.com/adrianyy/rw_socket_driver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ksocket]] · [[kernel-payload-comms]] · [[km-um-communication]] · [[ntmemory]] · [[read-write-driver]]
