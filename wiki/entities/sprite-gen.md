---
title: sprite-gen
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/aldegad__sprite-gen.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# sprite-gen

**sprite-gen** (aldegad/sprite-gen) is a Python CLI and AI coding-agent skill that turns a single base character image into game-ready transparent sprite atlases or motion loops. Listed under README **Game Assets**. (source: wiki/sources/descriptions/aldegad__sprite-gen.md)

## Component-row atlas pipeline

Drives image and video generation through providers such as Codex, OpenAI, and Grok Imagine; locks character identity row by row; converts chroma backgrounds to real alpha; extracts clean frames; and emits runtime atlases with machine-readable `manifest.json` frame layouts. (source: wiki/sources/descriptions/aldegad__sprite-gen.md)

## Video and motion pipeline

A separate video pipeline generates seamless transparent GIF, WebP, or frame-strip loops per motion state, with optional curation tooling for comparing, rejecting, and nudging frames before export. (source: wiki/sources/descriptions/aldegad__sprite-gen.md)

## Post-processing and alignment

Built with Python, Pillow, and NumPy; supports recoloring, layer composition, and pixel-grid alignment so generative output lands on engine-ready grids rather than unusable demo sheets. (source: wiki/sources/descriptions/aldegad__sprite-gen.md)

## Export targets

Exports to engines and tooling including Aseprite, Phaser, and Flame — production-quality 2D sprite atlases from generative models for game developers and asset pipelines. (source: wiki/sources/descriptions/aldegad__sprite-gen.md)

## Positioning

Sits in the README **Game Assets** lane beside fal.ai web generators such as [[sprite-sheet-creator]] and Codex skillsets such as [[agent-sprite-forge]] and [[image-cockpit-for-codex-workflows]] — component-row state pipelines with alpha cleanup, frame extraction, and runtime atlas output rather than raw generative sheets.

## Links

- Repo: https://github.com/aldegad/sprite-gen [Codex/Claude skill for generating clean 2D game sprites and animation atlases via component-row state pipelines, alpha cleanup, frame extraction, and runtime atlas output]

## Related

[[overviews/game-engine]] · [[overviews/overview]] · [[sprite-sheet-creator]] · [[agent-sprite-forge]] · [[image-cockpit-for-codex-workflows]] · [[3d-asset-factory]]
