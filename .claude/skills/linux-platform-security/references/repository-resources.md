# Linux Platform Repository Resource Selection

Read this when selecting resources for native Linux, SteamOS/Steam Deck, Proton compatibility, or Linux forensic evidence. Repository categories overlap: find the exact labels below in the local [README](../../../../README.md) before assuming there is a dedicated Linux collection for every topic.

Local index and linked primary documentation reviewed: **2026-09-09**. These are defensive resource-selection guidelines, not compatibility guarantees for any game or distribution.

| Review question | Exact README location and representative source | Selection boundary and useful evidence |
|---|---|---|
| Is this game native or running through a compatibility stack? | `Cheat` → `Wine`: [Valve Proton](https://github.com/ValveSoftware/Proton) | Proton uses Wine to run Windows games on Linux. Select its release notes and component provenance for runtime questions; record the installed Proton version, game build, architecture and launch context. Establish a supported baseline before treating an unusual module or startup failure as suspicious. |
| Which Linux policy layer governs the operation? | `Cheat` → `Android Kernel Explorer`: [Linux kernel documentation](https://docs.kernel.org), including [LSM documentation](https://docs.kernel.org/admin-guide/LSM/index.html) | This generic Linux documentation link is indexed under Android. Select documentation matching the actual kernel for capabilities, namespaces, seccomp and LSM review; record active configuration and policy rather than importing defaults from the category name. `Cheat` → `Linux Kernel Explorer` is a separate tool-discovery category. |
| Does the issue specifically concern WSL? | `WSL`: [Microsoft WSL2-Linux-Kernel](https://github.com/microsoft/WSL2-Linux-Kernel) | The upstream repository contains WSL2 kernel source and configuration. Select it for a recorded WSL2 environment. A WSL result does not establish equivalent behavior on a native desktop distribution or SteamOS; record the host, guest kernel and configuration separately. |
| Can an existing Linux image support process or module findings? | `Anti Cheat` → `Information System & Forensics`: [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Select for authorized offline forensic analysis. Its [symbol documentation](https://volatility3.readthedocs.io/en/latest/symbol-tables.html) requires an exact Linux banner match, not just a matching release number. Preserve the image hash/provenance, matching symbol identity, plugin version, parsing errors and unavailable regions. |

## Avoid Misrouting

- Do not import Windows kernel structures or driver assumptions because the game executable is PE or uses Proton. Route Windows-native kernel findings to [windows-kernel](../../windows-kernel/SKILL.md), graphics translation/capture to [graphics-api](../../graphics-api/SKILL.md), and executable reconstruction to [reverse-engineering](../../reverse-engineering/SKILL.md).
- Android and WSL entries are useful discovery routes, not proof of the target's platform. Record the actual device/runtime before selecting a kernel branch or interpreting policy denials.
- `Some Tricks` → `Linux` is a miscellaneous index, not a deployment-hardening baseline. For rootkit or privileged-module reports, extract the claimed prerequisite and observable boundary without importing operational recipes.

## Deliver a Review Record

Return a stack map from game binary through compatibility components to the active kernel, plus a resource-selection table with exact README locator, upstream revision/date and applicability. Attach credential/namespace context, effective policy evidence and relevant diagnostics. Distinguish an unsupported runtime, a policy denial, missing visibility and a supported security finding; include a benign comparison and unresolved assumptions.

Use the shared [repository navigation](../../overview/references/repository-navigation.md) for local discovery layers, filename case, missing snapshots and currentness. Generated summaries are discovery aids, not evidence of installed software, effective policy or present support.
