---
title: AntiCheat-detection
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/vipmaycom__AntiCheat-detection.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# AntiCheat-detection

**AntiCheat-detection** (vipmaycom/AntiCheat-detection) is a research repository documenting how major **commercial game anti-cheat** stacks behave on Windows, from **static and dynamic reverse engineering** of their client and kernel components. Long-form markdown analyses sit beside **reconstructed C implementations** and Visual Studio projects that model **Riot Vanguard** user-mode/kernel services and an **Easy Anti-Cheat** EOS-style kernel driver for side-by-side study—not shipping binaries. (source: wiki/sources/descriptions/vipmaycom__AntiCheat-detection.md)

Distinct from version-scoped catalogs such as [[anti-cheat-observatory]] or single-product dossiers like [[ocean-anticheat-analysis]]: this tree spans **multiple vendors** (BattlEye, EAC, Vanguard, FACEIT, EA AntiCheat, Denuvo, related modules) with both narrative architecture notes and reference code.

## Documented surfaces

| Area | Coverage (per repo summary) |
|------|-----------------------------|
| **Kernel** | Callbacks, memory and syscall scanning |
| **Virtualization / DMA** | Hypervisor and DMA detection paths |
| **Identity / enforcement** | HWID and ban telemetry |
| **Forensics** | Cleanup traces left on disk/registry |
| **Vendors** | BattlEye, Easy Anti-Cheat, Riot Vanguard, FACEIT, EA AntiCheat, Denuvo, related clients/drivers |

## Artifacts

- Markdown reverse-engineering write-ups per major AC product
- Reconstructed Vanguard user-mode and kernel service models (C / VS projects)
- Reconstructed EAC EOS-style kernel driver skeleton for comparative reading

## Audience

**Game security researchers**, **reverse engineers**, and **defenders** who need structured, technical insight into real-world anti-cheat architecture rather than marketing summaries—listed under **Anti Cheat** / **Analysis Framework** in the README map. Pair with [[research-rigor]]; treat reconstructions as study aids, not ground truth for a specific shipped build.

## Links

- Repo: https://github.com/vipmaycom/AntiCheat-detection

## Related

[[ocean-anticheat-analysis]] · [[anti-cheat-research-index]] · [[ff-ace-anticheat-analysis]] · [[battleye-re]] · [[all-about-eac]] · [[vanguard]] · [[research-rigor]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
