---
title: ida-find-.data-ptr
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ida-find-.data-ptr.md
updated: 2026-08-08
confidence: medium
---

# ida-find-.data-ptr

Python IDAPython script for **`.data` pointer lookup** in IDA Pro databases: locate and cross-reference global/static pointers in the `.data` section during static game-client RE. Useful when triaging globals, vtables, singletons, or other writable data anchors without manual segment hopping. (source: wiki/sources/descriptions/gmh5225__ida-find-.data-ptr.md)

Data/xref triage—not rename automation, string association, or indirect-call recovery. Complements register xrefs via [[ida-plugins]], missing indirect targets via [[ida-missinglink]], and vtable skeleton work via [[ida-vtable-tools]] when the goal is “where does this `.data` pointer live and who references it?”

## Links

- Repo: https://github.com/gmh5225/ida-find-.data-ptr

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-plugins]] · [[ida-missinglink]] · [[ida-vtable-tools]] · [[idaplugins-list]]
