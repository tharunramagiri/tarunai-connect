# tarunai-connect-eth2-quickstart

CLI harness for `eth2-quickstart` so agents can deploy and operate hardened Ethereum nodes
through a consistent command surface with JSON output.

## Prerequisites

- Python 3.10+
- A local checkout of `https://github.com/chimera-defi/eth2-quickstart`
- Ubuntu host for real installation workflows

## Installation

```bash
cd eth2-quickstart/agent-harness
pip install -e .
tarunai-connect-eth2-quickstart --help
```

## Repo Discovery

The harness needs to know which `eth2-quickstart` checkout to operate on. It resolves the repo in
this order:

1. `--repo-root`
2. `ETH2QS_REPO_ROOT`
3. current working directory or one of its parents

```bash
export ETH2QS_REPO_ROOT=/srv/eth2-quickstart
tarunai-connect-eth2-quickstart --json health-check
```

## Usage

```bash
# Interactive REPL
tarunai-connect-eth2-quickstart

# Inspect machine-readable health
tarunai-connect-eth2-quickstart --json health-check

# Install phase 2 clients
tarunai-connect-eth2-quickstart --json install-clients \
  --network mainnet \
  --execution-client geth \
  --consensus-client lighthouse \
  --mev mev-boost \
  --confirm

# Configure validator metadata without touching secrets
tarunai-connect-eth2-quickstart --json configure-validator \
  --consensus-client lighthouse \
  --fee-recipient 0x1111111111111111111111111111111111111111 \
  --graffiti "tarunAI Connect"

# Install and start nginx-backed RPC exposure
tarunai-connect-eth2-quickstart --json start-rpc \
  --web-stack nginx \
  --server-name rpc.example.org \
  --confirm
```

## Commands

- `setup-node`
- `install-clients`
- `start-rpc`
- `configure-validator`
- `status`
- `health-check`

All commands support `--json`.

## Tests

```bash
cd eth2-quickstart/agent-harness
python3 -m pytest tarunai_connect/eth2_quickstart/tests/test_core.py -v
python3 -m pytest tarunai_connect/eth2_quickstart/tests/test_full_e2e.py -v
```
