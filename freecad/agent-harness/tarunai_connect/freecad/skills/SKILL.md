---
name: "tarunai-connect-freecad"
description: "Complete CLI harness for FreeCAD parametric 3D CAD modeler (258 commands). Covers ALL workbenches: Part (29 primitives + boolean + mirror + loft + sweep), Sketcher (26 cmds: geometry + constraints + editing), PartDesign (38 cmds: pad/pocket/groove/fillet/chamfer/patterns/hole/datum), Assembly (11 cmds), Mesh (16 cmds), TechDraw (15 cmds: views + dimensions + PDF/SVG), Draft (33 cmds: 2D shapes + arrays + transforms), FEM (12 cmds), CAM/CNC (10 cmds), Surface (6 cmds), Spreadsheet (7 cmds), Import (13 formats), Export (17 formats), Measure (12 cmds), Materials (21 presets). Headless FreeCAD export to STEP/IGES/STL/OBJ/DXF/PDF/glTF/3MF."
---

# tarunai-connect-freecad

Complete CLI harness for **FreeCAD** — 258 commands across 17 groups covering ALL workbenches.

## Prerequisites

FreeCAD must be installed: `freecadcmd` must be in PATH.

## Installation

```bash
pip install -e freecad/agent-harness
```

## Basic Usage

```bash
tarunai-connect-freecad --json <command>           # JSON output for agents
tarunai-connect-freecad --json -p proj.json <cmd>  # With project file
tarunai-connect-freecad                            # Interactive REPL
```

## Preview, Live Preview, and Motion

FreeCAD is currently the deepest preview integration in this branch.

Preview commands:

```bash
# List preview recipes
tarunai-connect-freecad --json -p proj.json preview recipes

# Capture a real 4-view bundle
tarunai-connect-freecad --json -p proj.json preview capture --recipe quick

# Start poll-mode live preview
tarunai-connect-freecad --json -p proj.json preview live start --recipe quick --mode poll --source-poll-ms 500

# Query current live state without rendering
tarunai-connect-freecad --json -p proj.json preview live status --recipe quick

# Stop live preview publication
tarunai-connect-freecad --json -p proj.json preview live stop --recipe quick
```

Typical `quick` bundle artifacts:

- `hero.png`
- `front.png`
- `top.png`
- `right.png`

Live preview persists:

- `session.json`
- immutable bundle directories
- `trajectory.json`

`preview live status --json` is intended for agents and includes a compact
`trajectory_summary` in addition to `_session_dir`, current bundle refs, and
`_trajectory_path`.

Viewer commands:

```bash
cli-hub previews inspect /path/to/bundle-or-session
cli-hub previews html /path/to/bundle-or-session -o page.html
cli-hub previews watch /path/to/session --open
cli-hub previews open /path/to/bundle-or-session
```

Motion commands remain separate from preview and are used for final truthful
frame rendering and showcase videos:

```bash
tarunai-connect-freecad --json -p proj.json motion new --name spin --duration 6 --fps 24
tarunai-connect-freecad --json -p proj.json motion keyframe spin --time 0.0 --part 0 --position 0,0,0
tarunai-connect-freecad --json -p proj.json motion render-video spin output.mp4
```

## Command Groups (258 commands)

### document (5) — Document management
```bash
tarunai-connect-freecad --json document new --name "Part" -o proj.json
tarunai-connect-freecad --json document new --profile print3d -o proj.json
tarunai-connect-freecad --json -p proj.json document info
tarunai-connect-freecad --json -p proj.json document save -o copy.json
tarunai-connect-freecad --json document profiles
```

