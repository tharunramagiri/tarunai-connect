---
name: "tarunai-connect-firefly-iii"
description: "Firefly III CLI - Personal finance management via tarunAI Connect"
version: "2.0.0"
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
| `accounts` | Account management (CRUD) | `/api/v1/accounts` |
| `transactions` | Transaction management (CRUD) | `/api/v1/transactions` |
| `budgets` | Budget management (CRUD + limits) | `/api/v1/budgets` |
| `categories` | Category management (CRUD) | `/api/v1/categories` |
| `tags` | Tag management (CRUD) | `/api/v1/tags` |
| `bills` | Bill management (CRUD) | `/api/v1/bills` |
| `piggy-banks` | Piggy bank management (CRUD + events) | `/api/v1/piggy-banks` |
| `autocomplete` | Autocomplete for various entities | `/api/v1/autocomplete/*` |
| `currencies` | Currency management (CRUD) | `/api/v1/currencies` |
| `recurrences` | Recurring transaction management (CRUD) | `/api/v1/recurrences` |
| `rules` | Rule management (CRUD + test/execute) | `/api/v1/rules` |
| `rule-groups` | Rule group management (CRUD + execute) | `/api/v1/rule-groups` |
| `summary` | Financial summaries | `/api/v1/summary/*` |
| `webhooks` | Webhook management (CRUD + trigger) | `/api/v1/webhooks` |
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

# Update account
tarunai-connect-firefly-iii --json accounts update --id 123 --name "New Name"

# Delete account
tarunai-connect-firefly-iii accounts delete --id 123
```

### Transaction Management

```bash
# List transactions
tarunai-connect-firefly-iii --json transactions list --limit 10

# List transactions with date range
tarunai-connect-firefly-iii --json transactions list --start 2024-01-01 --end 2024-01-31

# Create transaction
tarunai-connect-firefly-iii --json transactions create \
  --description "Grocery" \
  --amount 50.00 \
  --source-account 1 \
  --category "Food"

# Update transaction
tarunai-connect-firefly-iii --json transactions update --id 456 --description "Updated"

# Delete transaction
tarunai-connect-firefly-iii transactions delete --id 456
```

### Budget Management

```bash
# List budgets
tarunai-connect-firefly-iii --json budgets list

# Get budget details
tarunai-connect-firefly-iii --json budgets get --id 1

# Create budget
tarunai-connect-firefly-iii --json budgets create --name "Monthly Budget"

# Update budget
tarunai-connect-firefly-iii --json budgets update --id 1 --name "New Budget Name"

# Delete budget
tarunai-connect-firefly-iii budgets delete --id 1

# List budget limits
tarunai-connect-firefly-iii --json budgets limits --budget-id 1

# Create budget limit
tarunai-connect-firefly-iii --json budgets limit-create --budget-id 1 --amount 1000 --start 2024-01-01 --end 2024-01-31

# Update budget limit
tarunai-connect-firefly-iii --json budgets limit-update --id 1 --amount 1500

# Delete budget limit
tarunai-connect-firefly-iii budgets limit-delete --id 1
```

### Category Management

```bash
# List categories
tarunai-connect-firefly-iii --json categories list

# Get category
tarunai-connect-firefly-iii --json categories get --id 1

# Create category
tarunai-connect-firefly-iii --json categories create --name "Food"

# Update category
tarunai-connect-firefly-iii --json categories update --id 1 --name "Food & Dining"

# Delete category
tarunai-connect-firefly-iii categories delete --id 1
```

### Tag Management

```bash
# List tags
tarunai-connect-firefly-iii --json tags list

# Get tag
tarunai-connect-firefly-iii --json tags get --id "uuid-here"

# Create tag
tarunai-connect-firefly-iii --json tags create --tag "important"

# Update tag
tarunai-connect-firefly-iii --json tags update --id "uuid-here" --tag "important-updated"

# Delete tag
tarunai-connect-firefly-iii tags delete --id "uuid-here"
```

### Bill Management

```bash
# List bills
tarunai-connect-firefly-iii --json bills list

# Get bill
tarunai-connect-firefly-iii --json bills get --id 1

# Create bill
tarunai-connect-firefly-iii --json bills create \
  --name "Netflix" \
  --amount-min 15.99 \
  --amount-max 15.99 \
  --frequency monthly

# Update bill
tarunai-connect-firefly-iii --json bills update --id 1 --amount-min 19.99

# Delete bill
tarunai-connect-firefly-iii bills delete --id 1
```

### Piggy Bank Management

```bash
# List piggy banks
tarunai-connect-firefly-iii --json piggy-banks list

# Get piggy bank
tarunai-connect-firefly-iii --json piggy-banks get --id 1

# Create piggy bank
tarunai-connect-firefly-iii --json piggy-banks create \
  --name "Vacation Fund" \
  --account-id 1 \
  --target-amount 5000

# Update piggy bank
tarunai-connect-firefly-iii --json piggy-banks update --id 1 --name "New Name"

# Delete piggy bank
tarunai-connect-firefly-iii piggy-banks delete --id 1

# List piggy bank events
tarunai-connect-firefly-iii --json piggy-banks events --id 1

