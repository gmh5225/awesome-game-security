---
title: kernel_payload_comms
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__kernel_payload_comms.md
updated: 2026-08-08
confidence: medium
---

# kernel_payload_comms

Kernel research sample focused on **shared memory** as a Ring0↔usermode cheat / driver-communication channel—studying payload exchange without obvious IOCTL or named-device surfaces. Listed under cheat / driver communication; aimed at game-security researchers and reverse engineers studying offensive KM↔UM I/O. (source: wiki/sources/descriptions/gmh5225__kernel_payload_comms.md)

The author notes the code was written quickly and may contain oversights; treat it as an experimental reference adjacent to named-event channels such as [[evcommunication]] and hook-based stealth I/O such as [[gina-public]].

## Links

- Repo: https://github.com/gmh5225/kernel_payload_comms

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[evcommunication]] · [[gina-public]] · [[read-write-driver]] · [[r69-driver]]