### part (29) — 3D primitives, boolean, transforms, operations
```bash
# Primitives: box, cylinder, sphere, cone, torus, wedge, helix, spiral, thread, plane, polygon_3d
tarunai-connect-freecad --json -p p.json part add box -P length=20 -P width=15 -P height=5
tarunai-connect-freecad --json -p p.json part add cylinder -P radius=3 -P height=10 --position 10,7.5,0

# Operations
tarunai-connect-freecad --json -p p.json part boolean cut 0 1
tarunai-connect-freecad --json -p p.json part copy 0
tarunai-connect-freecad --json -p p.json part mirror 0 --plane XY
tarunai-connect-freecad --json -p p.json part scale 0 --factor 2.0
tarunai-connect-freecad --json -p p.json part loft --indices 0,1,2
tarunai-connect-freecad --json -p p.json part sweep 0 1
tarunai-connect-freecad --json -p p.json part revolve 0 --axis Z --angle 360
tarunai-connect-freecad --json -p p.json part extrude 0 --direction 0,0,1 --length 10
tarunai-connect-freecad --json -p p.json part fillet-3d 0 --radius 2
tarunai-connect-freecad --json -p p.json part thickness 0 --thickness 1
tarunai-connect-freecad --json -p p.json part compound --indices 0,1,2
tarunai-connect-freecad --json -p p.json part section 0 --plane XY
tarunai-connect-freecad --json -p p.json part info 0
tarunai-connect-freecad --json -p p.json part line-3d --start 0,0,0 --end 10,5,0
tarunai-connect-freecad --json -p p.json part wire --points "0,0,0;10,0,0;10,10,0"
```

### sketch (26) — 2D constrained sketching
```bash
tarunai-connect-freecad --json -p p.json sketch new --plane XY
tarunai-connect-freecad --json -p p.json sketch add-line 0 --start 0,0 --end 20,0
tarunai-connect-freecad --json -p p.json sketch add-circle 0 --center 10,10 --radius 5
tarunai-connect-freecad --json -p p.json sketch add-rect 0 --corner 0,0 --width 20 --height 15
tarunai-connect-freecad --json -p p.json sketch add-arc 0 --center 0,0 --radius 5
tarunai-connect-freecad --json -p p.json sketch add-ellipse 0 --center 0,0 --major-radius 10 --minor-radius 5
tarunai-connect-freecad --json -p p.json sketch add-polygon 0 --center 0,0 --sides 6 --radius 10
tarunai-connect-freecad --json -p p.json sketch add-bspline 0 --points "0,0;5,10;10,0;15,10"
tarunai-connect-freecad --json -p p.json sketch add-slot 0 --center1 0,0 --center2 10,0 --radius 2
tarunai-connect-freecad --json -p p.json sketch constrain 0 distance --elements 0,1 --value 10
tarunai-connect-freecad --json -p p.json sketch edit-element 0 0 --radius 8
tarunai-connect-freecad --json -p p.json sketch remove-element 0 2
tarunai-connect-freecad --json -p p.json sketch validate 0
tarunai-connect-freecad --json -p p.json sketch solve-status 0
# Constraints: coincident, horizontal, vertical, parallel, perpendicular, equal,
#   fixed, distance, angle, radius, tangent, symmetric, block, diameter,
#   point_on_object, distance_x, distance_y
```

### body (38) — PartDesign features
```bash
tarunai-connect-freecad --json -p p.json body new
tarunai-connect-freecad --json -p p.json body pad 0 0 --length 10
tarunai-connect-freecad --json -p p.json body pocket 0 1 --length 5
tarunai-connect-freecad --json -p p.json body groove 0 0 --angle 360
tarunai-connect-freecad --json -p p.json body fillet 0 --radius 2
tarunai-connect-freecad --json -p p.json body chamfer 0 --size 1.5
tarunai-connect-freecad --json -p p.json body revolution 0 0 --angle 360
tarunai-connect-freecad --json -p p.json body additive-loft 0 --sketch-indices 0,1
tarunai-connect-freecad --json -p p.json body additive-pipe 0 0 1
tarunai-connect-freecad --json -p p.json body additive-helix 0 0 --pitch 5 --height 20
tarunai-connect-freecad --json -p p.json body additive-box 0 -P length=10 -P width=10 -P height=10
tarunai-connect-freecad --json -p p.json body hole 0 0 --diameter 5 --depth 10 --threaded
tarunai-connect-freecad --json -p p.json body draft-feature 0 --angle 5
tarunai-connect-freecad --json -p p.json body thickness-feature 0 --thickness 1
tarunai-connect-freecad --json -p p.json body linear-pattern 0 --occurrences 5 --length 50
tarunai-connect-freecad --json -p p.json body polar-pattern 0 --occurrences 6 --angle 360
tarunai-connect-freecad --json -p p.json body mirrored 0 --plane XY
tarunai-connect-freecad --json -p p.json body datum-plane 0 --reference XY --offset 10
```

