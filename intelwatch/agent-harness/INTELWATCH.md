# Intelwatch CLI Harness

This harness integrates the Node.js `intelwatch` CLI tool with the tarunAI Connect framework. 
Because `intelwatch` is an `npx` (Node.js) tool, this harness acts as a thin wrapper that relays command-line arguments to `npx intelwatch`.

## Architecture
- **Language**: Python (`tarunai-connect-intelwatch`) wrapping Node.js (`npx intelwatch`).
- **Dependencies**: Requires `click` (Python) and `node`/`npx` (System).

## Setup
Install the python harness:
```bash
pip install -e .
```

Run:
```bash
tarunai-connect-intelwatch profile kpmg.fr --ai
```
