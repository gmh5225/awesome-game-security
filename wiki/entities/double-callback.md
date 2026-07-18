---
title: DoubleCallBack
kind: entity
topics: [windows-kernel, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/wbaby__DoubleCallBack.md
updated: 2026-07-18
confidence: medium
---

# DoubleCallBack

C/C++ research sample focused on **DWM in kernel**—kernel-level Desktop Window Manager work spanning rendering and memory analysis in the cheat / render-draw lane. Useful for studying how composition/overlay paths can be driven from Ring0 rather than user-mode Present hooks alone. (source: wiki/sources/descriptions/wbaby__DoubleCallBack.md)

Adjacent to composition-surface kernel channels such as [[data-ptr-swap]] and user-mode DWM/overlay samples under [[overviews/graphics-api]].

## Links

- Repo: https://github.com/wbaby/DoubleCallBack

## Related

[[data-ptr-swap]] · [[present-hook]] · [[eac-overlay]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
