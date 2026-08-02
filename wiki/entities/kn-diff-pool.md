---
title: kn-diff-pool
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/kernullist__kn-diff-pool.md
updated: 2026-08-02
confidence: medium
---

# kn-diff-pool

Windows kernel **Big Pool snapshot/diff toolkit**: a kernel driver captures pool allocation state and a user-mode **Go TUI** compares two snapshots to surface **new allocations** — useful for kernel object leak hunting, manual-map footprint analysis, and pool forensics without a full live walk. (source: wiki/sources/descriptions/kernullist__kn-diff-pool.md)

Complements Segment Heap–era [[kernel-pool-scanning]] heuristics (BigPool/VS/kLFH walks, PoolTag cross-ref) by offering a before/after diff workflow when studying driver load/unload or cheat lifecycle events. From the same maintainer as [[kn-live-dbg]] and [[windbg-decompile-ext]]; pair with [[research-rigor]] when generalizing pool layouts across Windows builds.

## Links

- Repo: https://github.com/kernullist/kn-diff-pool (README tag: Windows kernel Big Pool snapshot/diff tool with kernel driver and Go TUI)

## Related

[[kernel-pool-scanning]] · [[overviews/windows-kernel]] · [[kn-live-dbg]] · [[windbg-decompile-ext]] · [[revert-mapper]] · [[kernel-codecave-poc]] · [[research-rigor]]
