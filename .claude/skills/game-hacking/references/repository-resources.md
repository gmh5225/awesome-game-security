# Repository Resources for Game Threat Models

Repository categories and linked primary documentation reviewed: 2026-09-09.
Use this guide to select source, capture and baseline evidence for an attack-surface
question. These resources support comparison and defensive interpretation; their
presence in the index does not certify any game's security or a detector's accuracy.

## Select Evidence for the Claimed Capability

The following are literal categories in the local [README](../../../../README.md).
They provide useful controls for interpreting the memory, rendering, input and
network threat classes described in this skill.

| Question and README location | Representative | Choice, boundary and expected output |
|---|---|---|
| Where does an owned engine build create and consume state? `Game Engine > Source` | [godotengine/godot](https://github.com/godotengine/godot) | Start with a matching source/build context for lifecycle and ownership analysis. Produce a component/state map with the client/server authority assumptions identified. An open engine's source does not establish the behavior of a different engine or a particular shipped game. |
| What did an authorized packet capture retain? `Cheat > Packet Capture&Parse` | [seladb/PcapPlusPlus](https://github.com/seladb/PcapPlusPlus) | Its documented PCAP/PCAPNG reading and protocol parsing can support offline capture review. Return capture provenance, retained fields, ordering and missing-data limits. Parsed transport fields do not establish plaintext game state, server acceptance, human intent, or an enforcement decision. |
| Could a measured symptom come from rendering performance? `Game Testing` | [GameTechDev/PresentMon](https://github.com/GameTechDev/PresentMon) | The project captures and analyzes Windows graphics performance. Choose comparable builds, graphics paths and workloads for a performance baseline. Return metric definitions, capture interval and relevant variability; frame timing is not a memory-access or cheating verdict. |
| What does a legitimate development UI explain? `Cheat > UI Interface` | [ocornut/imgui_club](https://github.com/ocornut/imgui_club) | The author's extensions include a hexadecimal memory-editor widget with a read-only mode. Use an owned diagnostic UI or supplied buffer view as a benign control. Record buffer provenance and visible state; a UI widget does not establish how data was obtained or the purpose of another process using similar UI code. |

## Keep Threat Taxonomy Separate from Implementation Selection

The README's `Cheat > RPM`, `DMA`, `W2S`, `Overlay`, `Driver Communication`,
`Triggerbot & Aimbot` and `HWID` labels are useful discovery terms for classifying
claims. Describe the desired information or action, required access, trust
boundary, observation point and benign alternative. Category placement, a device
name, or an “external” label does not demonstrate that capability on a target.

For memory-source versus USB/network transport distinctions, use
[dma-attack](../../dma-attack/SKILL.md). For input coordinate spaces and uploaded
telemetry, use [input provenance](../../anti-cheat/references/input-provenance-and-measurement.md).
For replication and action acceptance, use
[game-server-security](../../game-server-security/SKILL.md). Binary reconstruction
belongs to [reverse-engineering](../../reverse-engineering/SKILL.md), and protection
or restriction claims to [anti-cheat](../../anti-cheat/SKILL.md).

An overlay, a capture, a driver, and a remote processor answer different questions.
Use the matching evidence family before associating them with one architecture.
Resource discovery should not produce an injection, input-automation, evasion or
restriction-circumvention workflow.

## Deliver a Capability and Evidence Map

For each hypothesis record: capability sought; necessary privilege/interface;
data source; transport and processing location; observable artifacts; matched
legitimate controls; source/build identity; and the remaining uncertainty.
Distinguish source-inspected behavior, captured observations, and assumptions.
Report the supported defensive conclusion and the evidence needed to resolve gaps.

Use [shared repository navigation](../../overview/references/repository-navigation.md)
for local discovery and current upstream checks. Generated descriptions and wiki
overviews provide leads rather than independent proof of project capabilities.
