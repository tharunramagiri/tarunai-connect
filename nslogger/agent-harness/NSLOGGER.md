# NSLogger CLI Harness — SOP

## What is NSLogger

NSLogger is a macOS application for receiving, viewing, and analyzing log messages
sent by iOS/macOS applications using the NSLogger client library.

## Core Concepts

| Concept | Description |
|---------|-------------|
| `.nsloggerdata` | Saved binary-plist session file (opened/exported by the GUI) |
| `.rawnsloggerdata` | Raw wire-protocol capture file |
| Message | A single log entry with: sequence, timestamp, level, tag, threadID, type, text |
| Message Types | `text`, `image`, `data` |
| Log Level | 0=error, 1=warning, 2=info, 3=debug, 4=verbose (higher=noisier) |
| Connection | A live client connection (by Bonjour or direct TCP on port 50000) |
| Filter | A predicate that restricts which messages are displayed |

## Wire Protocol (rawnsloggerdata)

NSLogger uses a custom binary protocol over TCP:

```
[4-byte big-endian total message length]
[4-byte big-endian sequence number]
[2-byte part count]
for each part:
    [1-byte part key]
    [1-byte part type]
    [4-byte big-endian data length]
    [N bytes data]
```

Part keys: `0=messageType`, `1=timestamp_s`, `2=timestamp_ms`, `3=timestamp_us`,
           `4=threadID`, `5=tag`, `6=level`, `7=message`, `8=imageWidth`,
           `9=imageHeight`, `10=messageSeq`, `11=filename`, `12=lineNumber`,
           `13=functionName`, `20=clientName`, `21=clientVersion`,
           `22=osName`, `23=osVersion`, `24=clientModel`, `25=uniqueID`

Part types: `0=string(UTF8)`, `1=binary`, `2=int16`, `3=int32`, `4=int64`,
            `5=image`

Message types: `0=log`, `1=blockStart`, `2=blockEnd`, `3=clientInfo`,
               `4=disconnect`, `255=marker`

## CLI Command Groups

```
tarunai-connect-nslogger read     # Parse and display .nsloggerdata / .rawnsloggerdata
tarunai-connect-nslogger filter   # Filter messages from a file (level, tag, thread, text, regex, type, time, seq)
tarunai-connect-nslogger export   # Export messages to text/JSON/CSV
tarunai-connect-nslogger stats    # Summary statistics for a file
tarunai-connect-nslogger listen   # Listen for live NSLogger connections
tarunai-connect-nslogger generate # Generate sample .rawnsloggerdata for testing
tarunai-connect-nslogger tail     # Show last N messages from a file
tarunai-connect-nslogger clients  # List all client_info records in a file
tarunai-connect-nslogger blocks   # Show block start/end structure as indented tree
tarunai-connect-nslogger merge    # Merge multiple files sorted by timestamp
```

## Typical Agent Workflow

```bash
# Inspect a captured log file
tarunai-connect-nslogger read session.rawnsloggerdata

# Find all errors
tarunai-connect-nslogger filter --level 0 session.rawnsloggerdata

# Filter within a time window
tarunai-connect-nslogger filter --after "10:30:00" --before "10:45:00" session.rawnsloggerdata

# Filter by sequence range
tarunai-connect-nslogger filter --from-seq 100 --to-seq 200 session.rawnsloggerdata

# Show last 50 messages
tarunai-connect-nslogger tail --count 50 session.rawnsloggerdata

# List connected clients
tarunai-connect-nslogger clients session.rawnsloggerdata

# Show block/call structure
tarunai-connect-nslogger blocks session.rawnsloggerdata

# Merge two capture files
tarunai-connect-nslogger merge a.rawnsloggerdata b.rawnsloggerdata --format json

# Export for further analysis
tarunai-connect-nslogger export --format json session.rawnsloggerdata > logs.json

# Get statistics
tarunai-connect-nslogger stats session.rawnsloggerdata

# Listen for live iOS logs via Bonjour, matching NSLogger.app
tarunai-connect-nslogger listen --bonjour --name bazinga --debug

# Mirror live logs to disk while still printing stdout
tarunai-connect-nslogger listen --bonjour --name bazinga --output app.log

# Direct TCP/TLS mode for manually configured clients
tarunai-connect-nslogger listen --port 50000 --ssl --debug
```
