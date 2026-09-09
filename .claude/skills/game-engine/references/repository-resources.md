# Engine Resource Selection

Load this guide when selecting an engine resource for a concrete review. The
paths below are categories in the local [README](../../../../README.md), checked
on 2026-09-09. For local discovery layers and snapshot limits, use
[repository navigation](../../overview/references/repository-navigation.md).

## Select by Artifact and Question

| README location and representative | Select when | Contract and common confusion | Expected review output |
|---|---|---|---|
| `Game Engine > Source`: [UnityCsReference](https://github.com/Unity-Technologies/UnityCsReference) | Checking documented C# engine/editor behavior against an identified Unity build | This is C# reference source, not the complete native engine or the game's original source. Match the repository's stated Unity version and branch; reference layouts can change. | Source-subset map, exact build/backend, supported claim, and missing native or game-specific evidence |
| `Game Develop > Source`: [Godot demo projects](https://github.com/godotengine/godot-demo-projects) | Selecting a small, owned baseline to understand an engine feature or diagnose a version difference | These are demo projects, separate from `Game Engine > Source` engine implementations. Upstream master targets development engine builds; stable demo branches target stable releases. | Demo revision and engine-version pair, expected behavior, observation, and target differences |
| `Game Engine > Game Engine Plugins:Unreal`: [RiderSourceCodeAccess](https://github.com/JetBrains/RiderSourceCodeAccess) | Classifying an editor integration in a plugin or build inventory | It provides Unreal Editor integration for choosing Rider as the source editor. Its presence in project sources does not establish that it ships or executes in the player build. Check plugin/module descriptors and the produced artifact. | Editor/build/runtime role ledger, declared compatibility, actual packaged modules, and required privileges |
| `Game Assets`: [UAssetAPI](https://github.com/atenfyr/UAssetAPI) | Interpreting owned serialized Unreal assets or explaining a reader mismatch | A low-level asset library is distinct from a UI, live object reflection, and the engine's native memory layout. Reader coverage depends on asset/engine version and schema information; parse failure alone is not corruption. | Asset provenance, reader revision, format/version and mapping assumptions, supported fields, and unresolved parse evidence |

Each linked upstream supports the stated resource role; capability documentation
was reviewed on 2026-09-09. These are selection examples, not endorsements of
every repository grouped under the same category.

## Apply the Boundary

First identify whether the disputed object is source, generated metadata,
serialized data, an editor extension, or a shipped module. Select one matching
resource above and record the exact revision and artifact it explains. A benign
version mismatch, unavailable symbols, cooked data, or an editor-only component
can explain an apparent discrepancy without an attack.

For an untrusted-asset scenario, establish that the artifact reaches an importer
before reviewing schema checks, external-resource access, and processing budgets.
For a plugin execution scenario, establish that the plugin is packaged and
loaded with the relevant permissions before assessing provenance and isolation.
Do not infer a compromised build from engine identification or a reader's output.

Use [game-server-security](../../game-server-security/SKILL.md) for decisions
about authoritative state and transport identity;
[game-supply-chain-security](../../game-supply-chain-security/SKILL.md) for
plugin publication, asset delivery, and update trust; and
[graphics-api](../../graphics-api/SKILL.md) for rendering observations. Keep the
final artifact map separate from any security finding or attribution.
