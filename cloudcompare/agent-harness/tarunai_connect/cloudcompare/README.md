# tarunai-connect-cloudcompare

Agent-friendly command-line harness for [CloudCompare](https://cloudcompare.org) —
the open-source 3D point cloud and mesh processing software.

## Prerequisites

### 1. Install CloudCompare (required)

```bash
# Linux — Flatpak (recommended)
flatpak install flathub org.cloudcompare.CloudCompare

# Linux — apt
sudo apt install cloudcompare

# macOS
brew install --cask cloudcompare

# Windows
# https://cloudcompare.org/release/index.html
```

### 2. Install the CLI harness

```bash
cd cloudcompare/agent-harness
pip install -e .
```

Verify:
```bash
tarunai-connect-cloudcompare --help
tarunai-connect-cloudcompare info
```

## Quick Start

```bash
# Create a project
tarunai-connect-cloudcompare project new -o survey.json

# Add a point cloud
tarunai-connect-cloudcompare --project survey.json cloud add scan.las

# Subsample (spatial, 5cm minimum distance)
tarunai-connect-cloudcompare --project survey.json cloud subsample 0 \
    -o scan_thin.las --method SPATIAL --param 0.05

# Statistical outlier removal
tarunai-connect-cloudcompare --project survey.json cloud filter-sor 0 \
    -o scan_clean.las --nb-points 6 --std-ratio 1.0

# Cloud-to-cloud distance
tarunai-connect-cloudcompare --project survey.json distance c2c \
    --compare 1 --reference 0 -o distances.las

# Export to PLY
tarunai-connect-cloudcompare --project survey.json export cloud 0 output.ply

# JSON output for agents
tarunai-connect-cloudcompare --json --project survey.json project info
```

## Interactive REPL

```bash
tarunai-connect-cloudcompare
# or with a project:
tarunai-connect-cloudcompare --project survey.json
```

## Command Groups

| Group | Purpose |
|-------|---------|
| `project` | Create, open, inspect projects |
| `cloud` | Load and process point clouds |
| `mesh` | Load and manage meshes |
| `distance` | C2C and C2M distance computation |
| `transform` | ICP registration |
| `export` | Export clouds/meshes to various formats |
| `session` | Save, history, undo, settings |
| `info` | Show CloudCompare installation info |

## Running Tests

```bash
cd cloudcompare/agent-harness

# Unit tests only (no CloudCompare required):
python3 -m pytest tarunai_connect/cloudcompare/tests/test_core.py -v

# Full E2E tests (CloudCompare required):
python3 -m pytest tarunai_connect/cloudcompare/tests/ -v -s

# Test with installed command:
TARUNAI_CONNECT_FORCE_INSTALLED=1 python3 -m pytest tarunai_connect/cloudcompare/tests/ -v -s
```

## Supported Formats

**Clouds:** .las, .laz, .ply, .pcd, .xyz, .txt, .asc, .csv, .e57, .bin
**Meshes:** .obj, .stl, .ply, .bin

## Agent Usage

Use `--json` for all programmatic interactions:

```bash
# Returns structured JSON
tarunai-connect-cloudcompare --json project info --project my.json

# Check output file was created
result=$(tarunai-connect-cloudcompare --json cloud subsample 0 -o out.las --project p.json)
echo $result | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['exists'])"
```
