---
title: Detect-MouseClassServiceCallback
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/KANKOSHEV__Detect-MouseClassServiceCallback.md
updated: 2026-08-24
confidence: medium
---

# Detect-MouseClassServiceCallback

**Kernel-mode proof of concept** focused on **MouseClassServiceCallback hook detection** (KANKOSHEV). Includes low-level hook-handling code and driver logic to **observe or validate mouse callback execution paths**. Structured as a Windows kernel project built with Visual Studio and WDK-style components. Primarily relevant to **anti-cheat** and **rootkit detection** research around input interception—not a production enforcement stack. (source: wiki/sources/descriptions/KANKOSHEV__Detect-MouseClassServiceCallback.md)

Complements offensive MouClass **ServiceCallback** injection PoCs such as [[mouseclassservicecallbacktrick]] and [[mouseclassservicecallbackmeme]], MouHid hook drivers such as [[mouhid-input-hook]], and user-mode movement validators such as [[mousedetection]] when threat-modeling ring-0 mouse input paths.

## Links

- Repo: https://github.com/KANKOSHEV/Detect-MouseClassServiceCallback

## Related

[[mouseclassservicecallbacktrick]] · [[mouseclassservicecallbackmeme]] · [[mouhid-input-hook]] · [[directinput]] · [[kernel-mouse]] · [[mousedetection]] · [[face-injector-v2]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
