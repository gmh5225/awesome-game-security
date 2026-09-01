---
title: astronaut00-apex-external
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/Astronaut00__apex-external.md
updated: 2026-09-01
confidence: medium
---

# astronaut00-apex-external

**ApexCheat** (Astronaut00/apex-external) is a C++ **external cheat and SDK** project for **Apex Legends** that reads game memory from outside the target process and drives features through an **ImGui** menu and overlay pipeline. Modules cover **glow** visuals, **aimbot** logic, and **memory-driven entity handling**. A companion **Rust** offset dumper helps maintain game structure offsets after updates. Intended for cheat prototyping and reverse-engineering experiments; repository notes describe the implementation as **outdated**. (source: wiki/sources/descriptions/Astronaut00__apex-external.md)

Sits in the Apex Legends external lane beside ImGui overlay samples such as [[apex-external]] and [[apex-external-cheat]], educational templates such as [[nullptr-apex-external]], and offset-maintenance tooling such as [[apex-legends-offset-dumper]] and [[apexdream]].

## Architecture highlights

| Component | Role |
|-----------|------|
| C++ external core | Out-of-process cheat + SDK with ImGui menu/overlay |
| Feature modules | Glow visuals, aimbot logic, entity iteration via memory reads |
| Rust offset dumper | Maintains game structure offsets across updates |

## Links

- Repo: https://github.com/Astronaut00/apex-external (External)

## Related

[[apex-external]] · [[apex-external-cheat]] · [[nullptr-apex-external]] · [[apex-legends-offset-dumper]] · [[apexdream]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
