# Supply-Chain Resource Selection

Load this guide to connect a repository entry to a release or content boundary.
Locations below match the local [README](../../../../README.md), checked on
2026-09-09. Follow [repository navigation](../../overview/references/repository-navigation.md)
for local discovery and source-currentness limits.

## Select by Stage

| README location and representative | Select when | Contract and common confusion | Expected review output |
|---|---|---|---|
| `Game CI`: [game-ci organization](https://github.com/game-ci) and `nikaera/Unity-GameCI-Sample` | Locating Unity workflow components and an integration example | The organization is an entry point, not one repository or a versioned action. Follow it to the relevant [Unity Builder documentation](https://game.ci/docs/github/builder/), then pin the actual action, editor, image, and project inputs. A sample workflow or successful build does not establish release authorization. | Build-input and authority map, resolved versions, artifact digest, secret/cache boundaries, and publication checks |
| `Game Tools`: [get-unity](https://github.com/neogeek/get-unity) | Identifying how a workflow resolves a Unity editor download | Upstream describes a download-URL locator for a selected version. URL selection and version discovery are separate from artifact authenticity and approved publisher/release policy. Review the resolved source and actual acquired artifact. | Requested/resolved editor version, source URL, installed artifact identity, verification evidence, and stale-resolution risk |
| `Game Hot Patch`: [xLua](https://github.com/Tencent/xLua) | Classifying a Lua/C# runtime or hot-patch dependency | xLua provides Lua integration and runtime replacement of C# logic. It also documents a signed-script loading example; do not infer that every integration enables it or that signature verification covers update freshness and channel authorization. Bind conclusions to the deployed loader and build configuration. | Script origin, loader and runtime versions, signing/authorization checks, exposed runtime capabilities, and compatibility/recovery owner |
| `Game Assets`: [glTF](https://github.com/KhronosGroup/glTF) and [TinyGLTF](https://github.com/syoyo/tinygltf) | Distinguishing the asset specification from a shipped parser and its dependencies | glTF is the format/specification family; TinyGLTF is an implementation. README currently labels TinyGLTF as C++11, while the upstream reviewed here identifies a v3 C runtime and legacy C++ code. Determine the actual shipped revision before applying language, I/O, or validation defaults. | Format/extensions, parser revision and build options, external-resource policy, decoder inventory, and processing budgets |

Linked author documents were reviewed on 2026-09-09. `Game CI` also lists
`EpicGames/lore`; this guide selects only the Unity-related entries for its CI
example. `game-ci/unity-builder` is an upstream follow-up from the organization
entry, not a separately claimed README listing. Upstream changes do not update
vendored copies automatically.

## Review the Transition

Choose the relevant transition: resolve a toolchain, build an artifact, authorize
a script update, or import an asset. Follow the [parent skill](../SKILL.md) for
provenance, signed metadata, freshness, publication policy, and recovery; a build
helper, runtime bridge, or parser is only one component of those decisions.

For artifact substitution, establish who can influence the selected input or
publication channel and inspect the downstream identity checks. For script abuse,
establish that the loader accepts the script and grants the relevant runtime
capability. For unsafe asset ingestion, establish that content reaches the
specific parser before reviewing path/resource policy, isolation, and limits.
These are review prerequisites, not claims that the listed projects are unsafe.

Use owned assets and existing build records to distinguish an integrity failure
from an unsupported format extension, parser-version mismatch, missing dependency,
or incompatible editor/runtime pair. Report authenticated origin, authorized
release, freshness, compatibility, and safe processing as separate conclusions.
