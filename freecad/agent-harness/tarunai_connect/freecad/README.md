# tarunai-connect-freecad

CLI harness for **FreeCAD** parametric 3D CAD modeler. Create, modify, and export
3D models from the command line or via AI agents — no GUI needed.

## Prerequisites

**FreeCAD** must be installed on your system. The CLI generates FreeCAD Python
macros and executes them headlessly via `freecadcmd`.

- **Windows**: Download from [freecad.org](https://www.freecad.org/downloads.php)
- **Linux**: `sudo apt install freecad` or `snap install freecad`
- **macOS**: `brew install --cask freecad`

Verify installation:
```bash
freecadcmd --version
```

## Installation

```bash
cd freecad/agent-harness
pip install -e .
```

Verify:
```bash
tarunai-connect-freecad --help
```

## Quick Start

### One-shot commands
```bash
# Create a new document
tarunai-connect-freecad document new --name "MyPart" -o project.json

# Add a box
tarunai-connect-freecad -p project.json part add box --name "Base" -P length=20 -P width=15 -P height=5

# Add a cylinder
tarunai-connect-freecad -p project.json part add cylinder --name "Hole" -P radius=3 -P height=10 --position 10,7.5,0

# Boolean cut (subtract cylinder from box)
tarunai-connect-freecad -p project.json part boolean cut 0 1 --name "BaseWithHole"

# Export to STEP
tarunai-connect-freecad -p project.json export render output.step --preset step
```

### Interactive REPL
```bash
tarunai-connect-freecad
# or with a project:
tarunai-connect-freecad -p project.json
```

### JSON output for agents
```bash
tarunai-connect-freecad --json document new --name "AgentProject" -o project.json
tarunai-connect-freecad --json -p project.json part add box
tarunai-connect-freecad --json -p project.json export render output.step
```

## Preview and Motion

FreeCAD supports both truthful preview bundles and final motion rendering.

```bash
# Capture a real 4-view preview bundle
tarunai-connect-freecad --json -p project.json preview capture --recipe quick

# Start poll-mode live preview
tarunai-connect-freecad --json -p project.json preview live start --recipe quick --mode poll --source-poll-ms 500

# Query current live status without rendering
tarunai-connect-freecad --json -p project.json preview live status --recipe quick

# Render a final motion sequence
tarunai-connect-freecad --json -p project.json motion render-video spin output.mp4
```

The preview side publishes `session.json`, immutable bundle dirs, and
`trajectory.json`. The default bundle includes `hero.png`, `front.png`,
`top.png`, and `right.png`.

Inspect/open the published previews with:

```bash
cli-hub previews inspect /path/to/bundle-or-session
cli-hub previews html /path/to/bundle-or-session -o page.html
cli-hub previews watch /path/to/session --open
cli-hub previews open /path/to/bundle-or-session
```

## Command Groups

| Group | Description |
|-------|-------------|
| `document` | Create, open, save, inspect documents |
| `part` | Add/remove 3D primitives, transform, boolean ops |
| `sketch` | Create 2D sketches with lines, circles, arcs, constraints |
| `body` | PartDesign bodies — pad, pocket, fillet, chamfer, revolution |
| `material` | Create and assign PBR materials |
| `export` | Export to STEP, IGES, STL, OBJ, BREP, FCStd |
| `session` | Undo/redo, status, history |

## Supported Primitives

Box, Cylinder, Sphere, Cone, Torus, Wedge

## Supported Export Formats

| Preset | Format | Description |
|--------|--------|-------------|
| `step` | .step | STEP AP214 (ISO 10303) — standard CAD exchange |
| `iges` | .iges | IGES format |
| `stl` | .stl | STL mesh (3D printing) |
| `stl_fine` | .stl | Fine-mesh STL |
| `obj` | .obj | Wavefront OBJ |
| `brep` | .brep | OpenCASCADE BREP |
| `fcstd` | .FCStd | Native FreeCAD document |

## Running Tests

```bash
cd freecad/agent-harness
python -m pytest tarunai_connect/freecad/tests/ -v -s
```

Force installed command testing:
```bash
TARUNAI_CONNECT_FORCE_INSTALLED=1 python -m pytest tarunai_connect/freecad/tests/ -v -s
```