### material (8) — PBR materials with engineering properties
```bash
# 21 presets: steel, aluminum, copper, brass, titanium, stainless_steel, cast_iron,
#   carbon_fiber, nylon, abs, pla, petg, plastic_white, plastic_black, wood, glass,
#   rubber, gold, concrete, granite, marble
tarunai-connect-freecad --json -p p.json material create --preset steel
tarunai-connect-freecad --json -p p.json material create --preset titanium
tarunai-connect-freecad --json -p p.json material assign 0 0
tarunai-connect-freecad --json -p p.json material set 0 density 7800
tarunai-connect-freecad --json -p p.json material import-material mat.json
tarunai-connect-freecad --json -p p.json material export-material 0 --output mat.json
```

### assembly (11) — Assembly management
```bash
tarunai-connect-freecad --json -p p.json assembly new --name "MyAssembly"
tarunai-connect-freecad --json -p p.json assembly add-part 0 0
tarunai-connect-freecad --json -p p.json assembly constrain 0 coincident --components 0,1
tarunai-connect-freecad --json -p p.json assembly constrain 0 distance --components 0,1 --distance 10
tarunai-connect-freecad --json -p p.json assembly solve 0
tarunai-connect-freecad --json -p p.json assembly dof 0
tarunai-connect-freecad --json -p p.json assembly bom 0
tarunai-connect-freecad --json -p p.json assembly explode 0 --factor 2.0
# Constraints: fixed, coincident, distance, angle, parallel, perpendicular,
#   tangent, revolute, prismatic, cylindrical, ball, planar, gear, belt
```

### mesh (16) — Mesh operations
```bash
tarunai-connect-freecad --json -p p.json mesh from-shape 0 --deviation 0.1
tarunai-connect-freecad --json -p p.json mesh import path/to/model.stl
tarunai-connect-freecad --json -p p.json mesh export 0 output.stl --format stl
tarunai-connect-freecad --json -p p.json mesh boolean union 0 1
tarunai-connect-freecad --json -p p.json mesh decimate 0 --target-faces 1000
tarunai-connect-freecad --json -p p.json mesh smooth 0 --iterations 5
tarunai-connect-freecad --json -p p.json mesh repair 0
tarunai-connect-freecad --json -p p.json mesh to-shape 0
```

### techdraw (15) — Technical drawings
```bash
tarunai-connect-freecad --json -p p.json techdraw new-page
tarunai-connect-freecad --json -p p.json techdraw add-view 0 0 --direction 0,0,1 --scale 1.0
tarunai-connect-freecad --json -p p.json techdraw add-projection-group 0 0
tarunai-connect-freecad --json -p p.json techdraw add-section-view 0 0
tarunai-connect-freecad --json -p p.json techdraw add-dimension 0 0 length --references 0,1
tarunai-connect-freecad --json -p p.json techdraw add-annotation 0 "Note text"
tarunai-connect-freecad --json -p p.json techdraw export-pdf 0 drawing.pdf
tarunai-connect-freecad --json -p p.json techdraw export-svg 0 drawing.svg
```

### draft (33) — 2D drafting
```bash
tarunai-connect-freecad --json -p p.json draft wire --points "0,0,0;10,0,0;10,10,0"
tarunai-connect-freecad --json -p p.json draft rectangle --width 20 --height 15
tarunai-connect-freecad --json -p p.json draft circle --radius 10
tarunai-connect-freecad --json -p p.json draft polygon --sides 6 --radius 10
tarunai-connect-freecad --json -p p.json draft text --content "Hello" --position 0,0,0
tarunai-connect-freecad --json -p p.json draft move 0 --vector 10,5,0
tarunai-connect-freecad --json -p p.json draft array-linear 0 --direction 1,0,0 --count 5 --spacing 10
tarunai-connect-freecad --json -p p.json draft array-polar 0 --center 0,0,0 --count 6
tarunai-connect-freecad --json -p p.json draft extrude 0 --direction 0,0,1 --length 10
tarunai-connect-freecad --json -p p.json draft to-sketch 0
```

