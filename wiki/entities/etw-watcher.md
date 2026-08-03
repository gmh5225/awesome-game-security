---
title: EtwWatcher
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/jonny-jhnson__EtwWatcher.md
updated: 2026-08-03
confidence: medium
---

# EtwWatcher

Web-based tool for browsing, comparing, and diffing Windows ETW (Event Tracing for Windows) provider manifests across different OS versions, with snapshot tracking and change visualization. Backed by ETWInspector. (source: wiki/sources/descriptions/jonny-jhnson__EtwWatcher.md)

Complements live GUI manifest browsers such as [[etw-explorer]] by tracking how provider schemas evolve between Windows builds—useful when AC/EDR telemetry design must account for OS-version drift.

## Links

- Repo: https://github.com/jonny-jhnson/EtwWatcher

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[etw-explorer]] · [[etw-threat-intelligence]]
