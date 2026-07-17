---
title: BusterCall
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/zer0condition__BusterCall.md
updated: 2026-07-17
confidence: medium
---

# BusterCall

Windows kernel research driver that enumerates registered process, thread, image-load, and registry [[kernel-callbacks]], attributes them to owning drivers, and can selectively remove or patch them—useful for studying how anti-cheat registers notify routines and how attackers try to disable them. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

README framing also positions the work around an [[hvci]] bypass path via PFN swapping to invoke arbitrary kernel functions from user mode. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

## Links

- Repo: https://github.com/zer0condition/BusterCall

## Related

[[kernel-callbacks]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