### measure (12) — Measurement and analysis
```bash
tarunai-connect-freecad --json -p p.json measure volume 0
tarunai-connect-freecad --json -p p.json measure area 0
tarunai-connect-freecad --json -p p.json measure distance 0 1
tarunai-connect-freecad --json -p p.json measure bounding-box 0
tarunai-connect-freecad --json -p p.json measure center-of-mass 0
tarunai-connect-freecad --json -p p.json measure check-geometry 0
```

### surface (6) — Surface operations
```bash
tarunai-connect-freecad --json -p p.json surface filling --edges 0,1,2
tarunai-connect-freecad --json -p p.json surface sections --sections 0,1,2
tarunai-connect-freecad --json -p p.json surface extend 0 --length 10
tarunai-connect-freecad --json -p p.json surface sew --indices 0,1
```

### fem (12) — Finite Element Analysis
```bash
tarunai-connect-freecad --json -p p.json fem new-analysis
tarunai-connect-freecad --json -p p.json fem add-fixed 0 --references face1,face2
tarunai-connect-freecad --json -p p.json fem add-force 0 --references face3 --magnitude 1000
tarunai-connect-freecad --json -p p.json fem set-material 0 0
tarunai-connect-freecad --json -p p.json fem mesh-generate 0 --max-size 5
tarunai-connect-freecad --json -p p.json fem solve 0
tarunai-connect-freecad --json -p p.json fem results 0
```

### cam (10) — CNC machining
```bash
tarunai-connect-freecad --json -p p.json cam new-job 0
tarunai-connect-freecad --json -p p.json cam set-stock 0 --stock-type box
tarunai-connect-freecad --json -p p.json cam set-tool 0 --diameter 6 --type endmill
tarunai-connect-freecad --json -p p.json cam add-profile 0
tarunai-connect-freecad --json -p p.json cam add-pocket 0 --depth 5
tarunai-connect-freecad --json -p p.json cam generate-gcode 0
tarunai-connect-freecad --json -p p.json cam export-gcode 0 output.nc
```

### spreadsheet (7) — Parametric data tables
```bash
tarunai-connect-freecad --json -p p.json spreadsheet new
tarunai-connect-freecad --json -p p.json spreadsheet set-cell 0 A1 "50"
tarunai-connect-freecad --json -p p.json spreadsheet set-cell 0 B1 "=A1*2"
tarunai-connect-freecad --json -p p.json spreadsheet set-alias 0 A1 plate_width
tarunai-connect-freecad --json -p p.json spreadsheet export-csv 0 data.csv
```

### import (13) — Import CAD/mesh files
```bash
tarunai-connect-freecad --json -p p.json import auto model.step
tarunai-connect-freecad --json -p p.json import step model.step
tarunai-connect-freecad --json -p p.json import stl model.stl
tarunai-connect-freecad --json -p p.json import dxf drawing.dxf
tarunai-connect-freecad --json -p p.json import info model.step
# Formats: step, iges, stl, obj, dxf, svg, brep, 3mf, ply, off, gltf
```

### export (3) — Export to 17 formats
```bash
# Presets: step, iges, stl, stl_fine, obj, brep, fcstd, dxf, svg, gltf, 3mf, ply, off, amf, pdf, png, jpg
tarunai-connect-freecad --json -p p.json export render output.step --preset step
tarunai-connect-freecad --json -p p.json export render model.stl --preset stl --overwrite
tarunai-connect-freecad --json -p p.json export presets
```

### session (4) — Undo/redo
```bash
tarunai-connect-freecad --json -p p.json session undo
tarunai-connect-freecad --json -p p.json session redo
tarunai-connect-freecad --json -p p.json session status
tarunai-connect-freecad --json -p p.json session history
```

## JSON Output

All commands support `--json`. Responses include structured data. Errors: `{"error": "message"}`.

## Error Handling

- Missing FreeCAD: Clear install instructions
- Invalid types: Lists valid options
- Index out of range: Reports valid range
- File exists: Use `--overwrite`

## Agent Preview Notes

- Use `preview capture --json` whenever geometric changes need visual verification.
- Use `preview live start` for iterative build loops; prefer poll mode when the
  project file is being saved repeatedly.
- Use `preview live status --json` as the cheap status probe before reading the
  full `trajectory.json`.
- Treat `_bundle_dir` as a single snapshot only; the stable live identity is
  `_session_dir` plus `_trajectory_path`.
- Use `cli-hub previews ...` only to inspect/open already-published previews.
