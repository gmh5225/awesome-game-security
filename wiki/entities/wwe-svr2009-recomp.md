---
title: WWE SmackDown vs. Raw 2009 Recomp
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/nefariousjosiah__WWE-SVR2009-RECOMP.md
  - wiki/sources/README-categories.md
updated: 2026-10-20
confidence: medium
---

# WWE SmackDown vs. Raw 2009 Recomp

**WWE SmackDown vs. Raw 2009 Recomp** (nefariousjosiah/WWE-SVR2009-RECOMP) statically recompiles the Xbox 360 retail build of *WWE SmackDown vs. Raw 2009* into native Windows, Linux, and Steam Deck executables without a full-system emulator. Listed under README **Xbox** (link_count 13). (source: wiki/sources/descriptions/nefariousjosiah__WWE-SVR2009-RECOMP.md) (source: wiki/sources/README-categories.md)

## Static recompilation

Uses the **ReXGlue** SDK (Xenia-derived) to lift PowerPC guest code to x86-64, with **XenosRecomp** ahead-of-time conversion of Xbox 360 shaders and a native renderer (re:Blue / plume) targeting **Direct3D 12** or **Vulkan**. Hooks, pipeline caching, and optional D3D call census / shader dumping support GPU translation RE. (source: wiki/sources/descriptions/nefariousjosiah__WWE-SVR2009-RECOMP.md)

## Stack and audience

C++ and CMake. Intended for Xbox 360 recompilation researchers, GPU translation study, and preservation-minded players who supply their own disc image— not live anti-cheat or online-service analysis. (source: wiki/sources/descriptions/nefariousjosiah__WWE-SVR2009-RECOMP.md)

## Positioning

Sits in the README **Xbox** static-recomp cluster beside ReXGlue ports such as [[nhl-legacy-remaster]] and XenonRecomp titles such as [[mcla-pc]] and [[dead-rising-2-case-zero-xenon-recomp]], contrasting with JIT HLE via [[xenia]]. Pair shader dump tooling with [[ida-vmx128-helper]] / [[idaxex]] for upstream X360 binary work. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/nefariousjosiah/WWE-SVR2009-RECOMP

## Related

[[nhl-legacy-remaster]] · [[mcla-pc]] · [[dead-rising-2-case-zero-xenon-recomp]] · [[xenia]] · [[idaxex]] · [[ida-vmx128-helper]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
