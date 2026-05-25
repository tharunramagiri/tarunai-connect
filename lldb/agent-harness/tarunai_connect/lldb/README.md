# tarunai-connect-lldb

Command-line interface for LLDB debugger using LLDB Python API.

The package exposes two agent-facing entry points:

- `tarunai-connect-lldb`: JSON CLI / REPL workflows with a persistent session daemon
- `tarunai-connect-lldb-dap`: stdio Debug Adapter Protocol server for editor-style and AI debug clients

## Installation

```bash
cd lldb/agent-harness
pip install -e .
```

## LLDB Prerequisites

Install LLDB:

```bash
# macOS
xcode-select --install

# Ubuntu
sudo apt install lldb python3-lldb

# Windows
winget install LLVM.LLVM
```

Ensure `lldb` is on `PATH`. The harness auto-discovers Python bindings via:

```bash
lldb -P
```

## Quick Start

```bash
# Show help
tarunai-connect-lldb --help

# Create a target
tarunai-connect-lldb --json target create --exe /path/to/executable

# Launch process
tarunai-connect-lldb --json process launch --arg foo --arg bar

# Stop at process entry before user code
tarunai-connect-lldb --json process launch --stop-at-entry

# Set breakpoint by function
tarunai-connect-lldb --json breakpoint set --function main

# Pending breakpoints are explicit
tarunai-connect-lldb --json breakpoint set --function PluginEntry --allow-pending

# Continue and inspect
tarunai-connect-lldb --json process continue
tarunai-connect-lldb --json process interrupt
tarunai-connect-lldb --json thread backtrace
tarunai-connect-lldb --json frame locals

# Evaluate expression
tarunai-connect-lldb --json expr "argc"

# Close the persistent session when you are done
tarunai-connect-lldb --json session close

# Start REPL (default mode)
tarunai-connect-lldb
```

Non-REPL commands share a persistent LLDB session automatically, so commands
such as `target create`, `breakpoint set`, `process launch`, and follow-up
inspection commands can run as separate CLI invocations against the same live
debugger state. The default session state file lives in a per-user application
directory, not the global temp directory. Use `--session-file` or
`TARUNAI_CONNECT_LLDB_SESSION_FILE` when an agent needs an explicit session path,
and run `session close` when finished.

By default, `breakpoint set` fails if LLDB creates a pending breakpoint with no
resolved locations. Use `--allow-pending` only when the target or symbols are
expected to load later. Breakpoint payloads include `resolved` and
`location_details` so agents can tell whether a stop is actually reachable.

## Debug Adapter Protocol

Run the formal stdio DAP server with:

```bash
tarunai-connect-lldb-dap
tarunai-connect-lldb-dap --profile /path/to/stop-rules.json
```

or through the CLI convenience command:

```bash
tarunai-connect-lldb dap
tarunai-connect-lldb dap --profile /path/to/stop-rules.json
```

The DAP server owns one in-process `LLDBSession` and writes only DAP frames to
stdout. Debuggee stdout/stderr is suppressed during DAP launches so protocol
messages are not corrupted.

Supported requests include:

- `initialize`, `launch`, `attach`, `configurationDone`, `disconnect`
- `setBreakpoints`, `setFunctionBreakpoints`
- `threads`, `stackTrace`, `scopes`, `variables`, `setVariable`, `evaluate`
- `continue`, `pause`, `next`, `stepIn`, `stepOut`
- `source`, `loadedSources`, `readMemory`, `modules`, `exceptionInfo`, `disassemble`

DAP launch-time unresolved breakpoints are returned as `verified: false` and
updated with breakpoint events after launch if LLDB resolves them.
Variables support expandable child references for structs/classes/arrays, and
`setVariable` can update stopped-frame locals or child values when LLDB allows
the assignment.

For long-running GUI targets, DAP `continue` responds before the blocking LLDB
`SBProcess.Continue()` call completes, then waits on a background thread for the
next stop. DAP `pause` uses `SBProcess.SendAsyncInterrupt()` so the adapter stays
responsive while the debuggee is running. If `setBreakpoints` or
`setFunctionBreakpoints` arrives during an active continue, the adapter first
requests an async interrupt, waits for the continue thread to observe a stopped
state, and only then mutates LLDB breakpoints. If the process does not stop in
time, the request fails clearly instead of hanging the DAP loop.

`launch` and `attach` accept non-standard stop-rule controls for noisy GUI
debuggees:

- `autoContinueInternalBreakpoints`: compatibility boolean that enables built-in
  rules for NVIDIA `__jit_debug_register_code` / `jit-debug-register` and
  Windows `Exception 0x80000003` at ``ntdll.dll`DbgBreakPoint``.
- `stopRules`: inline structured rules with optional `name`, `action`
  (`stop` or `continue`), `origin`, `reason`, `module`, `function`, and `regex`.
  Each rule must include at least one matcher, so a profile cannot accidentally
  classify every stop.
- `stopRuleProfile` / `stopProfile` / `profile`: external JSON profile path
  loaded for that launch/attach request.

The DAP process also accepts `--profile` to load a base profile at adapter
startup. Profiles are JSON objects such as:

```json
{
  "autoContinueInternalBreakpoints": true,
  "stopRules": [
    {
      "name": "c4d-nvidia-jit",
      "action": "continue",
      "origin": "internalTrap",
      "module": "nvgpucomp64.dll",
      "function": "__jit_debug_register_code"
    }
  ]
}
```

Every DAP `stopped` event includes `body.cliAnythingStop` with
`origin` (`manualPause`, `internalTrap`, or `debuggee`), LLDB stop reason,
module/function/frame metadata, and the matched rule when applicable. Running
`tarunai-connect-lldb-dap` processes do not hot-load code or profile changes;
restart the adapter and re-attach/re-launch the target for new rules to take
effect.

The persistent session daemon now speaks a localhost JSON socket protocol and
stores its session token in an owner-scoped state file. `memory find` scans in
64 KiB chunks and caps each request at 1 MiB.

## Command Groups

- `target`: `create`, `info`
- `process`: `launch`, `attach`, `continue`, `interrupt`, `detach`, `info`
- `breakpoint`: `set`, `list`, `delete`, `enable`, `disable`
- `thread`: `list`, `select`, `backtrace`, `info`
- `frame`: `select`, `info`, `locals`
- `step`: `over`, `into`, `out`
- `expr`
- `memory`: `read`, `find`
- `core`: `load`
- `session`: `info`, `close`
- `dap`
- `repl`

## JSON Output

Use `--json` for all commands in agent workflows:

```bash
tarunai-connect-lldb --json process info
```

## Testing

```bash
cd lldb/agent-harness
pytest tarunai_connect/lldb/tests/test_core.py -v
pytest tarunai_connect/lldb/tests/test_full_e2e.py -v
pytest tarunai_connect/lldb/tests -q
```

E2E tests require:
- a working C compiler (`clang`, `gcc`, or `cc`) so the tests can build a small debug helper
- no extra env vars for the default suite; `LLDB_TEST_CORE` is optional if you want to point the negative-path core-load check at a specific local file
- `memory find` scans are chunked and capped at 1 MiB per invocation
