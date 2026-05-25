# tarunai-connect-adguardhome

CLI harness for AdGuardHome - control your ad blocker from the command line or via agents.

## Prerequisites

AdGuardHome must be running. Install:

```bash
# Linux - native
curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v

# Docker
docker run --name adguardhome -p 3000:3000 adguard/adguardhome
```

## Installation

```bash
cd agent-harness
pip install -e .
tarunai-connect-adguardhome --help
```

## Configuration

```bash
export AGH_HOST=localhost
export AGH_PORT=3000
export AGH_USERNAME=admin
export AGH_PASSWORD=secret

# Or save to config file
tarunai-connect-adguardhome --host localhost --port 3000 --username admin --password secret config save
```

## Usage

```bash
# Interactive REPL (default)
tarunai-connect-adguardhome

# One-shot commands
tarunai-connect-adguardhome server status
tarunai-connect-adguardhome filter list
tarunai-connect-adguardhome --json stats show

# Filtering
tarunai-connect-adguardhome filter add --url https://somehost.com/list.txt --name "My List"
tarunai-connect-adguardhome filter refresh

# DNS rewrites
tarunai-connect-adguardhome rewrite add --domain "myserver.local" --answer "192.168.1.50"
tarunai-connect-adguardhome rewrite list

# Clients
tarunai-connect-adguardhome clients add --name "My PC" --ip 192.168.1.100

# Stats
tarunai-connect-adguardhome stats show
tarunai-connect-adguardhome stats reset
```

## Tests

```bash
cd agent-harness
python3 -m pytest tarunai_connect/adguardhome/tests/test_core.py -v
python3 -m pytest tarunai_connect/adguardhome/tests/test_full_e2e.py -v -s
TARUNAI_CONNECT_FORCE_INSTALLED=1 python3 -m pytest tarunai_connect/adguardhome/tests/ -v -s
```
