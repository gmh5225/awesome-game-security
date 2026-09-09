---
name: game-engine-resources
description: Analyze Unreal, Unity, Source, Godot, and custom engine trust boundaries and select matching repository resources. Use for engine/build identification, full source versus C# reference subsets, version-matched demos, editor versus shipped plugins, reflection and object lifecycles, Mono/IL2CPP, asset schemas, and replication ownership. Produce a versioned artifact and boundary map; route transport authority, release trust, and graphics measurements to their dedicated skills.
---

# Game Engine Development Resources

## Overview

This skill covers game engine development resources from the awesome-game-security collection, including both commercial (Unreal, Unity) and open-source engines.

When choosing resources from this repository, read the
[engine resource guide](references/repository-resources.md) for source subsets,
versioned demos, editor integration, and serialized-asset readers.

Engine globals, object layouts, metadata formats, and helper APIs vary by engine
branch, build configuration, platform, and game modifications. Verify the exact
version and binary artifacts; use
[`research-rigor`](../research-rigor/SKILL.md) before generalizing signatures or
offsets.

## Engine Trust Boundaries and Evidence

For tick/frame distinctions, prediction, replication ordering and replay
limitations, use [time and replay evidence](../game-server-security/references/time-ordering-and-replay.md).

Use [game-server-security](../game-server-security/SKILL.md) for authority,
sessions, inventory and purchases, and
[game-supply-chain-security](../game-supply-chain-security/SKILL.md) for build,
update and mod-distribution trust. For owned-build diagnostic reports, use
[robustness and triage](../research-rigor/references/robustness-and-triage.md).

Baseline the engine branch, game build/hash, platform/ABI, scripting backend,
stripping configuration, symbol availability, and plugin versions. Separate
reflected metadata, native/managed execution, serialized assets, plugins, and
client/server replication; each exposes a different research surface.

Describe attack scenarios by the boundary that must fail: untrusted content
accepted by an importer, a plugin granted in-process execution, or client
assertions accepted as authoritative game state. Correlate asset provenance,
plugin inventory, owned-build diagnostics, serialization checks, and server
validation evidence. Engine identification or object discovery alone does not
establish compromise.

- Unreal reflection covers annotated members; native-only members and object
  lifetime require separate evidence. A reflected schema is not a complete C++
  layout. [Epic Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/objects-in-unreal-engine)
