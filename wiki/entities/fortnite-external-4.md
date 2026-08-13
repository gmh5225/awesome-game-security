---
title: fortnite-external-4
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Fortnite-External-4.md
updated: 2026-08-13
confidence: medium
---

# fortnite-external-4

External Fortnite cheat sample (gmh5225; cheat / game:fortnite [External]; circa 2019). Out-of-process **ESP** and **aimbot** built on a **socket-based kernel driver** for cross-process memory access. Loads its communication driver via a **Capcom.sys-based driver mapper**—a legacy [[byovd]] manual-map path in the same historically abused LOLdriver lane as [[dolboeb-executor]]. Useful for studying early external-cheat stacks that pair vulnerable-driver mapping with kernel-socket RPM instead of conventional IOCTL device objects on [[easy-anti-cheat]]-protected Fortnite clients. (source: wiki/sources/descriptions/gmh5225__Fortnite-External-4.md)

Sits beside newer gmh5225 external Fortnite samples such as [[fortnite-external]], [[fortnite-external-5]], and [[fortnite-external-cheat-winsense-leak]], and beside Capcom-mapper research such as [[known-driver-mappers]] and [[ksocket]] (kernel WSK socket comm research).

## Links

- Repo: https://github.com/gmh5225/Fortnite-External-4

## Related

[[easy-anti-cheat]] · [[byovd]] · [[world-to-screen]] · [[dolboeb-executor]] · [[known-driver-mappers]] · [[ksocket]] · [[fortnite-external]] · [[fortnite-external-5]] · [[fortnite-external-cheat-winsense-leak]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
