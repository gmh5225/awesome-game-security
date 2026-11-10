---
title: Remote Package Installer NG
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/AldySan__Remote-Package-Installer-NG.md
  - wiki/sources/README-categories.md
updated: 2026-11-10
confidence: medium
---

# Remote Package Installer NG

**Cross-platform** desktop application (Rust; **egui** UI; **Tokio** async I/O) that installs **PlayStation 4** `.pkg` files over a **home LAN** without USB sticks or FTP. A separate core library implements the **PS4 Remote Package Installer** protocol, **local HTTP** file serving, **console discovery**, and **PKG** parsing. Users can queue one or many packages with **progress**, **pause**, **resume**, and **crash recovery** that reconciles install state with the console. (source: wiki/sources/descriptions/AldySan__Remote-Package-Installer-NG.md)

Targets **PS4 homebrew** workflows with **GoldHEN** Package Installer or compatible **RPI NextGen** payloads on the console. Useful for researchers studying **console package delivery**, **network installers**, and **reimplemented proprietary transfer protocols**.

README lists it under **PlayStation** (projected category map).

## Links

- Repo: https://github.com/AldySan/Remote-Package-Installer-NG

## Related

[[psfree-enhanced]] · [[cheatrunner-patches]] · [[drive-cloning-for-ps4-ps5]] · [[ghidra-orbis]] · [[ida-ps4-helper]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
