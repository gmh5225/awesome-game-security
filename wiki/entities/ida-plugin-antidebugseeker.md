---
title: ida-plugin-antidebugseeker
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/LAC-Japan__IDA_Plugin_AntiDebugSeeker.md
updated: 2026-08-23
confidence: medium
---

# ida-plugin-antidebugseeker

**AntiDebugSeeker** is an IDA Pro plugin (Python, PyQt5) that automatically detects potential **anti-debugging logic** in analyzed binaries. It scans for suspicious Windows API usage and keyword-based anti-debug techniques using **configurable rule files**, then highlights matches, annotates addresses, and supports quick navigation to detections. An in-IDE configuration editor lets analysts extend or tune rules without leaving IDA. Aimed at malware analysts and security researchers who need faster triage of anti-debug protections in protected clients, packers, and AC modules. (source: wiki/sources/descriptions/LAC-Japan__IDA_Plugin_AntiDebugSeeker.md)

Complements static rule scanners such as [[ida-security-scanner]] on decompiled pseudocode, Windows anti-debug technique catalogs such as [[makin]] and [[al-khaser]], and ScyllaHide-class hide plugins such as [[scyllahide-for-ida9.0rc]] when mapping debugger-evasion surfaces before bypass work.

## Links

- Repo: https://github.com/LAC-Japan/IDA_Plugin_AntiDebugSeeker

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[ida-security-scanner]] · [[anti-debugging]] · [[makin]] · [[al-khaser]] · [[scyllahide-for-ida9.0rc]] · [[list-of-ida-plugins]]
