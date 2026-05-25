# tarunai-connect-sbox

CLI harness for s&box game engine (Facepunch Studios, Source 2). 79 commands across 14 groups.

## Prerequisites

- Python 3.9+
- s&box installed via Steam (auto-detected, or set `SBOX_PATH`)

## Installation

```bash
cd agent-harness/
pip install -e .
```

## Commands

### project - Manage projects

```bash
tarunai-connect-sbox project new --name MyGame --output-dir ./MyGame
tarunai-connect-sbox --json project info
tarunai-connect-sbox project config --max-players 32 --tick-rate 64
tarunai-connect-sbox --json --project ./MyGame project add-package facepunch.libsdf
tarunai-connect-sbox --json --project ./MyGame project remove-package facepunch.libsdf
# Project lint - find broken asset refs, duplicate GUIDs, malformed inputs
tarunai-connect-sbox --json --project ./MyGame project validate
tarunai-connect-sbox --project ./MyGame project validate --no-inputs --no-guids
```

### scene - Manipulate .scene files

```bash
tarunai-connect-sbox scene new --name gameplay -o ./Assets/scenes/gameplay.scene
tarunai-connect-sbox --json scene info ./Assets/scenes/minimal.scene
tarunai-connect-sbox --json scene list ./Assets/scenes/minimal.scene
tarunai-connect-sbox scene add-object ./scene.scene Enemy --position "100,0,0" --components "model,box_collider,rigidbody" --tags "enemy"
tarunai-connect-sbox scene remove-object ./scene.scene --name Enemy
tarunai-connect-sbox scene add-component ./scene.scene <guid> Sandbox.PointLight
tarunai-connect-sbox scene remove-component ./scene.scene <guid> --component-type Sandbox.Rigidbody
tarunai-connect-sbox --json scene modify-object ./scene.scene --guid <guid> --name NewName --position "200,0,0"
tarunai-connect-sbox --json scene clone-object ./scene.scene --name Enemy --new-name EnemyCopy --position "300,0,0"
tarunai-connect-sbox --json scene get-object ./scene.scene --name Sun
tarunai-connect-sbox scene set-property ./scene.scene --fixed-update-freq 64 --timescale 0.5
tarunai-connect-sbox scene set-navmesh ./scene.scene --enabled --agent-height 72 --agent-radius 16
tarunai-connect-sbox --json scene list-presets
# Find objects matching one or more filters (AND-combined)
tarunai-connect-sbox --json scene query ./scene.scene --has-component rigidbody --has-tag tower
tarunai-connect-sbox --json scene query ./scene.scene --name-regex "^Tower\d$" --in-bounds "0,-500,-50,1000,500,50"
# Extract every asset reference (.vmdl, .vmat, .vsnd, .vtex, .vpcf, .prefab) from a scene
tarunai-connect-sbox --json scene refs ./scene.scene
# Apply the same modification to every object that matches a query
tarunai-connect-sbox --json scene bulk-modify ./scene.scene --has-tag tower --position "0,0,100" --enable
# Structural diff between two scenes (added/removed/modified GameObjects + SceneProperties)
tarunai-connect-sbox --json scene diff ./old.scene ./new.scene
# Insert a prefab as a GameObject in a scene
tarunai-connect-sbox --json scene instantiate-prefab ./level.scene ./Assets/prefabs/bullet.prefab --position "10,0,0"
```

### prefab - Manage .prefab files

```bash
tarunai-connect-sbox prefab new --name Bullet -o ./Assets/prefabs/bullet.prefab --components "model,sphere_collider,rigidbody"
tarunai-connect-sbox --json prefab info ./Assets/prefabs/bullet.prefab
tarunai-connect-sbox prefab from-scene ./scene.scene <guid> -o ./Assets/prefabs/extracted.prefab
tarunai-connect-sbox --json prefab add-component ./prefab.prefab rigidbody
tarunai-connect-sbox prefab remove-component ./prefab.prefab --component-type Sandbox.Rigidbody
# Extract asset references from a prefab
tarunai-connect-sbox --json prefab refs ./prefab.prefab
# Modify a component's properties on a prefab
tarunai-connect-sbox --json prefab modify-component ./prefab.prefab --component-type Sandbox.Rigidbody --properties '{"Gravity":false,"MassOverride":50}'
# Structural diff between two prefabs (root + children by Name)
tarunai-connect-sbox --json prefab diff ./old.prefab ./new.prefab
```

### codegen - Generate C# code

```bash
# Component
tarunai-connect-sbox codegen component --name PlayerController --methods OnUpdate,OnFixedUpdate -o ./Code/PlayerController.cs
tarunai-connect-sbox --json codegen component --name Tower --properties '[{"name":"Damage","type":"float","default":"25f"}]'

# Networked component with RPC
tarunai-connect-sbox codegen component --name NetPlayer --networked --rpc-methods "Fire:Broadcast,Die:Host" -o ./Code/NetPlayer.cs

# GameResource
tarunai-connect-sbox codegen gameresource --name TowerData --display-name "Tower Data" --extension tower -o ./Code/TowerData.cs

# Editor menu
tarunai-connect-sbox codegen editor-menu --name MyTools --menu-path "Editor/My Tools/Open" -o ./Editor/MyTools.cs

# Razor UI component (generates .razor + .razor.scss)
tarunai-connect-sbox codegen razor --name HudPanel --properties '[{"name":"Score","type":"int","default":"0"}]' -o ./UI/HudPanel.razor

# PanelComponent + sibling ScreenPanel scaffold (handles the s&box gotcha
# where input only works when both are on the same GameObject).
# Emits .razor + .razor.scss + a paste-ready GameObject snippet, or appends
# directly to a scene with --scene.
tarunai-connect-sbox --json codegen panel-component --name HudBar -o ./UI/HudBar.razor
tarunai-connect-sbox codegen panel-component --name Crosshair -o ./UI/Crosshair.razor --scene ./Assets/scenes/game.scene
```

