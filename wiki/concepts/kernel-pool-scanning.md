---
title: Kernel Pool Scanning
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/descriptions/kernullist__kn-diff-pool.md
  - wiki/sources/descriptions/ioncodes__pooldump.md
  - wiki/sources/descriptions/hLunaaa__hLunaaa.github.io.md
  - wiki/sources/descriptions/gmh5225__Allocating-individual-pages.md
updated: 2026-08-15
confidence: high
---

# Kernel Pool Scanning

Anti-cheat and EDR techniques that walk kernel pool allocators to find hidden drivers, shellcode, and executable memory without a matching loaded module. Windows 10 19H1+ **Segment Heap** pool internals materially changed scanner design. (source: wiki/sources/skills/anti-cheat.md)

## Why Segment Heap matters

Cheat drivers often allocate in **NonPagedPool** for shellcode, hook tables, and manually mapped images. Segment Heap (19H1+) split allocation paths (kLFH, VS, Segment, Large), XOR-encoded headers via **HeapKey**, and isolated metadata. Scanners must decode chunk headers and traverse allocator structures or risk false positives. (source: wiki/sources/skills/anti-cheat.md)

## Scan targets

1. **BigPool / large allocations** — walk `nt!PoolBigPageTable`; flag large chunks with no corresponding `DRIVER_OBJECT` or loaded module (common manual-map driver footprint).
2. **VS allocator chunks** — traverse `_SEGMENT_HEAP → VsContext → SubsegmentList`; decode `_HEAP_VS_CHUNK_HEADER` with `real_sizes = encoded_header ^ chunk_address ^ HeapKey`; inspect PoolTag and executable content.
3. **kLFH buckets** — `_SEGMENT_HEAP → LfhContext → Buckets[]`; randomized block placement and LfhKey-encoded FreeHint complicate adjacency heuristics; size-bucket grooming patterns can still be anomalous.
4. **Suspicious PoolTag** — cross-reference tags against known-good databases (`pooltag.txt`); tags present in pool but absent from any loaded module are suspicious.
5. **Executable NonPagedPool** — X-permission chunks without a backing module; content scan for cheat signatures, ROP gadgets, syscall stubs.
6. **Heap integrity** — validate build-specific `_SEGMENT_HEAP` layout/signature; verify VS header encoding consistency; tampered metadata may indicate heap exploitation.

## Scanner prerequisites

- `nt!RtlpHpHeapGlobals` (HeapKey, LfhKey) — often via pattern scan
- `nt!ExpPoolQuotaCookie` — ProcessBilled decoding
- Per-pool-type `_SEGMENT_HEAP` instances via `nt!PoolVector`
- Allocation-path routing (size → kLFH / VS / Segment / Large)

## KDP integration

Detection rule tables can live in **Kernel Data Protection (KDP) Secure Pool** (`ExAllocatePool3` + KDP). Correctly configured KDP can protect selected pages from ordinary VTL0 writes—including kernel R/W primitives—while hypervisor and policy paths remain trustworthy. (source: wiki/sources/skills/anti-cheat.md)

## Driver load forensics

Complementary to pool walks, anti-cheat inspects kernel bookkeeping tables for hostile driver activity. (source: wiki/sources/skills/windows-kernel.md)

| Artifact | Role |
|----------|------|
| **PiDDBCacheTable** | Historical driver load hashes + timestamps; detects BYOVD or test-signed loads; attackers may try post-load entry removal |
| **MmUnloadedDrivers** | Circular buffer of recently unloaded drivers (name + address range); not user-clearable; flags load-unload-reload patterns |
| **PoolBigPageTable** | Maps large (≥ page) pool allocations to owning driver tag; finds manual-map memory without a loaded module |

Offensive **driver trace cleaning** research such as [[hlunaaa-github-io]] documents **CI.dll** and **BigPool cache** artifacts targeted when hiding manual-map / BYOVD loads from PiDDBCache and pool-walk scanners — the hide side of the same forensics table. (source: wiki/sources/descriptions/hLunaaa__hLunaaa.github.io.md)

**Pool tag forensics:** every `ExAllocatePoolWithTag` / `ExAllocatePool2` allocation carries a 4-byte tag — scan for known cheat-driver signatures via `pooltag.txt`, PoolMon, or WinDbg `!poolfind`. Tags present in pool but absent from any loaded module are suspicious.

## Legacy vs modern pool walks

Pre-19H1 linear traversal via inline `_POOL_HEADER.BlockSize` **no longer works** under Segment Heap — scanners must route by allocation path (kLFH / VS / Segment / Large) and decode XOR-encoded VS headers. (source: wiki/sources/skills/windows-kernel.md)

## Snapshot / diff forensics

Before/after **Big Pool snapshots** compared via driver-backed tooling such as [[kn-diff-pool]] (kernel capture + Go TUI diff) help isolate **new allocations** after a driver load, cheat attach, or suspected leak — complementary to one-shot PoolMon / WinDbg walks when triaging object leaks or manual-map footprints. (source: wiki/sources/descriptions/kernullist__kn-diff-pool.md)

## Interactive enumeration / dump

Tools such as [[pooldump]] scan kernel pool pages to list allocation blocks (tags, sizes, owning drivers) and dump specific pool contents — useful when recovering manually mapped images (e.g. EAC manual-map DLL extraction) or inspecting driver/rootkit pool artifacts without a full live debugger session. (source: wiki/sources/descriptions/ioncodes__pooldump.md)

## Non-pool allocation evasion

Offensive research such as [[allocating-individual-pages]] allocates isolated kernel pages via `MmAllocateIndependentPagesEx` and related non-standard paths to avoid pool-tag tracking and BigPool walks — a complementary hide technique to [[nullmap]] pool cleanup and [[revert-mapper]] post-map scrubbing. (source: wiki/sources/descriptions/gmh5225__Allocating-individual-pages.md)

## Related

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[etw-threat-intelligence]] · [[kernel-codecave-poc]] · [[revert-mapper]] · [[allocating-individual-pages]] · [[kn-diff-pool]] · [[pooldump]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
