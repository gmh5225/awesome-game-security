# Windows Kernel Repository Resource Selection

Read this when choosing repository resources for a Windows driver review, a build-specific internals question, or an existing crash/memory artifact. The locations below are literal labels in the local [README](../../../../README.md), including its spelling. These are selection criteria for defensive analysis, not endorsements of every neighboring project.

Local index and linked primary documentation reviewed: **2026-09-09**. Match the relevant release, architecture, OS build and evidence type before using a resource.

| Review question | Exact README location and representative source | Selection boundary and useful evidence |
|---|---|---|
| Did a type, symbol or syscall change between builds? | `Cheat` → `Windows Kernel Explorer`: [WinDiff](https://github.com/ergrelet/windiff) | Select for PE/PDB-derived comparisons. Record both binary versions, architecture and symbol identity. Database coverage can be incomplete; a missing result does not establish that a kernel feature is absent. A structural delta alone does not establish reachable vulnerable behavior. |
| Which events does a provider describe? | `Cheat` → `RE Tools`: [EtwExplorer](https://github.com/zodiacon/EtwExplorer) | Select for ETW provider metadata, event fields and schema review. Deliver provider/schema identity and the fields relevant to the hypothesis; separately document whether a collector enabled, received and retained those events. Metadata is not a live observation. |
| Can owned driver logic be reviewed with unit-level evidence? | `Anti Cheat` → `Driver Unit Test Framework`: [WDUTF](https://github.com/wpdk/wdutf) | It provides a user-space environment with partially stubbed kernel functionality. Record the framework revision, supported architecture/toolchain and substituted APIs. A passing unit result cannot establish real IRQL, device, concurrency or complete KMDF behavior. |
| What can an already supplied dump support? | `Anti Cheat` → `Winows Kernel Dump Analysis`: [kdmp-parser](https://github.com/0vercl0k/kdmp-parser); `Anti Cheat` → `Information System & Forensics`: [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Distinguish parsing from OS-aware reconstruction. kdmp-parser documents 64-bit Windows kernel dump support; check the exact format against the chosen revision. Preserve image provenance, missing regions, parser/plugin versions and symbol identity. [Volatility symbol documentation](https://volatility3.readthedocs.io/en/latest/symbol-tables.html) explains Windows PDB matching. |

## Avoid Misrouting

- `Driver Signature enforcement`, `PatchGuard-related` and callback listings identify different trust boundaries. A project in one category does not establish current applicability to another. Describe access prerequisites, affected versions and observable artifacts without importing bypass recipes.
- A valid signature, a driver filename or an old generated description is not a present-day safety verdict. Use the platform-policy sources in the parent skill and observed host state when assessing a particular driver.
- Route physical bus initiators to [DMA analysis](../../dma-attack/SKILL.md); keep host-driver acquisition and IOCTL authorization here. Route game binary semantics to [reverse engineering](../../reverse-engineering/SKILL.md).

## Deliver a Review Record

For each chosen resource, include its exact README locator, upstream URL and revision/date, the reason it answers the question, build/architecture constraints, and the evidence actually inspected. Produce a small claim-to-artifact table: caller privilege and reachable boundary, relevant driver/hash or symbol/schema identity, observation, benign alternative, mitigation scope, and unresolved coverage. Keep untested hypotheses separate from findings.

Use the shared [repository navigation](../../overview/references/repository-navigation.md) for local discovery layers, filename case, missing snapshots and currentness. Generated wiki and descriptions help locate sources; they do not independently corroborate a claim.