# Add money to piggy bank
tarunai-connect-firefly-iii --json piggy-banks add-money --id 1 --amount 100
```

### Autocomplete

```bash
# Autocomplete accounts
tarunai-connect-firefly-iii --json autocomplete accounts --query "bank"

# Autocomplete categories
tarunai-connect-firefly-iii --json autocomplete categories --query "food"

# Autocomplete tags
tarunai-connect-firefly-iii --json autocomplete tags --query "important"

# Autocomplete transactions
tarunai-connect-firefly-iii --json autocomplete transactions --query "grocery"

# Autocomplete budgets
tarunai-connect-firefly-iii --json autocomplete budgets --query "monthly"

# Autocomplete bills
tarunai-connect-firefly-iii --json autocomplete bills --query "netflix"

# Autocomplete piggy banks
tarunai-connect-firefly-iii --json autocomplete piggy-banks --query "vacation"

# Autocomplete currencies
tarunai-connect-firefly-iii --json autocomplete currencies --query "dollar"

# Autocomplete rules
tarunai-connect-firefly-iii --json autocomplete rules --query "auto"

# Autocomplete rule groups
tarunai-connect-firefly-iii --json autocomplete rule-groups --query "finances"

# Autocomplete recurring
tarunai-connect-firefly-iii --json autocomplete recurring --query "rent"

# Autocomplete object groups
tarunai-connect-firefly-iii --json autocomplete object-groups --query "group"

# Autocomplete transaction types
tarunai-connect-firefly-iii --json autocomplete transaction-types --query "with"
```

### Currency Management

```bash
# List currencies
tarunai-connect-firefly-iii --json currencies list

# Get currency
tarunai-connect-firefly-iii --json currencies get --id 1

# Create currency
tarunai-connect-firefly-iii --json currencies create \
  --code "CNY" \
  --name "Chinese Yuan" \
  --symbol "¥"

# Update currency
tarunai-connect-firefly-iii --json currencies update --id 1 --symbol "元"

# Delete currency
tarunai-connect-firefly-iii currencies delete --id 1

# Get exchange rates
tarunai-connect-firefly-iii --json currencies exchange-rates --from USD --to EUR
```

### Recurring Transaction Management

```bash
# List recurring transactions
tarunai-connect-firefly-iii --json recurrences list

# Get recurring transaction
tarunai-connect-firefly-iii --json recurrences get --id 1

# Create recurring transaction
tarunai-connect-firefly-iii --json recurrences create \
  --title "Rent Payment" \
  --type withdrawal \
  --amount 1500 \
  --source-account 1 \
  --destination-account 2 \
  --frequency monthly

# Update recurring transaction
tarunai-connect-firefly-iii --json recurrences update --id 1 --amount 1600

# Delete recurring transaction
tarunai-connect-firefly-iii recurrences delete --id 1
```

### Rule Management

```bash
# List rules
tarunai-connect-firefly-iii --json rules list

# Get rule
tarunai-connect-firefly-iii --json rules get --id 1

# Create rule
tarunai-connect-firefly-iii --json rules create \
  --title "Auto-tag groceries" \
  --trigger "description_contains" \
  --value "grocery" \
  --action set_category \
  --action-value "Food"

# Update rule
tarunai-connect-firefly-iii --json rules update --id 1 --title "New Title"

# Delete rule
tarunai-connect-firefly-iii rules delete --id 1

# Test rule
tarunai-connect-firefly-iii --json rules test --id 1

# Execute rule
tarunai-connect-firefly-iii --json rules execute --id 1
```

### Rule Group Management

```bash
# List rule groups
tarunai-connect-firefly-iii --json rule-groups list

# Get rule group
tarunai-connect-firefly-iii --json rule-groups get --id 1

# Create rule group
tarunai-connect-firefly-iii --json rule-groups create --title "Finance Rules"

# Update rule group
tarunai-connect-firefly-iii --json rule-groups update --id 1 --title "New Title"

# Delete rule group
tarunai-connect-firefly-iii rule-groups delete --id 1

# Execute rule group
tarunai-connect-firefly-iii --json rule-groups execute --id 1
```

### Summary Reports

```bash
# Default summary set
tarunai-connect-firefly-iii --json summary default-set --start 2024-01-01 --end 2024-01-31

# Account summary
tarunai-connect-firefly-iii --json summary account-summary --start 2024-01-01 --end 2024-01-31

# Available budget summary
tarunai-connect-firefly-iii --json summary available-budget --start 2024-01-01 --end 2024-01-31

# Bill summary
tarunai-connect-firefly-iii --json summary bill-summary --start 2024-01-01 --end 2024-01-31

# Budget summary
tarunai-connect-firefly-iii --json summary budget-summary --start 2024-01-01 --end 2024-01-31

# Category summary
tarunai-connect-firefly-iii --json summary category-summary --start 2024-01-01 --end 2024-01-31

# Tag summary
tarunai-connect-firefly-iii --json summary tag-summary --start 2024-01-01 --end 2024-01-31

