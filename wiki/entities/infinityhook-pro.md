---
title: InfinityHook Pro
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/FiYHer__InfinityHookPro.md
updated: 2026-08-25
confidence: medium
---

# InfinityHook Pro

Windows kernel hooking implementation that modernizes **InfinityHook** compatibility across Windows 7 through newer Windows 11 builds. Written in C/C++ for Visual Studio, it focuses on maintaining reliable hook behavior across version-specific kernel offset changes. The source emphasizes low-level internals and includes extensive comments for understanding the implementation details. Primary use cases include kernel security research and anti-cheat or EDR reverse engineering. (source: wiki/sources/descriptions/FiYHer__InfinityHookPro.md)

Complements the original [[infinityhook]] C library, C++ wrappers such as [[etwhook-infinityhookclass]], and evolved frameworks such as [[infinityhook-promax]], [[infinityhook-latest]], and [[infinityhookpro-main]] in the ETW-backed syscall interception lane.

## Links

- Repo: https://github.com/FiYHer/InfinityHookPro (README tag: ETW Hook Ex)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[infinityhook]] · [[etwhook-infinityhookclass]] · [[infinityhook-promax]] · [[infinityhook-latest]] · [[infinityhookpro-main]] · [[patchguard]] · [[etw-syscall]] · [[etw-syscall-monitor]]