- Unity IL2CPP involves managed assemblies, stripping, C++ generation, and native
  compilation. Reconstructed names or metadata do not guarantee complete type
  coverage or original-source recovery.
  [Unity IL2CPP](https://docs.unity3d.com/Manual/il2cpp-introduction.html)
- Extension compatibility is versioned: the Godot 4.4 manifest documents engine
  compatibility and platform/build/architecture selection. Verify the target
  release rather than projecting this example onto all versions.
  [Godot 4.4 GDExtension manifest](https://docs.godotengine.org/en/4.4/tutorials/scripting/gdextension/gdextension_file.html)
- Distinguish open-source engines, licensed engine source, SDK game code, and
  reference-source subsets. Source SDK 2013 has its own non-commercial license;
  repository visibility does not imply unrestricted reuse.
  [Valve Source SDK 2013](https://github.com/ValveSoftware/source-sdk-2013)

Report the affected boundary, prerequisite, artifact, observed result, benign
controls, and version-dependent limits. Sources above were reviewed on 2026-09-09.

## README Coverage

- `Game Engine > Guide`
- `Game Engine > Source`
- `Game Engine Plugins:Unreal`
- `Game Engine Plugins:Unity`
- `Game Engine Plugins:Godot`
- `Game Engine Plugins:Lumix`
- `Game Engine Detector`
- `Cheat > SDK CodeGen`
- `Cheat > Game Engine Explorer:Unreal`
- `Cheat > Game Engine Explorer:Unity`
- `Cheat > Game Engine Explorer:Source`
- `Anti Cheat > Game Engine Protection:Unreal`
- `Anti Cheat > Game Engine Protection:Unity`
- `Anti Cheat > Game Engine Protection:Source`
- `Game Develop > MCP server`

## Major Engine Categories

### Unreal Engine
- Official documentation and forums
- Source code access (requires Epic Games account)
- Community guides and tutorials
- Plugin development references

### Unity Engine
- C# reference source code
- Asset store resources
- Unity-specific design patterns
- VR/AR development guides

### Open Engines and Source-Available SDKs
- **Godot**: Free and open-source, supports GDScript and C#
- **Cocos2d-x**: Cross-platform 2D game framework
- **CRYENGINE**: High-fidelity graphics engine
- **Source SDK**: Valve game-code SDKs with version-specific license terms

### Custom/Educational Engines
- Hazel Engine (TheCherno's educational series)
- Bevy (Rust-based data-driven engine)
- Fyrox (Rust game engine)

## Key Technical Areas

### Rendering
- Software renderers for learning
- Ray tracing implementations
- Shader development tutorials
- Post-processing effects

### Mathematics
- Linear algebra libraries (GLM, DirectXMath)
- Physics simulation (PhysX, Bullet)
- Collision detection algorithms

### Networking
- Client-server architectures
- KCP reliable UDP protocol
- Steam networking integration
- MMORPG server implementations

## Resource Categories

### Documentation & Guides
```markdown
- Learning resources and tutorials
- Architecture documentation
- Best practices and style guides
```

### Source Code
```markdown
- Complete engine implementations
- Subsystem references (renderer, physics, audio)
- Plugin and extension examples
```

### Plugins & Extensions
```markdown
- ImGui integration for debug UIs
- Scripting language bindings (Lua, .NET)
- Editor tool plugins
```

## Engine Selection Criteria

When researching engines for security analysis or development:

1. **Target Platform**: PC, mobile, console compatibility
2. **Source Access**: Open source vs proprietary
3. **Language**: C++, C#, Rust, or scripting
4. **Graphics API**: DirectX, OpenGL, Vulkan, Metal
5. **Community**: Documentation and support quality

## SDK Generation Workflows

### Unreal Engine (Dumper-7)
```
1. Identify UE version from binary signatures
2. Inject Dumper-7 into running game process
3. SDK output: C++ headers with UObject hierarchy
4. Key structures: UObject, FName, UClass, UFunction, UProperty
5. Generated SDK enables: property access, function calls, blueprint hooks
6. Alternative tools: UnrealDumper, UE4SS (live scripting + SDK dump)
```

### Unity (IL2CPPDumper)
```
1. Locate global-metadata.dat + GameAssembly.dll (or libil2cpp.so)
2. Run IL2CPPDumper → outputs: dump.cs, il2cpp.h, script.json
3. Load generated headers into IDA/Ghidra for symbol recovery
4. Key structures: Il2CppClass, MethodInfo, FieldInfo, Il2CppType
5. For Mono builds: directly decompile Assembly-CSharp.dll with dnSpy
```

### Source Engine (NetVar Parsing)
```
1. Walk ClientClass linked list from CHLClient
2. For each class, enumerate RecvTable → RecvProp entries
3. Build offset map: class name → property name → offset
4. Example: CCSPlayer → m_iHealth → 0x100
5. Tools: hazedumper, source2gen (Source 2)
```

## Engine Object Models

### Unreal Engine
```
Core hierarchy:
  UObject → UField → UStruct → UClass
  UObject → AActor → APawn → ACharacter → APlayerCharacter

Key globals:
  GUObjectArray / GObjects: registered UObject slots; lifecycle and reachability
    filtering are still required
  GNames / FNamePool: name storage; symbol and structure names vary by UE version
  GWorld (UWorld*): current world context
  GEngine (UEngine*): engine singleton

Memory layout:
  Common UObject fields include VTable, flags, internal index, class, name, and
  outer pointers; order, packing, and presence are build-specific
  Reflected property offsets come from the version-specific class metadata
```

### Unity (IL2CPP)
```
Core structures:
  Il2CppDomain → Il2CppAssembly → Il2CppImage → Il2CppClass
  Il2CppClass: fields, methods, vtable, static_fields pointer

Key patterns:
  il2cpp_domain_get() → domain singleton
  il2cpp_class_from_name() → class lookup by namespace + name
  il2cpp_runtime_invoke() → call managed methods from native

Metadata:
  global-metadata.dat contains string pool, type definitions, method signatures
  Encrypted metadata in some protected games (requires custom decryptor)
```

### Source Engine
```
Core systems:
  Entity list: IClientEntityList → GetClientEntity(index)
  ConVar system: ICvar → FindVar("sv_cheats")
  NetVars: RecvTable hierarchy for network-replicated properties

Key interfaces (accessed via CreateInterface export):
  IVEngineClient, IClientEntityList, IEngineTrace
  ISurface, IPanel (for overlay rendering in Source)
```

## MCP Servers for Game Development

```
The README's > MCP server subcategory includes servers relevant
to game engine workflows:

- Unreal Engine MCP: AI agent controls UE editor (spawn actors, modify properties, blueprints)
- Unity MCP: AI agent interacts with Unity editor and C# scripting
- Godot MCP: AI agent controls Godot editor and GDScript

These complement the RE-focused MCP tools (see reverse-engineering skill)
by enabling AI-assisted game development and rapid prototyping.
```

## Security Research Focus

For game security research, understanding engine internals helps with:
- Memory layout and object structures
- Rendering pipeline hooks
- Network protocol analysis
- Anti-cheat integration points

---

## Repository Navigation

For repository selection, load the [engine resource guide](references/repository-resources.md)
on demand. Use shared [repository navigation](../overview/references/repository-navigation.md)
for local lookup, casing, missing snapshots, and current-source verification.
The [compiled engine overview](../../../wiki/overviews/game-engine.md) is a discovery
map; generated summaries are not independent evidence of capability or behavior.
