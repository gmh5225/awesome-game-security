---
title: PE-bear
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hasherezade__pe-bear.md
updated: 2026-08-05
confidence: medium
---

# PE-bear

Portable executable (PE) file **viewer and editor** with a Qt-based GUI. Surfaces DOS/NT headers, section tables, import/export directories, resources, relocations, debug directories, TLS, and CLR metadata; supports hex editing, section manipulation, overlay extraction, and side-by-side comparison of multiple PE files. Aimed at malware analysts, reverse engineers, and security researchers doing manual PE structure analysis and modification. (source: wiki/sources/descriptions/hasherezade__pe-bear.md)

Useful for triage and light patching of game/client binaries before deeper IDA/Ghidra work—complements WPF viewers such as [[totalpe2]] and bundled lab installs such as [[retoolkit]].

## Links

- Repo: https://github.com/hasherezade/pe-bear

## Related

[[totalpe2]] · [[pe-sieve]] · [[retoolkit]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
