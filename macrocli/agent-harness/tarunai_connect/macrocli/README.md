# MacroCLI

**MacroCLI** is a layered CLI that converts GUI workflows into
parameterized, agent-callable macros. Agents call `macro run <name>` through
a stable CLI; the system routes execution to the right backend (native plugin,
file transform, semantic UI, or compiled GUI replay) — invisible to the agent.

## Installation

```bash
pip install -e .
```

**Dependencies:** Python 3.10+, PyYAML, click, prompt-toolkit

**Optional extras:**

```bash
pip install -e ".[visual]"      # visual_anchor backend (mss, Pillow, numpy, pynput)
pip install -e ".[gui_agent]"   # gui_agent backend     (openai, mss, Pillow)
pip install -e ".[all]"         # everything
```

The `gui_agent` backend uses the OpenAI SDK and is compatible with any
OpenAI-compatible API. Configure via environment variables:

| Variable           | Description                                 |
|--------------------|---------------------------------------------|
| `MACROCLI_MODEL`   | Model name (required, e.g. `gpt-4o`)        |
| `MACROCLI_API_KEY` | API key for the provider                    |
| `MACROCLI_BASE_URL`| Base URL (only needed for non-OpenAI hosts) |

## Usage

```bash
# List available macros
tarunai-connect-macrocli macro list --json

# Inspect a macro
tarunai-connect-macrocli macro info export_file --json

# Execute a macro
tarunai-connect-macrocli macro run transform_json \
    --param file=/tmp/config.json \
    --param key=theme --param value=dark --json

# Dry run
tarunai-connect-macrocli --dry-run macro run export_file \
    --param output=/tmp/out.txt --json

# Interactive REPL
tarunai-connect-macrocli
```

## Run Tests

```bash
cd macrocli/agent-harness
pip install -e ".[dev]"
python -m pytest tarunai_connect/macrocli/tests/ -v -s
```

## Architecture

```
tarunai-connect-macrocli (CLI)
  └─▶ macro run <name> --param key=value
         │
    MacroRuntime
         │  validate params
         │  check preconditions
         │  for each step:
         │    RoutingEngine → select backend
         │    Backend.execute(step, params)
         │  check postconditions
         └─▶ ExecutionResult { success, output, telemetry }
```

**Backends:**
- `native_api` — subprocess / shell commands
- `file_transform` — XML, JSON, text file editing
- `semantic_ui` — accessibility controls + keyboard shortcuts
- `visual_anchor` — template-matching click/type (requires `[visual]`)
- `gui_agent` — vision-model-driven automation (requires `[gui_agent]`)
- `gui_macro` — precompiled coordinate-based replay
- `recovery` — retry + fallback orchestration

## Adding a Macro

1. Create `tarunai_connect/macrocli/macro_definitions/my_macro.yaml`
2. Add it to `macro_definitions/manifest.yaml`
3. Verify: `tarunai-connect-macrocli macro validate my_macro --json`

See `skills/SKILL.md` (installed with the package) for full macro YAML schema.
