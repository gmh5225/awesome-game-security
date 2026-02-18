
# [`awesome-game-security`](https://gs.awesome.rip)[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![image](https://github.com/gmh5225/awesome-game-security/assets/13917777/a39c6322-40ed-45b5-afcb-93e8d5477a0b)
[![image](awesome-image.webp)](https://opensea.io/assets/ethereum/0x1c5ffb607ef75158b435bd21a898d848620b4b13/1)
```
If you find that some links are not working, you can simply replace the username with gmh5225. 
Or you can send an issue for me.
```
> Show respect to all the projects below, perfect works of art :saluting_face:

## How to contribute?
- https://github.com/HyunCafe/contribute-practice
- https://docs.github.com/en/get-started/quickstart/contributing-to-projects

## Skills for AI Coding Assistants
This repository provides skills that can be used with AI coding assistants like [Cursor](https://www.cursor.com/), [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex CLI](https://github.com/openai/codex), and other compatible tools. Install skills to get specialized knowledge about game security topics.

**Installation:**
```bash
npx skills add https://github.com/gmh5225/awesome-game-security --skill <skill-name>
```

**Available Skills:**
| Skill | Description |
|-------|-------------|
| `anti-cheat-systems` | Anti-cheat development and bypass techniques |
| `dma-attack-techniques` | DMA/PCIe-based attack methods |
| `game-engine-resources` | Game engine internals and modding |
| `game-hacking-techniques` | General game hacking methods |
| `graphics-api-hooking` | DirectX/OpenGL/Vulkan hooking |
| `mobile-security` | Android/iOS game security |
| `awesome-game-security-overview` | Overview of this repository |
| `reverse-engineering-tools` | RE tools and techniques |
| `windows-kernel-security` | Windows kernel exploitation |

**Example:**
```bash
# Install anti-cheat systems skill
npx skills add https://github.com/gmh5225/awesome-game-security --skill anti-cheat-systems

# Install multiple skills
npx skills add https://github.com/gmh5225/awesome-game-security --skill windows-kernel-security
npx skills add https://github.com/gmh5225/awesome-game-security --skill reverse-engineering-tools
```

## Contents
- [Game Engine](#game-engine)
- [Mathematics](#mathematics)
- [Renderer](#renderer)
- [3D Graphics](#3d-graphics)
- [AI](#ai)
- [Image Codec](#image-codec)
- [Wavefront Obj](#wavefront-obj)
- [Task Scheduler](#task-scheduler)
- [Game Network](#game-network)
- [PhysX SDK](#physx-sdk)
- [Game Develop](#game-develop)
- [Game Assets](#game-assets)
- [Game Hot Patch](#game-hot-patch)
- [Game Testing](#game-testing)
- [Game Tools](#game-tools)
- [Game Manager](#game-manager)
- [Game CI](#game-ci)
- [DirectX](#directx)
- [OpenGL](#opengl)
- [Vulkan](#vulkan)
- [Cheat](#cheat)
- [Anti Cheat](#anti-cheat)
- [Some Tricks](#some-tricks)
- [Windows Security Features](#windows-security-features)
- [WSL](#wsl)
- [WSA](#wsa)
- [Windows Emulator](#windows-emulator)
- [Linux Emulator](#linux-emulator)
- [Android Emulator](#android-emulator)
- [IOS Emulator](#ios-emulator)
- [Game Boy](#game-boy)
- [Nintendo Switch](#nintendo-switch)
- [Xbox](#Xbox)

## Game Engine
> Guide
- https://github.com/QianMo/Game-Programmer-Study-Notes
- https://github.com/raysan5/custom_game_engines [A comprehensive list of custom game engines]
- https://github.com/stevinz/awesome-game-engine-dev [Awesome Game Engine Development]
- https://github.com/Gforcex/OpenGraphic [Graphic Engine & Game Engine lists]
- https://github.com/bobeff/open-source-engines [A list of open source game engines]
- https://github.com/ThisisGame/cpp-game-engine-book
- https://github.com/netwarm007/GameEngineFromScratch
- https://forums.unrealengine.com [Unreal]
- https://docs.unrealengine.com [Unreal]
- https://www.unrealengine.com/resources [Unreal]
- https://github.com/donaldwuid/unreal_source_explained [Unreal]
- https://github.com/mikeroyal/Unreal-Engine-Guide [Unreal]
- https://github.com/Allar/ue5-style-guide [Unreal]
- https://github.com/revan1611/UE-Interview-Cheat-Sheet [Unreal]
- https://github.com/tomlooman/ue4-tutorials [Unreal]
- https://github.com/JaredP94/Unreal-Development-Guides-and-Tips [Unreal]
- https://github.com/lettier/3d-game-shaders-for-beginners [Shader]
- https://github.com/PardCode/OpenGL-3D-Game-Tutorial-Series [OpenGL]
- https://github.com/PardCode/CPP-3D-Game-Tutorial-Series [DirectX]
- https://github.com/ssloy/tinyrenderer [Render]
- https://github.com/crazyshader/GameDev [Unity]
- https://github.com/RyanNielson/awesome-unity [Unity]
- https://github.com/shadirvan/Unity-Cheat-Sheet [Unity]
- https://github.com/QianMo/Unity-Design-Pattern [Unity Design]
- https://github.com/whx-prog/The-Seed-Link-Future [Unity VR]
- https://github.com/twohyjr/Metal-Game-Engine-Tutorial [Apple's Metal Api]

> Source
- https://github.com/EpicGames/UnrealEngine
- https://github.com/Unity-Technologies/UnityCsReference [C# reference]
- https://github.com/cocos2d/cocos2d-x
- https://github.com/cocos/cocos-engine
- https://github.com/cocos/cocos4
- https://github.com/gmh5225/GameEngine-CRYENGINE
- https://github.com/panda3d/panda3d
- https://github.com/ValveSoftware/source-sdk-2013
- https://github.com/gmh5225/source-sdk-orangebox
- https://github.com/UTINKA/source-engine.2003
- https://github.com/ArcherTannic/SourceEngine2007
- https://github.com/nillerusr/source-engine
- https://github.com/gmh5225/GoldSourceRebuild [GoldSource engine rebuild]
- https://github.com/adriengivry/Overload
- https://github.com/gmh5225/GameEngine-MapleEngine
- https://github.com/inanevin/LinaEngine
- https://github.com/storm-devs/storm-engine
- https://github.com/minetest/minetest
- https://github.com/godotengine/godot
- https://github.com/ScriptedSnark/reGS
- https://github.com/nem0/LumixEngine
- https://github.com/urho3d/Urho3D
- https://github.com/KorokEngine/Korok [Golang]
- https://github.com/BoomingTech/Pilot
- https://github.com/Sirkles/JoshoEngine-Native
- https://github.com/ExplosionEngine/Explosion
- https://github.com/danhuynh0803/Campfire
- https://github.com/lowenware/dotrix [Rust]
- https://github.com/bevyengine/bevy [Rust]
- https://github.com/FyroxEngine/Fyrox [Rust]
- https://github.com/AmbientRun/Ambient [Rust]
- https://github.com/not-fl3/macroquad [Rust 2D]
- https://github.com/AbyssEngine/AbyssEngine [ARPG]
- https://github.com/skylicht-lab/skylicht-engine
- https://github.com/ValveSoftware/halflife [Half-Life 1]
- https://github.com/SamVanheer/halflife-unified-sdk [Half-Life SDK]
- https://github.com/alliedmodders/hl2sdk [Half-Life SDK]
- https://github.com/ezhangle/hlmaster [Half-Life Master Server]
- https://github.com/MonoGame/MonoGame [.NET]
- https://github.com/vchelaru/FlatRedBall [.NET 2D]
- https://github.com/nCine/nCine [2D]
- https://github.com/gameplay3d/gameplay [2D/3D]
- https://github.com/NoelFB/blah [C++ 2D]
- https://github.com/Squalr/Squally [C++ 2D]
- https://github.com/u3d-community/U3D [C++ 2D/3D]
- https://github.com/turbulenz/turbulenz_engine [HTML5]
- https://github.com/melonjs/melonJS [HTML5]
- https://github.com/egret-labs/egret-core [HTML5]
- https://github.com/pixijs/pixijs [HTML5]
- https://github.com/playcanvas/engine [HTML5 3D]
- https://github.com/TorqueGameEngines/Torque2D [2D]
- https://github.com/TorqueGameEngines/Torque3D [3D]
- https://github.com/gmh5225/GameEngine-CX3D [3D]
- https://github.com/solenum/exengine [C99 3D]
- https://github.com/TheCherno/Hazel
- https://github.com/duddel/yourgamelib
- https://github.com/Serious-Engine/Base
- https://github.com/benanil/Castle-Engine [DX11]
- https://github.com/OpenArena/engine [quake3]
- https://github.com/rbfx/rbfx [C# support and WYSIWYG editor]
- https://github.com/BobbyAnguelov/Esoterica
- https://github.com/ZDoom/gzdoom [Doom]
- https://github.com/L-Spiro/L.-Spiro-Engine-2022
- https://github.com/MohitSethi99/ArcEngine
- https://github.com/gscept/nebula
- https://github.com/irisengine/iris [cross-platform C++]
- https://github.com/WistfulHopes/NightSkyEngine [A fighting game engine written in Unreal Engine 5]
- https://github.com/ObEngine/ObEngine [2D+Lua]
- https://github.com/harukumo/HorizonEngine [3D rendering engine]
- https://github.com/benjinx/Toon [C++]
- https://github.com/chrismaltby/gb-studio [GameBoy]
- https://github.com/orx/orx [C++]
- https://github.com/volcoma/EtherealEngine [C++]
- https://github.com/clibequilibrium/EquilibriumEngine [C++] 
- https://github.com/turanszkij/WickedEngine [C++ 3D]
- https://github.com/AustinBrunkhorst/Ursine3D [C++ 3D]
- https://github.com/RavEngine/RavEngine [C++ 3D]
- https://github.com/asc-community/MxEngine [C++ 3D]
- https://github.com/jmorton06/Lumos [C++ 2D/3D]
- https://github.com/fredakilla/GPlayEngine [C++ 2D/3D]
- https://github.com/crownengine/crown [C++ 2D/3D]
- https://github.com/FlaxEngine/FlaxEngine [C++/C# 3D]
- https://github.com/stride3d/stride [C# 3D]
- https://github.com/Net5F/AmalgamEngine
- https://github.com/rxi/kit [pixels]
- https://github.com/isadorasophia/murder [pixel]
- https://github.com/nitaigao/engine-showcase [Old engine]
- https://github.com/PanosK92/SpartanEngine [Research-focused game engine designed for real-time solutions]
- https://github.com/OpenXRay/xray-16 [Improved version of the X-Ray Engine]
- https://github.com/love2d/love [2D game framework for Lua]
- https://github.com/PixelGuys/Cubyz [3D voxel sandbox game written by Zig language]


> Game Engine Plugins:Unreal
- [Plugin for UE4 to user Rider for Unreal Engine as code editor](https://github.com/JetBrains/RiderSourceCodeAccess)
- [Design-agnostic node system for scripting game’s flow in Unreal Engine](https://github.com/MothCocoon/FlowGraph)
- [Sample Unreal Engine 5.0.1 C++ Project That Incorporates Dear ImGui](https://github.com/stungeye/UE5-With-Dear-ImGui)
- [A set of tools and utilities for use with Unreal Engine projects using ImGui](https://github.com/nakdeyes/UnrealImGuiTools)
- [A simple Unreal Engine subsystem to provide a more accurate server world time to clients](https://github.com/Erlite/NetworkTimeSync)
- [UE4 UI Texture Validator Plugin](https://github.com/benui-dev/UE-BUIValidator)
- [Unreal Engine .NET 6 integration](https://github.com/nxrighthere/UnrealCLR)
- [Houdini Engine Plugin for Unreal Engine](https://github.com/sideeffects/HoudiniEngineForUnreal)
- [A small tutorial repository on capturing images with semantic annotation from UnrealEngine to disk](https://github.com/TimmHess/UnrealImageCapture)
- [UE4 plugin for live2d model](https://github.com/Arisego/UnrealLive2D)
- [An Unreal Engine code plugin that adds a custom asset type and editor to the engine](https://github.com/JanKXSKI/AssetTutorialPlugin)
- [Unreal Engine 4 Plugin for Lua APIs implementation](https://github.com/rdeioris/LuaMachine)
- [Debug Menu for UnrealEngine4](https://github.com/000-aki-000/GameDebugMenu)
- ['Dear Imgui' remote access library and application](https://github.com/sammyfreg/netImgui)
- [Customizable performance metric charts and STAT commands control panel](https://github.com/DarknessFX/DFoundryFX)
- [Unreal Engine plugin providing a set of Hermes endpoints](https://github.com/cdpred/RedTalaria)
- [Unreal Engine 4 Plugin for Lua APIs implementation](https://github.com/rdeioris/LuaMachine)
- [Copies the argument string to the clipboard and outputs the characters copied to the clipboard](https://github.com/aoharudesu/Clipboard_Tools-UE4)
- [Generic graph data structure plugin for ue4](https://github.com/jinyuliao/GenericGraph)
- [A quick implementation of modular game features for the 'BTS' test](https://github.com/BrUnOXaVIeRLeiTE/BT_ModularGameFeatures)

> Game Engine Plugins:Unity
- [A markdown viewer for unity](https://github.com/gwaredd/UnityMarkdownViewer)
- [An integrated solution for authoring / importing / simulating / rendering strand-based hair in Unity](https://github.com/Unity-Technologies/com.unity.demoteam.hair)
- [A maintained collection of useful & free unity scripts / library's / plugins and extensions](https://github.com/michidk/Unity-Script-Collection)
- [ChatGPT integration with Unity Editor](https://github.com/keijiro/AICommand)
- [Code editor integration for supporting Cursor as code editor for unity](https://github.com/boxqkrtm/com.unity.ide.cursor)

> Game Engine Plugins:Godot
- https://github.com/libriscv/godot-sandbox [Sandboxing that enables safe modding for Godot games]
- https://github.com/gtibo/Godot-Plush-Character [3D Plush Character for Godot 4.x]

> Game Engine Plugins:Lumix
- https://github.com/nem0/lumixengine_maps [Map downloader]


> Game Engine Detector
- https://github.com/walzer/game-engine-detector [Mobile Game]


## Mathematics
- https://github.com/nfrechette/rtm
- https://github.com/Groovounet/glm
- https://github.com/microsoft/DirectXMath
- https://github.com/Kazade/kazmath
- https://github.com/milakov/int_fastdiv
- https://github.com/freemint/fdlibm
- https://github.com/Jaysmito101/cgl

## Renderer
- https://github.com/bkaradzic/bgfx [Rendering library]
- https://github.com/DiligentGraphics/DiligentEngine [Rendering library]
- https://github.com/kanition/pbrtbook [Physically Based Rendering: From Theory To Implementation]
- https://github.com/keith2018/SoftGLRender
- https://github.com/DQLin/VolumetricReSTIRRelease
- https://github.com/HackerPoet/NonEuclidean
- [A graphics engine designed to run on a single thread on CPU](https://github.com/FHowington/CPUEngine) 
- https://github.com/paroj/gltut [OpenGL Render]
- https://github.com/ashawkey/raytracing [RayTracer]
- https://github.com/sultim-t/xash-rt [Xash3D FWGS with a real-time path tracing]
- https://github.com/crosire/reshade [A generic post-processing injector for games and video software]
- https://github.com/harukumo/HorizonEngine [3D rendering engine]
- https://github.com/Patryk27/strolle [Real-time rendering engine]
- https://github.com/ssloy/tinyraytracer [A brief computer graphics / rendering course]
- https://github.com/freetype/freetype [Render fonts]
- https://github.com/MethanePowered/MethaneKit [DirectX 12, Metal & Vulkan]
- https://github.com/EmbarkStudios/kajiya [Experimental real-time global illumination renderer]

## 3D Graphics
- https://github.com/Mesa3D/mesa
- https://github.com/MethanePowered/MethaneKit [DirectX 12, Metal & Vulkan]
- https://github.com/mrdoob/three.js [JavaScript 3D Library]

## AI
- https://github.com/ls361664056/GameAI-paper-list [zh]

## Image Codec
- https://github.com/nothings/stb
- https://github.com/libjpeg-turbo/libjpeg-turbo
- https://github.com/erkkah/tigr
- https://github.com/tsoding/olive.c

## Wavefront Obj
- https://github.com/tinyobjloader/tinyobjloader
- https://github.com/Twinklebear/tobj [Rust]

## Task Scheduler
- https://github.com/SergeyMakeev/TaskScheduler

## Game Network
> Guide
- https://github.com/MFatihMAR/Game-Networking-Resources
- https://partner.steamgames.com/doc/api/ISteamNetworkingMessages#functions_sendrecv [Steam]
- https://github.com/mcxiaoke/mqtt [mqtt]

> Source
- https://github.com/cloudwu/skynet
- https://github.com/ketoo/NoahGameFrame [Server Engine]
- https://github.com/chronoxor/CppServer
- https://github.com/Qihoo360/evpp
- https://github.com/ValveSoftware/GameNetworkingSockets [Steam]
- https://github.com/skywind3000/kcp [KCP]
- https://github.com/Unit-X/kcp-cpp [KCP]
- https://github.com/TLeonardUK/ds3os [Dark Souls 3]
- https://github.com/TLeonardUK/ds2os [Dark Souls 2]
- https://github.com/rathena/rathena [MMORPG]
- https://github.com/TrinityCore/TrinityCore [Server for WOW]
- https://github.com/uNetworking/uWebSockets [WebSockets]
- https://github.com/socketio/socket.io [Nodejs]
- https://github.com/mqttjs/MQTT.js [mqtt nodejs]
- https://github.com/eclipse/paho.mqtt.cpp [mqtt cpp]
- https://github.com/topfreegames/pitaya [Server framework]
- https://github.com/azerothcore/azerothcore-wotlk [Server for WOW]
- https://github.com/arlyon/azerust [Rust Server for WOW]
- https://github.com/arlyon/awesome-wow-rust [Rust Server for WOW]
- https://github.com/2601677867/One-Click-Run_Source_Server [Server for Source Engine]

## PhysX SDK
- https://github.com/NVIDIAGameWorks/PhysX
- https://github.com/NVIDIAGameWorks/PhysX-3.4
- https://github.com/bulletphysics/bullet3


## Game Develop
> Guide
- https://github.com/Calinou/awesome-gamedev
- https://github.com/notpresident35/learn-awesome-gamedev
- https://github.com/yrgo/awesome-educational-games
- https://github.com/bobeff/open-source-games [A list of open source games]
- https://github.com/michelpereira/awesome-open-source-games [Collection of Games]
- https://github.com/raizam/gamedev_libraries [A collection of open source c/c++ libraries for gamedev]
- https://github.com/gheja/game-design-documents [Game design documents]
- https://github.com/Kavex/GameDev-Resources [Game Development resources]
- https://github.com/crazyshader/GameDev [Unity]
- https://github.com/RyanNielson/awesome-unity [Unity]
- https://github.com/QianMo/Unity-Design-Pattern [Unity Design]
- https://github.com/michal-z/zig-gamedev [Building game development ecosystem for ziglang]
- https://github.com/OTFCG/Awesome-Game-Analysis [Video game tech analysis resources]
- https://github.com/killop/anything_about_game [Game Development resources]
- https://github.com/TastSong/GameProgrammerStudyNotes [Game Development notes]
- https://github.com/P0L3NARUBA/gtav-sourcecode-build-guide [GTA V Source Code Build Tutorial]

> Source
- https://github.com/PiMoNFeeD/csgo-src [Leaked CSGO]
- https://github.com/perilouswithadollarsign/cstrike15_src [Leaked CSGO With CI]
- https://github.com/gmh5225/Far-Cry-1-Source-Full [Leaked Far Cry 1]
- https://github.com/gmh5225/FarCry [Leaked Far Cry 1]
- https://github.com/SwagSoftware/Kisak-Strike [Open Source CSGO]
- https://github.com/SwagSoftware/KisakCOD [COD4 Open Source Reimplementation]
- https://github.com/hampta/csso-src [CSGO Mod]
- https://github.com/thomaseichhorn/cs16-client [Rewrote CS1.6]
- https://github.com/s1lentq/ReGameDLL_CS [Reversed CS1.6]
- https://github.com/Velaron/cs16-client [Reversed CS1.6]
- https://github.com/Source2ZE/CS2Fixes [CS2 mod]
- https://github.com/gmh5225/Game-GTA-re3 [Reversed GTA III, Vice City]
- https://github.com/P0L3NARUBA/reGTA [Reverse Engineered GTA III and GTA VC]
- https://github.com/gta-reversed/gta-reversed-modern [Reimplementation of GTA:SA 1.0 US]
- https://github.com/WastedHymn/Grand-Theft-Auto-Modding-Source [Code snippets for Vice City]
- https://github.com/SmileyAG/ReCZDS [Reversed CZeror]
- https://github.com/Harrison1/unrealcpp [UE4 C++ examples]
- https://github.com/QianMo/UE4-FPS-Game [UE4 FPS Game]
- https://github.com/KitchenGun/UE4_FPS [UE4 FPS Demo]
- https://github.com/tomlooman/SimpleFPSTemplate [UE4 FPS Demo]
- https://github.com/tomlooman/EpicSurvivalGame [UE4 FPS Game]
- https://github.com/QianMo/UE4-Tank-Game [UE4 Game]
- https://github.com/UE-DEMO/UE-UE5-FPS-wlaster [UE5 FPS Game]
- https://github.com/gmh5225/UE5-FPS-CryptRaider [UE5 FPS Game]
- https://github.com/LeroyTechnologies/ProjectM [UE5 FPS Game]
- https://github.com/invi1998/MultiplayerBlasterGame [UE5 FPS Game]
- https://github.com/DruidMech/MultiplayerCourseBlasterGame [UE5 FPS Game]
- https://github.com/caydenbullock/UE5MultiplayerProject [UE5 horror game with anti-cheat]
- https://github.com/perfect-hand/ue5-cardgame [UE5 Card Game]
- https://github.com/stackOverflower92/FightingGame-UE5 [UE5 Fighting Game]
- https://github.com/gmh5225/UnrealEngine5-UltimateStreetFighters [UE5 StreetFighters Game]
- https://github.com/EvelynSchwab/ComponentFuseMechanic [UE5 constraining system]
- https://github.com/CobraCodeDev/TP_2DSideScrollerBP [UE5 2D template]
- https://github.com/gmh5225/ue5-roll-a-ball-game [UE5 Roll a Ball Game]
- https://github.com/tomlooman/ActionRoguelike [UE Roguelike Game]
- https://github.com/Unity-Technologies/FPSSample [Unity Game]
- https://github.com/OguzKaira/FPS-Movement [Unity FPS]
- https://github.com/OguzKaira/SQLite-Unity3D [Unity SQLite]
- https://github.com/swordjoinmagic/MoBaDemo [Unity MoBa]
- https://github.com/gmh5225/U3D_MiniDNF [Unity mini DNF]
- https://github.com/gmh5225/unity-vrchat-template [Unity VRChat Template]
- https://github.com/Saukiya/Arknights [Unity Arknights]
- https://github.com/ZehMatt/SnakeRoyal [Mini Game With Server]
- https://github.com/MKXJun/Super-Fighter [DX11 Mini Game]
- https://github.com/MKXJun/Rubik-Cube [DX9/11 Mini Game]
- https://github.com/Suprcode/mir2 [MIR2]
- https://github.com/Suprcode/mir3-zircon [MIR3]
- https://github.com/WolfireGames/overgrowth [Overgrowth]
- https://github.com/solidi/hl-mods [Modification For Half-Life]
- https://github.com/codingben/maple-fighters [A small online game similar to MapleStory]
- https://github.com/gmh5225/WinAPI_MapleStory [WinAPI MapleStory]
- https://github.com/ZeromaXHe/MapleStoryCopy [Godot MapleStory]
- https://github.com/loqix/Fortnite [Fortnite]
- https://github.com/bradharding/doomretro [DOOM]
- https://github.com/Daivuk/PureDOOM [DOOM]
- https://github.com/NSG650/NtDOOM [Doom running in the NT kernel]
- https://github.com/Luxon98/Super-Mario-Bros-game [Remake of Super Mario]
- https://github.com/plibither8/2048.cpp [2048]
- [An open source re-implementation of RollerCoaster Tycoon 2](https://github.com/OpenRCT2/OpenRCT2)
- [This is the old Paradise SPRX BO2 soruce code](https://github.com/gopro2027/ParadiseBO2)
- https://github.com/dreamstalker/rehlds [Reverse-engineered HLDS]
- https://github.com/AndroidModLoader/AndroidModLoader [Android Mod Loader]
- https://github.com/marblexu/PythonPlantsVsZombies [PlantsVsZombies]
- https://github.com/mhyousefi/ZombiesVsPlants [PlantsVsZombies]
- https://github.com/Fewnity/Counter-Strike-DS-Unity-Project [Unity CS]
- https://github.com/Fewnity/Counter-Strike-Nintendo-DS [Nintendo CS]
- https://github.com/ppy/osu [osu]
- https://github.com/ppy/osu-framework [osu]
- https://github.com/dufernst/LegionCore-7.3.5 [wow]
- https://github.com/RageProject/5.4.7-Wow-source [wow]
- https://github.com/SkyFire/MopCore547 [wow]
- https://github.com/Arctium/WoW-Launcher [wow launcher]
- https://github.com/skMetinek/Non-Newtonian-New-York [Spider-Man Remastered Mod]
- https://github.com/playgameservices/cpp-android-basic-samples [Sample games using the Google Play Games C++ SDK]
- https://github.com/pafuhana1213/KawaiiPhysics [Simple fake Physics for UnrealEngine4 & 5]
- https://github.com/pafuhana1213/VTuberWithUE4 [UE4 VTuber]
- https://github.com/Bratah123/GojoTheSpire [Slay The Spire Remastered Mod]
- https://github.com/snesrev/zelda3 [A reimplementation of Zelda 3]
- https://github.com/kantam5/DeadByDaylight [Dead By Daylight Copy]
- https://github.com/Phobos-developers/Phobos [Red Alert 2: Yuri's Revenge engine extension]
- https://github.com/praydog/AutomataMP [NieR]
- https://github.com/xinyu-evolutruster/3D-Racing-Game [A racing game based on OpenGL]
- https://github.com/ProjectBorealis/PBCharacterMovement [HL2-style, classic FPS movement for UE4 implemented in C++]
- https://github.com/Merisho/tx-holdem [Texas Holdem Poker made by JS]
- https://github.com/raysan5/raylib [A simple and easy-to-use library to enjoy videogames programming]
- https://github.com/NotYetGames/WarriOrb [a Dark-Souls like action platformer using UE4]
- https://github.com/pjasicek/OpenClaw [Reimplementation of Captain Claw (1997) platformer]
- https://github.com/galaxyhaxz/devilution [Reversed Devilution]
- https://github.com/assaultcube/AC [FPS Game]
- https://github.com/fishfolk/jumpy [Pixels style]
- https://github.com/jynew/jynew [JinYongLegend]
- https://github.com/johndpope/pianogame [Piano Game]
- https://github.com/gmh5225/QQTang [QQTang]
- https://github.com/kvnxiao/storytime [Remake of MapleStory]
- https://github.com/deathkiller/jazz2-native [Remake of Jazz Jackrabbit 2]
- https://github.com/electronicarts/CnC_Red_Alert [Command and Conquer: Red Alert]
- https://github.com/huangkaoya/redalert2 [Red Alert 2 on Web]

> MCP server
- https://github.com/TensorBlock/awesome-mcp-servers [Awesome MCP]
- https://github.com/ahujasid/blender-mcp [Blender Model Context Protocol Integration]
- https://github.com/chongdashu/unreal-mcp [MCP for Unreal Engine]
- https://github.com/kvick-games/UnrealMCP [MCP for Unreal Engine]
- https://github.com/VedantRGosavi/UE5-MCP [MCP for Unreal Engine 5]
- https://github.com/justinpbarnett/unity-mcp [MCP for unity]
- https://github.com/wondeks/unity-mcp [MCP for unity]
- https://github.com/nasimali5/mcpup [MCP for unity]
- https://github.com/majidmanzarpour/vibe-blocks-mcp [MCP for Roblox Studio]
- https://github.com/LaurieWired/GhidraMCP [MCP for Ghidra]
- https://github.com/jtang613/GhidrAssistMCP [MCP for Ghidra]
- https://github.com/mrexodia/ida-pro-mcp [MCP for IDA pro]
- https://github.com/cnitlrt/headless-ida-mcp-server [MCP for IDA pro(headless)]
- https://github.com/MxIris-Reverse-Engineering/ida-mcp-server [MCP for IDA pro]
- https://github.com/taida957789/ida-mcp-server-plugin [MCP for IDA pro]
- https://github.com/fdrechsler/mcp-server-idapro [MCP for IDA pro]
- https://github.com/rand-tech/pcm [MCP for IDA pro]
- https://github.com/Iamgublin/ida-codex-mcp [IDA Codex MCP]
- https://github.com/axelmierczuk/tenrec [A headless, extendable, multi-session, IDA Pro MCP framework]
- https://github.com/blacktop/ida-mcp-rs [Headless IDA Pro MCP server]
- https://github.com/fosdickio/binary_ninja_mcp [MCP for Binary_Ninja]
- https://github.com/Invoke-RE/binja-lattice-mcp [MCP for Binary_Ninja]
- https://github.com/dnakov/radare2-mcp [Radare2 MCP Server]
- https://github.com/GLips/Figma-Context-MCP [Cursor Talk To Figma MCP server]
- https://github.com/gmh5225/hex2dec-mcp [MCP server that provides conversion between hexadecimal and decimal numbers]
- https://github.com/signal-slot/mcp-gdb [MCP for GDB]
- https://github.com/svnscha/mcp-windbg [MCP for WinDBG]
- https://github.com/AgentSmithers/x64DbgMCPServer [MCP for x64Dbg]
- https://github.com/IChooseYou/Reclass [MCP for Reclass]
- https://github.com/ant4g0nist/lisa.py [MCP for LLDB]
- https://github.com/droidrun/droidrun [MCP for Android]
- https://github.com/un4ckn0wl3z/MemMCP [Cheat Engine-like but MCP]
- https://github.com/Eruditi/CE-MCP-Plugin [MCP for Cheat Engine]
- https://github.com/zinja-coder/apktool-mcp-server [A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)]
- https://github.com/regenrek/deepwiki-mcp [MCP for deepwiki]
- https://github.com/jedisct1/zig-mcp-server [A high-performance implementation of the MCP protocol in Zig]
- https://github.com/noopstudios/interactive-feedback-mcp [Interactive User Feedback MCP]
- https://github.com/gmh5225/interactive-feedback-macos-mcp [A native macOS MCP server for collecting interactive user feedback with AppleScript dialogs and image support]
- https://github.com/datalayer/jupyter-mcp-server [MCP for Jupyter]
- https://github.com/PortSwigger/mcp-server [MCP for Burp Suite]
- https://github.com/cycraft-corp/BinaryAnalysisMCPs [Binary analysis MCPs collections]

> MCP server security
- https://github.com/johnhalloran321/mcpSafetyScanner [MCPSafetyScanner - Automated MCP safety auditing and remediation using Agents]
- https://github.com/appsecco/vulnerable-mcp-servers-lab [A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers]

> AI Agents
- https://github.com/0xeb/windbg-copilot [WinDbg Copilot - Agentic Debugging extension]


## Game Assets
- https://github.com/Miziziziz/Retro3DGraphicsCollection
- https://github.com/HitmanHimself/GOWTool [God of War 2018]
- https://github.com/KhronosGroup/glTF [Runtime 3D Asset Delivery]
- https://github.com/syoyo/tinygltf [Header only C++11 tiny glTF 2.0 library]
- https://github.com/atenfyr/UAssetGUI [Viewing and modifying UE4 game assets]
- https://github.com/UETools/UETools [Accessing, reading and deserializing UE4 assets]
- https://github.com/atenfyr/UAssetAPI [A low-level .NET library for reading and writing Unreal Engine game assets]

## Game Hot Patch
- https://github.com/Tencent/xLua
- https://github.com/Tencent/InjectFix
- https://github.com/focus-creative-games/hybridclr


## Game Testing
- https://github.com/UnityTech/GamesTestAutomationExample [The collecting ideas on how to do Test Automation in Games]
- https://github.com/nowsprinting/UnityAutomatedQAExamples [Unity Automated QA Guidebook]
- https://github.com/AirtestProject/Airtest [UI Automation Framework]
- https://github.com/dendibakh/perf-ninja [Performance Analysis]
- https://github.com/CookiePLMonster/UptimeFaker [Detecting High PC Uptime]
- https://github.com/GameTechDev/PresentMon [Graphics Performance]
- https://github.com/gatling/gatling [Server Testing]
- https://github.com/aristocratos/btop [Performance Monitor]
- https://github.com/Celtoys/Remotery [A realtime CPU/GPU profiler]
- https://github.com/Volkanite/Push [Monitor GPU/CPU/RAM performance]
- https://github.com/google/orbit [C/C++ Performance Profiler]
- https://github.com/wolfpld/tracy [C++ frame profiler]
- https://github.com/bombomby/optick [C++ Profiler For Games]
- https://github.com/RomanceTheHeart/Automation_Examples [Automating certain tasks in the Unreal editor]
- https://github.com/DaedalicEntertainment/ue4-test-automation [Facilitates setting up integration test suits with Unreal Engine 4 Gauntlet]
- https://github.com/DenuvoSoftwareSolutions/Onlooker [Tool to collect and visualize memory usage of a process tree]
- https://github.com/milostosic/rprof [CPU scope based profiling library]
- https://github.com/DarknessFX/DFoundryFX [UE Performance]

## Game Tools
- [Play your favorite games in a borderless window; no more time consuming alt-tabs](https://github.com/Codeusa/Borderless-Gaming)
- https://github.com/bad-antics/rce-shield [RCE hardening toolkit for PC gamers]
- https://github.com/Genymobile/scrcpy [Display and control your Android device]
- https://github.com/ryanjon2040/Unreal-Binary-Builder [Build UE Source]
- https://github.com/ryanjon2040/UnrealNetworkProfiler [Network Profiler for UE]
- [Command line tool for getting the download URL for the latest or specific version of Unity](https://github.com/neogeek/get-unity)
- https://github.com/recastnavigation/recastnavigation [Navigation-mesh Toolset for Games]
- https://github.com/TensorWorks/UE-Clang-Format [UE Clang-Format configuration]
- https://github.com/inflation/goldberg_emulator [Steam emulator]
- https://github.com/PixiEditor/PixiEditor [PixiEditor is a Universal Editor for all your 2D needs]

## Game Manager
- https://github.com/JosefNemec/Playnite

## Game CI
- https://github.com/game-ci
- https://github.com/nikaera/Unity-GameCI-Sample [Unity]

## DirectX
> Guide
- https://github.com/planetchili/hw3d [C++ 3D DirectX Tutorial]
- https://github.com/jpvanoosten/LearningDirectX12 [DX12]
- https://github.com/PAMinerva/LearnDirectX [DX12]
- https://github.com/MKXJun/DirectX11-With-Windows-SDK [DX11 zh]
- https://github.com/d3dcoder/d3d12book [DX12]
- https://github.com/pkurth/D3D12Renderer [DX12]

> Hook
- https://github.com/rdbo/DX11-BaseHook [DX11 Imgui]
- https://github.com/DrNseven/D3D12-Hook-ImGui [DX12 Imgui]
- https://github.com/niemand-sec/DirectX11Hook [DX11 Imgui]
- https://github.com/guided-hacking/GH_D3D11_Hook [DX11]
- https://github.com/gogo9211/Discord-Overlay-Hook [DX11]
- https://github.com/ocornut/imgui/commit/923bd2fd217c1dc1e75fa92b0284d3817904988b [DX11/12 ResizeBuffers]
- https://github.com/marlkiller/d3dhook_imgui [d3d opengl hook imgui x86/x64]
- [Universal graphical hook for a D3D9-D3D12, OpenGL and Vulkan based games](https://github.com/Rebzzel/kiero)
- https://github.com/jmpews/Dobby [a lightweight, multi-platform, multi-architecture hook framework]
- https://github.com/Sh0ckFR/Universal-Dear-ImGui-Hook [An universal Dear ImGui Hook]
- https://github.com/bruhmoment21/UniversalHookX [DX/OpenGL/Vulkan]

> Tools
- https://github.com/visotw/3d9 [Fixing broken stereoscopic effects in DX11 games]

> Emulation 
- https://github.com/code-tom-code/Software_D3D9 [DX9]

> Compatibility
- https://github.com/CnCNet/cnc-ddraw [Old Game]
- https://github.com/microsoft/D3D9On12 [The Direct3D9-On-12 mapping layer]
- https://github.com/Daniel-Lobo/WineHooks [Compatibility and enhancement framework for classic PC games]
- https://github.com/samuelgr/Xidi [DirectInput interface for XInput controllers]

> Overlay
- https://github.com/SeanPesce/Direct3D9-Overlay

## OpenGL
> Guide
- https://github.com/JoeyDeVries/LearnOpenGL

> Source
- https://github.com/brackeen/glfm [Write OpenGL ES code in C/C++]

> Hook
- https://github.com/bruhmoment21/UniversalHookX

## Vulkan
> Guide
- https://github.com/googlesamples/android-vulkan-tutorials

> API
- https://github.com/liblava/liblava [Modern and easy-to-use library for Vulkan]
- https://github.com/corporateshark/lightweightvk

> Hook
- https://github.com/Rebzzel/kiero [X86/64 Windows]
- https://github.com/bruhmoment21/UniversalHookX [X86/64 Windows]
- https://github.com/DrNseven/Vulkan-Hook [X86/64 Windows]
- https://github.com/Sh0ckFR/Universal-Dear-ImGui-Hook
- https://github.com/Halen84/ImGuiRDR2Hook

## Cheat
> Guide
- https://github.com/dsasmblr/game-hacking
- https://github.com/dsasmblr/hacking-online-games
- https://github.com/jbro129/android-modding [A collection of repositories related to Android game modding]
- https://github.com/kovidomi/game-reversing
- https://github.com/TheZong/Game-Hacking
- https://github.com/mytechnotalent/Reverse-Engineering
- https://github.com/wtsxDev/reverse-engineering
- https://github.com/mytechnotalent/Hacking-Windows
- https://github.com/kotae4/intro-to-gamehacking
- https://blog.can.ac/author/can1357
- https://github.com/SinaKarvandi/Hypervisor-From-Scratch [Hypervisor]
- https://secret.club
- https://back.engineering
- https://vollragm.github.io
- https://www.triplefault.io
- https://advancedvectorextensions.github.io
- https://bright.engineer
- https://reversing.info
- https://www.unknowncheats.me
- https://forum.ragezone.com
- https://guidedhacking.com
- https://github.com/guided-hacking
- https://gamehacking.academy
- https://github.com/GameHackingAcademy
- https://areweanticheatyet.com [A list of games using anti-cheats]
- https://github.com/aclist/aclist.github.io [Anti-cheat compatibility list]
- https://github.com/imadr/Unity-game-hacking [Unity]
- https://vollragm.github.io/posts/unity-reversing [Unity]
- https://wiki.cheatengine.org/index.php?title=Mono [CE Mono]
- https://github.com/krampus-nuggets/ce-tutorial [CE]
- https://il2cppdumper.com [IL2CPP]
- https://www.unknowncheats.me/forum/unity/465283-il2cppruntimedumper.html [IL2CPP]
- https://github.com/shalzuth/NativeNetSharp [Injecting C# code]
- https://github.com/januwA/game-reversed-study [CE Guide zh]
- https://github.com/csgohacks/master-guide [CSGO Guide]
- [different-ways-hooking](https://www.unknowncheats.me/forum/general-programming-and-reversing/154643-different-ways-hooking.html) [Hook Guide]
- http://pwnadventure.com [Hackable Game]
- https://github.com/GameCrashProject/UE4-Hacking-Guideline [Unreal]
- https://github.com/TimMisiak/WinDbgCookbook [WinDbg]
- https://github.com/anhkgg/awesome-windbg-extensions [WinDbg]
- [Undetected Cheat Engine](https://www.unknowncheats.me/forum/anti-cheat-bypass/504191-undetected-cheat-engine-driver-2022-bypass-anticheats-eac.html)
- [Guide about remote Windows kernel debugging](https://github.com/konstantin89/windows-kernel-debugging-guide)
- https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Games.md [Game Hacking]
- https://github.com/cragson/osmium [C++ Framework for external cheats]
- https://github.com/WangXuan95/Xilinx-FPGA-PCIe-XDMA-Tutorial [DMA Tutorial]
- https://github.com/NetKingJ/awesome-android-security [Android (Samsung) Security Research References]
- https://github.com/gregkh/kernel-development [Linux kernel development]
- https://github.com/MatheuZSecurity/Rootkit [Collection of codes focused on Linux rootkits]
- https://github.com/ARandomPerson7/Appsealing-Reversal [A Reversal and bypass for Appsealing]
- https://klecko.github.io/posts/selinux-bypasses [Bypass selinux]
- https://github.com/Solaree/pairipcore [Public researchings of the Google's Android apps protection]
- https://github.com/enjoy-digital/litepcie [Small footprint and configurable PCIe core]
- https://lolc2.github.io [collection of C2 frameworks that leverage legitimate services to evade detection]

> Debugging
- https://github.com/stars/gmh5225/lists/debugger [List]
- https://github.com/cheat-engine/cheat-engine
- https://github.com/SinaKarvandi/Hypervisor-From-Scratch [Hypervisor]
- https://github.com/JasonGoemaat/CheatEngineMonoHelper [CE Mono Helper]
- https://github.com/DoranekoSystems/frida-ceserver [CE Server For IOS]
- https://github.com/DoranekoSystems/ceserver-ios [Porting ceserver to iOS.Dynamic analysis]
- https://github.com/0xiuks/ceserver-ios [An iOS port of Cheat Engine's ceserver]
- https://github.com/gmh5225/cheat-engine-ceserver-pcileech [CE Server For Pcileech]
- https://github.com/user23333/veh [CE Plugin For Manualmap VEH Dll]
- https://github.com/x64dbg/x64dbg [A debugger for Windows x86/64]
- https://github.com/marakew/syser [A debugger for Windows x86/64]
- https://github.com/keowu/koidbg [A debugger for Windows ARM64]
- https://github.com/DoranekoSystems/DynaDbg [A debugger for Android/IOS]
- https://github.com/Yayoi-cs/fastDbg [x86_64 native/qemu kernel debugger]
- https://github.com/noword/GDB-Windows-Binaries [GDB]
- https://github.com/ajkhoury/ReClassEx
- https://github.com/ReClassNET/ReClass.NET
- https://github.com/niemand-sec/ReClass.NET-DriverReader [ReClass DriverReader]
- https://github.com/BeneficialCode/KReClassEx [Kernel ReClassEx]
- https://github.com/imerzan/ReClass-DMA [ReClass DMA]
- https://github.com/IChooseYou/Reclass [Reclass MCP refactored]
- https://github.com/Metick/CheatEngine-DMA [CheatEngine DMA]
- https://github.com/kaijia2022/Cheat-Engine-DMA-Plugin [CheatEngine DMA]
- https://github.com/x64dbg/DotX64Dbg
- https://github.com/imugee/xdv
- https://github.com/eteran/edb-debugger [For Linux]
- https://github.com/korcankaraokcu/PINCE [For Linux]
- https://github.com/djolertrk/kLLDB [LLDB based debugger for Linux Kernel]
- https://github.com/mrexodia/TitanHide
- https://github.com/Air14/HyperHide 
- https://github.com/HyperDbg/HyperDbg
- https://github.com/3526779568/vt-debuger
- https://github.com/teemu-l/execution-trace-viewer
- https://github.com/changeofpace/Force-Page-Protection [Bypass Remap Memory]
- https://github.com/icsharpcode/ILSpy [For Unity]
- https://github.com/dnSpy/dnSpy [For Unity]
- https://github.com/HoLLy-HaCKeR/dnSpy.Extension.HoLLy [For Unity]
- https://github.com/mandiant/dncil [For Unity]
- https://github.com/hugsy/CFB [Monitor IRP]
- https://github.com/Kharos102/IOCTLDump [Monitor IRP]
- https://ioninja.com/downloads.html [Protocol Analyzer]
- https://github.com/wilszdev/SteamAntiAntiDebug [Steam]
- https://github.com/H5GG/H5GG [IOS cheat engine]
- https://github.com/ri-char/pwatch [HWBP on linux/android]
- https://github.com/enenH/pwatch-c [HWBP on linux/android]
- https://github.com/Ylarod/hardware-breakpoint [HWBP on linux/android]
- https://github.com/roger1337/JDBG [Java Runtime Reverse Engineering and Debugging Tool]
- https://github.com/Sh11no/eDBG [eBPF-based lightweight debugger for Android]
- https://github.com/ShinoLeah/eHook [eBPF hook]
- https://github.com/SeeFlowerX/stackplz [eBPF-based debugger for Android]
- https://github.com/Satar07/edbgserver [eBPF-powered debugger server for Linux and Android]
- https://github.com/g2wfw/qbdi-tracer-android [Android assembly instruction tracing tool]
- https://github.com/un4ckn0wl3z/MemMCP [Cheat Engine-like but MCP]
- https://github.com/LLeavesG/eBPFDexDumper [DexDumper based eBPF on Android Platform]

> Packet Sniffer&Filter
- https://github.com/WPO-Foundation/win-shaper
- https://github.com/wiresock/ndisapi
- https://github.com/Akebi-Group/Akebi-PacketSniffer
- https://github.com/basil00/Divert [Packet Divert]
- https://github.com/fksvs/inject
- https://github.com/hercul3s/Packet-Sniffer [Packet Logger/Decryptor]

> Packet Capture&Parse
- https://github.com/seladb/PcapPlusPlus [Pcap]
- https://github.com/nmap/npcap

> SpeedHack
- https://github.com/absoIute/Speedhack
- https://github.com/Letomaniy/Speed-Hack
- https://github.com/IamSanjid/ce_speed_hack

> RE Tools
- https://dogbolt.org
- https://github.com/msd0pe-1/cve-maker [Tool to find CVEs and Exploits]
- https://github.com/mentebinaria/retoolkit [Reverse Engineer's Toolkit]
- https://github.com/stevemk14ebr/RETools
- https://github.com/BataBo/ACEPatcher [.NET Patcher]
- https://github.com/waryas/KACE [Emulate Drivers in RING3 with self context mapping or unicorn]
- https://github.com/Qfrost911/KACE [Emulate Drivers in RING3 with self context mapping or unicorn]
- https://github.com/VollRagm/PTView [Browse Page Tables on Windows]
- https://github.com/iBotPeaches/Apktool [Apk]
- https://github.com/user1342/Obfu-DE-Scate [Apk]
- https://github.com/AndnixSH/APKToolGUI [GUI for apktool, signapk, zipalign and baksmali utilities]
- https://github.com/Genymobile/scrcpy  [Display and control your Android device]
- https://github.com/barry-ran/QtScrcpy [Display and control your Android device]
- https://github.com/guided-hacking/GH-Offset-Dumper [Scans for signatures and netvars and dumps their relative offsets]
- https://github.com/guided-hacking/GH-Entity-List-Finder [Scans game processes for most likely entity list addresses]
- https://github.com/rednaga/APKiD [PEiD for Android]
- https://github.com/Col-E/Recaf [Java]
- https://github.com/tomvita/SE-tools [Nintendo Switch]
- https://github.com/StudentBlake/XCI-Explorer [XCI Explorer]
- https://github.com/Anonym0ose/JitDumper [A CIL method body dumper]
- https://github.com/cfig/Android_boot_image_editor [A tool for reverse engineering Android ROM images]
- https://github.com/hasherezade/pe-bear [PE Viewer]
- https://github.com/zodiacon/TotalPE2 [PE Viewer]
- https://github.com/APKLab/APKLab [Android Reverse-Engineering Workbench for VS Code]
- https://github.com/zboralski/unflutter [Static analyzer for Flutter/Dart AOT snapshots]
- https://github.com/evild3ad/MemProcFS-Analyzer [Windows Forensic Analysis]
- https://github.com/eybisi/kavanoz [Statically unpacking common android banker malware]
- https://github.com/cyberark/PipeViewer [Shows detailed information about named pipes in Windows]
- https://github.com/cursey/regenny [Reconstruct structures and generate header files]
- https://github.com/zodiacon/EtwExplorer [View ETW Provider manifest]
- https://github.com/DoranekoSystems/ceserver-ios [Porting ceserver to iOS.Dynamic analysis]
- https://github.com/VoidSec/ioctlpus [Be used to make DeviceIoControl requests with arbitrary inputs]
- https://github.com/horsicq/Nauz-File-Detector [Linker/Compiler/Tool detector]
- https://github.com/gcarmix/HexWalk [Hex Viewer/Editor/Analyzer]
- https://github.com/RomanRybachek/ioctl_helper [GUI tool for sending IOCTL to windows drivers]
- https://github.com/sevaa/dwex [DWARF Explorer]
- https://github.com/katahiromz/RisohEditor [Win32 resource editor]
- https://github.com/Fadi002/de4py [Toolkit for python reverse engineering]
- https://github.com/skelsec/minidump [Python library to parse and read Microsoft minidump file format]
- https://github.com/zodiacon/QuickAsm [x86/x86 assembler and emulator]
- https://github.com/aqilc/chasm [Chasm Runtime Assembler]
- https://github.com/skylot/jadx [Dex to Java decompiler]
- https://github.com/narumii/Deobfuscator [A deobfuscator for java]
- https://github.com/google/android-classyshark [Android and Java bytecode viewer]
- https://github.com/marin-m/vmlinux-to-elf [vmlinux to elf]
- https://github.com/emlinhax/DbgViewEx [A tool to log ETW Events and system debug logs]
- https://github.com/amosshi/binaryinternals [View Internals of Binary File]
- https://github.com/WerWolv/ImHex [A Hex Editor for Reverse Engineers]
- https://github.com/microsoft/pdblister [Faster version of `symchk /om` for generating PDB manifests]
- https://github.com/yaxinsn/vermagic [Change vermagic and CRCs of a Linux Kernel Module]
- https://github.com/rhboot/pesign [Linux tools for signed PE-COFF binaries]
- https://github.com/SV-Foster/UnSign [Remove all digital signatures from PE/COFF executable]
- https://github.com/colinsenner/PECleaner [Strips all RICH header information from x86/x64 binaries]
- https://github.com/kouzhudong/AntiHook [Enum and Remove Hook in Windows]
- https://github.com/jixiaoyong/ApkSigner [Android Apk Sign Tool]
- https://github.com/4d61726b/VirtualKD-Redux [A revival and modernization of VirtualKD]
- https://github.com/ax/apk.sh [A Bash script that makes reverse engineering Android apps easier]
- https://github.com/vm03/payload_dumper [Android OTA payload dumper]
- https://github.com/ssut/payload-dumper-go [Android OTA payload dumper]
- https://github.com/MlgmXyysd/Xiaomi-HyperOS-BootLoader-Bypass [Xiaomi HyperOS BootLoader Bypass]
- https://github.com/null-luo/btrace [Android App Dynamic Behavior Tracking Tool using eBPF]
- https://github.com/michaelmsonne/SignToolGUI [signtool GUI]
- https://disasm.pro/ [A realtime assembler/disassembler]
- https://github.com/iofomo/abyss [Android system call hook]
- https://github.com/uuksu/RPGMakerDecrypter [Tool for extracting RPG Maker XP, VX and VX Ace encrypted archives]
- https://github.com/gmh5225/compiler-binary-richprint [Print compiler information stored in Rich Header of PE executable]
- https://github.com/mandiant/GoReSym [Go symbol recovery tool]
- https://github.com/PartialVolume/shredos.x86_64 [Disk Eraser]
- https://github.com/ssnob/hidden_syscall_monitoring [monitors hidden syscalls called from call of duty anticheat]
- https://github.com/cansarigol/pdbr [pdb + Rich library]
- https://github.com/microsoft/pdb-rs [Tools and documents for working with Microsoft PDB files, in Rust]
- https://github.com/roger1337/JDBG [Java Runtime Reverse Engineering and Debugging Tool]
- https://github.com/atrexus/vulkan [A PE dumper for processes protected by user mode anti-tamper solutions (hyperion, theia, etc.)]
- https://github.com/linuxboot/fiano [Go-based tools for modifying UEFI firmware]
- https://github.com/leeqwind/PESignAnalyzer [A Simple PE File Signature information Extracting Tool]
- https://github.com/microsoft/SDCM [Surface Dev Center Manager tool to automate WHQL/Attestation submissions]
- https://github.com/MxIris-Reverse-Engineering/RuntimeViewer [Objective-C Runtime Viewer for macOS and iOS]
- https://github.com/skylot/raung [Assembler/disassembler for java bytecode]
- https://github.com/hx1997/dayu [Open/HarmonyOS abc file parser and decompiler]
- https://github.com/jd-opensource/arkdecompiler [HarmonyOS NEXT decompilation tool]
- https://github.com/loerting/dalvikus [Android reverse-engineering tool / smali editor]
- https://github.com/poppopjmp/VMDragonSlayer [Advanced Virtual Machine Detection and Analysis Framework]
- https://github.com/Byrom90/XenonDumper [Dumps files & data required to use the Xenon Xbox 360 Low Level Emulator]
- https://github.com/WenzWenzWenz/DelphiReSym [A Delphi symbol name recovery tool for reverse engineers]
- https://github.com/Hexorg/Ouroboros [A Symbolic-Execution Decompiler written in Rust]
- https://github.com/pandaadir05/re-architect [RE-Architect is an advanced automated reverse engineering platform that utilizes binary analysis techniques and machine learning to understand binary files and extract meaningful information]
- https://github.com/gmh5225/js-debugger-bypass-script [JS Debugger Bypass UserScript]
- https://github.com/diversenok/DiaSymbolView [PDB file inspection tool]
- https://github.com/CheckPointSW/Nodejs-Tracer [Simple Node.jstracer that logs calls to analyze heavily obfuscated Node.js malware]
- https://github.com/jsacco/ntoskrnlwalker [Resolve offsets, gadgets and symbols from NTKernel]

> Mixed boolean-arithmetic
- https://github.com/Colton1skees/mba-resources [List of mixed boolean-arithmetic resources]

> Fix VMP
- https://github.com/Obfuscator-Collections/VMProtect
- https://github.com/wallds/NoVmpy
- https://github.com/gmh5225/VMP-Vmp3_64bit_disasm-prerelease-
- https://github.com/gmh5225/Vmp3_utils
- https://github.com/archercreat/titan
- https://github.com/NaC-L/Mergen
- https://github.com/fjqisba/VmpHelper
- https://github.com/xtremegamer1/vmdevirt-vtil
- https://github.com/oureveryday/VMPUnpacker/tree/master [Unpacker]
- https://github.com/poppopjmp/VMDragonSlayer [Advanced Virtual Machine Detection and Analysis Framework]

> Fix Themida
- https://github.com/sodareverse/TDE
- https://github.com/ergrelet/themida-unmutate
- https://github.com/stuxnet147/Themida-Research [Themida 3.x research]

> Fix OLLVM
- https://bbs.pediy.com/thread-272414.htm
- https://github.com/obpo-project/obpo-plugin
- https://github.com/IIIImmmyyy/AntiOllvm [AntiOllvm Fla with Fake Runtime]
- https://github.com/Mrack/DeObfBR [libtprt.so]
- https://github.com/zhuzhu-Top/deobf [libtprt.so]
- https://github.com/cdong1012/ollvm-unflattener [unflattener]
- https://github.com/JbvrgtonYT/ollvm-unflattener [unflattener]

> Dynamic Binary Instrumentation
- https://github.com/hzqst/unicorn_pe
- https://github.com/momo5502/sogen [Windows User Space Emulator]
- https://github.com/mojtabafalleh/emulator [Windows User Space Emulator]
- https://github.com/binsnake/KUBERA [A x86 environment emulator for Windows user and kernel binaries]
- https://github.com/ZehMatt/zyemu [x86-64 user mode emulation using Zydis]
- https://github.com/Nitr0-G/PeVisor [PE]
- https://github.com/googleprojectzero/TinyInst
- https://github.com/revsic/cpp-veh-dbi
- https://github.com/ZehMatt/CovCane
- https://github.com/bitdefender/river
- https://github.com/beehive-lab/mambo [ARM]
- https://github.com/DynamoRIO/drmemory
- https://github.com/aroxby/dynre-x86
- https://github.com/WaterlooBridge/adbi [For Android]
- https://github.com/crmulliner/adbi [For Android]
- https://github.com/ndrewh/pyda [Write dynamic binary analysis tools in Python]
- https://github.com/redthing1/w1tn3ss [dynamic binary instrumentation, analysis, and patching framework]
- https://github.com/g2wfw/qbdi-tracer-android [Android assembly instruction tracing tool]
- https://github.com/facebookresearch/CUTracer [A dynamic binary instrumentation tool for tracing and analyzing CUDA kernel instructions]

> Launcher Abuser
- https://github.com/Ricardonacif/launcher-abuser

> PatchGuard-related
- https://github.com/armasm/EasyAntiPatchGuard
- https://github.com/9176324/Shark
- https://github.com/gmh5225/Patchguard-2023 [Shark]
- https://github.com/hfiref0x/UPGDSED [File]
- https://github.com/Mattiwatti/EfiGuard [EFI]
- https://github.com/zzhouhe/PG1903 [Demo NX]
- https://gist.github.com/gmh5225/0a0c8e3a2d718e2d6f9b6a07d5e0f80a [PG CTX]
- https://github.com/gmh5225/QuickPGTrigger [Stress Testing]
- https://github.com/tandasat/Sushi [Monitoring PG]
- https://github.com/gmh5225/Disabling-Hyper-V [Disable Hyper-V]
- https://github.com/AdamOron/PatchGuardBypass
- https://github.com/zer0condition/Demystifying-PatchGuard
- https://github.com/4l3x777/dse_pg_bypass [DSE & PG bypass via BYOVD attack]
- https://github.com/gmh5225/VulnerablePatchGuardExploit [A Vulnerable PatchGuard Exploit that can be used to disable PatchGuard on Runtime]
- https://github.com/emlinhax/tableflipper [partially disable patchguard up to win11 21H2]
- https://github.com/AmitMoshel1/PatchGuardEncryptorDriver [Self-implemented PatchGuard]
- https://r0keb.github.io/posts/PatchGuard-Internals [PatchGuard Internals]
- https://github.com/NeoMaster831/kurasagi [Windows 11 24H2 Runtime PatchGuard Bypass]

> Driver Signature enforcement
- https://github.com/gmh5225/dse_hook
- https://github.com/gmh5225/Dse-Patcher-2
- https://github.com/gmh5225/DisableDSE

> Windows Kernel Explorer
- https://github.com/NullArray/WinKernel-Resources [Guide]
- https://github.com/supermanc88/Document/tree/master/Windows%20Driver%20Development [Guide]
- https://windiff.vercel.app [Diff]
- https://github.com/gmh5225/ntoskrnl_file_collection [Various versions of ntoskrnl files]
- https://github.com/gmh5225/win32k_file_collection [Various versions of win32k files]
- https://github.com/gmh5225/win32k_file_collection2 [Various versions of win32k files]
- https://github.com/jiubanlo/WinNT5_src_20201004 [Leaked Windows XP Source]
- https://github.com/BlackINT3/OpenArk [Tool]
- https://github.com/BeneficialCode/WinArk [Tool]
- https://github.com/hfiref0x/KDU [Kernel Driver Utility Tool]
- https://github.com/jthuraisamy/TelemetrySourcerer [Enumerate and disable callbacks/ETW]
- https://github.com/preludeorg/ThreatIntelligenceConsumer [Consuming from the Threat-Intelligence ETW provider without a driver or PPL privilege]
- https://github.com/progmboy/openprocmon [open source process monitor]
- https://github.com/winsiderss/systeminformer [The original name is "Process Hacker"]
- https://github.com/0xcpu/ExecutiveCallbackObjects [Callback]
- https://github.com/0xcpu/WinAltSyscallHandler [AltSystemCallHandlers]
- https://github.com/DownWithUp/CallMon [AltSystemCallHandlers]
- https://github.com/everdox/InfinityHook [ETW Hook]
- https://github.com/AyinSama/Anti-AntiDebuggerDriver [ETW Hook]
- https://github.com/gmh5225/AcDrv [ETW Hook]
- https://github.com/FiYHer/InfinityHookPro [ETW Hook Ex]
- https://github.com/gmh5225/ETWHOOK-InfinityHookClass [ETW Hook Ex]
- https://github.com/DearXiaoGui/InfinityHookPro-main [ETW Hook WIN11]
- https://github.com/ThomasonZhao/InfinityHookProMax [ETW Hook WIN11]
- https://github.com/Oxygen1a1/InfinityHook_latest [ETW Hook WIN11]
- https://github.com/gmh5225/PDF-PMC-X86 [A Study on PMI in x86-Architecture]
- https://github.com/KelvinMsft/ThreadSpy [PMI Callback]
- https://github.com/KelvinMsft/PerfMon [PMI Callback]
- https://github.com/gmh5225/PMI-hpc [PMI]
- https://github.com/marcusbotacin/BranchMonitoringProject [PMI]
- https://github.com/gmh5225/NMI-EnumNmiCallback [Enumerate NMI]
- https://github.com/gmh5225/Disable-nmi-callbacks [Disable NMI]
- https://github.com/DErDYAST1R/NMICallbackBlocker2 [Disable NMI]
- https://github.com/gmh5225/NMI-nmi_callback [Triggering NMI]
- https://github.com/gmh5225/Kernel_Anti-Cheat [NMI]
- https://github.com/jlgreathouse/AMD_IBS_Toolkit [AMD Sampling]
- https://github.com/intelpt/WindowsIntelPT [Intel PT]
- https://github.com/CristiNacu/ingsoc [Intel PT]
- https://github.com/DProvinciani/pt-detector [Intel PT]
- https://github.com/googleprojectzero/winafl [Intel PT Fuzzer]
- https://github.com/intelpt/winipt [ipt.sys]
- https://github.com/australeo/libipt-rs [ipt.sys]
- https://github.com/intelpt/processor-trace [Intel PT Decoder]
- https://github.com/gmh5225/Driver-intel-PEBs-LoopHPCs [Intel PEBs]
- https://github.com/libiht/libiht [Intel Hardware Trace Library]
- https://github.com/ilovecsad/Ark [Tool]
- https://github.com/gmh5225/ntoskrnl_file_collection [Ntoskrnl Version]
- https://github.com/gmh5225/win32k_file_collection [Win32k Version]
- https://github.com/gmh5225/win32k_file_collection2 [Win32k Version]
- https://github.com/gmh5225/MSSymbolsCollection [Kernel Symbols]
- https://github.com/am0nsec/wkpe [Enumerate VAD]
- https://github.com/armvirus/DriverDllFInder [Find Driver Useless Memory]
- https://github.com/MahmoudZohdy/APICallProxy [Windows API Call Obfuscation]
- https://github.com/Spuckwaffel/Simple-MmcopyMemory-Hook [Hook MmcopyMemory]
- https://github.com/VollRagm/PTView [Browse Page Tables on Windows]
- https://github.com/misc0110/PTEditor [PT Editor]
- https://github.com/IcEy-999/Ntoskrnl_Viewer [Ntoskrnl Viewer]
- https://github.com/ekknod/Nmi [Blocking NMI interrupts]
- https://github.com/EquiFox/KsDumper [Dumping processes using the power of kernel space]
- https://github.com/mastercodeon314/KsDumper-11 [Classic and legendary KsDumper]
- https://github.com/not-matthias/Nemesis [Dumping processes using the power of kernel space]
- https://github.com/allogic/KDBG [Tool]
- https://github.com/backengineering/Voyager [A Hyper-V Hacking Framework For Windows 10 x64 (AMD & Intel)]
- https://github.com/gmh5225/Voyager [A Hyper-V Hacking Framework For Windows 10 x64 (AMD & Intel)]
- https://github.com/noahware/hyper-reV [memory introspection and reverse engineering hypervisor powered by leveraging Hyper-V]
- https://github.com/LabGuy94/Diskjacker [Runtime Hyper-V Hijacking with DDMA]
- https://github.com/zer0condition/BusterCall [HVCI bypass via PFN swapping to call arbitrary kernel functions from user-mode]
- https://github.com/NurdAlert/modded-voyager
- https://github.com/gmh5225/Fortnite-VoyagerTF [Voyager for Fortnite]
- https://github.com/repnz/apc-research [APC Internals Research Code]
- https://github.com/intel/pcm [Processor Counter Monitor]
- https://github.com/ChengChengCC/Ark-tools [Some kernel research]
- https://github.com/alal4465/KernelMon [Monitoring Windows Kernel Drivers]
- https://github.com/gmh5225/Practical-Reverse-Engineering-Solutions [DPC+APC]
- https://github.com/br-sn/CheekyBlinder [Enumerating and removing kernel callbacks using signed vulnerable drivers]
- https://github.com/GetRektBoy724/DCMB [Removing kernel callbacks]
- https://github.com/V-i-x-x/kernel-callback-removal [Removing kernel callbacks]
- https://github.com/Air14/KDBGDecryptor [A simple example how to decrypt kernel debugger data block]
- https://github.com/FaEryICE/MemScanner [Memory scanner]
- https://github.com/Oliver-1-1/RwxScanner [RWX Memory scanner]
- https://github.com/irql/nokd [Kernel debugger protocol]
- https://github.com/DejavuSecure/DetectNtoskrnlIntegrity [Windows Kernel Security: Memory Integrity Verification with Disk Verification of ntoskrnl.exe]
- https://github.com/brew02/BudgetEPT [Create stealthy, inline, EPT-like hooks using SMAP and SMEP]
- https://github.com/synacktiv/windows_kernel_shadow_stack [Shadow Stack]
- https://github.com/noahware/apic [C++ library for sending processor interrupts via x2apic & xapic]
- https://github.com/zer0condition/NTMemory [Usermode NT Explorer - Query kernel addresses, translate virtual to physical addresses, inspect the PFN database, and more.]

> Linux Kernel Explorer
- https://github.com/MatheuZSecurity/Rootkit [Collection of codes focused on Linux rootkits]
- https://github.com/MatheuZSecurity/ksentinel [Kernel integrity monitor for detecting syscall hooking]
- https://github.com/djolertrk/kLLDB [LLDB based debugger for Linux Kernel]
- https://github.com/sad0p/venom [Linux Kernel Rookit Hooking Mechanism]

> Magisk
- https://github.com/PShocker/Zygisk-MagiskHide
- https://github.com/longpoxin/hideroot
- https://github.com/canyie/Riru-MomoHider
- https://github.com/newbit1/rootAVD [root AVD]
- https://github.com/Fox2Code/FoxMagiskModuleManager [A module manager for Magisk]
- https://github.com/Dr-TSNG/ZygiskOnKernelSU [Run Zygisk on KernelSU]
- https://github.com/svoboda18/magiskboot [Boot Image Modification Tool]
- https://github.com/xiaoxindada/magiskboot_ndk_on_linux [Boot Image Modification Tool]
- https://github.com/ookiineko/magiskboot_build [Boot Image Modification Tool]
- https://github.com/gmh5225/magiskboot-linux [Use GitHub Actions to build magiskboot]
- https://github.com/the-dise/EasyPixel [Magisk module that disguises a device under Google Pixel]
- https://github.com/gmh5225/MagiskHide [Portable MagiskHide]
- https://github.com/lico-n/ZygiskFrida [Injects frida gadget using zygisk]
- https://github.com/Admirepowered/Zygisk_mod [Standalone implementation of Zygisk]
- https://github.com/anasfanani/Magisk-Tailscaled [Magisk module for running Tailscale]
- https://github.com/j-hc/FlagSecurePatcher [Disable flag secure and screenshot listeners]
- https://github.com/hackcatml/zygisk-memdump [A zygisk module that dumps so file from process memory]
- https://github.com/PerformanC/ReZygisk [Transparent implementation of Zygisk]
- https://github.com/jiqiu2022/Zygisk-MyInjector [Zygisk Injector]
- https://github.com/Exo1i/MagiskHluda [Run a more undetectable frida server on boot using magisk]
- https://github.com/MhmRdd/NoHello [A Zygisk module to hide root]
- https://github.com/ys1231/MoveCertificate [A Magisk/KernelSU/APatch module for moving user certificates to system certificates. Supports Android 7-15]
- https://github.com/ri-char/zygisk-dump-dex [A zygisk module that hooks `libdexfile.so` to dump dex]

> Xposed
- https://github.com/NPC2000/AppPealing-new [An Xposed module that disables Inka AppSealing, a popular anti-cheat and anti-root solution]

> Frida
- https://github.com/hackcatml/frida-watchpoint-tutorial [Frida's setHardwareWatchpoint tutorial]
- https://github.com/CrackerCat/strongR-frida-android
- https://github.com/gmh5225/frida-ue4dump [UE4]
- https://github.com/jcalabres/hook-updater [Update Frida hooks automatically]
- https://github.com/gmh5225/frida-boot [A binary instrumentation workshop, with Frida, for beginners]
- https://github.com/smartdone/Frida-Scripts [Some scripts]
- https://github.com/0xdea/frida-scripts [Some scripts]
- https://github.com/SeeFlowerX/frida-smali-trace [Smali trace]
- https://github.com/Ylarod/Florida [anti-detection version of frida-server]
- https://github.com/noobpk/frida-android-hook [Trace classes/functions/and modify the return values]
- https://github.com/apkunpacker/AntiFrida_Bypass [Bypass Some AntiFrida Checks]
- https://github.com/Abbbbbi/Frida-Seccomp [Frida-Seccomp]
- https://github.com/rednaga/frida-stack [Getting better stacks and backtraces in Frida]
- https://github.com/DoranekoSystems/frida-FindoutWhatAccess [Find out what accesses this address]
- https://github.com/piotrbania/frida_usb_dump [Frida script that allows to sniff & dump USB traffic on macOS]
- https://github.com/hackcatml/frida-findJNINativeMethods [Find JNI native methods while the app is running]
- https://github.com/miticollo/xpc-tracer [A tracer based on frida for XPC messages in iOS and macOS]
- https://github.com/0xCD4/SSL-bypass [Root Detection & SSL Bypass Script]
- https://github.com/aimardcr/FridaDetectionBypass [Debugger Detection Bypass]
- https://github.com/seanistethered/FridaScript [Low level scripting app for iOS]
- https://github.com/AsenOsen/frida-stealth [Stealth patch for Frida, stealth knowledge collection]
- https://github.com/Exo1i/MagiskHluda [Run a more undetectable frida server on boot using magisk]
- https://github.com/suifei/fridare [Powerful Frida repackaging tool for iOS and Android. Easily modify Frida servers to enhance stealth and bypass detection]

> Hook ART(android)
- https://github.com/PAGalaxyLab/YAHFA
- https://github.com/canyie/pine

> Hook syscall(android)
- https://github.com/iofomo/abyss [Android system call hook]

> Android Terminal Emulator
- https://github.com/termux/termux-app
- https://github.com/sylirre/neotty
- https://github.com/jackpal/Android-Terminal-Emulator
- https://github.com/NeoTerrm/NeoTerm

> Android File Explorer
- https://github.com/nzcv/note [Guide-zh]
- https://github.com/iBotPeaches/Apktool [A tool for reverse engineering Android apk files]
- https://github.com/AndnixSH/APKToolGUI [GUI for apktool, signapk, zipalign and baksmali utilities]
- https://github.com/pxb1988/dex2jar
- https://github.com/skylot/jadx [Dex to Java decompiler]
- https://github.com/LuckyPray/DexKit-Android [dex deobfuscator]
- https://github.com/LSPosed/DexBuilder [Generate dex file by c++]
- https://github.com/rednaga/APKiD [PEiD for Android]
- https://github.com/APKLab/APKLab [Android Reverse-Engineering Workbench for VS Code]
- https://github.com/pgp/XFiles [File explorer for (rooted) Android]
- https://github.com/gmh5225/AdbFileManager [File manager using ADB protocol]
- https://github.com/MuntashirAkon/AppManager [A full-featured package manager and viewer]
- https://github.com/pgp/XFiles [A general-purpose file explorer for (rooted) Android]
- https://github.com/Raival-e/File-Explorer [An Android file explorer]
- https://github.com/obfusk/apksigcopier [apksigcopier - copy/extract/patch android apk signatures & compare apks]
- https://github.com/loerting/dalvikus [Android reverse-engineering tool / smali editor]

> Android Memory Explorer
- https://github.com/misc0110/PTEditor [PT Editor]
- https://github.com/joaomlneto/procmap
- https://github.com/kp7742/MemDumper [Dump]
- https://github.com/LLeavesG/eBPFDexDumper [DexDumper based eBPF on Android Platform]
- https://github.com/mrcang09/Android-Mem-Edit
- https://github.com/ExploitTheLoop/writemem
- https://github.com/abcz316/rwProcMem33 [Linux read & write process memory module]
- https://github.com/ri-char/rwMem [The fork version of rwProcMem33]
- https://github.com/IAIK/armageddon [Cache attacks on ARM]
- https://github.com/tamirzb/CVE-2021-1961 [CVE RW]
- https://github.com/MJx0/KittyMemory [Runtime code patching]
- https://github.com/gmh5225/KittyMemory-IOS [Runtime code patching for IOS]
- https://github.com/vrolife/mypower [Memory scanner]
- https://github.com/DoranekoSystems/memory_server [Memory scanner & analyzer with REST API]
- https://github.com/KuhakuPixel/AceTheGame [Game Hacking Tools]
- https://github.com/gmh5225/Android-MemoryTool [RPM]
- https://github.com/Anonym0usWork1221/C-Android-Memory-Tool [RPM]
- https://github.com/Poko-Apps/MemKernel [RPM]
- https://github.com/DeNA/mempatch [Memory tampering tool]
- https://github.com/hackcatml/zygisk-memdump [A zygisk module that dumps so file from process memory]
- https://github.com/mrexodia/lldbext-dump [Extension to create a full memory dump using LLDB on Android]
- https://github.com/block/stoic [Run code within any debuggable Android process, without modifying its APK]
- https://github.com/g2wfw/qbdi-tracer-android [Android assembly instruction tracing tool]

> Android Application CVE
- https://github.com/nahid0x1/CVE-2024-0044 [a vulnerability affecting Android version 12 & 13]

> Android Kernel CVE
- https://github.com/ScottyBauer/Android_Kernel_CVE_POCs [List]
- https://github.com/tangsilian/android-vuln [List]
- https://github.com/jiayy/android_vuln_poc-exp [List]
- https://github.com/jsirichai/CVE-2019-2215 [Root for Pixel 2/XL]
- https://github.com/bluefrostsecurity/CVE-2020-0041 [Root for Pixel 3]
- https://github.com/j4nn/CVE-2020-0041 [Root for Pixel 3]
- https://github.com/polygraphene/DirtyPipe-Android [Root for Pixel 6]
- https://github.com/tiann/DirtyPipeRoot [Root for Pixel 6]
- https://github.com/Markakd/bad_io_uring [Root for Pixel 6]
- https://github.com/0x36/Pixel_GPU_Exploit [Root for Pixel7/8 Pro with Android 14]
- https://soez.github.io/posts/CVE-2022-22265-Samsung-npu-driver [Root for Samsung]
- https://github.com/0xbinder/android-kernel-exploitation-lab [CVE-2019-2215]
- https://github.com/zhuowei/cheese [CVE-2025-21479]
- https://github.com/farazsth98/poc-CVE-2025-38352 [CVE-2025-38352]

> Android Bootloader Bypass
- https://github.com/MlgmXyysd/Xiaomi-HyperOS-BootLoader-Bypass [Xiaomi HyperOS BootLoader Bypass]

> Android ROM
- https://xdaforums.com [Guide]
- https://github.com/Akipe/awesome-android-aosp [Guide]
- https://github.com/musabcel/android_rom_list [List]
- https://github.com/vm03/payload_dumper [Android OTA payload dumper]
- https://developer.android.com/studio/run/win-usb [Google USB Driver]
- http://www.miui.com/unlock/download.html [Unlocker for xiaomi]
- https://miuiver.com/miflash [MiFlash]
- https://xiaomifirmwareupdater.com [Xiaomi Firmware Updater]
- https://sourceforge.net/projects/recovery-for-xiaomi-devices/files [TWRP for xiaomi]
- https://github.com/cfig/Android_boot_image_editor [Android ROM tool]
- https://github.com/badabing2005/PixelFlasher [Android ROM tool for Pixel]
- https://github.com/Ctapchuk/android_bootable_recovery-OFRP [OrangeFox Recovery]

> Android Device Trees
- https://github.com/MiCode/kernel_devicetree [xiaomi device trees]
- https://github.com/cupid-development/ [xiaomi device trees]
- https://github.com/PixelOS-AOSP/official_devices [PixelOS device trees]
- https://github.com/ymdzq/OFRP-device_xiaomi_mondrian [OFRP for Redmi K60 (mondrian)]
- https://github.com/flakeforever/device_xiaomi_mondrian [Pixel Experience Plus for for Redmi K6/POCO F5 Pro]

> Android Kernel Source
- https://source.android.com/docs/setup/build/building-kernels [Docs]
- https://android.googlesource.com/kernel/manifest/+refs [manifest]
- https://android.googlesource.com/kernel/manifest [manifest]
- https://android.googlesource.com/kernel/common [GKI]
- https://github.com/aosp-mirror/kernel_common [GKI]
- https://github.com/PixelOS-AOSP/manifest [An AOSP based ROM aiming to provide the best of Pixel]
- https://www.android-x86.org [X86]
- https://blissos.org [X86]
- https://github.com/MiCode/Xiaomi_Kernel_OpenSource [xiaomi kernel]
- https://github.com/xiaomi-sm8450-kernel [xiaomi kernel]
- https://github.com/Danda420/kernel_xiaomi_sm8250 [xiaomi kernel for POCO F3/F4]
- https://github.com/LowTension/android_kernel_xiaomi_sm8475 [Pixel Experience Plus for for Redmi K6/POCO F5 Pro]
- https://github.com/GrapheneOS-Archive/kernel_msm-coral [Pixel 4/4XL/4a]
- https://github.com/msnx/KernelSU-Pixel4XL [KernelSU for Google Pixel4XL]
- https://github.com/universal5433/android_kernel_samsung_universal5433 [samsung 15433]
- https://github.com/SM7325-AE/android_kernel_motorola_dubai [Moto Edge 30]
- https://github.com/mylove90/pc_ginkgo [Redmi Note 8/8T with KernelSU]
- https://github.com/fiqri19102002/android_kernel_xiaomi_sweet [Redmi Note 10 Pro]
- https://github.com/ExWhyZed9/android_kernel_gki_common_5.10 [Redmi Note 11T Pro(+) / POCO X4 GT]
- https://github.com/psavarmattas/android_kernel_oneplus_sm7250-WKSU [KernelSU for Oneplus]
- https://github.com/huawei-mediatek-devs/android_kernel_huawei_mt6761 [huawei mt6761]
- https://github.com/pascua28/android_kernel_samsung_sm7150 [samsung sm7150]
- https://github.com/devhunter1/A146B-KSU [KernelSU for SAMSUNG A14 5G (a14x)]
- https://github.com/utziacre/android_kernel_xiaomi_pipa [Xiaomi Pad 6 kernel]
- https://github.com/utziacre/android_kernel_oneplus_sm8250 [OnePlus 8/8T/8Pro/(9R?) kernel]

> Android Root
- https://github.com/fynks/awesome-android-root [Awesome Android Root]
- https://github.com/topjohnwu/Magisk
- https://github.com/tiann/KernelSU
- https://github.com/riarumoda/KernelSU-4.4 [Adapted for Linux Kernel 4.4 + Google GCC 4.9]
- https://github.com/bmax121/APatch
- https://github.com/lzghzr/APatch_kpm [APatch modules]
- https://github.com/abcz316/SKRoot-linuxKernelRoot
- https://github.com/0x36/Pixel_GPU_Exploit
- https://github.com/0xCD4/SSL-bypass [Root Detection & SSL Bypass Script]

> Android Kernel driver development
- https://github.com/gmh5225/AndroidDriveSignity [Bypass driver signature verification in Android kernel(ARMv8.3)]
- https://github.com/gmh5225/android-kernel-driver-template [A GKI Android kernel driver(AArch64) template]
- https://github.com/dabao1955/kernel_build_action [a action to build kernel automatically]
- https://github.com/TheWildJames/kernel_build_scripts [kernel build scripts]
- https://github.com/fuqiuluo/android-wuwa [Android aarch64 rootkit]
- https://github.com/fuqiuluo/ovo [Android aarch64 kernel driver module providing efficient memory operations, touch simulation and IPC. Features include fast memory remapping]

> Android Kernel Explorer
- https://docs.kernel.org [Linux Kernel documentation]
- https://armv8-ref.codingbelief.com/en [ARM Architecture Reference Manual for ARMv8-A]
- https://github.com/yhnu/op7t [DIY Kernel]
- https://github.com/yabinc/simpleperf_demo [Perf]
- https://github.com/gmh5225/android_ebpf [EBPF]
- https://github.com/PShocker/Android_bpf_sys [EBPF]
- https://github.com/SeeFlowerX/stackplz [EBPF]
- https://github.com/Sh11no/eDBG [eBPF-based lightweight debugger for Android]
- https://github.com/cloudfuzz/android-kernel-exploitation [Android Kernel Exploitation]
- https://github.com/Snoopy-Sec/Localroot-ALL-CVE [Root CVE]
- https://github.com/xmmword/dpatch [Syscall Dispatcher Patching PoC]
- https://github.com/aquasecurity/tracee [Linux Runtime Security and Forensics using eBPF]
- https://github.com/AndroidReverser-Test/Kernel-Trace [A kpm kernel module based on uprobe, capable of simultaneously hooking a large number of user address space functions]
- https://github.com/fuqiuluo/android-wuwa [Android aarch64 rootkit]
- https://github.com/fuqiuluo/rnidbg [An Android-ARM64 kernel emulator written in Rust. (Rewrite from unidbg)]

> Android Kernel Driver
- https://github.com/rogxo/kernel_hack
- https://github.com/Jiang-Night/Kernel_driver_hack
- https://github.com/WeiJiLab/kernel-hook-framework [Kernel inline hook framework]
- https://github.com/Poko-Apps/MemKernel [RPM]

> Android Network Explorer
- https://github.com/emanuele-f/PCAPdroid

> Android memory loading
- https://github.com/icculus/mojoelf
- https://github.com/lockedbyte/so_loader

> IOS jailbreak
- https://github.com/KpwnZ/Def1nit3lyN0tAJa1lbr3akTool [iOS 15.7 and iOS 16.5]
- https://github.com/opa334/Dopamine [iOS 15 and 16]
- https://github.com/roothide/Dopamine2-roothide [iOS 15 and 16]
- https://github.com/felix-pb/kfd [iOS 15 and 16]
- https://github.com/0x36/weightBufs [ANE kernel r/w exploit for iOS 15 and macOS 12]
- https://github.com/jjolano/shadow
- https://github.com/gmh5225/IOS-jailbreak--Fugu15
- https://github.com/Kc57/iHide
- https://github.com/palera1n/palera1n
- https://github.com/checkra1n
- https://github.com/opa334/TrollStore [jailed app]
- https://github.com/paradiseduo/IPAPatch [Patch iOS Apps without Jailbreak]
- https://github.com/34306/mdc0 [CVE-2025-24203]
- https://github.com/jailbreakdotparty/dirtyZero [CVE-2025-24203]
- https://github.com/staturnzz/oob_entry [iOS 3.0-10.3.4 tfp0 kernel exploit]

> IOS Memory Explorer
- https://github.com/hackcatml/kfd-explorer [iOS kernel memory explorer]
- https://github.com/DerekSelander/dynadump [A runtime ObjC class-dump]
- https://github.com/jsherman212/xnuspy [an iOS kernel function hooking framework for checkra1n'able devices]
- https://gist.github.com/gmh5225/95151b245267a27b3cdbea949632c680 [DirtyZero Exp]
- https://github.com/MxIris-Reverse-Engineering/RuntimeViewer [Objective-C Runtime Viewer for macOS and iOS]

> IOS File Explorer
- https://github.com/DerekSelander/dynadump [A runtime ObjC class-dump]
- https://github.com/LaurieWired/Malimite [Malimite is an iOS and macOS decompiler designed to help researchers analyze and decode IPA files and Application Bundles]

> Virtual Environments
- https://github.com/FBlackBox/BlackBox [Android]
- https://github.com/ServenScorpion/VirtualApp [Android]
- https://github.com/mandiant/flare-vm
- https://github.com/hzqst/VmwareHardenedLoader
- https://github.com/d4rksystem/VMwareCloak
- https://github.com/utmapp/UTM [Run virtual machines on iOS]

> Decompiler
- IDA Pro
- Binary Ninja
- https://github.com/radareorg
- https://github.com/NationalSecurityAgency/ghidra
- https://github.com/avast/retdec
- https://github.com/Col-E/Recaf [Java]
- https://github.com/Konloch/bytecode-viewer [Java]
- https://github.com/java-deobfuscator/deobfuscator [Java]
- https://github.com/angr/binsync [Sync]
- https://github.com/crytic/ethersplay [EVM dissassembler]
- https://github.com/Hexorg/Ouroboros [A Symbolic-Execution Decompiler written in Rust]

> IDA themes
- https://github.com/pr701/dp701 [Dark theme for IDA Pro]
- https://github.com/seanwupi/ida-dark-plus [Dark+ Theme]
- https://github.com/ioncodes/long_night
- https://github.com/can1357/IdaThemer

> IDA Plugins
- https://github.com/vmallet/ida-plugins [List of IDA Plugins]
- https://github.com/onethawt/idaplugins-list [List of IDA Plugins]
- https://github.com/williballenthin/idawilli [IDA Pro resources, scripts, and configurations]
- https://github.com/NyaMisty/idasdk-collection/tree/master [IDA SDK]
- https://github.com/HexRaysSA/ida-sdk [IDA SDK]
- https://github.com/zyantific/IDASkins [Skins]
- https://github.com/endofunky/ida-nord-theme [Skins]
- https://github.com/giladreich/ida_migrator [Migrate Database]
- https://github.com/can1357/NtRays [Windows Kernel Enhance]
- https://github.com/JustasMasiulis/ida_bitfields [Windows Kernel Enhance]
- https://github.com/VoidSec/DriverBuddyReloaded [Windows Kernel Analysis]
- https://github.com/jhftss/IDA2Obj [COFF Relink]
- https://github.com/synacktiv/dotNIET [Import .NET Symbol]
- https://github.com/aliyunav/Finger [Recognizing Function By Cloud]
- https://github.com/FelixBer/FindFunc [Recognizing Function By Pattern]
- https://github.com/kweatherman/sigmakerex [Signature Maker]
- https://github.com/A200K/IDA-Pro-SigMaker [Signature Maker]
- https://github.com/mahmoudimus/ida-sigmaker [Signature Maker]
- https://github.com/Mixaill/FakePDB [PDB Generation From IDA]
- https://github.com/illera88/Ponce [Symbolic Execution]
- https://github.com/airbus-cert/ttddbg [Time Travel Debugging]
- https://github.com/P4nda0s/LazyIDA [LazyIDA]
- https://github.com/HappyIDA/HappyIDA [Hex-Rays decompiler utilities: parameter labeling, SEH, Rust strings]
- https://github.com/quarkslab/qsynthesis [Greybox Synthesizer geared for deobfuscation of assembly instructions]
- https://github.com/medigateio/ida_medigate [RTTI]
- https://github.com/OALabs/findyara-ida [Yara]
- https://github.com/therealdreg/ida_vmware_windows_gdb [IDA+VMWARE+GDB]
- https://github.com/therealdreg/ida_bochs_windows [IDA+BOCHS]
- [An integration for IDA and VS Code which connects both to easily execute and debug IDAPython scripts](https://github.com/ioncodes/idacode)
- https://github.com/binarly-io/efiXplorer [UEFI firmware]
- https://github.com/Accenture/protobuf-finder [Protobuf]
- https://github.com/strazzere/golang_loader_assist [GO Reversed]
- https://github.com/GregoryMorse/GhidraDec [Ghidra Decompiler]
- https://github.com/AntoineBlaud/EasyRe [Trace Execution]
- https://github.com/flatz/ida_ps5_elf_plugin [PS5 elf loader]
- https://github.com/gaasedelen/tenet [Execution Traces]
- https://github.com/jiqiu2022/Tenet-IDA9.0 [Execution Traces]
- https://github.com/synacktiv/frinet [Frida-based tracer]
- https://github.com/polymorf/findcrypt-yara [Find crypto constants]
- https://github.com/anatolikalysch/VMAttack [VMAttack PlugIn for IDA Pro]
- https://github.com/cseagle/sk3wldbg [Unicorn]
- https://github.com/RicBent/Classy [Manage classes]
- https://github.com/archercreat/ida_names [Renames pseudocode windows with the current function name]
- https://github.com/helpsystems/turbodiff [diff]
- https://github.com/joxeankoret/diaphora [diff]
- [An IDAPython module for way more convienent way to Reverse Engineering iOS kernelcaches](https://github.com/cellebrite-labs/ida_kcpp)
- https://gitlab.com/eshard/d810 [Deobfuscate code at decompilation time by modifying IDA Pro microcode]
- https://github.com/CKCat/d810 [Deobfuscate code at decompilation time by modifying IDA Pro microcode]
- https://github.com/w00tzenheimer/d810-ng [D-810ng (Next Generation) is an evolution of d810 to deobfuscate code at decompilation time]
- https://github.com/airbus-seclab/AutoResolv [Resolves functions imported from external libraries]
- https://github.com/snare/ida-efiutils [EFI binaries]
- https://github.com/JusticeRage/Gepetto [ChatGPT]
- https://github.com/MayerDaniel/ida_gpt [ChatGPT]
- https://github.com/mahaloz/DAILA [ChatGPT]
- https://github.com/ke0z/VulChatGPT [ChatGPT]
- https://github.com/WPeace-HcH/WPeChatGPT [ChatGPT]
- https://github.com/lzyddf/IDA_Plugin_PCodeGPT [ChatGPT]
- https://github.com/deadeert/EWS [Emulation]
- https://github.com/patois/genmc [Display Hex-Rays Microcode]
- https://github.com/RolfRolles/HexRaysDeob [Hex-Rays Microcode]
- https://github.com/HexRaysSA/goomba [Simplify MBA]
- https://github.com/es3n1n/ida-wakatime-py [WakaTime integration for IDA Pro]
- https://github.com/senator715/IDA-Fusion [Fast Signature scanner & creator]
- https://github.com/cellebrite-labs/PPLorer [Resolves PPL calls to the actual underlying PPL function]
- https://github.com/kweatherman/ida_missinglink [Fills in missing indirect CALL & JMP target information]
- https://github.com/yubie-re/ida-jm-xorstr-decrypt-plugin [Attempts to decrypt JM Xorstr in some x64 binaries]
- https://github.com/timetravelthree/IDARustDemangler [Rust Demangler & Normalizer]
- https://github.com/gmh5225/ida-find-.data-ptr [.data ptr lookup script]
- https://github.com/repnz/ida-plugins [Register Cross References]
- https://github.com/lstaroth/AntiXorstr [Anti Xorstr]
- https://github.com/SentineLabs/AlphaGolang [Analyzing Golang Binaries]
- https://github.com/tmr232/Sark [IDAPython Made Easy]
- https://github.com/govcert-ch/ConfuserEx_IDAPython [Deobfuscation script for ConfuserEx]
- https://github.com/sonyps5201314/pdb [PDB plugin with enhance and bugfix]
- https://github.com/Coldzer0/IDA-For-Delphi [IDA-For-Delphi]
- https://github.com/AntonKukoba1/BetterCallStack [Improve call stack]
- https://github.com/za233/IDADeflat [deflat]
- https://github.com/RomanRybachek/Copy_RVA [Copy RVA]
- https://github.com/RevEngAI/reai-ida [RevEng.AI]
- https://github.com/gaasedelen/microavx [AVX Lifter]
- https://github.com/thalium/ida_kmdf [IDA kmdf]
- https://github.com/zengfr/XrefsExt [XrefsExt plugin]
- https://github.com/sterrasec/genpatch [Python script for patching binary]
- https://github.com/AzzOnFire/yarka [YARA signature creation]
- https://github.com/VirusTotal/vt-ida-plugin [VirusTotal plugin]
- https://github.com/crifan/AutoRename [Auto rename symbol]
- https://github.com/LAC-Japan/IDA_Plugin_AntiDebugSeeker [Extract anti-debugging]
- https://github.com/cseagle/blc [Integrate Ghidra's decompiler]
- https://github.com/Goatman13/ps2_ida_vu_micro [Find and disassembly vu microcode in ps2 executables]
- https://github.com/arizvisa/ida-minsc [Functional DWIM interface]
- https://github.com/wINfOG/IDA_Easy_Life [Deobfuscation]
- https://github.com/senko37/yarascan-ida [Scan file with Yara rules]
- https://github.com/SamuelTulach/ida-unity-pdb-downloader [Unity PDB Downloader]
- https://github.com/TrungNguyen1909/aarch64-sysreg-ida [A IDA plugin to show ARM MSRs nicely]
- https://github.com/danielplohmann/gui-plugin-template [A template for cross-compatible GUI plugins]
- https://github.com/gmh5225/IDA-MapSymbolParser [IDA Map File Symbol Renamer]
- https://github.com/gmh5225/IDA-KallsymsSymbolRenamer [IDA kallsyms Renamer]
- https://github.com/XMCVE/import-kallsyms [IDA Pro Plugin to import /proc/kallsyms for Linux Kernel]
- https://github.com/tomrus88/OpenLumina [Allows connecting to third party Lumina servers]
- https://github.com/stuxnet147/IDA-Assistant [Claude-3 models assistant]
- https://github.com/goseungduk/CE_Tracer-IDA [CheatEngine Value Tracer of IDA]
- https://github.com/binarly-io/idapcode [Displaying the P-Code for the current function]
- https://github.com/ElvisBlue/emotet-deobfuscator [IDA plugin to deobfuscate emotet CFF]
- https://github.com/threatlabz/pikabot-deobfuscator [Deobfuscating Pikabot's strings using RC4 and AES]
- https://github.com/Pycatchown/ClassMaker [IDA plugin to make classes automatically]
- https://github.com/airbus-cert/comida [An IDA Plugin that help analyzing module that use COM]
- https://github.com/Sandspeare/ida2llvm [Lifting IDA Microcode into LLVM IR]
- https://github.com/crtdll/ida-gameguard-str-dec [GameGuard String Decryption]
- https://github.com/kkent030315/IDARustCargo [Displaying potentially installed Cargo dependencies]
- https://github.com/dNop90/dOffset [IDA Pro and Cheat Engine to get the offset of the current module]
- https://github.com/sneakyevil/ida_functioncolor [IDA Plugin to colorize function definition in pseudocode]
- https://github.com/apkunpacker/IDA-Gepetto [IDA plugin which queries Local language models]
- https://github.com/Jackiemin233/Gemini-Genius [IDA python 3 plugin and binary file similarity comparison]
- https://github.com/lj94093/IDAAndroidBreakpoint [IDA plugin aid to set android so breakpoint]
- https://github.com/jonpalmisc/ida_screenshot [High-resolution screenshot capture plugin for IDA Pro]
- https://github.com/JANlittle/IDARustHelper [Small rust binary analysis helper for IDA]
- https://github.com/mefistotelis/ida-pro-loadmap [Plugin for IDA Pro disassembler which allows loading .map files]
- https://github.com/OALabs/hashdb-ida [HashDB API hash lookup plugin for IDA Pro]
- https://github.com/Vu1nT0tal/firmeye [IoT]
- https://github.com/sean2077/big5-decode-ida [IDA Plugin for decoding bytes as big5]
- https://github.com/Vis-Wing/Binoculars [Binoculars is an IDA PRO plugin with an integrated AI interface]
- https://github.com/Reodus/CBS [IDA Plugin to set custom breakpoints on mnemonics]
- https://github.com/matteyeux/IDArling [IDArling is a collaborative reverse engineering plugin for IDA Pro and Hex-Rays]
- https://github.com/richor1042/IDAFuncOutline [optimize the readability of decompiled code for iOS ARM64 binaries]
- https://github.com/Dump-GUY/IDA_PHNT_TYPES [Converted phnt to IDA TIL, IDC (Hex-Rays)]
- https://github.com/Mrack/DeObfBR [libtprt.so]
- https://github.com/janisslsm/ida-ps4-helper [A helper plugin for PS4 module loader]
- https://github.com/Antelcat/ida_copilot [ChatGPT Agent analyses your IDA pseudocode]
- https://github.com/crytic/ida-evm [IDA Processor Module for the Ethereum Virtual Machine (EVM)]
- https://github.com/NoneShell/IDAComments [a IDA plugin helps you to manage your IDA Comments]
- https://github.com/emoose/idaxex [Xbox360/Xenon loader plugin for IDA 9]
- https://github.com/junron/auto-enum [automatically identify and set enums for standard functions]
- https://github.com/ViRb3/swift-ida [IDA plugin to aid with Swift reverse engineering]
- https://github.com/Krietz7/IDA-DataExportPlus [a IDA Pro plugin to export data better]
- https://github.com/harlamism/IdaClu [For grouping similar functions]
- https://github.com/eset/DelphiHelper [help the analysis of x86/x86_64 binaries written in Delphi]
- https://github.com/milankovo/YaraVM [IDA processor for loading and disassembling compiled yara rules]
- https://github.com/cellebrite-labs/LabSync [An IDA plugin that can be used to partially synchronize IDBs between different users reversing the same binaries]
- https://github.com/cellebrite-labs/FunctionInliner [An IDA plugin that eases reversing of binaries that have been code-size-optimized with function outlining]
- https://github.com/herosi/PyClassInformer [RTTI Parsing IDA plugin]
- https://github.com/0xGotcha/XrefXpert [An advanced cross-reference navigation tool for IDA Pro]
- https://github.com/TKazer/ScyllaHide-For-IDA9.0RC [ScyllaHide-For-IDA9]
- https://github.com/mrexodia/ida-pro-mcp [MCP for IDA pro]
- https://github.com/MxIris-Reverse-Engineering/ida-mcp-server [MCP for IDA pro]
- https://github.com/taida957789/ida-mcp-server-plugin [MCP for IDA pro]
- https://github.com/fdrechsler/mcp-server-idapro [MCP for IDA pro]
- https://github.com/rand-tech/pcm [MCP for IDA pro]
- https://github.com/gmh5225/ida_export_functions [Export IDA Pro Function List to a Specified Path (Markdown Format)]
- https://github.com/L4ys/IDA-WPP-Remover [Remove WPP calls from hexrays decompiled code]
- https://github.com/0xdea/augur [Augur is a blazing fast IDA Pro headless plugin that extracts strings and related pseudo-code from a binary file]
- https://github.com/DennyDai/headless-ida [Run IDA scripts headlessly]
- https://github.com/gilboz/ida_kernelcache_ng [An IDA Plugin for analyzing iOS kernelcaches]
- https://github.com/mahmoudimus/ida-taskr [IDA Taskr is a pure Python library for IDA Pro related parallel computing]
- https://github.com/sigwl/AiDA [An AI-powered assistant for IDA 9.0+ to accelerate reverse engineering of C++ games]
- https://github.com/alexhude/FRIEND [FRIEND is an IDA plugin created to improve disassembly and bring register/instruction documentation right into IDA View]
- https://github.com/cycraft-corp/BinaryAnalysisMCPs [Binary analysis MCPs collections]
- https://github.com/SamuelTulach/unxorer [Yet another IDA Pro/Home plugin for deobfuscating stack strings]
- https://github.com/loyaltypollution/ida2llvm [IDA2LLVM - Dynamic Binary Lifting IDA code to LLVM IR]
- https://github.com/GAMMACASE/PltPatcher [Patches PLT sections when IDA fails to do so]
- https://github.com/yoavst/ida-ios-helper [Plugin to ease reversing iOS projects]
- https://github.com/poppopjmp/VMDragonSlayer [Advanced Virtual Machine Detection and Analysis Framework]
- https://github.com/milankovo/ida_enums_helper [IDA Enums Helper Plugin]
- https://github.com/axelmierczuk/tenrec [A headless, extendable, multi-session, IDA Pro MCP framework]
- https://github.com/blacktop/ida-mcp-rs [Headless IDA Pro MCP server]
- https://github.com/kweatherman/yara4ida [Unofficial YARA IDA Pro plugin]
- https://github.com/Berk000x/BinaryLens [An IDA plugin that uses LLM to speed up binary analysis]
- https://github.com/CyberSecurityUP/DriverVuln-Analyzer-IDA-Plugin [Driver Vuln Analyzer]
- https://github.com/ssmugabi/IDAPlugins [Integrate essential IDA Pro plugins for enhanced functionality, including deobfuscation, binary diffing, and custom cryptography support]
- https://github.com/momo5502/patch-finder [IDA plugin to find patched memory]
- https://github.com/HexRaysSA/ida-cyberchef [A Qt-based CyberChef interface designed for malware analysis workflows, particularly in IDA Pro]
- https://github.com/idkhidden/DrawIDA [Lightweight whiteboard plugin for IDA that allows reverse engineers to sketch and brainstorm directly inside IDA]
- https://github.com/rem0obb/rtti-parser [IDA script to parse RTTI information in executable support for IDA 9.2]
- https://github.com/19h/ida-semray [High-performance, AI-driven semantic analysis for the IDA Pro decompiler]
- https://github.com/K4ryuu/IDA-VTableExplorer [C++ virtual table detection and annotation tool for IDA Pro 9.x]
- https://github.com/19h/chernobog [A Hex-Rays IDA Pro plugin for deobfuscating binaries protected with the Hikari LLVM obfuscator]
- https://github.com/danielplohmann/mcrit-plugin [A plugin to use MCRIT from IDA Pro]
- https://github.com/dyussekeyev/ida-spotlight [Workflow-centric function triage and prioritization plugin for IDA Pro]
- https://github.com/s3rg0x/AIMachDec [AIMachDec is an IDA plugin for Apple AARCH64/ARM64 binaries that utilizes LLMs to translate assembly functions into readable pseudo-code in C, Objective-C, or Swift]
- https://github.com/not1cyyy/Kiroshi [An IDA Pro Plugin to detect common Anti-Cheat Artifacts]
- https://github.com/HexRaysSA/ida-claude-code-plugins [IDA Claude Code Plugins]
- https://github.com/stolevchristian/LUDA [Lua scripting plugin for IDA Pro]
- https://github.com/allthingsida/idasql [Interface with IDA in SQL via live virtual tables]
- https://github.com/a1ext/auto_re [IDA PRO auto-renaming plugin with tagging support]
- https://github.com/SymbioticSec/ida-security-scanner [A security-focused code scanner for IDA Pro]
- https://github.com/cristeigabriela/IDAFind [Ctrl+F search support for Pseudocode windows]
- https://github.com/thalium/symless [IDA Pro plugin that helps reconstruct structures]

> IDA Signature Database
- https://github.com/push0ebp/sig-database

> Binary Ninja Plugins
- https://github.com/Vector35/official-plugins
- https://github.com/Vector35/community-plugins
- https://github.com/FuzzySecurity/BinaryNinja-Themes [Theme]
- https://github.com/EliseZeroTwo/SEH-Helper [SEH Helper]
- https://github.com/Vector35/tanto [Slices Functions]
- https://github.com/ergrelet/triton-bn [Triton]
- https://github.com/google/binexport [BinDiff]
- https://github.com/Pusty/BinaryNinjaPlugins
- https://github.com/borzacchiello/seninja [Symbolic Execution]
- https://github.com/yellowbyte/opaque-predicates-detective
- https://github.com/ex0dus-0x/fuzzable [Fuzzer]
- https://github.com/jmprdi/binja-division-deoptimization [Division and Modulo Deoptimizer]
- https://github.com/Vector35/OpaquePredicatePatcher [Opaque Predicate Patcher]
- https://github.com/jmprdi/binja-division-deoptimization [Division and Modulo Deoptimizer]
- https://github.com/mrphrazer/obfuscation_detection [Collection of scripts to pinpoint obfuscated code]
- [Package Binary Code as a Python class using Binary Ninja and Unicorn Engine](https://github.com/pbiernat/ripr)
- https://github.com/seeinglogic/ariadne [Graph Analysis]
- https://github.com/skr0x1c0/binja_kc [Plugin for loading MachO kernelcache and dSYM files]
- https://github.com/Vector35/workflow_objc [Objective-C]
- https://github.com/apekros/binja_sigmaker [Create and find signatures]
- https://github.com/dayzerosec/AMD-SP-Loader [AMD-SP or PSP firmware]
- https://github.com/WhatTheFuzz/binaryninja-openai [Integrates OpenAI]
- https://github.com/dzervas/frinja [Frida plugin for Binary Ninja]
- https://github.com/danielplohmann/gui-plugin-template [A template for cross-compatible GUI plugins]
- https://github.com/ergrelet/themida-spotter-bn [Detect Themida/WinLicense and Code Virtualizer's obfuscated code locations]
- https://github.com/ahaggard2013/binaryninja-ollama [Binary Ninja Ollama]
- https://github.com/0xricksanchez/Shellcoder [BinaryNinja Shellcoder Plugin]
- https://github.com/pd0wm/binaryninja-pcode [This plugin serves as a bridge between Binary Ninja and Ghidra's disassembler]
- https://github.com/zhuzhu-Top/deobf [libtprt.so]
- https://github.com/junron/auto-enum [automatically identify and set enums for standard functions]
- https://github.com/otter-sec/bn-ebpf-solana [Binary Ninja plugin for Solana eBPF]
- https://github.com/fosdickio/binary_ninja_mcp [MCP for Binary_Ninja]
- https://github.com/Invoke-RE/binja-lattice-mcp [MCP for Binary_Ninja]
- https://github.com/mrphrazer/obfuscation_analysis [Binary Ninja plugin to analyze and simplify obfuscated code]
- https://github.com/ScriptWare-Software/native-predicate-solver [Binary Ninja plugin for removing opaque predicates]

> Ghidra Plugins
- https://github.com/AllsafeCyberSecurity/awesome-ghidra [List]
- https://github.com/CENSUS/ghidra-frida-hook-gen
- https://github.com/Gekkio/GhidraBoy [Sharp SM83 / Game Boy extension for Ghidra]
- https://github.com/fmagin/ghidra-openai [ChatGPT]
- https://github.com/securityjoes/ThreatResearch [ChatGPT]
- https://github.com/evyatar9/GptHidra [ChatGPT]
- https://github.com/moyix/gpt-wpre [ChatGPT]
- https://github.com/pudii/gba-ghidra-loader [GameBoy]
- https://github.com/MEhrn00/Ghidra_COFFParser [COFF]
- https://github.com/ghidragolf/ghidra_scripts [Scripts]
- https://github.com/PAGalaxyLab/ghidra_scripts [Scripts]
- https://github.com/danbrodsky/GFred [Command Palette]
- https://github.com/Nalen98/AngryGhidra [Use angr in Ghidra]
- https://github.com/justfoxing/ghidra_bridge [Python 3 bridge to Ghidra's Python scripting]
- https://github.com/astrelsky/GhidraOrbis [Orbis OS specific software and file formats]
- https://github.com/astrelsky/Ghidra-Cpp-Class-Analyzer [C++ Class and Run Time Type Information Analyzer]
- https://github.com/DMaroo/GhidRust [Rust decompiler]
- https://github.com/Comsecuris/gdbghidra [GDB session]
- https://github.com/hyuunnn/Hyara [Yara]
- https://github.com/Deatty/Ghidra-Obfuscation-Detection [Detect obfuscated/complex code]
- https://github.com/advanced-threat-research/GhidraScripts [Some scripts]
- https://github.com/fuzzypickles14/BetterStringAnalyzer [A better string analyzer for Ghidra]
- https://github.com/clearbluejar/ghidriff [Python Command-Line Ghidra Binary Diffing Engine]
- https://github.com/Katharsas/ghidra-struct-importer [Struct Importer]
- https://github.com/danielplohmann/gui-plugin-template [A template for cross-compatible GUI plugins]
- https://github.com/astrelsky/GhidraGradlePlugin [Gradle]
- https://github.com/jtang613/GhidrAssist [An LLM extension for Ghidra to enable AI assistance in RE]
- https://github.com/DSecurity/efiSeek [Ghidra analyzer for UEFI firmware]
- https://github.com/LaurieWired/GhidraMCP [MCP for Ghidra]
- https://github.com/Rantanen/ghidra-minidump-loader [Windows Minidump loader for Ghidra]
- https://github.com/jtang613/GhidrAssistMCP [An MCP extension for Ghidra]
- https://github.com/poppopjmp/VMDragonSlayer [Advanced Virtual Machine Detection and Analysis Framework]

> Radare Plugins
- https://github.com/radareorg/r2a [local language model for radare2]
- https://github.com/radareorg/radius2 [Fast binary emulation and symbolic execution framework using radare2]
- https://github.com/seifreed/r2morph [A metamorphic binary transformation engine based on r2pipe and radare2]

> Windbg Plugins
- https://github.com/comaeio/SwishDbgExt
- https://github.com/lowleveldesign/comon [Trace COM]
- https://github.com/bruce30262/TWindbg [PEDA-like debugger UI for WinDbg]
- https://github.com/JKornev/cfgdump [Analyze Control Flow Guard map]
- https://github.com/yardenshafir/WinDbg_Scripts [WinDbg scripts]
- https://github.com/long123king/dk [Refactored version of tokenext]
- https://github.com/ch3rn0byl/WinDbg-Extensions [Callback Extension]
- https://github.com/KasperskyLab/WinDbg-JS-Scripts [JS Scripts]
- https://github.com/DumpAnalysis/WinDbg_Copilot [WinDbg Copilot]
- https://github.com/eversinc33/drvtrace [Trace driver module transitions]

> X64DBG Plugins
- https://github.com/x64dbg/x64dbg/wiki/Plugins
- https://github.com/horsicq/x64dbg-Plugin-Manager
- https://github.com/m417z/Multiline-Ultimate-Assembler
- https://github.com/x64dbg/Classroom
- https://github.com/VenTaz/Themidie
- https://github.com/Ahmadmansoor/x64dbgScript
- https://github.com/push0ebp/xMalHunter [Detect malicious materials]
- https://github.com/morsisko/xFindOut
- https://github.com/jdavidberger/chaiScriptPlugin
- https://github.com/gmh5225/X64DBG-ViewDllNotification
- https://github.com/legendabrn/AutoAttach
- https://github.com/secrary/idenLib [Generate signatures]
- https://github.com/GregoryMorse/GhidraDec [Ghidra Decompiler]
- https://github.com/x64dbg/x64dbgbinja [Binary Ninja]
- https://github.com/DNLINYJ/Anti_miHoYo_Jcc_Obfuscate
- https://github.com/mrexodia/DisableParallelLoader [Disable parallel loading of dependencies]
- https://github.com/ElvisBlue/x64dbgpython [Running python3 script]
- https://github.com/secrary/idenLibX [Library Function Identification]
- https://github.com/x64dbg/SlothBP [Collaborative Breakpoint Manager]
- https://github.com/Kwansy98/ApiBreakpoint [Api Breakpoint]
- https://github.com/0ffffffffh/yummyPaste [paste string formatted byte data block into x64dbg easy]
- https://github.com/horsicq/x64dbg-Plugin-Manager [Plugin manager for x64dbg]
- https://github.com/ZehMatt/x64dbgPlaytime [Lua script]
- https://github.com/milcert/ExpoMon [Exports monitoring]
- https://github.com/m417z/x64dbg-xfg-marker [Marks XFG call signatures as data]
- https://github.com/Kwansy98/x64dbgCallFinder [Call Finder]
- https://github.com/gmh5225/X64DBG-MapLdr [Loads the map file generated by IDA Pro]
- https://github.com/mibho/x64dbgTraceReader [Trace Reader]
- https://github.com/Steesha/CodeCleaner [Cleaning Themida Mutation Assembly codes]
- https://github.com/notpidgey/ManyTypes [x64dbg typeparsing plugin with Windows types]
- https://github.com/cycraft-corp/BinaryAnalysisMCPs [Binary analysis MCPs collections]

> Cheat Engine Plugins
- https://github.com/FreeER/CE-Extensions [Lua Extensions]
- https://github.com/Skyrimfus/CE-lua-extensions [Lua Extensions]
- https://github.com/bbfox0703/Mydev-Cheat-Engine-Tables [CT]
- https://github.com/inuNorii/Elden-Ring-CT-TGA [Elden Ring]
- https://github.com/gmh5225/CE-remap-plugin [Remap]
- https://github.com/gmh5225/overwatch-iat-fixer [Overwatch IAT Fixer]
- https://github.com/FreeER/CE-Examples [Some Examples]
- [Porting ce's monodatacollector to android/ios](https://github.com/gmh5225/frida-il2cpp-datacollector)
- https://github.com/DoranekoSystems/wasm-ceserver [Analyzing WebAssembly]
- https://github.com/Eruditi/CE-MCP-Plugin [MCP for Cheat Engine]

> Injection:Windows
- https://github.com/itaymigdal/awesome-injection [awesome injection]
- https://github.com/btbd/smap [Scatter Manual Map]
- https://github.com/btbd/modmap [Extend Manual Map]
- https://github.com/KGB-1337/memmap [Extend Manual Map]
- https://github.com/weak1337/ModExMap [Extend Manual Map]
- https://github.com/mactec0/Kernelmode-manual-mapping-through-IAT [IAT Manual Map]
- https://github.com/charliewolfe/Stealthy-Kernelmode-Injector [PTE/VAD Manipulation Manual Map]
- https://github.com/wbenny/injdrv [APC]
- https://github.com/alexkrnl/Kernel-dll-injector [APC]
- https://github.com/w1u0u1/kinject [Map + APC]
- https://github.com/1401199262/RemoteCall [APC Remote Call]
- https://github.com/TheCruZ/Simple-Manual-Map-Injector [Manual Map]
- https://github.com/andrew9382/manual_mapping_dll_injector [Manual Map]
- https://github.com/danielkrupinski/MemJect [Manual Map]
- https://github.com/can1357/ThePerfectInjector [PTE.User]
- https://github.com/dumbasPL/fumo_loader [PTE.User]
- https://github.com/estimated1337/executor [PTE.User]
- https://github.com/Nou4r/PresentInjector [PTE.User]
- https://github.com/JGonz1337/kernel-eac-be-injector [PTE.User]
- https://github.com/Cr4sh/KernelForge [Hijack ROP]
- https://github.com/Compiled-Code/be-injector [Attack COW]
- https://github.com/ergrelet/dll-hot-reload [Hot Reload]
- https://github.com/ExpLife0011/KeUserModeCallBack [KeUserModeCallBack]
- [KeUserModeCallBack Win10](https://github.com/Splitx12/eft/blob/834064aacaab7353173e36acc15933a3cf9289b3/eft/usercallback.h#L50)
- https://github.com/YouNeverKnow00/Kernelmode-DLL-Injector [Manual Map]
- [windows kernelmode driver to inject dll into each and every process and perform systemwide function hooking](https://github.com/sum-catnip/kptnhook)
- https://github.com/Broihon/GH-Injector-Library [inject library and tool]
- https://github.com/5paceman/nightshade [inject tool]
- https://github.com/deepinstinct/Dirty-Vanity [RtlCreateProcessReflection]
- https://github.com/LloydLabs/ntqueueapcthreadex-ntdll-gadget-injection [NtQueueApcThreadEx + gadget]
- https://github.com/S12cybersecurity/FrankensteinAPCInjection [NtQueueApcThreadEx2 + existing handles & natural RWX]
- https://github.com/3xpl01tc0d3r/ProcessInjection [Various process injection techniques]
- https://github.com/zorftw/lsass-extend-mapper [Manual mapper from LSASS]
- https://github.com/zorftw/revert-mapper [Map x64 DLLs in WoW64]
- https://github.com/SDXT/MMInject [Using NX Bit Swapping and VAD hide]
- https://github.com/Fahersto/code_injection [Several code injection techniques]
- https://github.com/KameronHawk/Kernel-VAD-Injector [Hide VAD]
- https://github.com/nettitude/Tartarus-TpAllocInject [TpAllocInject]
- https://github.com/SafeBreach-Labs/PoolParty [ThreadPool]
- https://github.com/hasherezade/thread_namecalling [SetThreadDescription]
- https://github.com/Cracked5pider/earlycascade-injection [Early Cascade Injection]
- https://github.com/0xPrimo/KMDllInjector [kernel-mode DLL Injector]
- https://github.com/mohanad1-maker/StealthAPCDispatcher [Thread scheduling stealth method using APC with encrypted shellcode]
- https://github.com/isiddique2024/Page-Table-Injector [Page Table Injector (PT-Injector)]
- https://github.com/xan105/Mini-Launcher [Application launcher with DLL Injection and Lua Scripting]

> Injection:Linux
- https://github.com/itaymigdal/awesome-injection [awesome injection]
- https://github.com/ixty/mandibule

> Injection:Android
- https://github.com/gmh5225/Android-ModGamesByInjectZygote
- https://github.com/gmh5225/Android-DLL-Injector
- https://github.com/reveny/Android-Ptrace-Injector
- https://github.com/reveny/Android-LD-Preload-Injector
- https://github.com/ohchase/yaui
- https://github.com/cs1ime/AndroidSuperInject [Injecting into SELinux-protected system service processes]
- https://github.com/erfur/linjector-rs [Code injection on Android without ptrace]
- https://github.com/NepMods/InjectARM64 [Non-root injection]
- https://github.com/reveny/Android-Virtual-Inject [Inject through Virtual Space without root permissions]

> Injection:IOS
- https://github.com/opa334/opainject [iOS runtime dylib injection tool]

> Injection:PlayStation
- https://github.com/buzzer-re/NineS [A PlayStation 5 ELF injector]


> DLL Hijack
- https://github.com/Sh0ckFR/DLLirant [Hijacking researches]
- https://github.com/redteamsocietegenerale/DLLirant [Hijacking researches Tool]
- https://github.com/knight0x07/ImpulsiveDLLHijack [Hijacking researches]
- https://github.com/wietze/HijackLibs [Project for tracking publicly disclosed DLL Hijacking opportunities]
- https://github.com/gmh5225/DLL-Hijack-ExportDumper [Dump the export table of PE files]
- https://github.com/cyberark/DLLSpy [DLL Hijacking Detection Tool]
- [Project for identifying executables and DLLs vulnerable to relative path DLL hijacking](https://github.com/wietze/windows-dll-hijacking)
- https://github.com/anhkgg/SuperDllHijack [A general DLL hijack technology]
- https://github.com/ctxis/DLLHSC [DLL Hijack SCanner]

> Hook
- https://github.com/stars/gmh5225/lists/hook [Lists]
- https://github.com/microsoft/Detours
- https://github.com/wbenny/DetoursNT
- https://github.com/kalhotky/ntminhook [A modified version of MinHook that only uses the Windows Native API]
- https://github.com/stevemk14ebr/PolyHook
- https://github.com/stevemk14ebr/PolyHook_2_0
- https://github.com/WopsS/RenHook
- https://github.com/bmax121/KernelPatch [Hooking the Linux kernel]
- https://github.com/Zeex/subhook
- https://github.com/axhlzy/PyAsmPatch
- https://github.com/gmh5225/Driver-KDtour [Easy Kernel Detour]
- https://github.com/nelfo/PGHooker [Page Guard]
- https://github.com/weak1337/SkipHook [Skip Hook]
- https://github.com/0mdi/edgegdi_hook [gdi32 .data swap]
- https://github.com/noobpk/frida-android-hook [frida hook for android]
- https://github.com/SamuelTulach/LightHook [cross-platform hook library]
- https://github.com/3intermute/arm64_silent_syscall_hook [ARM64 Patching exception handler]
- https://github.com/kubo/plthook [PLT(Procedure Linkage Table) hook]
- https://github.com/WeiJiLab/kernel-hook-framework [linux kernel inline hook framework]
- https://github.com/Rprop/And64InlineHook [Android ARMv8 inline hook framework]
- https://github.com/GToad/Android_Inline_Hook_ARM64 [Android ARMv8 inline hook framework]
- https://github.com/BossKoopa/BWSR [Arm64 inline hooking for iOS, Android, OSX, and Linux]
- https://github.com/regomne/ilhook-rs [Rust x86]
- https://github.com/iofomo/abyss [Android system call hook]
- https://github.com/jsherman212/xnuspy [an iOS kernel function hooking framework for checkra1n'able devices]

> ROP Finder
- https://github.com/0vercl0k/rp [rp++ is a fast C++ ROP gadget finder for PE/ELF/Mach-O x86/x64/ARM/ARM64 binaries]
- https://github.com/JonathanSalwan/ROPgadget [This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation]
- https://github.com/helpsystems/Agafi [A gadget finder and a ROP-Chainer tool for x86 platforms]
- https://github.com/hugsy/ropgadget-rs [Another (bad) ROP gadget finder, but this time in Rust]
- https://github.com/Boyan-MILANOV/ropium [ROPium is a tool that helps you building ROP exploits by finding and chaining gadgets together]
- https://github.com/angr/angrop [angrop is a rop gadget finder and chain builder]

> ROP Generation
- https://github.com/d4em0n/exrop

> Anti Signature Scanning
- https://github.com/scrt/avdebugger

> RPM
- https://github.com/btbd/access
- https://github.com/crvvdev/intraceptor [access]
- https://github.com/juniorjacob/readwrite-kernel-stable
- https://github.com/DarthTon/Blackbone
- https://github.com/HoShiMin/Kernel-Bridge
- https://github.com/waryas/EUPMAccess
- https://github.com/waryas/UMPMLib
- https://github.com/EBalloon/Remap [Clone process]
- https://github.com/TheCruZ/EFI_Driver_Access [EFI RPM]
- https://github.com/SamuelTulach/efi-memory [EFI RPM]
- https://github.com/ekknod/SubGetVariable [EFI RPM]
- https://www.unknowncheats.me/forum/anti-cheat-bypass/489305-read-write-process-attach.html
- https://www.unknowncheats.me/forum/anti-cheat-bypass/444289-read-process-physical-memory-attach.html
- https://github.com/gamozolabs/mempeek [Linux]
- https://github.com/SamuelTulach/meme-rw [kdmapper]
- https://github.com/gmh5225/Driver-RPM-DirectPageManipulation [read physical memory]
- https://github.com/btbd/ddma [Disk based DMA for ATA and SCSI]
- https://github.com/gmh5225/DDMA-1 [Disk based DMA for ATA and SCSI]
- https://github.com/ekknod/vm [Minimal memory library for Windows/Linux]
- https://github.com/ALittlePatate/TaxiDriver [W/RPM Driver and usermode for Linux]
- https://github.com/gmh5225/Android-MemoryTool [RPM for Android]
- https://github.com/Poko-Apps/MemKernel [RPM for Android]
- https://github.com/Anonym0usWork1221/C-Android-Memory-Tool [RPM for Android]
- https://github.com/0xenia/remem [RPM for Windows]
- https://github.com/un4ckn0wl3z/DMAInvoker [DMA RPM for Windows]
- https://github.com/Vekor64/Driver-physical-rw [Kernel-mode W/RPM for Windows]
- https://github.com/nbqofficial/norsefire [Kernel-mode W/RPM/mouse_event for Windows]
- https://github.com/M3351AN/Shirakumo [RPM for Windows]
- https://github.com/M3351AN/Usugumo [Kernel-mode W/RPM/mouse_event for Windows]
- https://github.com/waryas/WaryasSWHE [Usermode exploit to bypass any AC using a 0day shatter attack]

> DMA
- https://github.com/JPShag/DMA-FW-Guide-2.0 [Guide]
- https://github.com/Rakeshmonkee/DMA [Guide]
- https://github.com/PacktPublishing/Learn-FPGA-Programming [Guide]
- https://github.com/enjoy-digital/litepcie [Small footprint and configurable PCIe core]
- https://github.com/cakehonolulu/pciem [A Linux framework for synthetic PCIe device emulation entirely in userspace]
- https://github.com/ufrisk/pcileech
- https://github.com/ekknod/pcileech-wifi [pcileech-fpga with wireless card emulation]
- https://github.com/Cr4sh/pico_dma
- https://github.com/kWAYTV/dma-cheat-base [Cheat base]
- https://github.com/Spuckwaffel/DMALib [DMA library]
- https://github.com/Metick/DMALibrary [DMA library]
- https://github.com/ekknod/vm [Minimal memory library for Windows/Linux]
- https://github.com/imerzan/ReClass-DMA [ReClass DMA]
- https://github.com/Metick/CheatEngine-DMA [CheatEngine DMA]
- https://github.com/kaijia2022/Cheat-Engine-DMA-Plugin [CheatEngine DMA]
- https://github.com/un4ckn0wl3z/DMACheatEngineLoader [CheatEngine DMA, not open-source]
- https://github.com/bbgsm/MemTools [Windows/Linux DMA testing tools]
- https://github.com/sonodima/physpatch [Scanning and patching of the entire Windows Kernel using DMA]
- https://github.com/gmh5225/DMA-PCIE-BOARD-75T [DMA-PCIE-BOARD-75T]
- https://github.com/gmh5225/DMA-E3100-CFW-BYPASS [DMA-BYPASS-Killer]
- https://github.com/dom0ng/pcileech-wifi-v2 [pcileech-fpga with wireless card emulation]
- https://github.com/Trustings/DMA_PE_Dumper [DMA PE (Portable Executable) Dumper with DTB patching capabilities]
- https://github.com/mltpig/PCILeech-FPGA-DMA_VMD [PCILeech FPGA DMA VMD Controller Simulation Project]
- https://github.com/Herooyyy/Free-DMA-Firmware-pcileech [Free DMA Firmware.Bypass VGK/FAC and MSI-X interrupt]
- https://github.com/Herooyyy/Pcileech-AMDPCI [Using no interrupt bypass faceit/vgk]
- https://github.com/Herooyyy/Pcileech-Intel-I226-V-FullEmu [Intel-I226-V]
- https://github.com/Herooyyy/Pcileech-ISABridge [Use specific PID/VID to bypass faceit]
- https://github.com/d1skq/vgk-dma-bypass [VGK DMA bypass]
- https://github.com/Ptolemaios9/Pcileech-DMA-NVMe-VMD [Firmware real camouflage through motherboard VMD function.（Pcileech-DMA）]

> W2S
- https://github.com/DrNseven/D3D11-Worldtoscreen-Finder

> Overlay
- https://github.com/coltonon/D2DOverlay
- https://github.com/SurgeGotTappedAgain/Window-Hijack
- https://github.com/SeanPesce/Direct3D9-Overlay [DX9]
- https://github.com/Unkn0wnH4ck3r/GameOverlayUIHook [Steam]
- https://github.com/gmh5225/Steam-Hook-Render-PoC [Steam]
- https://github.com/xo1337/steam-overlay-x64 [Steam]
- https://github.com/Splitx12/StrongSteam [GDI + Steam]
- https://github.com/gmh5225/dwmhook [DWM]
- https://github.com/LoxTus/dwm-overlay [DWM]
- https://github.com/rlybasic/DWM_Hook [DWM]
- https://github.com/mfxiaosheng/dwmhook [DWM VFTable]
- https://github.com/iraizo/nvidia-overlay-hijack [Hijack Nvidia]
- https://github.com/Brattlof/D3DOverlay-Nvidia-Hijack [Hijack Nvidia]
- https://github.com/gmh5225/NVIDIA-OVERLAY [Hijack Nvidia]
- https://github.com/Calvin-LLC/nvidia-overlay-hijack [Hijack Nvidia]
- https://github.com/es3n1n/nvidia-overlay-renderer [Nvidia]
- https://github.com/muturikaranja/overlay [SetWindowsHookEx]
- https://github.com/gmh5225/OBS-graphics-hook32-Hook [OBS Hook]
- https://github.com/plu1337/OBS-Hook [OBS Hook]
- https://github.com/PierreCiholas/NotAnOverlay [Duplicating with GDI]
- https://github.com/SsageParuders/Android_Native_Surface [Android Native Overlay]
- https://github.com/fgsqme/Android_Native_Surface [Android Native Overlay]
- https://github.com/xBrunoMedeiros/eac-overlay [EAC Overlay]
- https://github.com/3r4y/imgui-external-overlay [imgui overlay]
- https://github.com/J0xna/Kernel-Overlay-Hider [Kernel Overlay Hider]
- https://github.com/geeksonsecurity/android-overlay-malware-example [Android]
- https://github.com/SamuelTulach/OverlayCord [Discord] 

> Render/Draw
- https://github.com/vmcall/dxgkrnl_hook
- https://github.com/thesecretclub/window_hijack [Hijacking thread contexts]
- https://github.com/r1cky33/krnl-gdi-render [Dxgkrnl + GDI]
- https://github.com/BadPlayer555/KernelGDIDraw [Kernel + GDI]
- https://github.com/NSG650/NtDOOM [Kernel + GDI]
- https://github.com/Splitx12/StrongSteam [GDI + Steam]
- https://github.com/Sentient111/KernelDrawing [Drawing from kernelmode without any hooks]
- https://github.com/wbaby/DoubleCallBack [DWM In Kernel]
- https://github.com/cs1ime/KernelDwm [DWM In Kernel]
- https://github.com/gmh5225/DWM-DwmDraw [DWM StackWalk]
- https://github.com/Yukin02/Dwm-Overlay [DWM Overlay without modify .text]
- https://github.com/Polarmods/PolarImGui [Imgui On Android]
- https://github.com/vrolife/android_native_app_imgui [Imgui On Android]
- https://github.com/LGLTeam/Android-Mod-Menu [Floating mod menu for Android]
- https://github.com/springmusk026/ImGui-Unity-With-Layout [Imgui For Unity]
- https://github.com/springmusk026/Imgui-Unity [Imgui For Unity]
- https://github.com/gmh5225/Android-Mod-Menu-ImGui [Imgui For Unity]
- https://github.com/Octowolve/Unity-ImGUI-Android [Imgui For Unity]
- https://github.com/lbertitoyt/ImGUI-Zygisk-Unity [Imgui For Unity]
- https://github.com/gmh5225/zygisk-imgui-modmenu [ImGui with Zygisk]
- https://github.com/gmh5225/ImGui-Unity-Android [Imgui For Unity]
- https://github.com/gmh5225/BepInEx-IL2CPPBase [IL2CPP Menu]
- https://github.com/springmusk026/Android-Mod-Menu-Kotlin [IL2CPP Menu]
- https://github.com/gmh5225/Android-OpenGL-ES-Chams [Chams]
- https://github.com/RequestFX/ImGUI-Advanced-Cheat-Menu [Imgui Menu]
- https://github.com/gmh5225/External-imgui-Cheat-Menu-Example-2023 [External Imgui Menu]
- https://github.com/gmh5225/External-ImGui-Android [External Imgui Menu for Android]
- https://github.com/xProHackerx/imgui-ios-mod-menu [Imgui Menu for IOS]
- https://github.com/sy1ntexx/egui-d3d11 [Menu]
- https://github.com/springmusk026/Android-ModMenu-SemiJni [Menu for imgui]
- https://github.com/fedes1to/Zygisk-ImGui-Menu [ImGui menu using Zygisk]
- https://github.com/reveny/Zygisk-ImGui-Mod-Menu [ImGui menu using Zygisk]
- https://github.com/s4m33r89/Imgui-Native-ModMenu [Imgui Menu for Android]
- https://github.com/joeyjurjens/iOS-Mod-Menu-Template-for-Theos [IOS mod menu]

> UI Interface
- https://github.com/adamhlt/ImGui-Standalone

> Vulnerable Driver 
- https://www.loldrivers.io/drivers [Living Off The Land Drivers]
- https://github.com/magicsword-io/LOLDrivers [Living Off The Land Drivers]
- https://github.com/ghostbyt3/BYOVDFinder [Identifies LOLDrivers that are not blocked by the active HVCI policy]
- https://github.com/rtfmkiesel/loldrivers-client [Scan loldrivers]
- https://github.com/FourCoreLabs/LolDriverScan [Scan loldrivers]
- https://github.com/trailofbits/HVCI-loldrivers-check [HVCI loldrivers check]
- https://github.com/hacksysteam/HackSysExtremeVulnerableDriver [Guide]
- https://github.com/xct/windows-kernel-exploits [Guide]
- https://github.com/namazso/physmem_drivers [Vulnerable Driver List]
- https://github.com/alfarom256/drivers_and_shit [Vulnerable Driver List]
- https://github.com/NullArray/WinKernel-Resources/tree/main/Drivers [Vulnerable Driver List]
- https://github.com/CaledoniaProject/drivers-binaries [Vulnerable Driver List]
- https://github.com/Xxmmy/vulnerable-driver-scanner [Scans for vulnerable drivers]
- https://github.com/Sentient111/VulnerableDriverScanner [Scans for vulnerable drivers]
- https://github.com/shareef12/cpuz [CPU-Z]
- https://github.com/SamLarenN/CPUZ-DSEFix [CPU-Z]
- https://github.com/gmh5225/gdrv-loader/tree/1909_mitigation [gdrv.sys]
- https://github.com/backengineering/VDM [gdrv enhance]
- https://github.com/Compiled-Code/eac-mapper [gdrv.sys]
- https://github.com/gmh5225/CVE-2018-19320-LPE [gdrv.sys]
- https://github.com/gmh5225/CVE-2018-19320 [gdrv.sys]
- https://github.com/gmh5225/gdriver-lib [gdrv.sys]
- https://github.com/holi4m/gdrv-loader-v2 [gdrv.sys]
- https://github.com/gmh5225/KDP-compatible-driver-loader [gdrv.sys]
- https://github.com/1337kenzo/gdrv-loader-updated [gdrv.sys Win11]
- https://github.com/AmitMoshel1/gdrv_sys_exploit [gdrv.sys Win11]
- https://github.com/eddeeh/kdmapper [iqvw64e.sys]
- https://github.com/TheCruZ/kdmapper [iqvw64e.sys]
- https://github.com/Brattlof/kdmapper-1909 [iqvw64e.sys]
- https://github.com/paysonism/saturn-mapper [iqvw64e.sys]
- https://github.com/rmccrystal/kdmapper-rs [A kdmapper library for Rust]
- https://github.com/kkent030315/MsIoExploit [MsIo64.sys]
- https://github.com/gmh5225/VulnerableKernel_Driver [MsIo64.sys]
- https://github.com/kkent030315/evil-mhyprot-cli [Mhyprot2.sys]
- https://github.com/leeza007/evil-mhyprot-cli [Mhyprot2.sys]
- https://github.com/zer0condition/mhydeath [Mhyprot2.sys]
- https://github.com/keowu/mhyprot2 [Mhyprot2.sys]
- https://github.com/kagurazakasanae/Mhyprot2DrvControl [Mhyprot2.sys]
- https://github.com/gmh5225/CVE-2020-36603 [Mhyprot2.sys]
- https://github.com/tanduRE/AvastHV [Avast]
- https://github.com/iPower/KasperskyHook [Kaspersky]
- https://github.com/SamuelTulach/EvilKaspersky [Kaspersky]
- https://github.com/mathisvickie/CVE-2021-21551 [dbutil_2_3.sys]
- https://github.com/ch3rn0byl/CVE-2021-21551 [dbutil_2_3.sys]
- https://github.com/SpikySabra/Kernel-Cactus [dbutil_2_3.sys]
- https://github.com/mzakocs/CVE-2021-21551-POC [dbutil_2_3.sys]
- https://github.com/Flerov/TS-Fucker [dbutil_2_3.sys]
- https://github.com/Splitx12/imxyviMapper [AsUpIO.sys]
- https://github.com/archercreat/vdk [Speedfan.sys]
- https://github.com/SamLarenN/SpeedFan-Exploit [Speedfan.sys]
- https://github.com/Gbps/CapcomLib [Capcom.sys]
- https://github.com/es3n1n/dolboeb-executor [Capcom.sys]
- https://github.com/SamLarenN/CapcomDKOM [Capcom.sys]
- https://github.com/Exploitables/CVE-2015-2291 [IQVW64.sys]
- https://github.com/KiFilterFiberContext/AsIO-Exploit [AsIO3.sys]
- https://github.com/zer0condition/AsusDrv [AsusBiosIoDrv64.sys]
- https://github.com/IamM47Z/OpenHardwareMonitor-PoC [OpenHardwareMonitorLib.sys]
- https://github.com/RedCursorSecurityConsulting/PPLKiller [RTCore64.sys]
- https://github.com/Processus-Thief/PsNotifRoutineUnloader [RTCore64.sys]
- https://github.com/zeze-zeze/CYBERSEC2023-BYOVD-Demo [RTCore64.sys]
- https://github.com/oakboat/RTCore64_Vulnerability [RTCore64.sys]
- https://github.com/ReCryptLLC/CVE-2022-42045 [amsdk.sys]
- https://github.com/j3h4ck/WatchDogKiller [amsdk.sys]
- https://github.com/gmh5225/CVE-2022-3699 [LenovoDiagnosticsDriver.sys]
- https://github.com/estimated1337/lenovo_mapper [LenovoDiagnosticsDriver.sys]
- https://github.com/estimated1337/lenovo_exec [LenovoDiagnosticsDriver.sys]
- https://github.com/kkent030315/CVE-2022-42046 [wfshbr64.sys]
- https://github.com/tijme/amd-ryzen-master-driver-v17-exploit [AMD's Ryzen Master Driver]
- https://github.com/OmriBaso/RToolZ [ProcExp152.sys]
- https://github.com/SamuelTulach/nullmap [Afd.sys]
- https://github.com/gmh5225/Windows-10-22H2-Vulnerable-driver-communication [asromgdrv.sys]
- https://github.com/alfarom256/HPHardwareDiagnostics-PoC [etdsupp.sys]
- https://github.com/ZeroMemoryEx/Blackout [gmer64.sys]
- https://github.com/ZeroMemoryEx/Terminator [zam64.sys]
- https://github.com/gmh5225/zam64-zemina [zam64.sys]
- https://github.com/gmh5225/CVE-2017-9769 [rzpnk.sys]
- https://github.com/kite03/echoac-poc [echo_driver.sys]
- https://github.com/pseuxide/kur [echo_driver.sys]
- https://github.com/gmh5225/NVDrv [nvaudio.sys]
- https://github.com/gmh5225/UCMapper [nvaudio.sys]
- https://github.com/zeze-zeze/HITCON-2023-Demo-CVE-2023-20562 [AMDCpuProfiler.sys]
- https://github.com/keowu/BadRentdrv2 [rentdrv2.sys]
- https://github.com/gmh5225/S4Mapper [SignalRgbDriver.sys]
- https://github.com/gmh5225/dse_hook [winio64.sys]
- https://github.com/enkomio/s4killer [probmon.sys]
- https://github.com/floesen/KExecDD [KSecDD.sys]
- https://github.com/scrt/KexecDDPlus [KSecDD.sys]
- https://github.com/varwara/CVE-2024-26229 [csc.sys]
- https://github.com/zer0condition/ZeroHVCI [csc.sys]
- https://github.com/gmh5225/Win-Driver-EXP/tree/main/CVE-2024-33218 [AsUpIO64.sys]
- https://github.com/gmh5225/Win-Driver-EXP/tree/main/CVE-2024-30804 [AsInsHelp64.sys]
- https://github.com/gmh5225/CVE-2020-14974 [IObitUnlocker.sys]
- https://github.com/CyberSecurityUP/ProcessKiller-BYOVD [viragt64.sys]
- https://github.com/CyberSecurityUP/UrekMazino-Malware [viragt64.sys]
- https://github.com/BlackSnufkin/BYOVD/tree/main/Viragt64-Killer [viragt64.sys]
- https://github.com/MrAle98/ATDCM64a-LPE [[atdcm64a.sys](https://security.humanativaspa.it/exploiting-amd-atdcm64a.sys-arbitrary-pointer-dereference-part-1/)]
- https://github.com/varwara/CVE-2024-35250 [ks.sys]
- https://github.com/varwara/CVE-2024-21338 [appid.sys]
- https://github.com/MrAle98/CVE-2024-49138-POC [CLFS.sys]
- https://github.com/gmh5225/CVE-2025-21333-POC [vkrnlintvsp.sys]
- https://github.com/Xacone/Eneio64-Driver-Exploit [eneio64.sys]
- https://github.com/BlackSnufkin/BYOVD/tree/main/TfSysMon-Killer [SysMon.sys]
- https://github.com/BlackSnufkin/BYOVD/tree/main/Ksapi64-Killer [ksapi64.sys]
- https://github.com/BlackSnufkin/BYOVD/tree/main/BdApiUtil-Killer [BdApiUtil64.sys]
- https://github.com/0xJs/BYOVD_EDRKiller/tree/main/BdApiUtil [BdApiUtil64.sys]
- https://github.com/BlackSnufkin/BYOVD/tree/main/Wsftprm-Killer [wsftprm.sys]
- https://github.com/0xJs/BYOVD_EDRKiller/tree/main/Wsftprm [wsftprm.sys]
- https://github.com/0xJs/BYOVD_EDRKiller/tree/main/truesight [truesight.sys]
- https://github.com/kyxiaxiang/360WFP_Exploit [BYOVD: Use 360netmon_x64.sys_wfp ​​WFP driver to block EDR/XDR network connection]
- https://blog.talosintelligence.com/decrement-by-one-to-rule-them-all [AsIO3.sys]
- https://github.com/SaadAhla/Killer-Exercice [An Exercice for Red Team to Reverse & Exploit, that's a valide BYOVD Killer, not HVCI Blocklisted, and not in LOLBIN]
- https://github.com/gmh5225/ampa.sys-exp [ampa.sys]
- https://github.com/0xJs/BYOVD_read_write_primitive [BYOVD Read Write primitive]
- https://github.com/U65535F/ThrottleStopPoC [ThrottleStop.sys]
- https://github.com/ANYLNK/NSecSoftBYOVD [NSecKrnl.sys]
- https://github.com/moiz-2x/CVE-2025-24990_POC [ltmdm64.sys]
- https://github.com/symeonp/Lenovo-CVE-2025-8061 [PoC for popping a system shell against the LnvMSRIO.sys driver]
- https://github.com/SaadAhla/Killer [Non HVCI Block listed - Microsoft signed driver exploited to kill AV/EDR's processes]

> Driver Communication
- https://github.com/gmh5225/Driver-Communication-List
- https://github.com/gmh5225/ida-find-.data-ptr [.data ptr lookup script]
- https://github.com/EBalloon/Common-Registry [Registry Callback]
- https://github.com/gmh5225/Common-Registry-Jmp-RCX [Registry Callback]
- https://github.com/0xGREG/registry-callbacks [Registry Callback]
- https://github.com/adrianyy/rw_socket_driver [Socket]
- https://github.com/zoand/BOOM [Hijack Beep.sys]
- https://github.com/gmh5225/Driver-read_write [Hijack IRP Beep.sys]
- https://github.com/isoadam/gina_public [Hijack IRP Null]
- https://github.com/Barracudach/Swap-control-ioctl [Hijack IRP SpeedFan.sys]
- https://github.com/adspro15/km-um-communication
- https://github.com/Spuckwaffel/Kernel-Thread-Driver [Thread]
- https://github.com/Astronaut00/DoubleDataPointer [Double Data Pointer]
- https://github.com/btbd/access [NtConvertBetweenAuxiliaryCounterAndPerformanceCounter]
- https://github.com/paradoxwastaken/Poseidon [NtConvertBetweenAuxiliaryCounterAndPerformanceCounter]
- https://github.com/FarmEquipment69/umap-mapper [NtConvertBetweenAuxiliaryCounterAndPerformanceCounter]
- https://github.com/0mWindyBug/DataptrHooks [NtConvertBetweenAuxiliaryCounterAndPerformanceCounter]
- https://github.com/weak1337/EvCommunication [NtTokenManagerCreateFlipObjectReturnTokenHandle]
- https://github.com/gmh5225/Driver-kaldereta [NtTokenManagerGetAnalogExclusiveTokenEvent]
- https://github.com/UCFoxi/Shared-FlushFileBuffers-Communication [FlushFileBuffers]
- https://github.com/gmh5225/UCFoxi-Shared-FlushFileBuffers-Communication-Update FlushFileBuffers]
- https://github.com/Sinclairq/DataCommunication [NtCompareSigningLevels]
- https://github.com/ExpLife0011/NtCompareSigningLevel-hook [NtCompareSigningLevels]
- https://github.com/muturikaranja/AfdIrpCallDispatch [.data Pointer hook in Afd.sys]
- https://www.unknowncheats.me/forum/anti-cheat-bypass/483093-vtable-kernel-function-hook-communication.html [NtUserMessageCall]
- https://github.com/EBalloon/MapPage [NtUserGetObjectInformation]
- https://github.com/Compiled-Code/eac-mapper [NtMapVisualRelativePoints]
- https://github.com/gmh5225/eac-bypass-1 [NtMapVisualRelativePoints]
- https://git.back.engineering/_xeroxz/NtWin32k [NtUserGetThreadState]
- https://github.com/sbsbsbssbsbs/boundcallback [KeRegisterBoundCallback]
- https://github.com/Skengdoo/DataPtrSwap-driver [NtSetCompositionSurfaceAnalogExclusive]
- https://github.com/xPasters/.data-ptr-swap [NtSetCompositionSurfaceAnalogExclusive]
- https://github.com/ryan-weil/ReadWriteDriver [NtUserSetSysColors]
- https://github.com/D3DXVECTOR2/NtUserUpdateWindowTrackingInfo [NtUserUpdateWindowTrackingInfo]
- https://github.com/KiFilterFiberContext/windows-software-policy [clip]
- https://github.com/gmh5225/Interep-Driver-Leak [NtGdiPolyPolyDraw]
- https://github.com/gmh5225/Comm-data-ptr-driver [NtGdiPolyPolyDraw]
- https://github.com/JGonz1337/kernel-eac-be-comm [NtGdiPolyPolyDraw]
- https://github.com/Lynnette177/Rigel-Driver [NtGdiDdDDINetDispGetNextChunkInfo]
- https://github.com/NullTerminatorr/NullHook [NtDxgkGetTrackedWorkloadStatistics]
- https://github.com/gmh5225/Kernel-Cheat-for-directx3D [NtDxgkGetTrackedWorkloadStatistics]
- https://github.com/gmh5225/Comm-Data-Pointer-Swap [NtDCompositionSetChildRootVisual]
- https://github.com/gmh5225/Comm-NekoSwap [Win32kApiSetTable]
- https://github.com/Deputation/kernel_payload_comms [Shared Memory]
- https://github.com/Chase1803/UCMiraka-ValorantExternal [NtUserGetPointerProprietaryId]
- https://github.com/gmh5225/Comm-ImMiraclela [NtDxgkGetTrackedWorkloadStatistics/NtDxgkGetAvailableTrackedWorkLoadIndex]
- https://www.unknowncheats.me/forum/2976731-post45.html [IsWin32KSyscallFiltered]
- https://github.com/J0xna/Kernel-Overlay-Hider [NtMITPostWindowEventMessage]
- https://github.com/gmh5225/Eac-Injector-Driver [NtQueryIntervalProfile]
- https://github.com/gmh5225/job_communication [NtQueryInformationJobObject]
- https://github.com/estimated1337/custom_data_ptr_swap_sample [NtQueryLicenseValue]
- https://github.com/zer0condition/ZeroThreadKernel [NtCreateCompositionSurfaceHandle]
- https://github.com/gmh5225/NullDriverCheat [NtOpenCompositionSurfaceSectionInfo]
- https://www.unknowncheats.me/forum/anti-cheat-bypass/560809-firmwaretablehandler.html [FirmwareTableHandler]
- https://github.com/oakboat/DataPtrHookWin11 [NtUserSetGestureConfig]
- https://github.com/GetRektBoy724/Win32kHooker [.data ptr swapper for newer win32k versions]

> EFI Driver
- https://github.com/mrexodia/EfiCMake
- https://github.com/tandasat/MiniVisorPkg
- https://github.com/Oliver-1-1/SmmInfect [SMM Driver]
- https://github.com/Shtan7/VisualUEFI-2.0 [Debug source with clion+clang+gdb]
- https://github.com/SamuelTulach/EasyUefi [Visual Studio template for GNU-EFI]
- https://github.com/btbd/umap [EFI Manual Map]
- https://github.com/ekknod/sumap [EFI Manual Map]
- https://github.com/xtremegamer1/xigmapper [EFI Manual Map]
- https://github.com/Valthrun/valthrun-uefi-mapper [EFI Manual Map]
- https://github.com/ekknod/KiSystemStartupMeme [Custom KiSystemStartup]
- https://github.com/SamuelTulach/efi-memory [RPM]
- https://github.com/TheCruZ/EFI_Driver_Access [RPM]
- https://github.com/gmh5225/Driver-efi-bootkit
- https://github.com/SamuelTulach/rainbow [HWID]
- https://github.com/gmh5225/-Rainbow---EFI [HWID]
- https://github.com/Kiaoee/Fortnite-EFI-External [Fortnite]
- https://github.com/ajkhoury/UEFI-Bootkit
- https://github.com/SamuelTulach/negativespoofer [HWID]
- https://github.com/SamuelTulach/EfiDump [Dump]
- https://github.com/ekknod/Nmi [Blocking NMI interrupts]
- https://github.com/ekknod/smm [Smm cheat]
- https://github.com/sa413x/UEFI-Bootloader [Simple mmapper which using UEFI runtime driver]
- https://github.com/realoriginal/bootlicker [Generic UEFI bootkit used to achieve initial usermode execution]
- https://github.com/ekknod/efi-monitor [Hooking MmCopyMemory PG safe]
- https://github.com/leap0x7b/luaboot [A fully scriptable UEFI bootloader]
- https://github.com/Cr4sh/SmmBackdoorNg [UEFI backdoor]
- https://github.com/Oliver-1-1/UEFI-Graphic [Simpel usage of graphic in UEFI]
- https://github.com/Jamesits/BGRTInjector [Changes the boot screen image on a UEFI computer]
- https://github.com/NoInitRD/Memory-Dump-UEFI [A UEFI application for dumping the contents of RAM]
- https://github.com/NSG650/NoMoreBugCheckReloaded [NoMoreBugCheck Reloaded]
- https://github.com/x90skysn3k/x260-lenovo-opencore [Lenovo-X260-Hackintosh-BigSur-OpenCore-0.8.5]
- https://github.com/microsoft/OfflineCrashDumpUefi [EDK2 UEFI implementation for writing an Offline Crash Dump]
- https://github.com/Twobot7/advanced-efi-driver-with-gdi-and-kernel-mouse-input [A UEFI-based driver for direct memory access and process manipulation, with built-in security features and stealth capabilities]

> QEMU/KVM/PVE/VBOX
- https://github.com/david942j/kvm-kernel-example [Guide]
- https://github.com/airbus-seclab/qemu_blog [Guide]
- https://github.com/VirtualBox/virtualbox [VirtualBox Git mirror]
- https://github.com/mirror/vbox [VirtualBox Git mirror]
- https://github.com/BigAnteater/KVM-GPU-Passthrough [GPU Passthrough]
- https://github.com/dmaivel/ntoseye [Kernel Debugger]
- https://github.com/ispras/qemu/tree/windbg [Windbg]
- https://github.com/cyberus-technology/virtualbox-kvm [VirtualBox with KVM Backend]
- https://github.com/quic/gunyah-hypervisor [Type-1 hypervisor for ARM64]
- https://github.com/Qemu-Gang
- https://github.com/memflow/memflow-kvm
- https://github.com/IntroVirt/IntroVirt [Guest introspection library]
- https://github.com/MisterY52/apex_dma_kvm_pub
- https://github.com/SamuelTulach/BetterTiming [Bypass CPU Timing]
- https://github.com/WCharacter/RDTSC-KVM-Handler [Bypass RDTSC]
- https://github.com/batusan/Hardened-qemu [Hidden QEMU]
- https://github.com/zhaodice/qemu-anti-detection [Hidden QEMU]
- https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html [I made my VM think it has a CPU fan]
- https://github.com/kila58/qemu-patched [Hidden QEMU]
- https://github.com/Scrut1ny/Hypervisor-Phantom [Hidden QEMU]
- https://github.com/zhaodice/proxmox-ve-anti-detection [Hidden PVE]
- https://github.com/tteck/Proxmox [PVE Helper Scripts]
- https://github.com/nyx-fuzz/QEMU-Nyx [Intel-PT]
- https://github.com/doomedraven/Tools/blob/master/Virtualization/kvm-qemu.sh [QEMU Script]
- https://github.com/GlacierW/MBA [QEMU Malware Behavior Analyzer]
- https://github.com/Qemu-Gang/Escape-from-TuxKov [EFT]
- https://github.com/LWSS/Ape-ex-Abominations [Apex]
- https://github.com/Qemu-Gang/QemuUnrealDumper-4.25 [UE SDK Dump By QEMU]
- https://github.com/panda-re/panda [Platform for Architecture-Neutral Dynamic Analysis]
- https://github.com/cs1ime/blacksun-framework [Framework for game cheat development]
- https://github.com/cs1ime/ceserver-rawmem [CE]
- https://github.com/gmh5225/kvm-csgo-cheat [CSGO]
- https://github.com/atombottle/cs2_kvm_dma [CS2]
- https://github.com/gmh5225/cs16-trigger-kvm [CS1.6]
- https://github.com/tenclass/mvisor [C++ remake]
- https://github.com/k3v1n1990s/docker-win [wsl2]
- https://github.com/SingularityCloud/KVM.Performance [ioapic]
- https://github.com/xqemu/xqemu [Play original Xbox games]
- https://github.com/alephsecurity/xnu-qemu-arm64 [xnu]
- https://github.com/ktock/qemu-wasm [QEMU on browser]

> Wine
- https://github.com/ValveSoftware/Proton [Steam]
- https://github.com/pgarba/ptrace_read_teb [use ptrace to read the TEB of a process on Linux]

> Anti Screenshot
- https://github.com/KANKOSHEV/NoScreen [Hide Window]
- https://github.com/gmh5225/dwmhook [DWM]
- https://github.com/wongfei/wda_monitor_trick
- https://github.com/Mes2d/Screenshot-Detection-Bypass [BitBlt]
- https://github.com/oakboat/DisableNvidiaScreenshot [DWM]

> Spoof Stack
- https://github.com/mgeeky/ThreadStackSpoofer
- https://github.com/danielkrupinski/x86RetSpoof
- https://github.com/Apex-master/return-address-spoofing
- https://github.com/Peribunt/Exception-Ret-Spoofing
- https://github.com/Peribunt/Ret-Spoofing
- https://github.com/WithSecureLabs/CallStackSpoofer
- https://github.com/gmh5225/CallStackSpoofer-2
- https://github.com/Barracudach/CallStack-Spoofer
- https://github.com/frkngksl/NimicStack
- https://github.com/thesecretclub/callout-poc
- https://github.com/veryboreddd/Return-address-spoofer
- https://www.unknowncheats.me/forum/anti-cheat-bypass/512002-x64-return-address-spoofing.html
- https://github.com/Kudaes/Unwinder [Another approach to thread stack spoofing]
- https://github.com/klezVirus/SilentMoonwalk [a TRUE call stack spoofer]
- https://github.com/gmh5225/spoof-stack-SafeCall [header only]
- https://github.com/fortra/hw-call-stack [HWBP]
- https://github.com/evilashz/ProxyAPICall [Custom stack call]
- https://github.com/Kudaes/Shelter [ROP-based sleep obfuscation]
- https://github.com/susMdT/LoudSunRun [Stack Spoofing with Synthetic frames based on the work of namazso, SilentMoonWalk, and VulcanRaven]
- https://github.com/NtDallas/Fenrir [Stack spoofing using jmp rdi]
- https://github.com/HackerCalico/StackSpoofer_Macro [An easy-to-use and powerful Macro for Stack Spoofing]
- https://github.com/HulkOperator/Spoof-RetAddr [Spoofing the return address of a WinAPI call by modifying the stack]

> Hide
- https://github.com/JKornev/hidden
- https://github.com/sina85/hide-file [Hide File]
- https://github.com/ch3rn0byl/ANTfs [Delete File]
- https://github.com/KANKOSHEV/NoScreen [Hide Window]
- https://github.com/gmh5225/WindowProtect [Hide Window]
- https://github.com/nlepleux/MappedCallback [Hide Callback]
- https://github.com/rogerxiii/kernel-codecave-poc [Find Codecave]
- https://github.com/armvirus/SinMapper [Manual Map In Signed Driver]
- https://github.com/0xf1a/DSMM [Discarded Driver Section Manual Map]
- https://github.com/ekknod/sumap [EFI Manual Map]
- https://github.com/VollRagm/lpmapper [Manual Map To Large Page Driver]
- https://github.com/armvirus/CosMapper [Signed Driver Map]
- https://github.com/gmh5225/HideDriverTesting [Hide Driver]
- https://github.com/IcEy-999/Drv_Hide_And_Camouflage [Hide Driver]
- [Exploring CI.dll and Bigpool Cache](https://github.com/hLunaaa/hLunaaa.github.io/blob/4eb5450cb245217543733b475ce1198b812551a6/_posts/2025-04-25-Bypassing-CR3-Abuse-with-Physical-RW%20copy.markdown) [Driver Trace Cleaner]
- https://github.com/BadPlayer555/TraceCleaner [Driver Trace Cleaner]
- https://github.com/Sentient111/ClearDriverTraces [Driver Trace Cleaner]
- https://github.com/KelvinMsft/NoTruth [Hide Memory By VT]
- https://github.com/EBalloon/MapPage [Self Map Driver]
- https://github.com/Compiled-Code/eac-mapper [Self Map Driver]
- https://github.com/nbqofficial/HideDriver [Hide Driver By Modify Flink/Blink]
- https://github.com/ExpLife0011/HideDriver [Hide Driver By MiProcessLoaderEntryk]
- https://github.com/gmh5225/Driver-HideKernelThread-IoCancelIrp [Hide Kernel Thread]
- https://github.com/kitty8904/blanket [Hide Kernel Thread]
- https://github.com/jxy-s/herpaderping [Hide Process/File]
- https://github.com/Cracked5pider/KaynStrike [Spoofs Thread Start Address]
- [Using .reloc section to replace the typical allocation calls](https://github.com/gmh5225/memory-relocalloc)
- https://github.com/longpoxin/hideroot [Magisk]
- https://github.com/Rwkeith/Diglett [Hide Kernel Thread]
- https://github.com/gmh5225/Driver-SessionMapper [Session Driver]
- https://github.com/gmh5225/Map-file-in-system-space [MiMapViewInSystemSpace]
- https://github.com/gmh5225/Driver-DriverNoImage [Hijack Driver]
- https://github.com/gmh5225/Driver-Systemthread-from-PspCidTable-src [Hide Process/Thread/Handle]
- https://github.com/reveny/Android-Library-Remap-Hide [Remap a library for Android]
- https://github.com/rad9800/BootExecuteEDR [BootExecute EDR Bypass]

> Anti Forensics
- https://github.com/PaulNorman01/Forensia
- https://github.com/ashemery/Anti-Forensics

> Triggerbot & Aimbot
- https://github.com/changeofpace/MouHidInputHook
- https://github.com/gmh5225/AcDrv [mouse hook]
- https://github.com/ekknod/MouseClassServiceCallbackTrick
- https://github.com/ekknod/MouseClassServiceCallbackMeme
- https://github.com/blackhades00/PareidoliaTriggerbot
- https://github.com/adspro15/DirectInput
- https://github.com/nbqofficial/norsefire
- https://github.com/petercunha/Pine [Neural Network]
- https://github.com/gmh5225/AI-FPS-b00m-h3adsh0t [Neural Network]
- https://github.com/univrsal/input-overlay [Keyboard Mapper]
- https://github.com/Miffyli/gan-aimbots [Machine Learning]
- https://github.com/RootKit-Org/AI-Aimbot [Machine Learning YOLOv5]
- https://github.com/AMXZzzz/SF_TRT_61 [Machine Learning YOLO]
- https://github.com/Fragmentaim/Auto_aim [DXGI + TensorRT + driver-level input]
- https://github.com/Passer1072/RookieAI_yolov8 [Machine Learning YOLOv8]
- https://github.com/Leksa667/YOLOv8-Overlay-CS2 [YOLOv8 in CS2]
- https://github.com/dqforgive-sudo/pubg-ai-yolov4 [PUBG yolov4]
- https://github.com/lkeai2007/yolov5_PUBG [PUBG yolov5]
- https://github.com/Hellonihaohh/yolo-v8s [PUBG yolo dataset]
- https://github.com/Hellonihaohh/yolo-v8m [PUBG yolo dataset]
- https://github.com/lehmenkuehler/camera-triggerbot [Camera Triggerbot]
- https://github.com/BuddyBoi/KernelMoveMouse [gptCursorAsync]
- https://github.com/Zpes/mouse-input-injection [NtUserInjectMouseInput]
- https://github.com/gmh5225/Overwatch-1-cheat-source [NtUserInjectMouseInput]
- https://github.com/gmh5225/NtUserInjectMouseInput-syscall [NtUserInjectMouseInput SYSCALL]
- https://github.com/gmh5225/ClickPic [OpenCV + Triggerbot]
- https://github.com/gmh5225/OpenCV-SmartAimBot [OpenCV + Triggerbot]
- https://github.com/Lexikos/AutoHotkey_L
- https://github.com/tgillam/HumanMouseMovement
- https://github.com/AsfhtgkDavid/windmouse [Human-like mouse movement using WindMouse algorithm]
- https://github.com/Chaoses-Ib/IbInputSimulator [Simulating keyboard, mouse]
- https://github.com/ekknod/logitech-cve [logitech]
- https://github.com/gmh5225/razer-rzctl [Razer]
- https://github.com/vsaint1/kernel-mouse [MouClass]
- https://github.com/gmh5225/android_touch [For Android]
- https://github.com/muchenspace/android_virtualTouch [For Android]
- https://github.com/gmh5225/PTFakeTouch [For IOS]
- https://github.com/M3351AN/mouse_input_injection [NtUserInjectMouseInput]
- https://github.com/M3351AN/Usugumo [Kernel-mode mouse_event]
- https://github.com/BatogiX/logitech-cve [A Rust library for interacting with Logitech virtual driver]

> WallHack
- https://github.com/DrNseven/D3D11-Wallhack

> HWID
- https://github.com/dword64/Ow-Anti-Flag
- https://github.com/btbd/hwid
- https://github.com/gmh5225/Driver-HWID-btbd-modified
- https://github.com/gmh5225/HWID-Permanent-HWID-Spoofer
- https://github.com/gmh5225/PrecisionSpoofer-CPP
- https://github.com/Theordernarkoz/Hwid-Spoofer-EAC-BE
- https://github.com/semihcevik/hwidspoofer
- https://github.com/Theordernarkoz/Hwid--Spoofer
- https://github.com/Theordernarkoz/Hwid-Spoofer
- https://github.com/gmh5225/Apex-Spoofer
- https://github.com/gmh5225/HWID-EclipsedSpoofer-EAC-BE
- https://github.com/BuzzerFelix/HWIDSpooferEAC
- https://github.com/SamuelTulach/rainbow [EFI]
- https://github.com/firebitsbr/-Rainbow---EFI [EFI]
- https://github.com/btbd/wpp [Intercepting DeviceControl via WPP]
- https://github.com/vmcall/owned_alignment [Abusing Alignment]
- https://github.com/gmh5225/HWID-Kernel-Spoofer
- [HWID-Spoofer-UD-Fortnite-WarZone-Apex-Rust-Escape-From-Tarkov-and-all-EAC-BE-Games-IMGUI-Loader-Base](https://github.com/KakashiiiSan/HWID-Spoofer-UD-Fortnite-WarZone-Apex-Rust-Escape-From-Tarkov-and-all-EAC-BE-Games-IMGUI-Loader-Base)
- https://github.com/SamuelTulach/mutante
- https://github.com/Veuqx0/ImGui-Spoofer-Leaked
- https://github.com/gupr0x4/HWID-Spoofer-for-Fortnite-and-Valorant
- https://github.com/gmh5225/Full-Hwid-Spoofer-V6
- https://github.com/gmh5225/HWID-SteamSpywareTerminator [Steam]
- https://github.com/SamuelTulach/negativespoofer [EFI]
- https://github.com/Alex3434/wmi-static-spoofer
- https://github.com/ReFo0/hwid-spoofer
- https://github.com/namazso/hdd_serial_spoofer
- https://github.com/gmh5225/EASY-HWID-SPOOFER
- https://github.com/singhhdev/Spoofer-AMIDEWIN
- https://github.com/gmh5225/HWID-Pasted-Hwid-Spoofer
- https://github.com/Skotschia/hwid_spoofer
- https://github.com/SamuelTulach/tpm-spoofer [TPM]
- https://github.com/s0ngidong3/TPM-SPOOFER [TPM]
- https://github.com/Android1500/AndroidFaker [Android]
- https://github.com/Scrut1ny/Windows-Spoofer
- https://github.com/roomyoni/Nvidia-GPU-Spoof [Spoofing the NVIDIA GPU UUID by modifying "nvlddmkm.sys"]
- https://github.com/5ec1cff/TrickyStore [trick of keystore. Android 12 or above is required]
- https://github.com/beakthoven/TrickyStore [A trick of keystore. Android 10 or above is required]

> Bypass Page Protection
- https://github.com/illegal-instruction-co/CountHook [WorkingSet]

> SDK CodeGen
- https://github.com/cursey/sdkgenny
- https://github.com/praydog/luagenny
- https://github.com/ssyuqixe/obfCoder

> Game Engine Explorer:Unreal
- https://github.com/UE4SS-RE [UE RE]
- https://github.com/praydog/UEVR [Universal Unreal Engine VR Mod (4.8 - 5.4)]
- https://github.com/asjbdkabs/shootergame-Hack [ShooterGame Demo]
- https://github.com/cqcallaw/shootergame [ShooterGame Demo]
- https://github.com/CorrM/CleanCheat [Game cheat base]
- https://github.com/trumank/patternsleuth [Unreal Engine address scanner and test suite]
- https://github.com/trumank/jmap [Unreal Engine reflection data format and extractor]
- https://github.com/Encryqed/Dumper-7 [SDK Dump for all of UE4 and UE5]
- https://github.com/Spuckwaffel/UEDumper [SDK Dump for UE 4.19 - 5.2]
- https://github.com/BadBrojo/UEDumper-MemProcFS [UEDumper+MemProcFS 4.19 - 5.2]
- https://github.com/Chuan212/UnrealSDKDumper [SDK Dump for UE 4.23 - 4.27]
- https://github.com/BobHUnrealTech/UnrealSDKDumper-4.25 [SDK Dump for UE 4.23 - 4.27]
- https://github.com/Shhoya/Shh0yaUEDumper [SDK Dump]
- https://github.com/guttir14/UnrealDumper-4.25 [SDK Dump]
- https://github.com/EZFNDEV/UEDumper [SDK Dump]
- https://github.com/gmh5225/frida-ue4dump [SDK Dump For Android/IOS]
- https://github.com/MJx0/AndUE4Dumper [SDK Dump For Android]
- https://github.com/kp7742/UE4Dumper [SDK Dump For Android]
- https://github.com/gmh5225/UE4-Apk-Dumper [SDK Dump For Android]
- https://github.com/Zakaria-Master/UE4Dumper_Emulator [SDK Dump For Android]
- https://github.com/BigWhite666/BigWhiteTool [SDK Dump For Android]
- https://github.com/MJx0/iOS_UE4Dumper [SDK Dump For IOS]
- https://github.com/yring-me/ts-ue4dumper [TypeScript and Frida UE4dumper]
- https://github.com/CorrM/Unreal-Finder-Tool [SDK View]
- https://github.com/spudgy/UnrealEngine4-SwissKnife [SDK View]
- https://github.com/shalzuth/UnrealSharp [SDK View]
- https://fearlessrevolution.com/viewtopic.php?f=23&t=14414 [UE4 CE Table]
- https://github.com/cursey/ue4genny [SDK Generator]
- https://github.com/Zebratic/UE4Injector [Inject]
- https://github.com/N-T33/UE4-Silent-Aim [Aimbot]
- https://github.com/YMY1666527646/ue4_base [SDK Template]
- https://github.com/percpopper/UE4-Freecam [FOV Changer]
- https://github.com/RussellJerome/UnrealModLoader [Mod Loader]
- [Intercept ProcessEvent calls on any game object (Unreal Engine 4)](https://github.com/Skengdo/ue4-processevent-intercept)
- [UE4 Cheat Source Code](https://github.com/1hAck-0/UE4-Cheat-Source-Code)
- https://github.com/bbgsm/ue4_cheat_engine [UE4 Cheat For Android]
- [unpack, pack, list, check and mount Unreal Engine 4 .pak archives](https://github.com/panzi/rust-u4pak)
- https://github.com/Qemu-Gang/QemuUnrealDumper-4.25 [SDK Dump By QEMU]
- https://github.com/gmh5225/UE-UnrealEngineSDK [Universal Cheat development kit]
- https://github.com/atenfyr/UAssetGUI [Viewing and modifying UE4 game assets]
- https://github.com/UE-Explorer/UE-Explorer [Browser and decompiler for UE packages]
- https://github.com/UE4SS-RE/RE-UE4SS [Re-Host of Unreal Engine 4/5 Scripting System]
- https://github.com/SerseDioRe/Unreal-Engine-5-PDB [UE5 PDB]

> Game Engine Explorer:Unity
- https://github.com/mono/mono [mono]
- https://github.com/dnSpy/dnSpy-Unity-mono [mono]
- https://github.com/Misaka-Mikoto-Tech/MonoHook [mono hook]
- https://github.com/dnSpy/Mono.Debugger.Soft [Mono Debugger]
- https://github.com/imerzan/unispectDMAPlugin [Mono Dump + DMA]
- https://github.com/Perfare/Il2CppDumper [Il2Cpp Dump]
- https://github.com/khang06/Il2CppDumper-YuanShen [Il2Cpp Dump for Genshin Impact]
- https://github.com/Perfare/Il2CppDumper [Il2Cpp Dump GUI]
- https://github.com/Poko-Apps/Il2cppDumpDroidGUI [Il2Cpp Dump GUI]
- https://github.com/shalzuth/Il2CppRuntimeDumper [Il2Cpp Dump Runtime]
- https://github.com/Perfare/Zygisk-Il2CppDumper [Il2Cpp Dump for Android Platform]
- https://github.com/kp7742/IL2CPPDumper [Il2Cpp Dump for Android Platform]
- https://github.com/yukiarrr/Il2cppSpy [Unity IL2CPP Disassembler (for apk)]
- https://github.com/djkaty/Il2CppInspector [Il2Cpp Dump]
- https://github.com/oobbb/android-il2cpp-modspeed [Il2Cpp hack speed]
- https://github.com/gmh5225/qiling-il2cpp-dump  [Il2Cpp Dump using qiling]
- https://github.com/sinai-dev/UnityExplorer
- https://github.com/4ch12dy/il2cpp [Il2Cpp Version]
- https://github.com/nneonneo/Il2CppVersions [Il2Cpp Version]
- https://github.com/sneakyevilSK/IL2CPP_Resolver [IL2CPP resolver]
- https://github.com/extremeblackliu/IL2CPP_Resolver_External [IL2CPP resolver]
- https://github.com/knah/Il2CppAssemblyUnhollower
- https://github.com/reahly/mono-external-lib [External Mono Example]
- https://github.com/Compiled-Code/external-il2cpp [Il2Cpp]
- https://github.com/Octowolve/Il2CppSDKGenerator [Il2Cpp SDK generator for Android]
- https://github.com/00christian00/UnityDecompiled [An unofficial repo of decompiled Unity dll files]
- https://github.com/knah/Il2CppAssemblyUnhollower [Managed->IL2CPP proxy assemblies]
- https://github.com/CodeCracker-Tools/MegaDumper [Dump native and .NET assemblies]
- https://github.com/SeriousCache/UABE [Extracting assets]
- https://devxdevelopment.com/Unpacker [Extracting assets]
- https://github.com/AssetRipper/AssetRipper [Extracting assets]
- https://github.com/Perfare/AssetStudio [Extracting assets]
- https://github.com/Razviar/assetstudio [Extracting assets/2025 updated]
- https://github.com/axhlzy/Il2CppHookScripts [Il2Cpp Hook Scripts]
- https://github.com/gmh5225/Il2Cpp-HookScripts [Il2Cpp/Mono Hook Scripts]
- https://github.com/BataBo/ACEPatcher [.NET Patcher]
- [A tool translate a apk file to common android project and support so hook include il2cpp c++ scaffolding](https://github.com/Efaker/FakerAndroid)
- https://github.com/xxzzddxzd/unitySpeedTools [IOS Speed Tools]
- https://github.com/gmh5225/il2cpp-finder [Il2Cpp Finder]
- https://github.com/gmh5225/frida-il2cpp-datacollector [Il2Cpp datacollector for Android/IOS]
- https://github.com/BepInEx/BepInEx [plugin/modding framework]
- https://github.com/gmh5225/IL22CPP [ReMake of Il2cpp internal reflection system in C++]
- https://github.com/sunnamed434/UnityVulnerableEntryPoint [Looks for a vulnerable entry point]
- https://github.com/Azvanzed/MatScan [A multi-threaded rust material scanner]
- https://github.com/vfsfitvnm/frida-il2cpp-bridge [Frida dump Il2Cpp]
- https://github.com/issuimo/UnityResolve.hpp [Unity cheat framwork]
- https://github.com/ByNameModding/BNM-Android [Modding il2cpp games]
- https://github.com/SsageParuders/CheatUnityGames [Unity cheat framwork]
- https://github.com/sanqiuu/AndroidCheatTemplate [Unity cheat framwork]

> Game Engine Explorer:Source
- https://github.com/anarh1st47/Source2Dumps [Dump]
- https://github.com/CallumCVM/ValveGen [SDK Generator]
- https://github.com/praydog/Source2Gen [SDK Generator]
- https://github.com/neverlosecc/source2gen [SDK Generator]
- https://github.com/keowu/sourceengineexplorer [Explorer]
- https://github.com/neverlosecc/source2sdk

> Explore UWP
- https://github.com/Wunkolo/UWPDumper
- https://github.com/Francesco149/uwpinject [dll injector for uwp apps]
- https://github.com/Francesco149/uwpspy [dll that hooks uwp interfaces]

> Explore AntiCheat System:VAC
- https://github.com/danielkrupinski/VAC-Bypass-Loader
- https://github.com/danielkrupinski/vac-hooks
- https://github.com/mdilai/Shtreeba [Injector]
- https://github.com/zyhp/vac3_inhibitor
- https://github.com/krispybyte/Vook [VAC hook]
- https://github.com/ioncodes/vacation3-emu [VAC3 module emulator]
- https://github.com/username639/Vac-Emulator [VAC Emulator]
- https://github.com/altoid29/VACDumper [Dump]
- https://github.com/x1tan/vac3-dumper [Dump]
- https://github.com/nevioo1337/VAC-ModuleDumper [Dump]
- https://github.com/Jackbail4/VAC-Bypass
- https://github.com/n00bes/PreventVAC
- https://github.com/b1scoito/cozinha_loader [Injector]
- https://github.com/shuruk421/VACKeyRetrieval [Retrieves VAC module ice encryption key]
- https://github.com/RenardDev/DumpVAC [PoC to disable VAC and dump modules with automatic decryption]
- https://github.com/crvvdev/vac-bypass-kernel [Fully working kernel-mode VAC bypass]

> Explore AntiCheat System:EAC
- https://github.com/thesecretclub/CVEAC-2020 [Integrity Checks]
- https://github.com/Schnocker/EAC_dbp [Debug]
- https://github.com/Compiled-Code/eac-mapper [Eac Mapper]
- https://github.com/EBalloon/MmCopyMemory [Bypass MmCopyMemory]
- https://github.com/gmh5225/EAC-Kernel-Packet-Fucker [Packet Fucker]
- https://github.com/gmh5225/EAC-HydraHook [Packet Fucker]
- https://github.com/woomy144/EazyAntiCheatSRC [Reversed Source]
- https://github.com/chaeyk/eac-leak [EAC sdk's memory leak]
- https://github.com/gmh5225/EAC [SDK]
- https://github.com/ksoju/Eac-Bypass
- https://github.com/EBalloon/EasyAntiCheat-SRC
- https://github.com/gmh5225/EAC-EasyAntiCheat-Src-1
- https://www.unknowncheats.me/forum/anti-cheat-bypass/458928-eacs-maskable-interrupt-callback.html [NMI]
- https://www.unknowncheats.me/forum/anti-cheat-bypass/464943-eac-nmi-bypass-callbacks.html [NMI Bypass]
- https://github.com/CheeZeDark/EasyAntiCheat-Reversing
- https://github.com/Sinclairq/hiearchy-eac [Integrity Checks]
- https://github.com/Rat431/EAC_Emu [Simple EasyAntiCheat x64 emulator]
- https://github.com/xBrunoMedeiros/eac-overlay [EAC Overlay]
- https://github.com/gmh5225/ce-EasyAntiCheat-Bypass [UD CE]
- https://github.com/ioncodes/pooldump [Extract the DLL that EACs manualmaps into the game process]
- https://github.com/gmh5225/EAC-VmCheck.asm [Virtual machine checking]
- https://www.unknowncheats.me/forum/anti-cheat-bypass/561479-eacs-instrumentation-callback-bypass.html
- https://github.com/gmh5225/Eac-Injector-Driver [Injector]
- https://github.com/gmh5225/EAC-EasyAntiCheatMemorySig [Memory sig maker]
- https://github.com/gmh5225/EAC-shellcode-1 [Shellcode]
- https://github.com/gmh5225/EAC-Driver-UD-for-now [Sample]
- https://github.com/lguilhermee/EAC-Extractor-Utility [Decrypt and Extract the files from the EAC]
- https://advancedvectorextensions.github.io/posts/easyanticheat-eprocess-emulation [EProcess Emulation]
- https://advancedvectorextensions.github.io/posts/easyanticheat-cr3-protection [CR3 Protection]
- https://github.com/Sinclairq/hierarchy-eac [Bypassing self-integrity]
- https://github.com/SamuelTulach/eac_cr3_shuffle [Bypassing CR3 protection]
- https://github.com/Robert01337/Bypassing-EasyAntiCheat-Integrity-check [Bypassing integrity check]
- https://github.com/CamxxCore/EasyAntiCheat-Emulator [EAC Emulator]
- https://github.com/Azvanzed/EAC-Runtime-Extractor [Extracts eac's driver at runtime without it touching the disk]
- https://gist.github.com/gmh5225/b89938f55bcb65637168f88a433c3d4d [Skip EAC thread detection]
- https://github.com/kprprivate/EAC-CR3-BYPASS [A simple UM + KM example of how to bypass EAC CR3]


> Explore AntiCheat System:BE
- https://github.com/Schnocker/NoEye
- https://github.com/ZoondEngine/NoBastian_v2 [Elevating Handle By LSASS]
- https://github.com/haram/splendid_implanter
- https://github.com/HadockKali/battleye-user-mode-bypass [SetWindowsHookExW]
- https://github.com/unreaIuser/BE-Emulator
- https://github.com/masterpastaa/BattlEye-Handler-BYPASS
- https://github.com/dllcrt0/battleye-decryption
- https://github.com/dllcrt0/bedaisy-reversal
- https://github.com/dllcrt0/battleye-shellcode [shellcode]
- https://github.com/gmh5225/BE-BattlEye_shellcode [shellcode]
- https://github.com/Compiled-Code/be-injector [Attack COW]
- https://github.com/Aki2k/BEDaisy
- https://github.com/Luohuayu/BadEye
- https://github.com/zouxianyu/BlindEye [Packet Fucker]
- https://github.com/huoji120/goodeye
- https://github.com/LilPidgey/BEClient
- https://github.com/lguilhermee/Battleye-Shellcode-Dumper [BEClient2.dll Dumper]
- https://github.com/es3n1n/be-shellcode-tester [BattlEye shellcodes tester]
- https://github.com/steffalon/battleye-rust [BattlEye RCON UDP connection]
- https://github.com/Hypercall/FakeEye [Emulator]
- https://github.com/mexploitui/FakeEye [Emulator]
- https://github.com/tr1xxx/battleye-region-walking
- https://github.com/SurgeGotTappedAgain/Pink-Eye
- https://github.com/R4YVEN/beservice_intcallbacks [Instrumentation Callback]
- https://github.com/crtdll/bedaisy-bypass [BEDaisy.sys report bypass]

> Explore AntiCheat System:EQU8
- https://blog.back.engineering/12/08/2021
- https://github.com/kkent030315/EQU8-PoC
- https://github.com/hotline1337/equ8_bypass

> Explore AntiCheat System:Ricochet
- https://github.com/weak1337/ricochet_deobfuscator
- https://github.com/gmh5225/AurumRE
- https://github.com/gmh5225/ricochet-disabler

> Explore AntiCheat System:RIOT
- https://github.com/Nuxar1/DecryptionDumper [Dump]
- https://github.com/lil-skies/val-exception-handler [ZwRaiseException Dump]
- https://github.com/gmh5225/Dump-val-exception-handler [RtlpCallVectoredHandlers Dump]
- https://github.com/AdvancedVectorExtensions/VanguardImportResolver [Resolve vgk's protected imports]
- https://github.com/armvirus/VanguardTrace [Decrypting and intercepting encrypted imports of Vanguards Kernel Driver]
- https://www.unknowncheats.me/forum/anti-cheat-bypass/578829-unveiling-unseen-vanguards-guarded-regions.html [CR3 Protection]
- https://github.com/gmh5225/vgk-illegal-pf-logger [VGK's illegal PF]
- https://github.com/zer0condition/KernelSnippets/blob/main/VGK_SwapContextHk.h [VGK's SwapContextHk]

> Explore AntiCheat System:XignCode
- https://github.com/Skengdo/XignCode-Dump
- https://github.com/st4ckh0und/XignCode3-bypass-alternative
- https://github.com/st4ckh0und/XignCode3-bypass

> Explore AntiCheat System:ACE
- https://github.com/H3d9/sguard_limit
- https://github.com/rogxo/ReadPhys

> Explore AntiCheat System:G-Presto
- https://github.com/ARandomPerson7/G-Presto-Anti-Cheat-Reverse-Engineered/blob/main/Main.cpp

> Explore AntiCheat System:NeacSafe
- https://github.com/gmh5225/NeacSafe-Analysis

> Explore AntiCheat System:BadlionAnticheat
- https://github.com/KiFilterFiberContext/BadlionLogger

> Explore AntiCheat System:Byfron
- https://byfron.com/
- https://www.unknowncheats.me/forum/anti-cheat-bypass/505486-byfron-tech-anti-cheat-released.html
- https://gist.github.com/gmh5225/cbe40345a9400b01329e025478ffb826 [hash]
- https://github.com/EnrickMartins/byfron-bypass
- https://github.com/atrexus/vulkan [A PE dumper for processes protected by user mode anti-tamper solutions (hyperion, theia, etc.)]

> Explore AntiCheat System:NGS
- https://github.com/st4ckh0und/NexonGameSecurity-bypass
- https://github.com/st4ckh0und/NexonGameSecurity-bypass-alternative
- https://github.com/st4ckh0und/NexonGameSecurity-bypass-wow64

> Explore AntiCheat System:FACEIT
- https://github.com/ekknod/EC_PRO-LAN

> Explore AntiCheat System:CS2
- https://github.com/danielkrupinski/cs2-anticheat

> Game:MapleStory
- https://forum.ragezone.com/threads/getting-packet-structures-opcodes-using-ida.792436/ [Packet]
- https://github.com/Bratah123/SpiritIDAPlugin [IDA-Plugin]
- https://github.com/icelemon1314/mapleLemon [Private Server-CMS-027]
- https://github.com/ellermister/MapleStory [Private Server-CMS-079]
- https://github.com/mrzhqiang/ms079 [Private Server-CMS-079]
- https://github.com/mimilewis/MapleStory143 [Private Server-CMS-143]
- https://github.com/unsafeblackcat/MapleStoryEx [Private Server-CMS-079]
- https://github.com/gmh5225/maplestory-v83MaplestoryCPP [Private Server-GMS-083 C++]
- https://github.com/Fraysa/Destiny [Private Server-GMS-083 C#]
- https://github.com/Bratah123/ElectronMS [Private Server-KMS-316]
- https://github.com/reanox/MapleStory-v113-Server-Eimulator [Private Server-TMS-113]
- https://github.com/izarooni/MapleEzorsia [v83 edits for creating a custom resolution client]
- https://github.com/Bratah123/BattleAnalysis176 [Battle Analysis]
- https://github.com/johnsonjason/MapleStoryBuildFramework [AntiCheat]
- https://github.com/Noosh404/Maplestory-V179-Cheat-Engine [V179 CT]
- https://github.com/gmh5225/MapleStory-HeavenClient [Heaven Client]
- https://github.com/Inndy/TWMS-Hacking-Data [TMS CT]
- https://github.com/Inndy/MSDoggy [TMS Old Hack]
- https://github.com/PrinceFroggy/MSB [GMS Old Hack 128-140]
- https://github.com/PrinceFroggy/MSC [GMS Bot]
- https://github.com/v3921358/Rebirth [Private Server-GMS-095 C#]
- https://github.com/MapleStoryGameHack/mnwvs196 [Private Server-TMS-196]
- https://github.com/Maxcloud/MapleResearch [GMS-095 Client Analysis]
- https://github.com/blackmaple2018/MapleStory-CMS95-Client-Address [CMS-095 Client Analysis]
- https://github.com/neeerp/RustMS [Private Server-Rust]
- https://github.com/Kagamia/WzComparerR2 [Maplestory online Extractor]
- [Generate machine learning object detection samples from Maplestory in different formats](https://github.com/charlescao460/MapleStoryDetectionSampleGenerator)
- https://github.com/Elem8100/MapleStory-GM-Client [Offline MapleStory Client Emulator]
- https://github.com/gmh5225/maplestory-packer-ModPacker [MapleStory Wolrds .mod file packing/unpacking tools]
- https://github.com/Riremito/JMSv186 [JMS v186]
- https://github.com/ryantpayton/MapleStory-Client [HeavenMS Client]
- https://github.com/ryantpayton/MapleStory-Server [HeavenMS Server]
- https://github.com/YohananTzeviyah/LibreMaple-Client [LibreMaple Client]
- https://github.com/speedyHKjournalist/MapleServerAndroid [GMS 083 server on Android]
- https://github.com/Bratah123/ElectronMS [Private Server-KMS-316]
- https://github.com/SoulGirlJP/AzureV316 [Private Server-KMS-316]
- https://github.com/Elem8100/MapleNecrocer [MapleStory Client Emulator]
- https://github.com/StephLin/maplestory-artale-explab [Experience gain & HP/MP cost lab for MapleStory Worlds Artale]
- https://github.com/KenYu910645/MapleStoryAutoLevelUp [An auto level up script for Maple Story Artale]

> Game:Minecraft
- [A minecraft server backend written in c++](https://github.com/mmbednarek/minecpp)

> Game:Sword With Sauce
- https://github.com/1hAck-0/UE4-Cheat-Source-Code

> Game:Gunfire Reborn
- https://github.com/shalzuth/AutoGunfireReborn

> Game:Fall Guys
- https://github.com/shalzuth/FallGuysSharp
- https://github.com/ioncodes/FallGuys
- https://github.com/aci1337/Flying-Guys-fully-modified
- https://github.com/FarmEquipment69/FlyingGuys

> Game:Remnant
- https://github.com/shalzuth/RemnantESP

> Game:LostArk
- https://github.com/shalzuth/LostArkDumper
- https://github.com/shalzuth/LostArkLogger
- https://github.com/realrespecter/LOST-ARK-SDK
- https://github.com/cpz/Lost-Ark-SDK
- https://github.com/cpz/LostArk

> Game:Battlerite
- https://github.com/shalzuth/BattleriteBot

> Game:CrossFire
- https://github.com/crvvdev/titancf
- https://github.com/serjam/cfclap

> Game:TGame
- https://github.com/3tnet/nzPerspective [D3D9]

> Game:LOL
- https://github.com/LeagueSharp
- https://github.com/SwipeDan/LeagueSharp
- https://github.com/ensoulsharp-io
- https://ferrisbot.com/ferrisaio
- https://github.com/SwipeDan/EloBuddy-Addons
- https://github.com/shalzuth/LeagueSharp
- https://github.com/shalzuth/LoLClient
- https://github.com/RyukOP/L-Assemblies
- https://github.com/korllan/LeagueSharp.Loader
- https://github.com/R3nzTheCodeGOD/R3nzSkin [Skin]
- https://github.com/R3nzTheCodeGOD/R3nzSkinTFT [Skin]
- https://github.com/B3akers/LeagueSkinChanger [Skin]
- https://github.com/real-web-world/hh-lol-prophet
- https://github.com/Nuxar1/DecryptionDumper [Dump]
- https://github.com/tarekwiz/LeagueDumper [Dump]
- https://github.com/tarekwiz/League-Unpacker [Dump]
- https://github.com/0x6461726B/lol-offset-dumper [Dump]
- https://github.com/LeaguePrank/LeagueTeamBoost
- https://github.com/LeagueSandbox
- https://github.com/MythicManiac/lol-unpackman
- [A bran-new League of Legends assistant software, a replacement for WeGame](https://github.com/Java-S12138/frank)
- https://github.com/orkido/LViewLoL [Python based scripting platform]
- https://github.com/KebsCS/KBotExt [LCU]
- https://github.com/botkalista/ayaya-league-external [Nodejs based scripting platform]
- https://github.com/jfd02/TFT-OCR-BOT [TFT]
- https://github.com/sooqua/VanderLeague [Hypervisor-assisted]
- https://github.com/KebsCS/League-DirectX11-Internal [Internal]
- https://github.com/sr-henry/league-base [External]
- https://github.com/DimitriFourny/lol_patcher

> Game:NARAKA
- https://www.unknowncheats.me/forum/other-fps-games/490052-naraka-bladepoint-reversal-structs-offsets.html
- https://github.com/xkp95175333/DummyDlls_NARAKA_1_9_21 [Dump]
- https://github.com/Rythorndoran/Naraka-Hack

> Game:Thetan
- https://github.com/xkp95175333/Thetan_ArenaSDK

> Game:Dota2
- https://github.com/ikhsanprasetyo/dota2dumped [Offset dumper]
- https://github.com/skrixx68/Dota2-Overlay-2.0
- https://github.com/gmh5225/Dota2-Overlay-OffsetUpdater
- https://github.com/interception-team/dota-cheat
- https://github.com/LWSS/McDota [linux]
- https://github.com/ExistedGit/Dota2Cheat

> Game:WOW
- https://github.com/helloobaby/wow-IAT-fix
- https://github.com/namreeb/dumpwow
- https://github.com/adde88/WoWDumpFix
- https://github.com/xakepru/x14.08-coverstory-blizzard
- https://github.com/fail46/OHack [An open-source hack for World of Warcraft]
- https://github.com/adde88/SkyEngine [Wow Lua Unlocker]
- https://github.com/gmh5225/WOW-WowAutoFishing [Auto Fishing]

> Game:Warcraft III
- https://github.com/stijnherfst/HiveWE [editor]

> Game:Half-Life 2
- https://github.com/codereversing/hl2aimbot
- https://github.com/codereversing/hl2esp

> Game:CS1.6
- https://github.com/k4ne1337/hpp-hack
- https://github.com/BloodSharp/CSHackCreator-2-Demo
- https://github.com/oxiKKK/oxware
- https://github.com/execnone/simple-cs-16-multihack
- https://github.com/bit-paper/sakura
- https://github.com/eversinc33/1.6_C2 [C2]
- https://github.com/3a1/Zodiak [CS 1.6 Fastcup Full Kernel Driver Cheat]
- https://github.com/3a1/Evelion [External]

> Game:CSS
- https://github.com/yoshisaac/CounterStrikeSource-Linux-Trainer [Linux External]
- https://github.com/M3351AN/UkiaRPM [External]

> Game:CSGO
- https://github.com/csgohacks/master-guide [Guide]
- https://github.com/Akandesh/blazedumper [Offset]
- https://github.com/frk1/hazedumper [Offset]
- https://github.com/KittenPopo/csgo-offsets [Offset]
- https://github.com/ofDataa/offsets [Offset]
- https://github.com/Akandesh/csgo_auto_dumper [Auto Dump]
- https://github.com/dretax/GarHal_CSGO
- https://github.com/danielkrupinski/Osiris
- https://github.com/danielkrupinski/GOESP [Cross-platform]
- https://github.com/danielkrupinski/Anubis
- https://github.com/s3pt3mb3r/Dainsleif
- https://github.com/lagcomp/csgo_sdk
- https://github.com/felix-rs/csgo-sdk [SDK for Rust]
- https://github.com/ekknod/csf_w [Win SDK]
- https://github.com/ekknod/csf [Linux SDK]
- https://github.com/Speedi13/ROP-COMPILER
- https://github.com/AimTuxOfficial/AimTux [Linux]
- https://github.com/seksea/gamesneeze [Linux]
- https://github.com/otvv/csgo-linux-cheat-sdk [Linux]
- https://github.com/EternityX/DEADCELL-CSGO
- https://github.com/nbqofficial/kernel-csgo
- https://github.com/HeathHowren/CSGO-Cheats
- https://github.com/Kruziikrel1/CSGO-FindMDL [Model Changer]
- https://github.com/ekknod/nv_v2 [Sound ESP]
- https://github.com/DerGrosse-prog/Improved-CSGO_Simple
- https://github.com/0TheSpy/SpyExternal1337hax [External]
- https://github.com/0TheSpy/Seaside [Internal]
- https://github.com/whereisr0da/Lumina-Cheat [Internal]
- https://github.com/nbqofficial/norsefire [Driver + Mouse Emulation]
- https://github.com/boltgolt/boltobserv [Radar]
- https://github.com/worse-666/csgo_external_ahk_hack [External]
- https://github.com/ch4ncellor/CSGO-P2C-Dumper [Dump]
- https://github.com/Akatsyk/2k17-club
- https://github.com/flowxrc/csgo-xenforo-loader
- https://github.com/ALittlePatate/ezfrags
- https://github.com/Neaxic/CSGO-MAIN-INTERNAL
- https://github.com/W1lliam1337/digital-sdk
- https://github.com/sneakyevilSK/CSGO_BacktrackPatch [Backtrack Patch]
- https://github.com/NullTerminatorr/NullBase [External]
- https://github.com/krxdev-kaan/AqHax-CSGO
- https://github.com/slack69/csgo-dma-overlay [DMA]
- https://github.com/rrpvm/csgo-external-cheat
- https://github.com/petercunha/Pine [Neural Network]
- https://github.com/Bartis1313/csgo 
- https://github.com/NullHooks/NullHooks [Internal]
- https://github.com/Skarbo/CSGOCrosshair [Crosshair Generator]
- https://github.com/ekknod/G37OBS [obs-studio plugin for csgo]
- https://github.com/Sentient111/Csgo-Full-kernel [Running from kernelmode]
- https://github.com/razixNew/CompiledProtection [Cheat Compiler]
- https://github.com/ekknod/EC
- https://github.com/soyware/heck_csgo_external [External]
- https://github.com/martinjanas/Sensum [Internal]
- https://github.com/cazzwastaken/kakhack [Internal]
- https://github.com/Spelchure/CSGO-Internal [Internal]
- https://github.com/binkynz/cstrike-hack
- https://github.com/R4YVEN/raybot-zero [Kernel-mode]
- https://github.com/gmh5225/CSGO-Loader [Loader]
- https://github.com/gmh5225/CSGO-NIXWARE-CSGO [Nixware]
- https://github.com/designer1337/csgo-cheat-base [Internal]
- https://github.com/yourmnbbn/tiny-csgo-client [Tiny csgo client for connecting dedicated server]
- https://github.com/click4dylan/CSGO_AnimationCode_Reversed [CSGO animation code]
- https://github.com/spirthack/CSGOSimple [Internal]
- https://github.com/ViddeBoiiii/CSGO-Ormbunke-x86 [Imgui Menu]
- https://github.com/MavenCoding157/legit-csgo-cheat-menu [Menu]
- https://github.com/skep1337/autismware [HvH]
- https://github.com/emilyinure/solace-csgo [Internal]
- https://github.com/bruhmoment21/csgo-sdk-improved [Internal]
- https://github.com/IVBecy/cartmanv2 [Internal]
- https://github.com/gmh5225/CSGO-aw-v5.1.13 [aw-v5.1.13]
- https://github.com/ricencheese/csgo-bot
- https://github.com/forceinline/csgo-external-esp [External]
- https://github.com/VladislavAlpatov/avhook
- https://github.com/si1kyyy/csgo_cheat_external [External]
- https://github.com/latuh/nebulite-external [External]
- https://github.com/lstrsrt/csgo_internal_base [Internal]
- https://github.com/404Kurama/Astra [External]
- https://github.com/gmh5225/CSGO-Alphen
- https://github.com/Enzo0721/ExternalCheatV3 [External]
- https://github.com/SteamDatabase/Protobufs/tree/master/csgo [Protobuf]
- https://github.com/kyojig/csgo_kns [Internal]
- https://github.com/M3351AN/saphire [Internal]
- https://github.com/VitorMob/GHInterfacesCSGO [Internal]
- https://github.com/superyu1337/memcs [External]
- https://github.com/rabbitfishy/sdk [SDK]
- https://github.com/bloesway/csgo_sdk [SDK]
- https://github.com/DeiVid-12/SmKernel-CSGO [Driver]
- https://github.com/notgoodusename/OsirisAndExtra [Internal]
- https://github.com/M3351AN/Echinoidea [External C#]
- https://github.com/Blaumaus/le_chiffre [External]

> Game:CS2
- https://github.com/danielkrupinski/Osiris
- https://github.com/ro0ti/CS2-Offsets [Offset]
- https://github.com/sezzyaep/CS2-OFFSETS [Offset]
- https://github.com/Salvatore-Als/cs2-signature-list [Signature]
- https://github.com/bruhmoment21/cs2-sdk [SDK]
- https://github.com/Omn1z/Counter-Strike2-SDK [SDK]
- https://github.com/0wk/cs2-sdk [SDK]
- https://github.com/gmh5225/CS2-SDK-Source2Gen [SDK]
- https://github.com/FrySimpl3/SDK_CS2 [SDK]
- https://github.com/nikkacs/cs2_sdk [SDK]
- https://github.com/NotOfficer/cs2-sdk [SDK]
- https://github.com/a2x/cs2-dumper [Dump]
- https://github.com/imnotdatguy/csgo2-cheat
- https://github.com/papstuc/counterstrike2
- https://github.com/nezu-cc/BakaWare4
- https://github.com/gmh5225/cs2-fov-changer [FOV changer]
- https://github.com/clauadv/cs2_webradar [undetected counter strike 2 browser based radar cheat]
- https://github.com/MoZiHao/CS2_DMA_Radar [DMA Radar]
- https://github.com/ferdinandoprates/cs2_webradar [Browser based radar cheat]
- https://github.com/MoZiHao/CS2_DMA_Extrnal [DMA External]
- https://github.com/gmh5225/vscript_lua51 [VScript]
- https://github.com/gmh5225/cs2_things [VScript]
- https://github.com/IMXNOOBX/cs2-external-esp [External]
- https://github.com/UnnamedZ03/CS2-external-base [External]
- https://github.com/Tokyodidit/cs2External [External]
- https://github.com/TKazer/CS2_External [External]
- https://github.com/Valthrun/Valthrun [External]
- https://github.com/Zckyy/CS2-External [External]
- https://github.com/sFIsAnExpert/CS2-External-Cheat [External]
- https://github.com/gmh5225/tim_apple [External]
- https://github.com/kristofhracza/tim_apple [External]
- https://github.com/gmh5225/CS2-Cheat [External]
- https://github.com/Half-People/HPCS2 [External]
- https://github.com/gmh5225/CS2-External-1 [External]
- https://github.com/M3351AN/AimStar [External]
- https://github.com/Fr0go1/Aeonix-Cs2 [External]
- https://github.com/xvorost/CS-2-Glow [External]
- https://github.com/yinleiCoder/cs2-cheat-cpp [External]
- https://github.com/ByteCorum/DragonBurn [External]
- https://github.com/yoshisaac/CounterStrike2-Linux-Cheat [Linux External]
- https://github.com/KisSsArt/CS2-Cheat-Base [Internal]
- https://github.com/redbg/CS2-Internal [Internal]
- https://github.com/Elsie-Kgafela/CS2-Cheat-Base [Internal]
- https://github.com/chaycee/CS2Internal [Internal]
- https://github.com/Elsie-Kgafela/csgo2-cheat [Internal]
- https://github.com/vortex1573/Aurora [Internal]
- https://github.com/clouddss/cs2-internal-sdk [Internal]
- https://github.com/W1lliam1337/cstrike2-hack [Rust-based internal]
- https://github.com/eden13378/CS2-DMA-Cheat [DMA]
- https://github.com/spookykokojunge/CS2-Dma-Radar [DMA]
- https://github.com/atombottle/cs2_kvm_dma [KVM] 
- https://github.com/M3351AN/Samidare [External Ring3/Ring0]
- https://github.com/Vekor64/PythonCS2 [Python External]
- https://github.com/maecry/asphyxia-cs2 [Internal]
- https://github.com/Leksa667/YOLOv8-Overlay-CS2 [YOLOv8 in CS2]
  
> Game:Assault Cube
- https://github.com/gmh5225/external-esp-hack-assaultcube [GDI overlay]
- https://github.com/SkarSys/AssaultCubeCheat
- https://github.com/201580ag/AssaultCube_Cheat
- https://github.com/kotae4/lab-esp-and-aimbot [Walkthrough of an ESP and aimbot cheat from scratch]

> Game:Valorant
- https://github.com/apekros/valorant_offsets [Offset]
- https://github.com/10HEAD/ValorantOffsets [Offset]
- https://github.com/ofDataa/offsets [Offset]
- https://github.com/gmh5225/valorant-externals [Offset]
- https://github.com/GLX-ILLUSION/valorant-offsets-autoupdater [Offset]
- https://github.com/Chuan212/ValorantOffsets-China-version [Offset]
- https://github.com/hadevn/Valorant-SDK-2024 [SDK]
- https://github.com/skechtew/valorant-gui-imgui-remake [GUI]
- https://github.com/reahly/valorant-internal
- https://github.com/gmh5225/Zenti-Valorant-Cheat-Hack-Internal-Spoofer-Driver-Injector-Protector-Auth
- https://github.com/gmh5225/Valorant-Hack-Esp-Aimbot-Driver-Injector-With-Spoofer-Temporary
- https://github.com/xehn1337/valorant-dumper [Dump]
- https://github.com/gmh5225/Valorant-Dumper-Tool [Dump]
- https://github.com/lil-skies/val-exception-handler [ZwRaiseException Dump]
- https://github.com/gmh5225/Valorant-Esp-Aimbot-Hack
- https://github.com/frankelitoc/UE4-c- [External]
- https://github.com/AryuInka/Valorant-Cheat-External [External]
- https://github.com/gmh5225/Valorant-Cheat
- [Iterate And Decrypt FNamePool->Entries On Valorant](https://github.com/percpopper/VALORANT-FNamePool)
- https://github.com/gmh5225/Valorant-External-1
- https://github.com/Chase1803/UCMiraka-ValorantExternal [NtUserGetPointerProprietaryId]
- https://github.com/gmh5225/Valorant-CheatExternal
- https://github.com/weedeej/ValorantCC [Crosshair Setting]
- https://github.com/gmh5225/Internal-Valorant-Cheat
- https://github.com/gmh5225/VALORANT-HACK-ESP-AIMBOT-SKINCHANGER
- https://github.com/MauhTon/valorant-esp-hack-with-driver
- https://github.com/MauhTon/Valorant-Aimbot-Bypass
- https://github.com/zeroday-z/CyberAntLoader
- https://github.com/gmh5225/Valorant.External
- https://github.com/R7flex/valorant-internal-base [Internal]
- https://github.com/gmh5225/VALORANT-HACK-ESP-AIMBOT-SKINCHANGER-SOURCE [Internal]
- https://github.com/gmh5225/Valorant-External-Source [External]
- https://github.com/gmh5225/Valorant-cheat-internal [Internal]
- https://github.com/gmh5225/Valorant-Esp-Aimbot-Cheat-Hack [External]
- https://github.com/94q/Valorant-Internal [Internal]
- https://github.com/DX9Paster/Valorant-External-P2C-Leaked [External]
- https://github.com/kali11211/valorant-internal-cheat [Internal]
- https://github.com/234945/valo-driver [External]
- https://github.com/kali11211/valorant-internal-cheat [Internal]
- https://github.com/gmh5225/ValorantCheatExternal [External]

> Game:VEILED EXPERTS
- https://github.com/EBalloon/VEILED-EXPERTS-SDK
- https://github.com/LagradOst/ProjectD-Win64-Shipping
- https://github.com/Da3kL3o/VeiledExpertsSDK
- https://github.com/percpopper/VX-It [Decrypt]

> Game:COD1
- https://github.com/attilathedud/CoD_Hacks

> Game:COD7
- https://github.com/nice-sprite/COD7-Tools

> Game:COD Black Ops 2
- https://github.com/momo5502/t7-linker [100% accurate Black Ops 2 FastFile linker]

> Game:COD Black Ops 3
- https://github.com/gmh5225/COD-boiii [Reverse engineering and analysis]

> Game:COD Warzone
- https://github.com/YMY1666527646/Call-of-Duty-Warzone-MW-HACK-ESP-AIMBOT
- https://github.com/serjam/mwclap
- https://github.com/NMan1/external-warzone-cheat
- https://github.com/NMan1/warzone-internal
- https://github.com/gmh5225/Call-Of-Duty-Warzone-Hack-Esp-Slient-Aimbot-Internal-Unlock-ALL
- https://github.com/gmh5225/Call-Of-Duty-Vanguard-Hack-Esp-AImbot-Unlock-All
- https://github.com/gmh5225/Warzone-internal-Cheat
- https://github.com/SpiroHappy/Warzone-MW-Internal
- https://github.com/gmh5225/-Modern-Warfare-Warzone-Cheat

> Game:CODM
- https://github.com/Poko-Apps/CodMDumper [il2cpp dump]
- https://github.com/gmh5225/CODM-ESP-Aimbot-Mod-Menu [ESP]

> Game:Battlefield 1
- https://github.com/Zakaria-Master/BF1-ESP-AND-AIMBOT
- https://github.com/younasiqw/BattleField-1-Internal

> Game:Battlefield 4
- https://github.com/Zakaria-Master/BF4-Internal-overlay

> Game:Battlefield 2042
- https://github.com/Skengdo/battlefield-2042-internal-sdk

> Game:Apex Legends
- https://github.com/dhanax26/Apex-Legends-Offset-Dumper [Offset]
- https://github.com/ofDataa/offsets [Offset]
- https://github.com/dword64/Apex-Legends-SDK-Remaster
- https://github.com/hooksteroid/ApexD3D_External
- https://github.com/NMan1/apex-legends-cheat
- https://github.com/gmh5225/Apex-SIMPLE-AIMBOT-GLOW-APEX
- https://github.com/TheCruZ/Direct-EFI-Apex-Cheat
- https://github.com/Astronaut00/apex-external
- https://github.com/YMY1666527646/Phoenix-Valorant-Cheat
- https://github.com/CasualX/apexbot
- https://github.com/TheCruZ/Apex_Legends_Driver_Cheat
- https://github.com/Keyzp1337/Fortnite
- https://github.com/Zurek0x/NuremX [AI]
- https://github.com/hadevn/apex_full_cheat
- https://github.com/gmh5225/Apex-ApexCheeseTest
- https://github.com/RavenOfTime/Apex-Legends-Esp
- https://github.com/gmh5225/Apex-ApexCheat
- https://github.com/Zakaria-Master/Apex_ESP_Old_Project
- https://github.com/cheatingwitdacode/apex-cheating
- https://github.com/LWSS/Ape-ex-Abominations [QEMU]
- https://github.com/Y33Tcoder/EzApexDMAAimbot [KVM]
- https://github.com/gmh5225/Apex-CHEAT-FIXED
- https://github.com/gmh5225/apex_legends_sdk
- https://github.com/ekknod/apex_linux [linux]
- https://github.com/XRadius/project-tanya [linux]
- https://github.com/EquinoxAlpha/ayypex [linux]
- https://github.com/KaylinOwO/Project-Branthium
- https://github.com/gmh5225/Apex-Legends-External-Esp-Aimbot-Skinchanger
- https://github.com/Neurosisccc/Apex-ItemGlow [Item glow]
- https://github.com/BaconToaster/UC-Apex-Remastered
- https://github.com/NekoRem/apex-external [External]
- https://github.com/M1fisto/nullptr-apex-external [External]
- https://github.com/3nolan5/R5Apex-UserMode [External]
- https://github.com/NaiJii/Apex-Mizu-Base [Internal]
- https://github.com/boowampp/ApexDmaCheatUpdated [DMA]

> Game:Fortnite
- https://github.com/kem0x/FortKit [Dump]
- https://github.com/ofDataa/offsets [Offset]
- https://github.com/Trydos/fortnite-offsets [Offset]
- https://github.com/masterpastaa/AutoOffsets [Offset]
- https://github.com/Zetolac/FortniteOffsetsAndSigs [Offset]
- https://github.com/Android1337/Fortnite-Offsets [Offset]
- https://github.com/Luksiuss/FortniteSigsUpdatedEveryUpdate [Offset]
- https://github.com/gmh5225/Fortnite-SigsUpdatedEveryUpdate [Offset]
- https://github.com/gmh5225/fortnite-W2S-offset-Fortnite [Offset]
- https://github.com/plu1337/fortnite-offsets [Offset]
- https://github.com/gmh5225/Fortnite-Offset-dumper [Offset & Dump]
- https://github.com/plu1337/fortnite-virtual-offsets [Virtual Table Offsets]
- https://github.com/plu1337/fortnite-sigs [Signature]
- https://github.com/F0NDO/fortnite-sigs [Signature]
- https://github.com/plu1337/fortnite-exploits [Exploits]
- https://github.com/ReallReaper/Fortnite-Offsets-Sigs-and-more [Offset]
- https://github.com/Makk5/FortConsole
- https://github.com/gmh5225/Fortnite-Leak5
- https://github.com/Zetolac/FortniteExternalW2S
- https://github.com/gmh5225/Fortnite-Internal-Cheat-Fixed-and-Updated
- https://github.com/gmh5225/Fortnite-EFI-External [EFI]
- https://github.com/gmh5225/Fortnite-External-Cheat-WinSense-Leak
- https://github.com/jooola00/fortnite-cheat-source-internal
- https://github.com/YMY1666527646/Fortnite-Hack-Esp-Exploits-With-Menu
- https://github.com/YMY1666527646/nigusFN
- https://github.com/Sheeedsh78/Cheto-Fortnite-Source-External-EAC-BE-undetected
- https://github.com/CheaterRehab/GodFather-Fortnite-Cheat-Cracked
- https://github.com/Keyzp1337/Fortnite
- https://github.com/vk-nom/Basic-Fortnite-Cheat-Source-Internal
- https://github.com/PasterWolf/Fortnite-UD-External
- https://github.com/gmh5225/Fortnite-Esp-Aimbot-Exploits-Hwid-Spoofer-Cleaner-Hack-Cheat
- https://github.com/Waihbe/Fortnite-Cheat-LEAK
- https://github.com/zinx-YT/Fortnite-Fltokens-and-offsets
- https://github.com/gmh5225/VOLTO-EXTERNAL-SPOWAR-UD-EAC-BE-FORTNITE-EXTERNAL-CHEAT
- https://github.com/gmh5225/Serenity.gg-FN-and-Loader
- https://github.com/Waihbe/Fortnite-External-Cheat-Leak
- https://github.com/AlfredIU/Spoofer [HWID]
- https://github.com/pastor-ritz/ritz-amazing-fortnite-internal
- https://github.com/plu1337/Fortnite-Masterpasta-ihack-Source-Leak
- https://github.com/gmh5225/Fortnite-Evo.cc-Source-External-Cheat
- https://github.com/KeyzpOnTheFluxxx/Fortnite-External
- https://github.com/gmh5225/Apple-Lite-Fortnite-Cheat
- https://github.com/gmh5225/Fortnite-External-Cheat-Source-Code
- https://github.com/0dayatday0/BattleFN-cheat-analysis
- https://github.com/gmh5225/fortnite-internal-updated-ritz [Internal]
- https://github.com/JeanToBinks/Fortnite-Cheato-UD-EAC-BE
- https://github.com/gmh5225/BE-Forcer-Fortnite [BE forcer for fortnite]
- https://github.com/DX9Paster/Fortnite-External [External]
- https://github.com/percpopper/Fortnite-CameraCachePOV
- https://github.com/percpopper/Fortnite-FNameEntry
- https://github.com/ritz-1337/fortnite-external-evo.gj [External]
- https://github.com/simply-codes/Fortnite-External-P2C [External]
- https://github.com/Zetolac/FortniteExternalExploits [External Exploits]
- https://github.com/xetzzy/Fortnite-External-Source [External]
- https://github.com/gmh5225/fortnite-triadz [External]
- https://github.com/gmh5225/Fortnite-External-5 [External]
- https://github.com/DontCry361x/ritz-amazing-fortnite-internal-updated [internal]
- https://github.com/NurdAlert/flirtnite [External]
- https://github.com/JetBrains-CLion/Fortnite-3.5 [Internal]
- https://github.com/gmh5225/ZeroGui-Fortnite-Internal [Internal]
- https://github.com/gmh5225/Fortnite-VoyagerTF [Voyager]
- https://github.com/gmh5225/Fortnite-External-4 [External]
- https://github.com/lauralex/fn-dma-cheat [DMA]

> Game:Bloodhunt
- https://github.com/ZZZ-Monster/bloodhunt_External
- https://github.com/PhysX1337/BloodHunt-v1.1
- https://github.com/gmh5225/blood-hunt

> Game:Super People
- https://github.com/EBalloon/Super-People-sdk
- https://github.com/gmh5225/Super-People-Esp-Aimbot-Magic-Hack
- https://github.com/gmh5225/superpeople-client

> Game:Splitgate
- https://github.com/percpopper/Splitgate-Internal

> Game:PUBG
- https://github.com/owdata1/pubg-dumper [Dump]
- https://github.com/orange088/pubg_dump_offset [Offset]
- https://github.com/Skengdoo/pubg-external-cheat
- https://github.com/ajkhoury/pubg_internal
- https://github.com/iCollin/pubg-internal
- https://github.com/K-cazb/pubg-public
- https://github.com/gmh5225/PlayerUnknown-s-Battlegrounds-Pubg-Steam-Hack-Esp-Aimbot
- https://github.com/dot1991/lilypublic
- https://github.com/kurt2467/PUBG_Internal
- https://github.com/gmh5225/PUBG-DX
- https://github.com/gmh5225/PUBGSTAR

> Game:PUBG Lite
- https://github.com/Zakaria-Master/Pubg-Lite-ESP

> Game:PUBGM
- https://github.com/Zakaria-Master/pubgm_sdk_and_offsets [Offset]
- https://github.com/atulkunal999/pubg_mobile_memory_hacking
- https://github.com/Mood-Coding/pubgm_shitty_source
- https://github.com/gmh5225/PUBGM-PUBGPatcher
- https://github.com/Zakaria-Master/PUBGM1.6-DeadGame
- https://github.com/mut1234/BYPASS-PUBG-MOBILE-IMGUI
- https://github.com/busmanl30/LastIslandOfSurvival-iOSCheat-Source
- https://github.com/halloweeks/pubg-mobile-pak-extract [pak extracting tool]
- https://github.com/gmh5225/pubg_mobile_memory_hacking_examples
- https://github.com/Super-Cssdiv/ChinaPubg
- https://github.com/wantao1008hh/pubg

> Game:Sausage Man
- https://github.com/gmh5225/AndroidCheatTemplate

> Game:The finals
- https://github.com/gmh5225/the-finals-interior-cheat

> Game:EFT
- https://github.com/patrickcjk/TOG [Offsets Generator]
- https://github.com/fcancelog/EftStreamedCheat
- https://github.com/Nou4r/pKernelInterface-EFT
- https://github.com/sailro/EscapeFromTarkov-Trainer
- https://github.com/vmwrite/tiny_eft
- https://github.com/CplNathan/Nathans-Tarkov-Radar-Public [Vmread + Radar]
- https://github.com/frankie-11/eft-external
- https://github.com/Splitx12/eft
- https://github.com/gmh5225/eft-internal
- https://github.com/gmh5225/EFT-Veil-EFT
- https://github.com/Qemu-Gang/Escape-from-TuxKov [QEMU]
- https://github.com/gmh5225/Comm-ImMiraclela
- https://github.com/krispybyte/Simple-EFT-Base
- https://github.com/bytemyass/EFTLeecher [DMA]
- https://github.com/gmh5225/eft-dma-radar-1 [DMA Radar]
- https://github.com/gmh5225/EFT-MonoEFT
- https://github.com/ZhaoKunqi/simple-eft-superman-training-bot
- https://github.com/gmh5225/EFT-NewTarkovCheatProject

> Game:Arena Breakout Infinite
- https://github.com/cra0/UE426_ABInfinite-Win64-Shipping [SDK]
- https://github.com/Ke4ton/hardware_bypass [GPU check bypass]

> Game:R6
- https://github.com/NMan1/Rainbow-Six-Cheat
- https://github.com/NMan1/OverflowR6V2
- https://github.com/NMan1/Internal-Rainbow-Six-Cheat-V3
- https://github.com/beans42/epic-r6-v9
- https://github.com/Kix48/R6Updater
- https://github.com/hooksteroid/R6Table_Internal
- https://github.com/JGonz1337/r6-internal
- https://github.com/SurgeGotTappedAgain/External-R6S-Cheat
- https://github.com/vctr74/R6-Internal-V3
- https://github.com/gmh5225/R6S-internal-Cheat
- https://github.com/gmh5225/Rainbow-Six-Siege-Rs6-External-Esp-Aimbot-Hack-Cheat
- https://github.com/gmh5225/Rainbow-6-Siege-Cheat
- https://github.com/rushzzz-max/r6-external [External]
- https://github.com/ArtemisDevGroup/Artemis [Internal]
- https://github.com/MuffinPanda/R6-Cheat-Dumper [External]
- https://github.com/Possbl/R6S-External-V2 [External]
- https://github.com/igromanru/R6-Chams-public [Chams]

> Game:Overwatch 
- https://github.com/blackhades00/PareidoliaTriggerbot [Triggerbot]
- https://github.com/OSNSON/Overwatch-1-cheat-source-.
- https://github.com/vmmcall/overwatch-iat-fixer [Overwatch IAT Fixer]
- https://github.com/Midi12/ow_unpack
- https://github.com/gmh5225/OW-Aeternum
- https://github.com/dword64/Ow-FOV [FOV]

> Game:Overwatch2
- https://github.com/gmh5225/Overwatch2-colorbot-Cheats
- https://github.com/gmh5225/Overwatch-2-Cheat-Aimbot-Esp
- https://github.com/nismo1337/meowsense
- https://github.com/gmh5225/Ow-Outlines [Shows Players through walls]
- https://github.com/ZEROWyt/Overwatch-2-TOPE-EXTERNAL-CHEAT
- https://github.com/gmh5225/OW2-wardenrekter [Emulate OW2 AC]

> Game:Paladins
- https://github.com/gmh5225/Paladins-Internal-Esp-Aimbot-Hack-Cheat-Hack
- https://github.com/gmh5225/Paladins-internal-Cheat

> Game:DayZ
- https://github.com/zhitkur/DayZzz
- https://github.com/SurgeGotTappedAgain/External-Dayz-Cheat
- https://github.com/gmh5225/DayZ-Cheat
- https://github.com/JonathanEke/DayZ-Server-Battleye-Remover [Disable battleye]

> Game:Rust
- https://github.com/Akandesh/rust-auto-dumper [Auto Dump]
- https://github.com/LabGuy94/OxideDumper [Auto Dump]
- https://github.com/NMan1/OverflowRust
- https://github.com/gmh5225/simple-rust-hack
- https://github.com/Facepunch-bot/rust-internal
- https://github.com/Facepunch-bot/Rust-External
- https://github.com/Facepunch-bot/Rico-Cheat-rust-external
- https://github.com/spyder1g/a-pasted-rust-script
- https://github.com/LordAbbot/Rust-External-Cheat
- https://github.com/ZentifyZ/Kors_lol [Internal]
- https://github.com/gmh5225/Rust-Internal [Internal]
- https://github.com/ZentifyZ/CRC32
- https://github.com/SteepCheat/Rust-Cheat-External
- https://github.com/krispybyte/Simple-Rust-Base
- https://github.com/vmwrite/sapphire
- https://github.com/Disline1337/Rust-Cheat-External-main
- https://github.com/gmh5225/Rust-RustInternal [Internal]
- https://github.com/gmh5225/rust-external-1 [External]
- https://github.com/gmh5225/Rust-External [External]
- https://github.com/gmh5225/Rust-ExternaL-and-Driver-AlienCheats [External]
- https://github.com/Rogue619Z/Rust-External-Source [External]
- https://github.com/gmh5225/immortal-rust
- https://github.com/IntelSDM/RustDMACheat [DMA]

> Game:Arma3
- https://github.com/Skengdo/arma3-external-variable-manager
- https://github.com/R3voA3/3den-Enhanced [Mod Editor]
- https://github.com/tym32167/arma3beclient [BattlEye Tool]

> Game:7 Days To Die
- https://github.com/IntelSDM/7DTD

> Game:AVA
- https://github.com/boylin0/AVA-Hack

> Game:Mordhau
- https://github.com/Skengdo/mordhau-simple-auto-block-cheat

> Game:Smite  [UE3]
- https://github.com/JackBro/SmiteESPAimbot 

> Game:POLYGON [UE5]
- https://github.com/gmh5225/POLYGON_UE5

> Game:PalWorld [UE5]
- https://www.unknowncheats.me/forum/other-fps-games/620076-palworld-reversal-structs-offsets.html
- https://github.com/gmh5225/Palworld-SDK-Dump
- https://github.com/gmh5225/Palworld-Server-Modding
- https://github.com/gmh5225/PalWorld-ServerInjector
- https://github.com/gmh5225/PalWorld-NetCrack
- https://github.com/luciouskami/palworld_rcon [Server on Windows]
- https://github.com/luciouskami/palworld_rcon [Server on Windows]
- https://github.com/A1RM4X/HowTo-Palworld [Server on Linux]
- https://github.com/jammsen/docker-palworld-dedicated-server [Server based on Linux and Docker]
- https://github.com/VeroFess/PalWorld-Server-Unoffical-Fix [Server patch]
- https://github.com/NattKh/PalWorld-Tools [Mod Patcher]
- https://github.com/localcc/PalworldModdingKit [A modding kit for Palworld]
- https://github.com/weizhking/PalworldSaved [Save]
- https://github.com/cheahjs/palworld-save-tools [Save]
- https://github.com/EternalWraith/PalEdit Save]
- https://github.com/DysonCheng/PalWorldSettingGenerator [Setting Generator]
- https://github.com/hualuoo/palworld-helper [Helper]
- https://github.com/shalzuth/PalWorldAntiCheat [Anti Cheat]
- https://github.com/g91/PalAntiCheat-poc [Anti Cheat]

> Game:Genshin Impact
- https://github.com/khang06/mhynot2
- https://github.com/khang06/genshinjumpfixer2 [Decode CFG]
- https://github.com/khang06/misc/tree/master/reversing/genshin [Decode CFG]
- https://github.com/DNLINYJ/Anti_miHoYo_Jcc_Obfuscate [Decode CFG By X64DBG]
- https://github.com/gmh5225/genshin-cheat
- https://github.com/Grasscutters/Grasscutter [Private Server]
- https://github.com/gmh5225/Genshin-Akebi-GC [Cheat]
- https://github.com/gmh5225/Akebi-Cheat-3.3 [Cheat]
- https://github.com/gmh5225/Genshin-GenshinData [Game Data]
- https://github.com/HolographicHat/YaeAchievement
- https://github.com/phonowell/genshin-impact-script [A sweet genshin impact script]
- https://github.com/KnsGoyoLV/GenshinImpact-Base
- https://github.com/360NENZ/Taiga74164-Akebi-GC
- https://github.com/Ev3nt/EasyPeasy-GC
- https://github.com/xTaiwanPingLord/GenshinDebuggerBypass
- https://github.com/gmh5225/Genshin-EasyPeasy-Bypass [Anti-Debug Bypass]
- https://github.com/ELJoOker2004/genshin-remove-banner
- https://github.com/Micah123321/AutoOpenCAK [Bypass tool]
- https://github.com/KillSKID/Genshin-Cheetos [Menu]

> Game:Honkai Impact
- https://github.com/BuIlDaLiBlE/BetterHI3Launcher
- https://github.com/Z4ee/HI3-ACE-B

> Game:Honkai Star Rail
- https://github.com/Z4ee/StarRail-S-GC
- https://github.com/Z4ee/StarRail-ACE-B
- https://github.com/aderfa/star_rail
- https://github.com/gmh5225/Pom-Pom
- https://github.com/LmeSzinc/StarRailCopilot [Script]
- https://github.com/CHNZYX/Auto_Simulated_Universe [Script]

> Game:osu
- https://github.com/fs-c/maniac [External]
- https://github.com/Ciremun/freedom [difficulty changer & bot]
- https://github.com/gmh5225/osu-aac [ANTI ANTI CHEAT]

> Game:EldenRing
- https://github.com/techiew/EldenRingMods [Mod]
- https://github.com/v-maxson/EldenRingLauncher [Launcher]
- https://github.com/Nordgaren/Elden-Ring-Debug-Tool [Debug tool for Elden Ring modding]

> Game:Dark Souls
- https://github.com/igromanru/Dark-Souls-III-Cheat-Engine-Guide
- https://github.com/dualshock-tools/ds4-tools [Scripts I use to play and reverse-engineer the DualShock 4]

> Game:Sea Of Thieves
- https://github.com/ToxSylph/SeaOfChoros

> Game:GTA III - Definitive Edition
- https://github.com/gmh5225/GTAIII-DE-GoldHook

> Game:GTA5
- https://github.com/P0L3NARUBA/gtav-sourcecode-build-guide [GTA V Source Code Build Tutorial]
- https://github.com/gmh5225/GTA-5-SIGS-1.59 [Offset]
- [About
Adds drag- to- resize functionality to the main GTA V window](https://github.com/CamxxCore/GTAV_DragResize)
- [Open-source cheat software for Grand Theft Auto V (PC)](https://github.com/gmh5225/GrandTheftAutoV-Cheat)
- https://github.com/Pocakking/BigBaseV2
- https://github.com/YimMenu/YimMenu
- https://github.com/Seanghost117/SpookiMystic-GTA-Leak [Menu]
- https://github.com/Rimmuru/gta-source
- https://github.com/SyDevTeam/gta5view [Viewer/Editor]
- https://github.com/skarockoi/pHake [Mod Menu]
- https://github.com/CamxxCore/ExtendedCameraSettings [Extending functionality of the gameplay camera]
- https://github.com/medusi/gta5cheat
- https://github.com/ssyatelandisi/gta5cheat_qt

> Game:Geometry Dash
- https://github.com/reservedcloud/gd-internal

> Game:8ball pool
- https://github.com/gmh5225/Alaa-8ball-pool-source-exposed

> Game:Wizard101
- https://github.com/AmJayden/wizard101-spoofer [HWID]

> Game:QQTang
- https://github.com/blackmaple/QQTangCheatEngine

> Game:Chess
- https://github.com/LeelaChessZero/lc0 [Chess Engine]
- https://github.com/official-stockfish/Stockfish [Chess Engine]

> Game:BLOCKPOST
- https://github.com/xo1337/BLOCKPOST-Cheat

> Game:Witch It
- https://github.com/guttir14/CheatIt

> Game:RO
- https://github.com/rAthenaCN/rAthenaCN

> Game:PokemonGo
- https://github.com/Jumboperson/PokemonGoDumper

> Game:L4D2
- https://github.com/Fox-Cult/L4D2-Cheat [Linux]
- https://github.com/Axactt/L4D2Basic

> Game:mhxy
- https://github.com/gmh5225/mhxy_kernel
- https://github.com/gmh5225/mhxy

> Game:Ironsight
- https://github.com/oluan/Lazysight

> Game:Devour
- https://github.com/ALittlePatate/DevourClient
- https://github.com/BitCrackers/DevourMenu [Menu]

> Game:Goose Goose Duck
- https://github.com/Liuhaixv/Goose_Goose_Duck_Hack

> Game:Team Fortress 2
- https://github.com/gmh5225/teamfortress2_internal
- https://github.com/BlueSnoopT/Cunthook [linux]
- https://github.com/Fedoraware/Fedoraware

## Anti Cheat
> Guide
- [An in-depth exploration of how C programs transform from source code to executable binaries. This repository contains a comprehensive guide to understanding linking, loading, and executable formats](https://github.com/mohitmishra786/underTheHoodOfExecutables)
- https://technology.riotgames.com/news/riots-approach-anti-cheat
- https://github.com/87andrewh/WeirdAntiCheatIdeas
- https://github.com/gmh5225/AntiCheat-chrysalis
- https://www.unknowncheats.me/forum/anti-cheat-bypass/481731-tutorial-ring3-anticheat-project.html
- https://github.com/dhondta/awesome-executable-packing [Executable File Packing]
- https://anti-debug.checkpoint.com [Anti Debug]
- https://github.com/DenuvoSoftwareSolutions/DVRT [DVRT]
- https://areweanticheatyet.com [A list of games using anti-cheats]
- https://github.com/MyHwu9508/alt-V-Anticheat-Guide [GTA5 MP servers]
- https://github.com/frank2/packer-tutorial [Packer]
- https://github.com/kid-gorgeous/ghostbusters [Senior Design: Anit-Cheat Detection system]
- https://github.com/Solaree/pairipcore [Public researchings of the Google's Android apps protection]
- https://github.com/bad-antics/rce-shield [RCE Shield - Remote Code Execution hardening toolkit for PC gamers. Scans game launchers, anti-cheat, mods, overlays, peripherals & network for vulnerabilities]

> Stress Testing
- https://github.com/niemand-sec/AntiCheat-Testing-Framework [Testing Framework]
- https://github.com/gmh5225/MemWars [Testing Framework]
- https://github.com/ekknod/EC [Testing Framework]
- https://github.com/stuxnet147/Known-Driver-Mappers [Known Driver Mappers]
- https://github.com/DanielRTeixeira/injectAllTheThings [Injection Testing]
- https://github.com/MahmoudZohdy/Process-Injection-Techniques [Injection Testing]
- https://github.com/zoand/Injectors [Injection Testing]
- https://github.com/guided-hacking/GuidedHacking-Injector [Injection Testing]
- https://github.com/gmh5225/rust-dll-crab [Injection Testing]
- https://github.com/odzhan/injection [Injection Testing]
- https://github.com/w1u0u1/kinject [Injection Testing]
- https://github.com/D4stiny/ThreadJect [Injection Testing]
- https://github.com/KooroshRZ/Windows-DLL-Injector [Injection Testing]
- https://github.com/Fahersto/code_injection [Injection Testing]
- https://github.com/deepinstinct/Dirty-Vanity [Injection Testing:RtlCreateProcessReflection]
- https://github.com/NullTerminatorr/ThreadHijackingInjector [Injection Testing]
- https://github.com/Skengdo/simple-SetWindowsHookExW-injector [Injection Testing:SetWindowsHookExW]
- https://github.com/gmh5225/SetWindowsHookEx-Injector [Injection Testing:SetWindowsHookExW]
- https://github.com/FULLSHADE/Jektor [Injection/Shellcode Testing]
- https://github.com/KANKOSHEV/face-injector-v2 [Injection/ Testing]
- https://github.com/notscimmy/libelevate [Elevating Handle]
- https://github.com/ZoondEngine/NoBastian_v2 [Elevating Handle By LSASS]
- https://github.com/Ricardonacif/launcher-abuser [Elevating Handle]
- https://github.com/ContionMig/LSASS-Usermode-Bypass [Elevating Handle By LSASS]
- https://github.com/gmh5225/LSASS-DumpThatLSASS [Elevating Handle By LSASS]
- https://github.com/kkent030315/Van1338 [Elevating Handle By Timing Attack]
- https://github.com/gmh5225/Handle-Ripper [DuplicateHandle]
- https://github.com/Kudaes/Dumpy [Reuse opened handles By LSASS]
- https://github.com/AlSch092/EasyHandles [Driver + DLL which allows us to open handles to callback-protected processes]
- https://github.com/zorftw/lsass-extend-mapper [Manual mapper from LSASS]
- https://github.com/Mattiwatti/EfiGuard [PG Testing]
- https://github.com/9176324/Shark [PG Testing]
- https://github.com/gmh5225/HideDriverTesting [Hide Driver Testing]
- https://github.com/nbqofficial/HideDriver [Hide Driver Testing]
- https://github.com/ExpLife0011/HideDriver [Hide Driver Testing]
- https://github.com/BadPlayer555/TraceCleaner [Hide Driver Testing]
- https://github.com/muturikaranja/disable-threat-tracing [ETW Testing]
- https://github.com/Mr-Un1k0d3r/AMSI-ETW-Patch [ETW Testing]
- [EDRSandblast/KernellandBypass/ETWThreatIntel.c](https://github.com/wavestone-cdt/EDRSandblast/blob/master/EDRSandblast/KernellandBypass/ETWThreatIntel.c) [ETW Testing]
- https://github.com/daswareinfach/Battleye-VAC-EAC-Kernel-Bypass [FsFilter Testing]
- https://github.com/aahmad097/MMFCodeInjection [User APC + File Mapping Testing]
- https://github.com/liors619/TtdAntiDebugging [Debug Testing]
- https://github.com/gmh5225/cheat-attack-thread-slemu [Hearbeat Testing]
- https://github.com/nkga/cheat-driver [MmCopyVirtualMemory Testing]
- https://github.com/zxd1994/vt-debuuger [Hacked Hypervisor Testing]
- https://github.com/3526779568/vt-debuger [Hacked Hypervisor Testing]
- https://github.com/zer0condition/hv [Hacked Hypervisor Testing]
- https://github.com/MellowNight/AetherVisor [Hacked Hypervisor Testing AMD]
- https://github.com/valium007/BareSVM [Hacked Hypervisor Testing AMD]
- https://github.com/noahware/hyper-reV [memory introspection and reverse engineering hypervisor powered by leveraging Hyper-V]
- https://github.com/LabGuy94/Diskjacker [Runtime Hyper-V Hijacking with DDMA]
- https://github.com/Idov31/NovaHypervisor [NovaHypervisor is a defensive x64 Intel host based hypervisor. The goal of this project is to protect against kernel based attacks]
- https://github.com/rbmm/LockFile-Poc [Lock File]
- https://github.com/gmh5225/UltraDriver-Game-Cheat [Cheat Driver]
- https://github.com/gmh5225/Kernel-Special-APC-ReadProcessMemory [RPM]

> Driver Unit Test Framework
- https://github.com/wpdk/wdutf

> Anti Debugging
- https://github.com/LordNoteworthy/al-khaser
- https://github.com/hfiref0x/WubbabooMark
- https://github.com/samshine/ScyllaHideDetector2 
- https://github.com/revsic/AntiDebugging
- https://github.com/Ahora57/MAJESTY-technologies
- https://github.com/AdvDebug/AntiCrack-DotNet [CSharp]
- https://github.com/weak1337/CEDetector [CE]
- https://github.com/gmh5225/Detection-CheatEngine [CE]
- https://github.com/gmh5225/Detection-CheatEngine-Ring0 [CE]
- https://github.com/gmh5225/AntiDbg-AmogusPlugin
- https://gtoad.github.io/2017/06/25/Android-Anti-Debug [Android]
- https://github.com/polaryy/AntiDebugandMemoryDump [Android]
- https://github.com/fiord/ADB-Debug-Detect-Checker [Android]
- [Sample anti-debug with detect ScyllaHide/HyperHide and TitanHide](https://github.com/gmh5225/antidbg-Baka)
- [Linux anti-debugging techniques](https://github.com/hiatus/adbg)
- https://github.com/HackOvert/AntiDBG
- https://github.com/BarakAharoni/LADD [Linux]
- https://github.com/0xor0ne/debugoff [Linux]
- https://github.com/gmh5225/AntiKernelDebug-POC [Windows Kernel]
- https://github.com/BaumFX/cpp-anti-debug
- https://github.com/Metick/Anti-Debug
- https://github.com/EvilBytecode/GoDefender [Anti Debugging]
- https://github.com/Ahora57/RaceCondition
- https://github.com/AdvDebug/AntiCrack-DotNet [DotNet]
- https://github.com/hotline1337/umium [C++/CLI]
- https://github.com/YouNeverKnow00/Anti-Debugger-Protector-Loader
- https://github.com/CheckPointSW/showstopper
- https://github.com/secrary/makin [Reveal anti-debugging and anti-VM tricks]
- https://github.com/android1337/brkida [C++ macro for x64 programs that breaks ida hex-rays decompiler tool]
- https://github.com/sapdragon/hint-break [A 25-year-old architectural blind spot affecting modern reverse engineering tools]

> Page Protection
- https://github.com/changeofpace/Self-Remapping-Code
- https://github.com/ReFo0/anti-crack-system
- https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-addsecurememorycachecallback
- https://github.com/weak1337/NO_ACCESS_Protection
- https://github.com/gmh5225/no-access-protection-x86
- https://github.com/hotline1337/page_no_access
- https://github.com/thefLink/DeepSleep
- https://github.com/janoglezcampos/DeathSleep
- https://github.com/gmh5225/Sleep-obf-T.D.P.
- https://github.com/mgeeky/ShellcodeFluctuation
- https://github.com/Gofrettin/veh-printf-hook [VEH + PAGE_GUARD]
- https://github.com/charliewolfe/PointerGuard [VEH + PAGE_GUARD]
- https://github.com/connormcgarr/EATGuard [VEH + PAGE_GUARD]
- https://github.com/gmh5225/MemoryGuard [VEH + PAGE_GUARD]
- https://github.com/vxCrypt0r/Voidmaw [VEH + PAGE_GUARD]
- https://github.com/ilovecsad/veh_hide_memory [VEH + PAGE_NOACCESS]
- https://github.com/gmh5225/PAGE_NO_ACCESS-not-byfron [VEH + PAGE_NOACCESS]
- https://github.com/saveme712/BinCon [VEH + PAGE_NOACCESS]

> Binary Packer
- https://github.com/dhondta/awesome-executable-packing
- https://github.com/phra/PEzor
- https://github.com/czs108/PE-Packer [X86]
- https://github.com/longqun/Packer [X86]
- https://github.com/ATsahikian/pe-protector [X86]
- https://github.com/mkaring/ConfuserEx [.NET]
- https://github.com/iArtorias/debug_remover [Strip Debug Info]
- https://github.com/ytk2128/pe32-password
- https://github.com/frkngksl/Huan
- https://github.com/frkngksl/HintInject [Hint/Name Table]
- https://github.com/ClaudiuGeorgiu/Obfuscapk [Android]
- https://github.com/magnussen7/Embuche [ELF]
- https://github.com/EgeBalci/amber
- https://github.com/SamLarenN/PePacker
- https://github.com/Systemcluster/wrappe [Rust]
- https://github.com/vsteffen/woody_woodpacker [ELF]
- https://github.com/n4sm/m0dern_p4cker [ELF]
- https://github.com/JonDoNym/peinjector
- https://github.com/craids/AresFramework
- https://github.com/andrew9382/exe_packer
- https://github.com/dr4k0nia/Origami [Compressing .net assemblies]
- https://github.com/mix64/ELFpacker [ELF]
- https://github.com/jnastarot/shibari [Linking multiple PE\PE + files to one]
- [Simple ELF runtime packer for creating stealthy droppers](https://github.com/ex0dus-0x/ward)
- [A simple packer working with all PE files which cipher your exe with a XOR implementation](https://github.com/nqntmqmqmb/xorPacker)
- https://github.com/r0ngwe1/petoy [PE]
- [An ELF / PE packer written in pure C](https://github.com/SilentVoid13/Silent_Packer)
- https://github.com/droberson/ELFcrypt [ELF RC4]
- https://github.com/timhsutw/elfuck [ELF]
- https://github.com/Eronana/packer [PE]
- https://github.com/akuafif/hXOR-Packer [PE XOR]
- https://github.com/arisada/midgetpack [ELF]
- https://github.com/friedkiwi/netcrypt [.NET]
- https://github.com/89luca89/pakkero [ELF]
- https://github.com/dimkr/papaw [LZMA]
- https://github.com/akawashiro/sloader [ELF loader which aims to replace ld-linux.so of glibc]
- https://github.com/cryonumb/elfloader [ELF Loader for ps5-jar-loader]
- https://github.com/MahmoudZohdy/IAT-Obfuscation [IAT Obfuscation]
- https://github.com/gmh5225/shellcode-EntropyFix [Reducing entropy]
- https://github.com/ORCx41/AtomPePacker [PE X64]
- https://github.com/Lima-X/Win32.Nebula [PE X64]
- https://github.com/TheAenema/hm-pe-packer [PE X64]
- https://github.com/hid3rx/PEPacker [PE X64]
- https://github.com/xsj3n/x64-EXE-Packer [PE X64]
- https://github.com/frkngksl/Shoggoth [Polymorphic Encryptor]
- https://github.com/GunshipPenguin/kiteshield [ELF X64]
- https://github.com/cff0x/KitsuPE [PE]
- https://github.com/KooroshRZ/Evader [PE]
- https://github.com/greyb1t/GreyM [PE]
- https://github.com/DavidBuchanan314/stelf-loader [ELF X64 loader]
- https://github.com/frank2/oxide [Written by Rust]
- https://github.com/Washi1337/AwaitFuscator [.NET]
- https://github.com/Fatmike-GH/Fatpack [A Windows PE packer with full TLS (Thread Local Storage) support]
- https://github.com/caprinux/rel-fuscate [Modifying the jmprel_entry->r_offset]
- https://github.com/dobin/SuperMega [Stealthily inject shellcode into an executable]

> CLR Protection
- https://github.com/endgameinc/ClrGuard

> Anti Disassembly
- https://github.com/rrbranco/blackhat2012

> Sample Unpacker
- https://github.com/hasherezade/mal_unpack_drv
- https://github.com/strazzere/android-unpacker [Android]

> Dump Fix
- https://github.com/t3ssellate/unmapper
- https://github.com/d35ha/DumpPE
- https://github.com/pr701/fix-arxan

> Encrypt Variable
- https://github.com/serge-14/encrypted_value [C++]
- https://github.com/momalab/e3 [C++]
- https://github.com/obama-gaming/xor-float [C++]
- https://github.com/emlinhax/xv [C++]
- https://github.com/nevergiveup-c/obfuscxx [Header-only compile-time variables obfuscation library for C++20 and later. Compiler Support: MSVC (+WDM), LLVM, GCC. Architecture Support: x86-64, ARM]

> Lazy Importer
- https://github.com/JustasMasiulis/lazy_importer
- https://github.com/hypervisor/kli
- https://github.com/gmh5225/kli-ex
- https://github.com/1hAck-0/zeroimport
- https://github.com/emlinhax/blitz

> Anti-Cheat Programming
- https://github.com/m417z/thread-call-stack-scanner [Safely manage the unloading of DLLs that have been hooked into a process. Context]

> Compile Time
- https://github.com/ManulMap/malstring [Using c++23 compile-time magic to produce obfuscated PIC strings and arrays]
- https://github.com/reveny/Android-Native-Import-Hide [A library for hiding and retrieving imports in ELF binaries]
- https://github.com/emlinhax/blitz [a header-only library to dynamically resolve modules and exports while also being able to call them directly]
- https://github.com/emlinhax/xv [single-header pointer/value encryption]
- https://github.com/ac3ss0r/obfusheader.h [Obfusheader.h is a portable header file for C++14 compile-time obfuscation]
- https://github.com/SecondNewtonLaw/DriverBase/blob/dev/Dependencies/obfusheader.h [obfusheader.h for windows driver]
- https://github.com/dronavallipranav/rust-obfuscator [Automatic Rust Obfuscator and Macro Library]
- https://github.com/Sherman0236/XorData [A C++17 framework designed to enable obfuscation of constants, variables, and strings]
- https://github.com/android1337/crycall [Compile-Time Calls Obfuscator for C++14]
- https://github.com/JustasMasiulis/inline_syscall [Inline syscalls made easy for windows on clang]
- https://github.com/66flags/inline-syscall [A simple direct syscall wrapper written in C++ with compatibility for x86 and x64 programs]
- https://github.com/sapdragon/syscalls-cpp [A modern C++20 header-only library for advanced direct system call invocation]
- https://github.com/cristeigabriel/STB [Compile-time conversion library, from IDA-style string to array]
- https://github.com/Deniskore/CompileTimeRandom [Compile time random implementation using C++11]
- https://github.com/ThatLing/limba [compile-time control flow obfuscation using mba]
- https://github.com/Nou4r/Polymorphic-Engine [Prototype runtime C++ polymorphic type engine]
- https://github.com/hanickadot/cthash [constexpr implementation of SHA-2 and SHA-3 family of hashes]
- https://github.com/PaulNorman01/Dynamizer [Reduce Dynamic Analysis Detection Rates With Built-In Unhooker, Anti Analysis Techniques, And String Obfuscator Modules]
- https://github.com/hanickadot/compile-time-regular-expressions [Compile Time Regular Expression in C++]
- https://github.com/CasualX/obfstr [String Crypter for rust]
- https://github.com/redskal/obfuscatxor [String Crypter for golang]
- https://github.com/Reijaff/static_string_obfuscation [String Crypter for Zig]
- https://github.com/pykaso/Swift-String-Obfuscator [String Crypter for Swift]
- https://github.com/android1337/crystr [String Crypter]
- https://github.com/adamyaxley/Obfuscate [String Crypter]
- https://github.com/igozdev/xorlit [String Crypter]
- https://github.com/JustasMasiulis/xorstr [String Crypter]
- https://github.com/skadro-official/skCrypter [String Crypter]
- https://github.com/rad9800/BloatedHammer [API Hammering with C++20 by folding (avoiding loops)]
- https://github.com/obama-gaming/xor-float [xor float]
- https://github.com/llxiaoyuan/oxorany [obfuscated any constant encryption in compile time on any platform]
- https://github.com/DosX-dev/obfus.h [Macro-header for compile-time C obfuscation (tcc, win x86/x64)]
- https://github.com/x86byte/Obfusk8 [Obfusk8: C++17-Based Obfuscation Library]
- https://github.com/nevergiveup-c/obfuscxx [Header-only compile-time variables obfuscation library for C++20 and later. Compiler Support: MSVC (+WDM), LLVM, GCC. Architecture Support: x86-64, ARM]
- https://github.com/Mowokuma/vm_str.hpp [Header only C++20 compile time string obfuscator]

> Shellcode Engine & Tricks
- https://github.com/Vector35/scc [shellcode compiler]
- https://github.com/jseclab/obj2shellcode
- https://github.com/lainswork/shellcode-factory
- https://github.com/H1d3r/GPU_ShellCode [hide the payload inside the gpu memory]
- https://github.com/Lavender-exe/Shellcrypt [A QoL tool to obfuscate shellcode. In the future will be able to chain encoding/encryption/compression methods]
- https://github.com/dobin/SuperMega [Stealthily inject shellcode into an executable]
- https://github.com/mrexodia/RiscyWorkshop [Payload Obfuscation for Red Teams workshop materials]
- https://github.com/umpolungfish/byvalver [Shellcode bad-byte banisher with preserved functionalities]
- https://github.com/wbenny/scfw [A cross-platform C++ framework for building Windows shellcode]

> Obfuscation Engine
- https://github.com/vi3t1/vmprotect-3.5.1
- https://github.com/DosX-dev/obfus.h [Macro-header for compile-time C obfuscation (tcc, win x86/x64)]
- https://github.com/connorjaydunn/BinaryShield
- https://github.com/mike1k/perses
- https://github.com/weak1337/Alcatraz
- https://github.com/FigmaFan/Alcatraz
- https://github.com/es3n1n/obfuscator
- https://github.com/jnastarot/furikuri
- https://github.com/nickcano/RelocBonus [Attack Reloc]
- https://github.com/maoabc/nmmp [Dex]
- https://github.com/CodingGay/BlackObfuscator [Dex]
- https://github.com/d35ha/CallObfuscator [Call Obfuscation]
- https://github.com/nelfo/Milfuscator
- https://github.com/romainthomas/the-poor-mans-obfuscator [elf/macho]
- https://github.com/Guardsquare/proguard [Java]
- https://github.com/xiaoweime/WProtect
- https://github.com/DeDf/WProtect
- https://github.com/jokerNi/WProtectSDK
- https://github.com/cxxrev0to1dev/nb_obfuscator
- https://github.com/gmh5225/cerberus [VM]
- https://github.com/layerfsd/phantasm-x86-virtualizer [VM]
- https://github.com/felix-rs/guardian-rs [VM]
- https://github.com/dmaivel/covirt [VM]
- https://github.com/CalebFenton/simplify [Java]
- https://github.com/open-obfuscator/dProtect [Java/Kotlin]
- https://github.com/Maldev-Academy/EntropyReducer [Reduce Entropy]
- https://github.com/Washi1337/AwaitFuscator [.NET]
- https://github.com/badhive/stitch [X86: Rewrite and obfuscate code in compiled binaries]
- https://github.com/keowu/Ryujin [X86 PE BIN2BIN]
- https://github.com/zx0CF1/shredder-rs [A high-fidelity x86_64 polymorphic mutation engine focused on instruction-level fragmentation and context preservation]

> Screenshot
- https://github.com/bavulapati/DXGICaptureApplication [Capture Desktop]
- https://github.com/Rick-laboratory/Windows-Screenshotcapture-DirectX/blob/master/main.cpp [DX9]
- https://github.com/lainswork/dwm-screen-shot [DWM]
- https://github.com/kirides/screencapture [DX11]
- https://github.com/bmharper/WindowsDesktopDuplicationSample [DXGI]
- https://github.com/PierreCiholas/GetPixel-vs-BitBlt_GetDIBits [GetPixel]
- https://github.com/gmh5225/ScreenShot [BitBlt]

> Game Engine Protection:Unreal
- https://github.com/zompi2/Static-Variables-Obfuscator-UE4
- https://github.com/gmh5225/UE-Plugin-SCUE4-Plugin
- https://github.com/gmh5225/UnrealEngine-Protection

> Game Engine Protection:Unity
- https://github.com/ls9512/USecurity
- https://github.com/bmjoy/Unity3D_Obfuscator
- https://github.com/Ether2023/Ether-Uprotector
- https://github.com/badApple001/Il2cppEncrtypt
- https://github.com/focus-creative-games/obfuz

> Game Engine Protection:Source
- [Source Engine serverside anti-cheat plugin. (CS:S, CS:GO, CS:P, TF2)](https://github.com/kanekikun420/NoCheatZ-3)

> Open Source Anti Cheat System
- https://github.com/mq1n/NoMercy
- https://github.com/NoMercy-ac [NoMercy]
- https://github.com/JackBro/BetaShield
- https://github.com/chztbby/RebirthGuard
- https://github.com/GravitLauncher/Avanguard
- https://github.com/Rycooop/Bloom-Anticheat
- https://github.com/Vasieco/Kernel-Anticheat [Kernel Anticheat]
- https://github.com/AvivShabtay/Stresser [Anti Virus in fact but also Anti Cheat]
- https://github.com/gmh5225/antivirus [Anti Virus in fact but also Anti Cheat]
- https://github.com/D4stiny/PeaceMaker [Anti Virus in fact but also Anti Cheat]
- https://github.com/danielkrupinski/VAC [Reversed VAC]
- https://github.com/ApexLegendsUC/anti-cheat-emulator
- https://github.com/ch4ncellor/EAC-Reversal [Reversed EAC]
- https://github.com/weak1337/BE-Shellcode [Reversed BE Shellcode]
- https://github.com/SamuelTulach/be_shellcode_dump [Reversed BE Shellcode]
- https://github.com/codetronik/AndroidAntiCheat [Android Platform]
- https://github.com/Lazenca/Lazenca-S [Android Platform]
- https://github.com/MrDiamond64/Scythe-AntiCheat [Minecraft]
- https://github.com/GrimAnticheat/Grim [Minecraft]
- https://github.com/mateusreb/AntiCheat
- https://github.com/ComodoSecurity/openedr [EDR]
- https://github.com/0xrawsec/whids [EDR]
- https://github.com/Neo23x0/Raccine [EDR]
- https://github.com/ION28/BLUESPAWN [EDR]
- https://github.com/TheHive-Project/TheHive [EDR]
- https://github.com/0xflux/Sanctum [Sanctum is an experimental proof-of-concept EDR, designed to detect modern malware techniques, above and beyond the capabilities of antivirus. Built in Rust]
- https://github.com/wazuh/wazuh [XDR]
- https://github.com/AlSch092/UltimateAntiCheat
- https://github.com/JonathanBerkeley/Quack
- [Source Engine serverside anti-cheat plugin. (CS:S, CS:GO, CS:P, TF2)](https://github.com/kanekikun420/NoCheatZ-3)
- [This is the Anti Cheat System for Knight Online Gamesoft vversion](https://github.com/luisfelipe18/GamesoftACS)
- [User-mode C++ Anti-Cheat written for German Roleplay Server GVMP.de](https://github.com/divodeuxsevres/gvmp-anticheat)
- [Cheat developer platform](https://github.com/c4kef/UAC)
- https://github.com/ekknod/Anti-Cheat-TestBench [TestBench]
- https://github.com/gmh5225/Malicious-code-detection-bugu [Malicious code detection and obfuscation]
- [Kernel Security driver used to block past, current and future process injection techniques on Windows Operating System](https://github.com/PI-Defender/pi-defender)
- https://github.com/gmh5225/Anticheat-android-cheap-engine [Sample implementation of anti-cheat in android]
- [Proof of concept Anti-Cheat plugin for CS:GO](https://github.com/ekknod/CSGO-AC)
- [Deep Learning Anti-Cheat For CSGO](https://github.com/LaihoE/DLAC)
- [Deep Learning Anti-Cheat For CSGO](https://github.com/bananya-ml/anti-cheat)
- https://github.com/jnastarot/anti-cheat
- https://github.com/jnastarot/ice9
- https://github.com/realTristan/Reborn [Designed with Rust]
- https://github.com/dllcrt0/Dynsec
- https://github.com/XZNX5/Basic_Anti-Cheat
- https://github.com/MegaAntiCheat
- https://github.com/donnaskiez/ac
- https://github.com/gmh5225/AcDrv
- https://github.com/sc-222/Mandragora [For Assault Cube]
- https://github.com/J-Tanzanite/Little-Anti-Cheat [For Source Games]
- https://github.com/noahware/darken-anticheat [Kernel anti-cheat for protecting software]

> Analysis Framework
- https://github.com/pandora-analysis/pandora

> Detection:Hook
- https://github.com/hasherezade/pe-sieve
- https://github.com/mike1k/HookHunter
- https://github.com/st4ckh0und/hook-buster
- https://github.com/gmh5225/Driver-Detect-nullshit
- https://github.com/paranoidninja/EtwTi-Syscall-Hook [Instrumentation Callback]
- https://github.com/Luchinkin/device-control-hooks-scanner [device-control-hooks-scanner]
- https://github.com/ORCx41/KnownDllUnhook [Replace the .txt section of the current loaded modules from \KnownDlls\]
- https://github.com/Teach2Breach/nt_unhooker [demo unhooking functions in ntdll]

> Detection:Memory Integrity
- https://github.com/afulsamet/integrity
- https://github.com/Midi12/QueryWorkingSetExample
- https://github.com/Deputation/integrity_experiments [header only]
- https://github.com/DejavuSecure/DetectNtoskrnlIntegrity [Windows Kernel Security: Memory Integrity Verification with Disk Verification of ntoskrnl.exe]
- https://github.com/MatheuZSecurity/ksentinel [Linux kernel integrity monitor for detecting syscall hooking]

> Detection:ShellCode
- https://github.com/jdu2600/EtwTi-FluctuationMonitor [ETW]
- https://github.com/jdu2600/Etw-SyscallMonitor [ETW]
- https://github.com/jdu2600/CFG-FindHiddenShellcode [CFG]

> Detection:Attach
- https://github.com/KANKOSHEV/Detect-KeAttachProcess

> Detection:Triggerbot & Aimbot
- https://github.com/KANKOSHEV/Detect-MouseClassServiceCallback
- https://github.com/changeofpace/MouHidInputHook
- https://github.com/KelvinMsft/UsbMon
- https://github.com/87andrewh/DeepAimDetector [Deep Learning]
- https://github.com/waldo-vision/waldo [Deep Learning]
- https://github.com/waldo-vision/aimbot-detection-prototype [Deep Learning]
- https://github.com/bananya-ml/anti-cheat [Deep Learning for CSGO]
- https://github.com/hkx3upper/Karlann [Keyboard]
- https://github.com/AsuNa-jp/HotkeybasedKeyloggerDetector [Detect RegisterHotKey API]
- https://github.com/Oliver-1-1/MouseDetection [Mouse]
- https://github.com/chrisgdt/DELBOT-Mouse [Deep learning to distinguish human and bot from mouse movements]
- https://github.com/Oliver-1-1/EtwKeyboardDetection [ETW]

> Detection:Hide
- https://github.com/KANKOSHEV/Detect-HiddenThread-via-KPRCB
- https://github.com/ekknod/Anti-Cheat-TestBench [KPRCB+PTE]
- https://github.com/weak1337/SystemThreadFinder
- https://github.com/mq1n/HiddenModuleDetector
- https://github.com/KelvinMsft/ThreadSpy
- https://github.com/Rwkeith/Nomad [Mapped Driver]
- https://github.com/Nou4r/ModFinder [Mapped Dll]
- https://github.com/1401199262/NMIStackWalk [Mapped Driver by NMI Callback]
- https://github.com/donnaskiez/nmi-callback-handler [Mapped Driver by NMI Callback]
- https://github.com/gmh5225/Kernel_Anti-Cheat [NMI]
- https://github.com/jafarlihi/modreveal [Find hidden Linux kernel modules]
- https://github.com/MatheuZSecurity/ksentinel [Linux kernel integrity monitor for detecting syscall hooking]
- https://github.com/gmh5225/Hidden-Thread-Finder [Detect hidden threads]
- https://github.com/gmh5225/StealthSytemThreadFinderBE [Detect hidden threads]
- https://github.com/eversinc33/unKover [Using NMI/APC to detect mapped drivers]
- https://github.com/gmh5225/Rootkit-2 [Using CsrRootProcess to detect hidden process]
- https://github.com/ait-aecid/rootkit-detection-ebpf-time-trace [Detection of rootkit file hiding activities through analysis of shifts in kernel function execution times]

> Detection:Vulnerable Driver
- https://github.com/Deputation/hygieia
- https://github.com/FaEryICE/MemScanner

> Detection:EFI Driver
- https://github.com/gmh5225/Detect-EFIGuard

> Detection: Hacked Hypervisor
- https://secret.club/2020/04/13/how-anti-cheats-detect-system-emulation.html
- https://github.com/helloobaby/Nmi-Callback [NMI Callback]
- https://github.com/momo5502/ept-hook-detection [Detect EPT]
- https://github.com/JustasMasiulis/rep_mov_ept_detecc [REP MOV based EPT detection]
- https://github.com/everdox/ermsb-meme [REP MOV based EPT detection]
- https://github.com/gmh5225/Detect-Hypervisor_detect_ring_0
- https://github.com/jonomango/nohv
- https://github.com/void-stack/Hypervisor-Detection
- https://github.com/cryotb/VmdtStr [Detect VMMs with faulty handling of STR exit]
- https://github.com/gmh5225/hv-detect [Hypervisor IDT Detections (SIDT / LIDT)]
- https://github.com/Skeletal-Group/Bloodhound [Various novel EPT/NPT hook detection mechanisms]

> Detection:Virtual Environments
- https://github.com/theo-abel/awesome-anti-virtualization [A curated list of awesome resources related to anti virtualization techniques]
- https://github.com/a0rtega/pafish
- https://github.com/gmh5225/Detection-Hyper-v [Hyper-v]
- https://github.com/gmh5225/Go-Detection-Hyper-v [Hyper-v]
- https://github.com/Ahora57/MAJESTY-technologies
- https://github.com/therealdreg/anticuckoo [Cuckoo]
- https://github.com/strazzere/anti-emulator [Android Anti-Emulator]
- https://github.com/gmh5225/Android-Emulator-Detection [Android Anti-Emulator]
- https://github.com/reveny/Android-Emulator-Detection [Android Anti-Emulator]
- https://github.com/LloydLabs/wsb-detect [Windows Sandbox ("WSB")]
- https://github.com/DevDaveid/AntiDebug-AntiVM [Vbox]
- https://github.com/LukeGoule/compact_vm_detector
- https://github.com/kernelwernel/VMAware [VM detection library]
- https://github.com/su-vikas/conbeerlib [Android library for detecting Android virtual containers]
- https://github.com/can1357/hvdetecc [Collection of hypervisor detections]
- https://github.com/0xTriboulet/T-1 [T-1 is a shellcode loader that leverages ML techniques to detect VM environments]
- https://github.com/SaadAhla/Anti-Sandbox [Detecting AnyRun sandbox]
- https://github.com/gmh5225/hv-detect [Hypervisor IDT Detections (SIDT / LIDT)]
- https://github.com/zer0condition/checkhv_um [CPUID leaf is explicitly defined for hypervisors to expose their presence and vendor ID; any honest vm stack should set this up]

> Detection:HWID
- [All methods of retrieving unique identifiers(HWIDs) on your PC](https://www.unknowncheats.me/forum/anti-cheat-bypass/333662-methods-retrieving-unique-identifiers-hwids-pc.html)
- https://github.com/medievalghoul/hwid-checker-mg
- https://github.com/weak1337/NvidiaApi
- https://github.com/paradoxwastaken/WindowsHardwareInfo
- https://github.com/gmh5225/query-gpu-name-rs [GPU name for windows]
- https://github.com/lavoiesl/osx-cpu-temp [CPU temperature for OSX]
- https://github.com/ashleyhung/WinRing0 [CPU temperature for windows]
- https://github.com/openhardwaremonitor/openhardwaremonitor
- https://github.com/LibreHardwareMonitor/LibreHardwareMonitor
- https://github.com/lfreist/hwinfo [cross platform C++ library for hardware information (CPU, RAM, GPU)]
- https://github.com/KDIo3/PCIBan [A PoC for requesting HWIDs directly from hardware]
- https://github.com/can1357/hvdetecc [Collection of hypervisor detections]
- https://github.com/synctop/tpm-mmio [Using MMIO (Memory-Mapped I/O) to read TPM 2.0 public Endorsement Key]
- https://github.com/asm1314/Uncloaking-RAID0-HWID-Serials [Gather original disk serials hidden behind RAID0]
- https://github.com/hubblo-org/windows-rapl-driver [Windows driver to get RAPL metrics from a bare metal machine]
- https://github.com/trustdecision/trustdevice-android [Android]
- https://github.com/imxiaoc996/DeviceWarLock [Android]
- https://github.com/trustdecision/trustdevice-ios [IOS]

> Detection:SpeedHack
- https://github.com/DoranekoSystems/cheap-engine [Android]

> Detection:Injection
- https://github.com/mq1n/DLLThreadInjectionDetector
- https://github.com/Nou4r/ModFinder [Mapped Dll]
- https://github.com/gmh5225/Driver-WatchOwl [ImageNotify+Stack Trace]
- https://github.com/xuanxuan0/TiEtwAgent [ETW]
- https://github.com/JingMatrix/Demo [A demo app to detect (Zygisk) library injections]

> Detection:Spoof Stack
- https://github.com/gabriellandau/ShadowStackWalk
- https://github.com/cryotb/RASD

> Detection:ESP
- https://github.com/weak1337/PresentHookDetection

> Detection:DMA
- https://github.com/cutecatsandvirtualmachines/DmaProtect [VT-d/AMD-Vi IOMMU]
- https://github.com/iqrw0/DieDMAProtection [IOMMU]
- https://github.com/tandasat/HelloIommuPkg [The sample DXE runtime driver demonstrating how to program DMA remapping]
- https://github.com/ekknod/drvscan [Scanner]
- https://github.com/gmh5225/PCIE-Detector [Config Space]

> Detection:Wall Hack
- https://github.com/87andrewh/CornerCulling
- https://github.com/87andrewh/CornerCullingSourceEngine

> Detection:Obfuscation
- https://github.com/mrphrazer/obfuscation_detection

> Detection:Android root
- https://github.com/rushiranpise/detection [Collection of Various Root Detection Apps for Android]
- https://github.com/vvb2060/KeyAttestation [Bootloader]
- https://github.com/VisionR1/KeyAttestation [Bootloader]
- https://github.com/reveny/Android-Native-Root-Detector [A tool for detecting root on android]
- https://github.com/Mrack/MemDetection [Calculate the CRC of libc.so and libart.so in memory and compare it with the file]
- https://github.com/apkunpacker/RootAppDetector [Small POC code that detects known root-related apps by attempting to launch their activities and monitoring security exception]
- https://github.com/Rem01Gaming/meowna_detector [Prove of concept of detecting meowna module]

> Detection:Magisk
- https://github.com/vvb2060/MagiskDetector
- https://github.com/canyie/MagiskKiller
- https://github.com/Dr-TSNG/ApplistDetector
- https://github.com/apkunpacker/MagiskDetection
- https://github.com/canyie/MagiskEoP [exploit]
- https://github.com/JingMatrix/Demo [A demo app to detect (Zygisk) library injections]
- https://github.com/apkunpacker/DetectZygisk [A POC to detect zygisk]

> Detection:Frida
- https://github.com/darvincisec/DetectFrida
- https://github.com/qtfreet00/AntiFrida
- https://github.com/muellerberndt/frida-detection
- https://github.com/apkunpacker/Anti-Frida [Some Of Anti-Frida Stuff]

> Detection:Overlay
- https://github.com/Oliver-1-1/TOPMOST-Detection [Detect simple top most windows]
- https://github.com/geeksonsecurity/android-overlay-protection [Android]

> Signature Scanning
- https://github.com/c3rb3ru5d3d53c/binlex
- https://github.com/mischasan/aho-corasick

> Information System & Forensics
- https://lolc2.github.io [collection of C2 frameworks that leverage legitimate services to evade detection]
- https://github.com/Enum0x539/Qvoid-Token-Grabber
- https://github.com/travisfoley/dfirtriage
- https://github.com/AlessandroZ/LaZagne
- https://github.com/thewhiteninja/ntfstool
- https://github.com/mgeeky/ntfs-journal-viewer
- https://github.com/volatilityfoundation/volatility
- https://github.com/volatilityfoundation/volatility3
- [Decrypt and export browser password, including Chromium,Edge and Firefox](https://github.com/BL0odz/BrowserPasswordExportor)
- https://github.com/gtworek/VolatileDataCollector
- https://github.com/mubix/netview
- https://github.com/rbmm/USN
- https://github.com/rbmm/SearchEx
- https://github.com/ch3rn0byl/ANTfs
- https://github.com/strozfriedberg/ntfs-linker
- https://github.com/NTFSparse/ntfs_parse
- https://github.com/bluecapesecurity/PWF [Windows Forensics Training]
- https://github.com/qwqdanchun/Pillager [For exporting and decrypting useful data from target computer]
- https://github.com/Psmths/windows-forensic-artifacts [Guide to the various Windows forensic artifacts]
- https://github.com/rabbitstack/fibratus [Windows kernel exploration and tracing]
- https://github.com/google/grr [remote live forensics]
- https://github.com/MrMugiwara/FTK-imager-OSX [Forensics Tools For MAC OS X]
- https://github.com/h4sh5/DumpIt-mirror [DumpIt for windows]
- https://github.com/MagnetForensics/dumpit-linux [DumpIt for linux]
- https://github.com/GuidoBartoli/sherloq [An open-source digital image forensic toolset]
- https://github.com/kyxiaxiang/CobaltStrikeBeaconCppSource [Out-of-the-box CobaltStrike Beacon source code use C++]
- https://github.com/olafhartong/BamboozlEDR [A comprehensive ETW (Event Tracing for Windows) event generation tool designed for testing and research purposes]
- https://github.com/artmih24/TeleParser [Simple parser for Telegram chats and channels with lemmatizer. Writes data in JSON, CSV and MongoDB]

> Dynamic Script
- https://github.com/can1357/NtLua
- https://github.com/mrexodia/NtPhp
- https://github.com/FastVM/minivm
- https://github.com/jnz/q3vm

> Kernel Mode Winsock
- https://github.com/MiroKaku/libwsk [Kernel-Mode Winsock library]

> Fuzzer
- https://github.com/0vercl0k/wtf

> OpenCV
- https://github.com/YouNeverKnow00/Rust-Auto-Weapon-Detection-OpenCV-Example

> Windows Ring3 Callback
- https://github.com/aahmad097/AlternativeShellcodeExec
- https://github.com/whokilleddb/function-collections [A collection of PoCs to do common things in unconventional ways]
- https://github.com/RixedLabs/IDLE-Abuse
- https://github.com/Wra7h/FlavorTown
- https://github.com/Deputation/instrumentation_callbacks [Instrumentation Callback]
- https://github.com/R4YVEN/beservice_intcallbacks [Instrumentation Callback]
- https://github.com/secrary/Hooking-via-InstrumentationCallback [Instrumentation Callback]
- https://github.com/paranoidninja/EtwTi-Syscall-Hook [Instrumentation Callback]
- https://github.com/jackullrich/syscall-detect [Instrumentation Callback]
- https://github.com/thetuh/anticheat-poc [Instrumentation Callback]
- https://github.com/1027565/InstrumentationCallbacks [Instrumentation Callback]
- https://github.com/asamy/NastyAlignment [Instrumentation Callback to handle unaligned access exceptions]
- [Register VEH by hooking RtlpCallVectoredHandlers](https://github.com/AmJayden/custom-VEH)
- [ATPMiniDump Callback](https://github.com/b4rtik/ATPMiniDump)
- https://github.com/jimbeveridge/readdirectorychanges [ReadDirectoryChangesW]
- https://github.com/blaquee/dllnotif [DllNotification]
- https://github.com/gmh5225/LdrRegisterDllNotification-modify-testing [DllNotification]
- https://github.com/brew02/KiUserExceptionDispatcherHook [Hooking the Windows usermode exception handler]
- https://github.com/whokilleddb/function-collections/tree/main/hijack_callbacks/vkAllocateMemory [vkAllocateMemory]
- https://github.com/whokilleddb/function-collections/tree/main/hijack_callbacks/InternetSetStatusCallback [InternetStatusCallback]
- https://github.com/whokilleddb/function-collections/tree/main/winapi_alternatives/NtAllocateMemoryEx [tprtdll.dll.NtAllocateVirtualMemoryEx]

> Windows Ring0 Callback
- https://github.com/gmh5225/kernel-callback-functions-list [Callback List]
- [Enumerate Callback](https://github.com/hfiref0x/WinObjEx64/blob/7284d711b2eeebfd965713fc79353b9b76e23083/Source/WinObjEx64/extras/extrasCallbacks.c#L117)
- [ImageNotify Callback With RtlWalkFrameChain](https://github.com/Staatsgeheim/PsImageNotifyRoutineSpamFilter)
- [SymlinkCallback](https://github.com/yardenshafir/SymlinkCallback)
- https://github.com/Archie-osu/PowerHook [Hooking KPRCB IdlePreselect]
- https://github.com/Dor00tkit/BamExtensionTableHook [bam!BampCreateProcessCallback]

> Winows User Dump Analysis
- https://github.com/0vercl0k/udmp-parser

> Winows Kernel Dump Analysis
- https://github.com/gmh5225/Tool-DIYSystemMemoryDump [DIY Dump Type]
- https://github.com/0vercl0k/kdmp-parser [Python 3 bindings]
- https://github.com/mrexodia/dumpulator [Emulating code in minidump files]
- https://github.com/0vercl0k/symbolizer [Execution trace symbolizer]
- https://github.com/libyal/libmdmp [Minidump]
- https://github.com/tasox/miniDumpReader [Minidump]

> Sign Tools
- https://github.com/mtrojnar/osslsigncode
- https://github.com/gmh5225/chainoffools [CVE]
- https://github.com/mattifestation/WDACTools [Decrypt p7b]
- https://github.com/utoni/PastDSE [Sign Leaked Cert]
- https://github.com/Jemmy1228/HookSigntool [Sign Leaked Cert]
- https://github.com/namazso/MagicSigner [Sign Leaked Cert]
- https://github.com/hzqst/FuckCertVerifyTimeValidity [Sign Leaked Cert]
- https://github.com/mathisvickie/sign-expired [Sign Leaked Cert]
- https://github.com/hackerhouse-opensource/SignToolEx [Sign Leaked Cert]

> Backup File
- https://github.com/guidoreina/minivers [Generates Backup Copies]

> Backup Drivers
- https://github.com/gloriouslegacy/ezDrvBAK [Backup & restrore the Windows-Drivers]

> Black Signature
- https://github.com/gmh5225/BlackSignatureDriver
- https://github.com/jsecurity101/MSFT_DriverBlockList
- https://github.com/Harvester57/CodeIntegrity-DriverBlocklist
- https://github.com/gmh5225/MS-Vulnerable-Driver-List [Convert Microsoft's blocklist to a hash list]

## Some Tricks
> Windows Ring0
- https://www.unknowncheats.me/forum/general-programming-and-reversing/495279-messagebox-kernel-mode.html [Msgbox]
- https://back.engineering/01/12/2020/ [Page Table Manipulation]
- https://git.back.engineering/_xeroxz/PSKP [PTE Hook]
- https://github.com/Rythorndoran/PageTableHook [PTE Hook]
- https://github.com/stdhu/windows-kernel-pagehook [PTE Hook]
- https://github.com/Xyrem/Yumekage [PTE Hook]
- https://github.com/brew02/FastPFHook [PF Hook]
- https://github.com/Compiled-Code/be-injector [Attack COW]
- https://github.com/Compiled-Code/eac-mapper [Vulnerable MmCopyMemory]
- https://github.com/EBalloon/MmCopyMemory [Bypass MmCopyMemory]
- https://github.com/Compiled-Code/be-injector [Attack COW]
- https://github.com/gmh5225/Allocating-individual-pages [MmAllocateIndependentPagesEx]
- https://github.com/gmh5225/Hook-HvlSwitchVirtualAddressSpace [HvcallCodeVa]
- https://github.com/1401199262/HookHvcallCodeVa [HvcallCodeVa]
- https://github.com/gmh5225/Driver-HypercallPageHook [HvcallCodeVa]
- https://github.com/Xyrem/HyperDeceit [HvcallCodeVa]
- https://github.com/gmh5225/CallMeWin32kDriver [Load your driver like win32k.sys]
- https://github.com/gmh5225/DSEDodge-Signed-Kernel-Driver [Leveraging PTT to defeat DSE]
- https://github.com/wbenny/KSOCKET [Kernel Berkeley socket]
- https://github.com/StephanvanSchaik/windows-kernel-rs [Writing Windows kernel drivers in Rust]
- https://github.com/ekknod/smm [Smm cheat]
- https://github.com/rbmm/KPDB [Parsing PDB in Driver]
- https://github.com/GetRektBoy724/KPDB [Parsing PDB in Driver]
- https://github.com/gmh5225/FakeEnclave [A poc that abuses Enclave]
- https://github.com/gmh5225/LetMeGG [A POC about how to prevent windbg break]
- https://github.com/UCFoxi/NotifyRoutineHijackThread [Hijack PspCreateThreadNotifyRoutine]
- [GetWindowName In Kernel Mode](https://www.unknowncheats.me/forum/anti-cheat-bypass/517022-getwindowname-kernel-mode.html)
- [GetWindowInfo In Kernel Mode](https://www.unknowncheats.me/forum/anti-cheat-bypass/519261-getwindowinfo.html)
- [Hook KdTrap(Windows global exception hander)](https://www.unknowncheats.me/forum/anti-cheat-bypass/500156-hook-kdtrap-windows-global-exception-hander.html) [Hook KdTrap]
- https://github.com/gmh5225/Hook-KdTrap [Hook KdTrap]
- https://github.com/gmh5225/AcDrv [Global exception/KdpDebugRoutineSelect]
- https://github.com/SamuelTulach/HookGuard [Global exception/KdpDebugRoutineSelect]
- https://github.com/gmh5225/AcDrv [SwapContext hook]
- https://github.com/1401199262/HookSwapContext [SwapContext hook]
- https://github.com/gmh5225/Driver-SoulExtraction [Extracting cert information]
- https://github.com/Ido-Moshe-Github/CiDllDemo [Use ci.dll API for validating Authenticode signature of files]
- https://github.com/mihaly044/pedigest [Calculating the authenticode digest]
- https://github.com/gmh5225/Kernel-Special-APC-ReadProcessMemory [Kernel APC RPM]
- https://github.com/NSG650/Bad-BugCheck-Old [BSOD]
- https://github.com/NSG650/Bad-Bugcheck [BSOD]
- https://github.com/NSG650/NoMoreBugCheck [BSOD]
- https://github.com/NSG650/BugCheckHack [BSOD]
- https://github.com/NSG650/BugCheck2Linux [BSOD]
- https://github.com/AnalogFeelings/KmdfMandelcheck [BSOD]
- https://github.com/stuxnet147/PiDqSerializationWrite-Example [PiDqSerializationWrite]
- https://github.com/Rythorndoran/enum_real_dirbase [Find real dirbase]
- https://github.com/backengineering/POC-ExFlushTb [A POC for monitoring Tb]
- https://github.com/Cr4sh/KernelForge [A library to develop kernel level Windows payloads for post HVCI era]
- https://gist.github.com/gmh5225/ab00f831ffdf4ef608ab3b6eb0d37250 [Create process from KernelMode via APC]
- https://github.com/gmh5225/Map-file-in-system-space [MiMapViewInSystemSpace]
- https://github.com/SamuelTulach/PwnedBoot [Using Windows' own bootloader as a shim to bypass Secure Boot]
- https://github.com/Archie-osu/PowerHook [Hooking KPRCB IdlePreselect]
- https://github.com/Th3Spl/IoCreateDriver [IoCreateDriver Implementation]
- https://github.com/brew02/BudgetEPT [Create stealthy, inline, EPT-like hooks using SMAP and SMEP]
- https://github.com/r0keb/Smep-Bypass [Various techniques used to bypass SMEP in the Windows Kernel]
- https://github.com/brew02/CovertThread [Creating covert system threads on Windows by leveraging the page tables and IDT]


> Windows Ring3
- https://secret.club/2021/01/04/thread-stuff.html [Anti Debug]
- https://github.com/utoni/PastDSE [Sign Leaked Cert]
- https://github.com/Jemmy1228/HookSigntool [Sign Leaked Cert]
- https://github.com/namazso/MagicSigner [Sign Leaked Cert]
- https://github.com/hzqst/FuckCertVerifyTimeValidity [Sign Leaked Cert]
- https://github.com/mathisvickie/sign-expired [Sign Leaked Cert]
- https://github.com/Sentient111/StealingSignatures [Stealing signatures from pe files]
- https://github.com/secretsquirrel/SigThief [Stealing signatures from pe files]
- https://github.com/dslee2022/SignatureKid [Stealing signatures from pe files]
- https://github.com/jfmaes/LazySign [Fake Cert]
- https://github.com/Tylous/Limelighter [Fake Cert]
- https://github.com/gmh5225/chainoffools [Fake Cert]
- https://github.com/gmh5225/FakeSign [Fake Cert]
- https://github.com/Adepts-Of-0xCC/MiniDumpWriteDumpPoC [Dump Memory]
- [A x64 Write-What-Where exploit+shellcode execution vulnerability](https://www.unknowncheats.me/forum/anti-cheat-bypass/503519-wwwaryasinject-x64-write-exploit-shellcode-execution-vulnerability.html)
- [Dll injection through code page id modification in registry](https://github.com/NtQuerySystemInformation/NlsCodeInjectionThroughRegistry)
- https://github.com/huoji120/Etw-Syscall [ETW Syscall]
- https://github.com/weak1337/SkipHook [Skip Hook]
- https://github.com/ekknod/SetWindowHookEx [Using SetWindowHookEx for preinjected DLL's]
- [A tool for patching authenticode signed PE files (exe, dll, sys ..etc) without invalidating or breaking the existing signature](https://github.com/med0x2e/SigFlip)
- [Simple program to stream offsets for your game cheat](https://github.com/gmh5225/OffsetStreaming)
- https://github.com/jnastarot/HIGU_ntcall [Direct System Calls]
- https://github.com/rbmm/LockFile-Poc [Lock File]
- https://github.com/EvilBytecode/IDontLikeFileLocks [Dump locked files by stealing memory-mapped section handle]
- [A kernel exploit leveraging NtUserHardErrorControl to elevate a thread to KernelMode and achieve arbitrary kernel R/W & more](https://github.com/gmh5225/ANGRYORCHARD)
- https://github.com/gmh5225/dll-encryptor [Able to stream a dll without touching your disk]
- [Running Shellcode Through EnumDisplayMonitors](https://marcoramilli.com/2022/06/15/running-shellcode-through-windows-callbacks/?utm_source=twitter&utm_medium=social&utm_campaign=ReviveOldPost)
- [open-source windows defender manager can disable windows defender permanently](https://github.com/qtkite/defender-control)
- [Read Memory without ReadProcessMemory for Current Process](https://github.com/gmh5225/CReadMemory)
- [get process token whose integrity level is system and manipulate it to get privilege escalation](https://github.com/gmh5225/manipulating_token)
- [A library that meant to perform evasive communication using stolen browser socket](https://github.com/Idov31/Venom)
- https://github.com/cpz/trinity [Fully disables & removes Windows Defender]
- https://github.com/EvilGreys/Disable-Windows-Defender- [Disable Windows Defender]
- https://github.com/gabriellandau/ShadowStackWalk [Finding Truth in the Shadows]
- https://github.com/gmh5225/r0ak [r0ak]
- https://github.com/ZeroMemoryEx/Wizard-Loader [Abuse Xwizard.exe for DLL Side-Loading]
- https://github.com/LloydLabs/shellcode-plain-sight [Hiding shellcode in plain sight within a large memory region]
- https://github.com/huntandhackett/process-cloning [Clone process]
- https://github.com/backengineering/msrexec [Elevate arbitrary MSR writes to kernel execution]
- https://github.com/deepinstinct/Dirty-Vanity [Abusing RtlCreateProcessReflection]
- https://github.com/mandiant/ShimCacheParser [Shim Cache parser]
- https://github.com/cmuratori/pmctrace [Real-time collection of PMCs via ETW]
- https://github.com/Idov31/EtwLeakKernel [Leaking kernel addresses from ETW consumers. Requires Administrator privileges]
- https://github.com/SamuelTulach/SecureGame [POC game using VBS enclaves to protect itself from cheating]
- https://github.com/Teach2Breach/moonwalk [find dll base addresses without PEB WALK]
- https://github.com/brew02/KiUserExceptionDispatcherHook [Hooking the Windows usermode exception handler]
- https://github.com/brew02/MountSystemPartition [Mounting the system partition on Windows]
- https://github.com/LloydLabs/delete-self-poc [A way to delete a locked file, or current running executable, on disk]
- https://github.com/rad9800/BootExecuteEDR [BootExecute EDR Bypass]
- https://github.com/unkvolism/Solemn [A command-line tool for Windows that automates adding drivers to the HVCI (HvciDisallowedImages) custom blocklist]
- https://github.com/2x7EQ13/CreateProcessAsPPL [This is the loader that supports running a program with Protected Process Light (PPL) protection functionality]
- https://github.com/waryas/WaryasSWHE [Usermode exploit to bypass any AC using a 0day shatter attack]
- https://github.com/Peribunt/VPGATHER [Using the peculiar behaviour of the VPGATHER instructions to determine if an address will fault before it is truly accessed]

> Linux
- https://github.com/MatheuZSecurity/RingReaper [Linux post-exploitation agent that uses io_uring to stealthily bypass EDR detection by avoiding traditional syscalls]

> Android
- https://github.com/WindySha/bypassHiddenApiRestriction [Bypass hidden api restriction]
- https://github.com/LSPosed/AndroidHiddenApiBypass [Bypass hidden api restriction]
- https://github.com/stars-one/ASCTool [Apk Signature Crack Tool]
- https://github.com/ekknod/usbsn [USB serial number changer (root only)]
- https://github.com/gmh5225/Android-privilege-CVE-2022-20452-LeakValue [Privilege Escalation]
- https://github.com/tiann/KernelSU [A Kernel based root solution for Android GKI]
- https://github.com/MlgmXyysd/KernelSU_Debug [KernelSU modified for debugging]
- https://github.com/CoolestEnoch/kernel-su-huawei-nova2 [KernelSU for huawei]
- https://github.com/gmh5225/android_kernel_huawei_hi6250-8_Exp [KernelSU for huawei]
- https://github.com/abcz316/SKRoot-linuxKernelRoot [Kernel root]
- https://github.com/Dr-TSNG/ZygiskOnKernelSU [Run Zygisk on KernelSU]


## Windows Security Features
- https://github.com/yardenshafir/cet-research [CET]
- https://github.com/gmh5225/CET-win10 [CET]
- [HyperGuard](https://windows-internals.com/hyperguard-secure-kernel-patch-guard-part-1-skpg-initialization)
- https://github.com/gmh5225/QueryShadowStack [Shadow Stack]
- https://github.com/synacktiv/windows_kernel_shadow_stack [Shadow Stack]
- https://namazso.github.io/x86/html/INCSSPD_INCSSPQ.html [CET]
- https://techcommunity.microsoft.com/t5/windows-os-platform-blog/understanding-hardware-enforced-stack-protection/ba-p/1247815 [CET]
- https://reviews.llvm.org/rG21b25a1fb32ecd2e1f336123c2715f8ef1a49f97 [CET]
- https://www.osronline.com/article.cfm%5earticle=469.htm [SEH]


## WSL
- https://github.com/microsoft/WSL
- https://github.com/microsoft/WSL2-Linux-Kernel
- https://github.com/sxlmnwb/windows-subsystem-linux
- https://github.com/Nevuly/WSL2-Linux-Kernel-Rolling [Stable Kernel for WSL2]

## WSA
- https://github.com/K3V1991/How-to-download-and-install-WSA [Guide]
- https://github.com/KiruyaMomochi/wsa-kernel-build [Build WSA Kernel with Docker]
- https://github.com/sergiovillaverde/win11_apk_installer
- https://github.com/LSPosed/MagiskOnWSA
- https://github.com/alesimula/wsa_pacman
- https://github.com/WSA-Community/WSA-Linux-Kernel
- https://github.com/Paxxs/BuildWSA
- https://github.com/LSPosed/MagiskOnWSALocal
- https://github.com/cinit/WSAPatch [Make WSA run on Windows 10]
- https://github.com/MustardChef/WSABuilds
- https://github.com/LSPosed/WSA-Kernel-SU [WSA with KernelSU]

## Windows Emulator
- https://github.com/brunodev85/winlator [Android application for running Windows applications with Wine and Box86/Box64]
- https://github.com/x86matthew/WinVisor [A hypervisor-based emulator for Windows x64 user-mode executables using Windows Hypervisor Platform API]
- https://github.com/momo5502/sogen [Windows User Space Emulator]
- https://github.com/mojtabafalleh/emulator [Windows User Space Emulator]
- https://github.com/binsnake/KUBERA [A x86 environment emulator for Windows user and kernel binaries]
- https://github.com/ShallowFeather/KDemu [A hybrid semi-emulated, semi-native Windows kernel driver emulator designed for advanced rootkit and anti-cheat analysis, addressing the limitations of existing emulation solutions]

## Linux Emulator
- https://github.com/OFFTKP/felix86 [Run x86-64 programs on RISC-V Linux]

## Android Emulator
- https://github.com/Genymobile
- https://github.com/Genymobile/genymotion-kernel
- https://github.com/anbox/anbox
- https://github.com/jwmcglynn/android-emulator
- https://github.com/google/android-emulator-hypervisor-driver
- https://github.com/ant4g0nist/rudroid [Rust]
- https://github.com/qemu-gvm/qemu-gvm [QEMU]
- https://github.com/quarkslab/AERoot [Root]

## IOS Emulator
- https://github.com/ChefKissInc/qemu-apple-silicon

## Game Boy
- https://github.com/xkevio/kevboy [Emulator]
- https://github.com/vojty/feather-gb [Emulator]
- https://github.com/chrismaltby/gb-studio [GB Studio]

## Nintendo Switch
- https://github.com/yuzu-mirror
- https://github.com/Ryujinx/Ryujinx
- https://github.com/gmh5225/Nintendo-Switch-Emulator-yuzu
- https://github.com/gmh5225/yuzu-android
- https://github.com/Logboy2000/yuzu-archive
- https://github.com/Gamer64ytb/Yuzu-Backup
- https://github.com/gmh5225/nuzu [Yuzu based repository]
- https://github.com/CTCaer/hekate [A GUI based Nintendo Switch Bootloader]
- https://github.com/Atmosphere-NX/Atmosphere [Customized firmware]
- https://github.com/tomvita/SE-tools [Memory hacking]
- https://github.com/jakcron/nstool [General purpose read/extract tool]

## Xbox
- https://github.com/xemu-project/xemu [Xbox Emulator for Windows]
- https://github.com/xenia-project/xenia [Xbox 360 Emulator Research Project]
- https://github.com/wmarti/xenia-mac [MacOS Port of the Xbox 360 Emulator]
- https://github.com/rexdex/recompiler [Porting Xbox360 executables to Windows]
- https://github.com/exploits-forsale/collateral-damage [Kernel exploit for Xbox SystemOS using CVE-2024-30088]
- https://github.com/Byrom90/XenonDumper [Dumps files & data required to use the Xenon Xbox 360 Low Level Emulator]
- https://github.com/exjam/xbox360-emu [A xbox 360 emulator]

