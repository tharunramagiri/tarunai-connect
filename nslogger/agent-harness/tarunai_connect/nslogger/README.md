# tarunai-connect-nslogger

CLI harness for [NSLogger](https://github.com/fpillet/NSLogger) — read, filter, export, and monitor NSLogger log files from the command line or from AI agents.

## Installation

```bash
cd agent-harness
pip install -e .
```

## Quick Start

```bash
# Generate a sample file
tarunai-connect-nslogger generate sample.rawnsloggerdata --count 50

# Read and display all messages
tarunai-connect-nslogger read sample.rawnsloggerdata

# Show only errors
tarunai-connect-nslogger read sample.rawnsloggerdata --level 0

# Filter by tag
tarunai-connect-nslogger filter sample.rawnsloggerdata --tag Network

# Export to JSON
tarunai-connect-nslogger export sample.rawnsloggerdata --format json

# Statistics
tarunai-connect-nslogger stats sample.rawnsloggerdata

# Listen for live iOS logs via Bonjour, matching the NSLogger.app GUI
tarunai-connect-nslogger listen --bonjour --name bazinga --debug

# Direct TCP/TLS mode for manually configured clients
tarunai-connect-nslogger listen --port 50000 --ssl --debug

# Listen and write received live logs to a file
tarunai-connect-nslogger listen --bonjour --name bazinga --output app.log

# Write machine-readable live logs as JSON Lines
tarunai-connect-nslogger listen --bonjour --name bazinga --output app.jsonl --output-format jsonl

# Interactive command REPL
tarunai-connect-nslogger
tarunai-connect-nslogger repl sample.rawnsloggerdata
```

## JSON Output (Agent Mode)

Every command accepts `--json` for machine-readable output:

```bash
tarunai-connect-nslogger read sample.rawnsloggerdata --json
tarunai-connect-nslogger stats sample.rawnsloggerdata --json
```

## Commands

| Command    | Description |
|-----------|-------------|
| `read`    | Parse and display messages from a file |
| `filter`  | Advanced filtering (level, tag, thread, regex) |
| `export`  | Export to text / JSON / CSV |
| `stats`   | Summary statistics |
| `listen`  | Receive live NSLogger connections via Bonjour or TCP/TLS |
| `generate`| Create sample `.rawnsloggerdata` for testing |
| `repl`    | Interactive command REPL with shared tarunai-connect skin |

## Log Levels

| Level | Name    |
|-------|---------|
| 0     | ERROR   |
| 1     | WARNING |
| 2     | INFO    |
| 3     | DEBUG   |
| 4     | VERBOSE |

## File Formats

| Extension | Description |
|-----------|-------------|
| `.rawnsloggerdata` | Raw NSLogger wire-protocol capture |
| `.nsloggerdata` | Binary plist archive saved by NSLogger.app |
