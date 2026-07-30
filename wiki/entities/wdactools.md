---
title: WDACTools
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/mattifestation__WDACTools.md
updated: 2026-07-30
confidence: medium
---

# WDACTools

PowerShell module suite for managing **Windows Defender Application Control (WDAC)** code-integrity policies. Cmdlets build base and supplemental CI policies, configure rule options (UMCI, WHQL, audit mode, managed installer), parse serialized policy binaries via **CIPolicyParser**, and deploy policies with **CiTool.exe** plus auditing support. Includes **Decrypt p7b** helpers for working with signed policy blobs. (source: wiki/sources/descriptions/mattifestation__WDACTools.md)

Useful research reference for the platform-trust / code-integrity lane when studying what [[hvci]] and kernel CI enforcement allow or deny—adjacent to HVCI blocklist tooling such as [[solemn]] and Defender-control utilities such as [[windefctl]] / [[defender-control]].

## Links

- Repo: https://github.com/mattifestation/WDACTools

## Related

[[hvci]] · [[solemn]] · [[windefctl]] · [[defender-control]] · [[bootbypass]] · [[kvc]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
