---
title: Scaxe AntiCheat OSS
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/ScaxeTeam__Scaxe-AntiCheat-OSS.md
updated: 2026-11-18
confidence: high
---

# Scaxe AntiCheat OSS

**Scaxe-AntiCheat-OSS** (ScaxeTeam) is an open release of **pretrained machine-learning weights** for scoring suspicious Minecraft player behavior from **temporal input features**, rather than a full server plugin or training pipeline. The published checkpoint **PRC-Open-0.5.5-1M** uses a compact **Conformer** encoder (~1M parameters), distributed as **Safetensors**, and expects batched **float32** tensors shaped for short behavioral sequences. Game-security researchers, server operators, and anti-cheat developers can study or integrate **sequence-based** cheat detection instead of rule-only heuristics. Materials are under **CC BY-NC-SA 4.0** (non-commercial share-alike with attribution). (source: wiki/sources/descriptions/ScaxeTeam__Scaxe-AntiCheat-OSS.md)

README category: open Conformer model weights for Minecraft temporal player-behavior anti-cheat inference.

## Model artifact

| Field | Detail |
|-------|--------|
| Checkpoint | `PRC-Open-0.5.5-1M` |
| Architecture | Conformer encoder (~1M params) |
| Format | Safetensors |
| Input | Batched float32, short behavioral sequences |

Weights-only distribution—integrators must supply feature extraction, labeling, calibration, and enforcement policy.

## Links

- Repo: https://github.com/ScaxeTeam/Scaxe-AntiCheat-OSS

## See also

[[minecraft-anticheatai]] · [[mlanticheat]] · [[chess-anti-cheat]] · [[research-rigor]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]]