---
title: Drv Hide And Camouflage
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/IcEy-999__Drv_Hide_And_Camouflage.md
updated: 2026-08-24
confidence: medium
---

# Drv Hide And Camouflage

Windows **kernel research project** focused on **driver hiding** and **identity camouflage** (IcEy-999). Demonstrates loading and masking an **unsigned driver** using many **unexported kernel routines**, **manual offset initialization**, and low-level **object or import-table manipulation**. Implemented mainly in **C** for ring-0 driver development; includes tests across **modern Windows versions**. Intended for advanced **kernel security** and **anti-detection** research scenarios. (source: wiki/sources/descriptions/IcEy-999__Drv_Hide_And_Camouflage.md)

Goes beyond simple Flink/Blink unlink samples such as [[hide-driver]] toward **load-time masking** and **driver-object identity camouflage** — closer to multi-artifact hide stress tests such as [[hide-driver-testing]] and trace-cleanup PoCs such as [[clear-driver-traces]], but emphasizing **unexported routine use** and **import-table/object manipulation** rather than only PiDDBCache / unload-buffer cleanup. Same author lane as [[ntoskrnl-viewer]] for live kernel introspection during offset and symbol research.

## Links

- Repo: https://github.com/IcEy-999/Drv_Hide_And_Camouflage

## Related

[[hide-driver]] · [[hide-driver-testing]] · [[clear-driver-traces]] · [[nullmap]] · [[ntoskrnl-viewer]] · [[kernel-pool-scanning]] · [[openark]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