# Transfer summary
tarunai-connect-firefly-iii --json summary transfer-summary --start 2024-01-01 --end 2024-01-31
```

### Webhook Management

```bash
# List webhooks
tarunai-connect-firefly-iii --json webhooks list

# Get webhook
tarunai-connect-firefly-iii --json webhooks get --id 1

# Create webhook
tarunai-connect-firefly-iii --json webhooks create \
  --title "My Webhook" \
  --trigger create \
  --url "https://example.com/webhook" \
  --secret "my-secret"

# Update webhook
tarunai-connect-firefly-iii --json webhooks update --id 1 --title "New Title"

# Delete webhook
tarunai-connect-firefly-iii webhooks delete --id 1

# Trigger webhook manually
tarunai-connect-firefly-iii --json webhooks trigger --id 1
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

# Transfer insights
tarunai-connect-firefly-iii --json insights transfer \
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

# Export budgets
tarunai-connect-firefly-iii --json export budgets

# Export categories
tarunai-connect-firefly-iii --json export categories
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

#### Set Up Recurring Budget

```bash
# 1. Create budget
tarunai-connect-firefly-iii --json budgets create --name "Monthly Groceries"

# 2. Set budget limit
tarunai-connect-firefly-iii --json budgets limit-create \
  --budget-id <budget_id> \
  --amount 500 \
  --start 2024-01-01 \
  --end 2024-01-31
```

#### Create Automation Rule

```bash
# 1. List rule groups
tarunai-connect-firefly-iii --json rule-groups list

# 2. Create rule
tarunai-connect-firefly-iii --json rules create \
  --title "Auto-tag groceries" \
  --trigger description_contains \
  --value "grocery" \
  --action set_category \
  --action-value "Food"

# 3. Execute rule to apply to existing transactions
tarunai-connect-firefly-iii --json rules execute --id <rule_id>
```

#### Monthly Financial Report

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

# 3. Budget summary
tarunai-connect-firefly-iii --json summary budget-summary \
  --start 2024-01-01 \
  --end 2024-01-31

# 4. Export data
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
5. **Validation error**: Check API documentation for valid parameter values

### Best Practices

1. **Use environment variables for credentials**: Avoid exposing PAT in command line
2. **Use `--json` for scripting**: Facilitates parsing and processing output
3. **Use presets to control permissions**: Choose appropriate preset based on scenario
4. **Query before modifying**: Avoid accidental operations
5. **Use autocomplete for quick lookups**: Great for finding existing entities

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

### Parameter Validation Errors

```
Error: Request parameter error: [details]
```

- Check required parameters are provided
- Verify date formats (YYYY-MM-DD)
- Verify currency codes (ISO 4217)
- Verify enum values match allowed choices

## Comparison with MCP Version

| Feature | MCP Version | tarunAI Connect Version |
|---------|------------|---------------------|
| Process Lifecycle | Long-running | Single call, immediate exit |
| Memory Usage | Continuous | On-demand, released after |
| Communication | Stdio/SSE | Command args + stdout |
| State Management | Stateful | Stateless |
| Preset Filtering | Supported | Supported |
| JSON Output | Built-in | `--json` flag |
| Full API Coverage | Partial | Full API coverage |

## API Coverage

This CLI covers the following Firefly III API endpoints:

- [x] `/api/v1/about` - System information
- [x] `/api/v1/accounts` - Account management (full CRUD)
- [x] `/api/v1/transactions` - Transaction management (full CRUD)
- [x] `/api/v1/budgets` - Budget management (full CRUD + limits)
- [x] `/api/v1/categories` - Category management (full CRUD)
- [x] `/api/v1/tags` - Tag management (full CRUD)
- [x] `/api/v1/bills` - Bill management (full CRUD)
- [x] `/api/v1/piggy-banks` - Piggy bank management (full CRUD + events)
- [x] `/api/v1/autocomplete/*` - All autocomplete endpoints
- [x] `/api/v1/currencies` - Currency management (full CRUD)
- [x] `/api/v1/recurrences` - Recurring transaction management (full CRUD)
- [x] `/api/v1/rules` - Rule management (full CRUD + test/execute)
- [x] `/api/v1/rule-groups` - Rule group management (full CRUD + execute)
- [x] `/api/v1/summary/*` - Summary endpoints
- [x] `/api/v1/webhooks` - Webhook management (full CRUD + trigger)
- [x] `/api/v1/insight/*` - Insight endpoints
- [x] `/api/v1/search/*` - Search endpoints
- [x] `/api/v1/data/export/*` - Export endpoints
- [x] `/api/v1/chart/*` - Chart endpoints
- [x] `/api/v1/configuration` - Configuration
- [x] `/api/v1/preferences` - User preferences
- [x] `/api/v1/available_budgets` - Available budgets
- [x] `/api/v1/object-groups` - Object groups
- [x] `/api/v1/links` - Transaction links
- [x] `/api/v1/attachments` - Attachments
- [x] `/api/v1/currency_exchange_rates` - Exchange rates
- [x] `/api/v1/data/bulk` - Bulk operations
- [x] `/api/v1/user-groups` - User groups (read-only)
- [x] `/api/v1/users` - User management (admin)

## License

MIT License