### input - Manage Input.config

```bash
tarunai-connect-sbox --json input list
tarunai-connect-sbox input add --name PlaceTower --group Gameplay --keyboard mouse1 --gamepad RightTrigger
tarunai-connect-sbox input remove --name PlaceTower
tarunai-connect-sbox input set --name Attack1 --keyboard mouse1
```

### collision - Manage Collision.config

```bash
tarunai-connect-sbox --json collision list
tarunai-connect-sbox collision add-layer --name projectile --default Collide
tarunai-connect-sbox collision add-rule --layer-a projectile --layer-b solid --result Collide
tarunai-connect-sbox collision remove-rule --layer-a projectile --layer-b solid
tarunai-connect-sbox collision remove-layer --name projectile
```

### material - Manage .vmat materials

```bash
tarunai-connect-sbox --json material new --name floor --shader complex --color-texture "textures/floor.tga" --metalness 0.3 -o ./Assets/materials/floor.vmat
tarunai-connect-sbox --json material info ./Assets/materials/floor.vmat
tarunai-connect-sbox --json material list
tarunai-connect-sbox --json material set ./Assets/materials/floor.vmat --metalness 0.8
```

### sound - Manage .sound events

```bash
tarunai-connect-sbox --json sound new --name gunshot --sounds "sounds/gun1.vsnd,sounds/gun2.vsnd" --volume 0.8 -o ./Assets/sounds/gunshot.sound
tarunai-connect-sbox --json sound info ./Assets/sounds/gunshot.sound
tarunai-connect-sbox --json sound list
tarunai-connect-sbox --json sound set ./Assets/sounds/gunshot.sound --volume 0.5
```

### localization - Manage translations

```bash
tarunai-connect-sbox localization new --lang en -o ./Localization/en.json
tarunai-connect-sbox localization set ./Localization/en.json --key "game.title" --value "My Game"
tarunai-connect-sbox --json localization list ./Localization/en.json
tarunai-connect-sbox localization get ./Localization/en.json --key "game.title"
tarunai-connect-sbox localization remove ./Localization/en.json --key "game.title"
```

### server - Dedicated server

```bash
tarunai-connect-sbox server info
tarunai-connect-sbox server start --game my_game --map facepunch.flatgrass
```

### asset - Asset management

```bash
tarunai-connect-sbox --json asset list --type scene
tarunai-connect-sbox --json asset info ./Assets/scenes/minimal.scene
tarunai-connect-sbox asset compile ./Assets/materials/floor.vmat
# Reverse lookup: which scenes/prefabs reference an asset?
tarunai-connect-sbox --json --project ./MyGame asset find-refs models/myteam/widget.vmdl
# Find unreferenced assets (per type or across all referenceable types)
tarunai-connect-sbox --json --project ./MyGame asset find-unused
tarunai-connect-sbox --json --project ./MyGame asset find-unused --type model --type material
# Rename an asset and update every scene/prefab reference (extension preserved if omitted)
tarunai-connect-sbox --json --project ./MyGame asset rename models/team/widget.vmdl gizmo
tarunai-connect-sbox --project ./MyGame asset rename models/team/widget.vmdl gizmo --dry-run
# Move an asset across directories and update every reference
tarunai-connect-sbox --json --project ./MyGame asset move models/team/widget.vmdl models/shared/widget.vmdl
```

### session - State management

```bash
tarunai-connect-sbox session status
tarunai-connect-sbox session undo
tarunai-connect-sbox session redo
```

### launch - Open in editor

```bash
tarunai-connect-sbox launch
```

## REPL Mode

Run with no arguments for interactive mode:

```bash
tarunai-connect-sbox
```

Type `help` for commands, `quit` to exit.

## JSON Output

Pass `--json` for machine-readable output (for AI agents):

```bash
tarunai-connect-sbox --json scene list ./Assets/scenes/minimal.scene
```

## 29 Component Presets

Use with `--components` on scene/prefab commands: `model`, `box_collider`, `sphere_collider`, `rigidbody`, `camera`, `light_directional`, `light_point`, `spot_light`, `ambient_light`, `player_controller`, `capsule_collider`, `plane_collider`, `model_collider`, `sprite_renderer`, `skinned_model_renderer`, `text_renderer`, `line_renderer`, `decal_renderer`, `particle_effect`, `sound_point`, `nav_mesh_agent`, `screen_panel`, `world_panel`, `fixed_joint`, `hinge_joint`, `spring_joint`, `ball_socket_joint`, `trail_renderer`, `character_controller`.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SBOX_PATH` | s&box installation directory | Auto-detected from Steam |
