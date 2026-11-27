---
title: GprzSS
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/GprzSS__GprzSS.md
updated: 2026-11-27
confidence: medium
---

# GprzSS

Windows **screenshare scanner** for **Minecraft Java Edition** server staff verifying a player machine during integrity checks. Implemented in **Python 3.10+** using only the **standard library**; optional **PyInstaller** one-file distribution. One scan run can drive a **local web UI** or emit **headless markdown or JSON** reports with **severity-graded** findings. (source: wiki/sources/descriptions/GprzSS__GprzSS.md)

## Forensic modules

Roughly **a dozen collectors** cover running **processes**, **JVM identification** across common JDK distributions, **in-memory heap** inspection, **Prefetch**, **Amcache**, **BAM**, the **NTFS change journal**, **browser artefacts**, filesystem traces, **services**, **accounts**, and **mods**. Hits match against **editable JSON signatures** for known cheat clients and injectors.

## Privilege and access

Uses **ctypes**-based Windows APIs for process and memory access; can **self-elevate** so privileged artifacts are read or explicitly marked **skipped** rather than reported as clean.

## Links

- Repo: https://github.com/GprzSS/GprzSS

## Related

[[avgar-anticheats]] · [[jvm-inspector]] · [[jaranalyzer]] · [[hapiscanner]] · [[orchard-obliterator]] · [[screenshare-signatures]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]