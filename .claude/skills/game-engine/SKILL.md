---
name: game-engine-resources
description: Guide for game-engine internals, source trees, plugins, and engine-specific security research. Use this skill when researching Unreal, Unity, Source, Godot, custom engines, engine detectors, engine explorers, or engine protection patterns relevant to modding, reverse engineering, and anti-cheat.
---

# Game Engine Development Resources

## Overview

This skill covers game engine development resources from the awesome-game-security collection, including both commercial (Unreal, Unity) and open-source engines.

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

### Open Source Engines
- **Godot**: Free and open-source, supports GDScript and C#
- **Cocos2d-x**: Cross-platform 2D game framework
- **CRYENGINE**: High-fidelity graphics engine
- **Source Engine**: Valve's game engine (various versions)

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
  GObjects (TUObjectArray): all live UObject instances
  GNames (TNameEntryArray): FName string pool
  GWorld (UWorld*): current world context
  GEngine (UEngine*): engine singleton

Memory layout:
  UObject header: VTable, ObjectFlags, InternalIndex, ClassPrivate, NamePrivate, OuterPrivate
  Properties follow at offsets defined in UClass::PropertySize
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

## Data Source

**Important**: This skill provides conceptual guidance and overview information. For detailed information use the following sources:

### 1. Project Overview & Resource Index

Fetch the main README for the full curated list of repositories, tools, and descriptions:

```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md
```

The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.

### 2. Repository Code Details (Archive)

For detailed repository information (file structure, source code, implementation details), the project maintains a local archive. If a repository has been archived, **always prefer fetching from the archive** over cloning or browsing GitHub directly.

**Archive URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/ufrisk/pcileech.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/000-aki-000/GameDebugMenu.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the archive URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name (no `.git` suffix).
3. Fetch the archive file — it contains a full code snapshot with file trees and source code generated by `code2prompt`.
4. If the fetch returns a 404, the repository has not been archived yet; fall back to the README or direct GitHub browsing.

### 3. Repository Descriptions

For a concise English summary of what a repository does, the project maintains auto-generated description files.

**Description URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/00christian00/UnityDecompiled/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/ufrisk/pcileech/description_en.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the description URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name.
3. Fetch the description file — it contains a short, human-readable summary of the repository's purpose and contents.
4. If the fetch returns a 404, the description has not been generated yet; fall back to the README entry or the archive.

**Priority order when answering questions about a specific repository:**
1. Description (quick summary) — fetch first for concise context
2. Archive (full code snapshot) — fetch when deeper implementation details are needed
3. README entry — fallback when neither description nor archive is available
