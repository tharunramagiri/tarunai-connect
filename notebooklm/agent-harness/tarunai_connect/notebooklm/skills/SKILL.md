---
name: tarunai-connect-notebooklm
description: Experimental NotebookLM harness for listing notebooks, managing sources, asking questions, generating artifacts, and downloading outputs through an installed notebooklm CLI.
---

# tarunai-connect-notebooklm

Experimental NotebookLM harness for tarunAI Connect.

## Installation

This package is intended to be installed from the harness directory:

```bash
cd notebooklm/agent-harness
python3 -m pip install -e .
```

Install the upstream NotebookLM CLI if needed:

```bash
python3 -m pip install --user 'notebooklm-py[browser]'
python3 -m playwright install chromium
```

## Requirements

- `notebooklm` command installed locally
- Valid local NotebookLM login session

## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-notebooklm --help

# Start with a notebook context
tarunai-connect-notebooklm --notebook nb_123 source list

# Prefer JSON for agent use
tarunai-connect-notebooklm --json notebook list
```

## Command Groups

| Group | Purpose |
| --- | --- |
| `auth` | login and auth validation |
| `notebook` | notebook list, create, summary |
| `source` | source listing and URL add |
| `chat` | ask questions and inspect history |
| `artifact` | list and generate artifacts |
| `download` | fetch generated outputs |
| `share` | inspect sharing state |

## Agent Workflow

1. Check auth with `tarunai-connect-notebooklm auth status`
2. Discover notebook IDs with `tarunai-connect-notebooklm --json notebook list`
3. Use explicit `--notebook` for follow-up commands
4. Prefer `--json` only where the upstream `notebooklm` command supports it

## Agent Guidance

- Prefer explicit notebook IDs with `--notebook`.
- Use `--json` for machine-readable output only on commands that support it upstream.
- Treat this harness as experimental and unofficial.
- Do not expose auth files or cookies in logs.
- NotebookLM is a Google product; this harness is unofficial and not affiliated with Google.

## References

- tarunAI Connect: https://github.com/tharunramagiri/tarunai-connect
- tarunAI Connect HARNESS.md: https://github.com/tharunramagiri/tarunai-connect/blob/main/tarunai-connect-plugin/HARNESS.md
- notebooklm-py: https://github.com/teng-lin/notebooklm-py
- Google NotebookLM help: https://support.google.com/notebooklm/answer/16206563
