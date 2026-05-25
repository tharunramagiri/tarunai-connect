---
name: "tarunai-connect-firefly-iii"
description: "Firefly III CLI - Personal finance management via tarunAI Connect"
version: "1.0.0"
author: "tarunAI Connect Community"
---

# Firefly III CLI

Firefly III command-line interface based on tarunAI Connect specification. Converts MCP mode to stateless CLI mode to avoid Node residual process issues.

## Installation

```bash
pip install tarunai-connect-firefly-iii
```

## Prerequisites

- Python 3.10+
- Running Firefly III instance
- Personal Access Token (PAT)

## Configuration

### Environment Variables (Recommended)

```bash
export FIREFLY_III_BASE_URL="https://firefly.yourdomain.com"
export FIREFLY_III_PAT="your-personal-access-token"
```

### Command Line Arguments

```bash
tarunai-connect-firefly-iii --base-url https://firefly.yourdomain.com --pat your-token
```

## Command Groups

| Command Group | Description | Corresponding API |
|--------------|-------------|-------------------|
| `accounts` | Account management | `/api/v1/accounts` |
| `transactions` | Transaction management | `/api/v1/transactions` |
| `budgets` | Budget management | `/api/v1/budgets` |
| `categories` | Category management | `/api/v1/categories` |
| `tags` | Tag management | `/api/v1/tags` |
| `bills` | Bill management | `/api/v1/bills` |
| `piggy-banks` | Piggy banks | `/api/v1/piggy-banks` |
| `insights` | Insights and reports | `/api/v1/insight/*` |
| `search` | Search | `/api/v1/search/*` |
| `export` | Data export | `/api/v1/data/export/*` |
| `info` | System information | `/api/v1/about` |

## Usage Examples

### Account Management

```bash
# List all accounts
tarunai-connect-firefly-iii --json accounts list

# List asset accounts
tarunai-connect-firefly-iii --json accounts list --type asset

# Get account details
tarunai-connect-firefly-iii --json accounts get --id 123

# Create account
tarunai-connect-firefly-iii --json accounts create --name "Cash" --type asset --currency-code USD

# Delete account
tarunai-connect-firefly-iii accounts delete --id 123
```

### Transaction Management

```bash
# List transactions
tarunai-connect-firefly-iii --json transactions list --limit 10

# Create transaction
tarunai-connect-firefly-iii --json transactions create \
  --description "Grocery" \
  --amount 50.00 \
  --source-account 1 \
  --category "Food"

# Get transaction details
tarunai-connect-firefly-iii --json transactions get --id 456

# Delete transaction
tarunai-connect-firefly-iii transactions delete --id 456
```

### Insights and Reports

```bash
# Expense report (by category)
tarunai-connect-firefly-iii --json insights expense \
  --start 2024-01-01 \
  --end 2024-01-31 \
  --group-by category

# Income report
tarunai-connect-firefly-iii --json insights income \
  --start 2024-01-01 \
  --end 2024-01-31

# Account overview
tarunai-connect-firefly-iii --json insights overview \
  --start 2024-01-01 \
  --end 2024-01-31
```

### Search

```bash
# Search transactions
tarunai-connect-firefly-iii --json search transactions --query "grocery"
```

### Data Export

```bash
# Export transactions
tarunai-connect-firefly-iii --json export transactions \
  --start 2024-01-01 \
  --end 2024-01-31

# Export accounts
tarunai-connect-firefly-iii --json export accounts
```

### System Information

```bash
# System information
tarunai-connect-firefly-iii --json info about

# Connection status
tarunai-connect-firefly-iii info status
```

## Preset Filtering

Use `--preset` parameter to filter available commands:

```bash
# Default preset
tarunai-connect-firefly-iii --preset default accounts list

# Full preset
tarunai-connect-firefly-iii --preset full accounts list

# Budget preset
tarunai-connect-firefly-iii --preset budget budgets list

# Reporting preset
tarunai-connect-firefly-iii --preset reporting insights expense --start 2024-01-01 --end 2024-01-31
```

Available presets:
- `default`: Core features (accounts, transactions, categories, tags, bills, search)
- `full`: All features
- `basic`: Basic features (accounts, transactions, categories, tags, search)
- `budget`: Budget-related (accounts, budgets, transactions, summary, insight)
- `reporting`: Reporting-related (accounts, transactions, categories, insight, summary, search)
- `admin`: Admin features (about, configuration, currencies, users, preferences)
- `automation`: Automation (rules, recurrences, webhooks, transactions)

## Agent Guidelines

### Basic Usage

1. **Use `--json` for structured output**: All commands support `--json` flag, returning JSON format data
2. **Call `info status` first to check connection**: Confirm Firefly III connection is normal before executing operations
3. **Use presets to reduce command count**: Filter unnecessary commands via `--preset`

### Common Workflows

#### View Account Balances

```bash
# 1. Check connection
tarunai-connect-firefly-iii info status

# 2. List asset accounts
tarunai-connect-firefly-iii --json accounts list --type asset

# 3. View account details (get balance)
tarunai-connect-firefly-iii --json accounts get --id <account_id>
```

#### Record Expense

```bash
# 1. Find expense accounts
tarunai-connect-firefly-iii --json accounts list --type expense

# 2. Create transaction
tarunai-connect-firefly-iii --json transactions create \
  --description "Lunch" \
  --amount 15.50 \
  --source-account <asset_account_id> \
  --destination-account <expense_account_id> \
  --category "Food"
```

#### Monthly Report

```bash
# 1. Expense report
tarunai-connect-firefly-iii --json insights expense \
  --start 2024-01-01 \
  --end 2024-01-31 \
  --group-by category

# 2. Income report
tarunai-connect-firefly-iii --json insights income \
  --start 2024-01-01 \
  --end 2024-01-31

# 3. Export data
tarunai-connect-firefly-iii --json export transactions \
  --start 2024-01-01 \
  --end 2024-01-31
```

### Error Handling

Common errors and solutions:

1. **Connection failed**: Check if FIREFLY_III_BASE_URL is correct
2. **Authentication failed**: Check if FIREFLY_III_PAT is valid
3. **Resource not found**: Check if ID is correct
4. **Parameter error**: Check if required parameters are provided

### Best Practices

1. **Use environment variables for credentials**: Avoid exposing PAT in command line
2. **Use `--json` for scripting**: Facilitates parsing and processing output
3. **Use presets to control permissions**: Choose appropriate preset based on scenario
4. **Query before modifying**: Avoid accidental operations

## Troubleshooting

### Connection Issues

```
Error: Cannot connect to Firefly III instance
```

- Check if Firefly III instance is running
- Check network connection
- Check if base URL is correct

### Authentication Issues

```
Error: Authentication failed: Personal Access Token is invalid
```

- Check if PAT is correct
- Generate new PAT in Firefly III Options > Profile > OAuth
- Ensure PAT has not expired

## Comparison with MCP Version

| Feature | MCP Version | tarunAI Connect Version |
|---------|------------|---------------------|
| Process Lifecycle | Long-running | Single call, immediate exit |
| Memory Usage | Continuous | On-demand, released after |
| Communication | Stdio/SSE | Command args + stdout |
| State Management | Stateful | Stateless |
| Preset Filtering | Supported | Supported |
| JSON Output | Built-in | `--json` flag |

## License

MIT License
