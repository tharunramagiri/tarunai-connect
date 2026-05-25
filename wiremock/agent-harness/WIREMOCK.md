# WireMock CLI Harness — Standard Operating Procedure

## What is WireMock?

WireMock is a flexible HTTP mock server used to stub and record HTTP interactions. It exposes a REST Admin API at `/__admin/` for managing stubs, inspecting requests, controlling stateful scenarios, and recording traffic from real backends.

This CLI harness wraps those admin endpoints so agents and developers can control WireMock from the terminal or scripts without needing to craft raw HTTP calls.

---

## Starting WireMock Standalone

### Download

```bash
curl -fsSL https://repo1.maven.org/maven2/org/wiremock/wiremock-standalone/3.3.1/wiremock-standalone-3.3.1.jar \
     -o wiremock-standalone.jar
```

### Start (default port 8080)

```bash
java -jar wiremock-standalone.jar --port 8080 --verbose
```

### Start with persistent mappings directory

```bash
java -jar wiremock-standalone.jar \
  --port 8080 \
  --root-dir ./wiremock-data \
  --verbose
```

### Start with HTTPS

```bash
java -jar wiremock-standalone.jar \
  --port 8443 \
  --https-port 8443 \
  --verbose
```

### Docker (alternative)

```bash
docker run -d --name wiremock \
  -p 8080:8080 \
  wiremock/wiremock:latest
```

---

## Installing the CLI

```bash
cd /path/to/agent-harness
pip install -e .
tarunai-connect-wiremock --help
```

---

## Connection Configuration

All connection parameters can be set via environment variables or CLI flags.

| Environment Variable | CLI Flag     | Default     | Description          |
|----------------------|--------------|-------------|----------------------|
| `WIREMOCK_HOST`      | `--host`     | `localhost` | WireMock host        |
| `WIREMOCK_PORT`      | `--port`     | `8080`      | WireMock port        |
| `WIREMOCK_SCHEME`    | `--scheme`   | `http`      | `http` or `https`    |
| `WIREMOCK_USER`      | `--user`     | (none)      | Basic auth username  |
| `WIREMOCK_PASSWORD`  | `--password` | (none)      | Basic auth password  |
| `WIREMOCK_JSON`      | `--json`     | false       | JSON output mode     |

**Example — connect to a remote WireMock instance:**

```bash
export WIREMOCK_HOST=wiremock.internal
export WIREMOCK_PORT=9090
tarunai-connect-wiremock status
```

---

## Common Workflows

### 1. Verify the server is running

```bash
tarunai-connect-wiremock status
```

### 2. Create a simple stub

```bash
# Quick form: METHOD URL STATUS_CODE [--body JSON]
tarunai-connect-wiremock stub quick GET /api/users 200 --body '{"users":[]}'

# Full JSON form
tarunai-connect-wiremock stub create '{
  "request": { "method": "POST", "url": "/api/orders" },
  "response": { "status": 201, "body": "{\"id\":42}", "headers": { "Content-Type": "application/json" } }
}'
```

### 3. List all stubs

```bash
tarunai-connect-wiremock stub list
tarunai-connect-wiremock stub list --json   # machine-readable
```

### 4. Get a specific stub

```bash
tarunai-connect-wiremock stub get <stub-id>
```

### 5. Delete a stub

```bash
tarunai-connect-wiremock stub delete <stub-id>
```

### 6. Reset all stubs to defaults

```bash
tarunai-connect-wiremock stub reset
```

### 7. Persist stubs to disk

```bash
tarunai-connect-wiremock stub save
```

### 8. Import stubs from a file

```bash
tarunai-connect-wiremock stub import ./my-stubs.json
```

---

### Request Verification

```bash
# List recent requests
tarunai-connect-wiremock request list
tarunai-connect-wiremock request list --limit 10

# Find requests matching a pattern
tarunai-connect-wiremock request find '{"method": "GET", "url": "/api/users"}'

# Count matching requests (useful for assertion)
tarunai-connect-wiremock request count '{"method": "POST", "urlPath": "/api/orders"}'

# List unmatched requests (404s)
tarunai-connect-wiremock request unmatched

# Clear the request journal
tarunai-connect-wiremock request reset
```

---

### Stateful Scenario Testing

WireMock supports state machines (scenarios) to simulate multi-step workflows.

```bash
# List all scenarios and their current state
tarunai-connect-wiremock scenario list

# Set a specific scenario to a state
tarunai-connect-wiremock scenario set "login-flow" "logged-in"

# Reset all scenarios to initial state
tarunai-connect-wiremock scenario reset
```

---

### Recording Traffic from a Real Backend

Use recording to auto-generate stubs from real API traffic.

```bash
# Start recording — proxy traffic to a real backend
tarunai-connect-wiremock record start https://api.example.com

# ... make requests to http://localhost:8080 — they are proxied and captured ...

# Stop recording and inspect captured stubs
tarunai-connect-wiremock record stop

# Check if currently recording
tarunai-connect-wiremock record status

# Take a snapshot of in-memory requests as stubs
tarunai-connect-wiremock record snapshot
```

---

### Server Management

```bash
# Check WireMock version
tarunai-connect-wiremock settings version

# Get global settings
tarunai-connect-wiremock settings get

# Full reset (stubs + requests + scenarios)
tarunai-connect-wiremock reset

# Shutdown the server
tarunai-connect-wiremock shutdown
```

---

## JSON Output Mode

All commands support `--json` for machine-readable output suitable for scripting or agent use:

```bash
tarunai-connect-wiremock --json stub list
tarunai-connect-wiremock --json request count '{"method":"GET","url":"/health"}'
```

JSON output varies by command type:

- **Data commands** return the raw WireMock API JSON directly (e.g. `stub list` returns `{"mappings": [...], "total": N}`)
- **Void operations** (delete, reset, save) return `{"status": "ok"}`
- **`status` command** returns `{"status": "running"|"stopped", "host": "...", "port": N}`
- **Errors** return `{"status": "error", "message": "..."}` (printed to stderr in human mode)
