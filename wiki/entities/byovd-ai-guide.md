---
title: BYOVD AI Guide
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/LongpanZhou__BYOVD-AI-Guide.md
  - wiki/sources/README-categories.md
updated: 2026-10-26
confidence: medium
---

# BYOVD AI Guide

Educational Windows kernel **[[byovd]]** research corpus and repeatable methodology for finding signed drivers that expose dangerous kernel memory-write primitives. Bundles a large harvested driver binary set with static audit reports, deduplication, and **LOLDrivers** / Microsoft blocklist gates, plus PowerShell tooling to collect and manifest new candidates from vendor installers. The workflow targets AI-assisted headless Ghidra or IDA review of IOCTL dispatch paths, then proof-of-concept verification in a disposable VMware guest with WinDbg triage—without touching live host kernel memory. Documentation and agent prompts define severity tiers, audit scope, and a loop from harvest through blocklist checks to dynamic validation. (source: wiki/sources/descriptions/LongpanZhou__BYOVD-AI-Guide.md)

## Links

- Repo: https://github.com/LongpanZhou/BYOVD-AI-Guide

## Related

[[byovd]] · [[loldrivers]] · [[byovdfinder]] · [[hvci-loldrivers-check]] · [[kernel-cve-analysis]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
