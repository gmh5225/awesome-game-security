# Repository Resources for Binary Evidence

Repository categories and linked primary documentation reviewed: 2026-09-09.
Use this guide when choosing analysis resources for a supplied binary, dump,
trace, or pair of builds. The selection criteria and evidence requirements below
are a research framework, not performance claims about the tools.

## Locate and Choose a Resource Family

In the local [README](../../../../README.md#cheat), subsection names below are
literal blockquote labels under the indicated heading. Search the label together
with the owner/repository; a category alone includes tools with different scopes.

| Question and README location | Representative or resource family | Selection boundary and expected evidence |
|---|---|---|
| What does this binary appear to do? `Cheat > Decompiler` | Ghidra family; the index includes `gmh5225/ghidra` | Establish the exact fork/version and supported architecture. Produce addresses, annotated instructions, type hypotheses and unresolved control flow; pseudocode is an interpretation of the binary. See the [upstream Ghidra guide](https://ghidra.re/ghidra_docs/GhidraClass/Beginner/Introduction_to_Ghidra_Student_Guide.html). |
| What happened during a bounded user-mode observation? `Cheat > Debugging` | [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) | The author describes a Windows user-mode debugger. Match executable architecture and record the observed interval, modules and debugger-induced conditions. A user-mode trace does not establish kernel or whole-system coverage. |
| What changed between two supplied builds? `Cheat > Ghidra Plugins` | [clearbluejar/ghidriff](https://github.com/clearbluejar/ghidriff) | Use binary-diff reports to organize changed functions and review their semantics. Keep both binary hashes and analysis settings; symbol, compiler and layout differences can change matching. A match or changed function is not a demonstrated security defect. |
| What can an existing dump support? `Anti Cheat > Winows User Dump Analysis` and `Winows Kernel Dump Analysis` | [0vercl0k/udmp-parser](https://github.com/0vercl0k/udmp-parser), [0vercl0k/kdmp-parser](https://github.com/0vercl0k/kdmp-parser) | Choose a user-minidump or kernel-dump parser after checking the actual dump format. Return decoded metadata and retained memory/context with absent ranges identified. Parsing a dump does not acquire memory or recreate omitted execution history. |

The two `Winows` labels preserve the README's spelling. Treat the indexed Ghidra
fork and upstream documentation as distinct provenance; confirm their relationship
for the selected revision before transferring a capability claim.

## Route by the Finding, Not the Tool Name

Use [windows-kernel](../../windows-kernel/SKILL.md) for documented driver/IRQL and
callback contracts, [game-engine](../../game-engine/SKILL.md) for engine build and
object-model context, and [linux-platform-security](../../linux-platform-security/SKILL.md)
for native Linux versus Proton interpretation. Detection quality and enforcement
belong to [anti-cheat](../../anti-cheat/SKILL.md).

The `RE Tools` and plugin categories mix inspection utilities with tools that
modify or execute targets. A wrapper, MCP interface, or generated summary does
not establish safe observation, accuracy, or authorization for those actions.
For defensive attack analysis, record the affected interface, necessary privilege,
observable behavior and counterevidence without turning tool selection into an
exploitation or concealment sequence.

## Deliver a Reviewable Evidence Note

Include the repository/category selected, why it fits the artifact, exact input
hashes and tool revision, file/RVA/runtime address convention, symbols and settings,
direct observations, inferred semantics, missing coverage, and the narrow
defensive conclusion. Corroborate consequential pseudocode or diff findings with
the relevant instructions or available execution evidence.

Use [shared repository navigation](../../overview/references/repository-navigation.md)
for discovery, snapshot availability and current upstream verification. Compiled
wiki and generated descriptions help find candidates; they are not independent
corroboration of the source they summarize.
