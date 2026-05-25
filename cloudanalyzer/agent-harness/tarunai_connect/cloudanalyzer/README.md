# tarunai-connect-cloudanalyzer

Agent-friendly CLI harness for [CloudAnalyzer](https://github.com/rsasaki0109/CloudAnalyzer) — a QA platform for mapping, localization, and perception point cloud outputs.

## Quick Start

```bash
pip install tarunai-connect-cloudanalyzer

# Evaluate a point cloud
tarunai-connect-cloudanalyzer --json evaluate run output.pcd reference.pcd

# Run config-driven QA
tarunai-connect-cloudanalyzer --json check run cloudanalyzer.yaml

# Trajectory evaluation with quality gate
tarunai-connect-cloudanalyzer --json trajectory evaluate est.csv gt.csv --max-ate 0.5

# Ground segmentation QA
tarunai-connect-cloudanalyzer --json evaluate ground est_g.pcd est_ng.pcd ref_g.pcd ref_ng.pcd --min-f1 0.9

# Baseline management
tarunai-connect-cloudanalyzer baseline save qa/summary.json --history-dir qa/history/
tarunai-connect-cloudanalyzer --json baseline decision qa/summary.json --history-dir qa/history/

# Interactive REPL
tarunai-connect-cloudanalyzer
```

## Why a Harness?

CloudAnalyzer is already CLI-first, but this harness adds:

- **Structured `--json` output** on every command for agent consumption
- **REPL mode** for interactive exploration
- **Project/session management** with operation history and undo
- **SKILL.md** for agent auto-discovery via tarunAI Connect ecosystem
- **Unified Click interface** grouping 27 commands into logical groups

## Commands

See [SKILL.md](tarunai_connect/cloudanalyzer/skills/SKILL.md) for the full command reference.

| Group | Commands | Description |
|---|---:|---|
| evaluate | 6 | Point cloud evaluation (Chamfer, F1, AUC, ground segmentation) |
| trajectory | 3 | Trajectory QA (ATE, RPE, drift, lateral, longitudinal) |
| check | 2 | Config-driven quality gates |
| baseline | 3 | Baseline evolution (promote/keep/reject) |
| process | 6 | Downsample, split, filter, merge, convert |
| inspect | 3 | Visualization and browser inspection |
| info | 2 | Metadata and version |
| session | 2 | Project and session management |

## Requirements

- Python 3.10+
- CloudAnalyzer (`pip install cloudanalyzer`)
