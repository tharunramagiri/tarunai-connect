---
name: "tarunai-connect-lldb"
description: Stateful LLDB debugging via LLDB Python API
version: 1.0.0
command: tarunai-connect-lldb
install: pip install tarunai-connect-lldb
requires:
  - lldb (Python bindings)
  - click>=8.0
  - prompt-toolkit>=3.0
categories:
  - debugging
  - native
  - lldb
---

# LLDB CLI Skill

Use this CLI to run structured LLDB debugging workflows with JSON output.

## Capabilities

- Create debug target from executable path
- Launch process or attach by pid/name
- Manage breakpoints (set/list/delete/enable/disable)
- Inspect threads, frames, locals, and backtrace
- Evaluate expressions in current frame
- Read/find process memory
- Load core dumps
- Interactive REPL with persistent session state
- Formal stdio Debug Adapter Protocol server for AI/editor clients

## Quick Commands

```bash
tarunai-connect-lldb --json target create --exe /path/to/exe
tarunai-connect-lldb --json process launch --arg foo --arg bar
tarunai-connect-lldb --json breakpoint set --function main
tarunai-connect-lldb --json breakpoint set --function PluginEntry --allow-pending
tarunai-connect-lldb --json process continue
tarunai-connect-lldb --json process interrupt
tarunai-connect-lldb --json thread backtrace --limit 20
tarunai-connect-lldb --json frame locals
tarunai-connect-lldb --json expr "myVar"
tarunai-connect-lldb --json memory read --address 0x1000 --size 64
tarunai-connect-lldb --json session close
```

## Debug Adapter Protocol

Use the DAP entry point when an AI client needs a real debug adapter lifecycle
instead of shelling out separate CLI commands:

```bash
tarunai-connect-lldb-dap
tarunai-connect-lldb-dap --profile /path/to/stop-rules.json
```

or:

```bash
tarunai-connect-lldb dap
tarunai-connect-lldb dap --profile /path/to/stop-rules.json
```

The DAP server speaks stdio `Content-Length` frames and must have exclusive
stdout. Do not print logs to stdout around it. Supported requests include
`initialize`, `launch`, `attach`, `configurationDone`, `setBreakpoints`,
`setFunctionBreakpoints`, `threads`, `stackTrace`, `scopes`, `variables`,
`setVariable`, `evaluate`, `continue`, `pause`, `next`, `stepIn`, `stepOut`,
`source`, `loadedSources`, `readMemory`, `modules`, `exceptionInfo`,
`disassemble`, and `disconnect`.

DAP variables can expose child references for structs/classes/arrays. Use
`setVariable` only while stopped; LLDB may reject writes to optimized-out or
read-only values.

For long-running GUI debuggees, DAP `continue` is non-blocking from the client's
point of view: the adapter sends the response and `continued` event first, then
waits for LLDB on a background thread. DAP `pause` uses LLDB async interrupt.
If an agent needs to change breakpoints while the debuggee is running, the
adapter interrupts first and waits for a stopped state before mutating LLDB
breakpoints; if the target does not stop in time, retry after an explicit
`pause`/`stopped` cycle.

For GUI apps that stop on debugger-internal startup or shader-JIT breakpoints,
`launch` and `attach` accept the non-standard boolean argument
`autoContinueInternalBreakpoints`. Enable it only when those internal stops are
noise for the task; the adapter emits an `output` event before auto-continuing.
For target-specific noise, prefer structured stop rules through inline
`stopRules` or an external `stopRuleProfile`/`--profile` JSON file. Rules can
match by `reason`, `module`, `function`, and/or `regex`, then either `stop` with
clear `cliAnythingStop.origin` metadata or `continue` automatically. Use
profiles for apps such as C4D so their NVIDIA shader-JIT/startup traps live
outside the generic adapter.

DAP `stopped` events include `body.cliAnythingStop.origin`: `manualPause` for a
client pause request, `internalTrap` for a matched internal rule, and `debuggee`
for ordinary program stops. Existing `tarunai-connect-lldb-dap` processes do not
hot-load new code or profile contents; restart the adapter and re-attach or
re-launch before expecting new rules to apply.

## Command Groups

### target
```bash
tarunai-connect-lldb --json target create --exe /path/to/exe [--arch x86_64]
tarunai-connect-lldb --json target info
```

### process
```bash
tarunai-connect-lldb --json process launch [--arg ARG ...] [--env KEY=VALUE ...] [--cwd DIR] [--stop-at-entry]
tarunai-connect-lldb --json process attach --pid 1234
tarunai-connect-lldb --json process attach --name myapp --wait-for
tarunai-connect-lldb --json process continue
tarunai-connect-lldb --json process interrupt
tarunai-connect-lldb --json process detach
tarunai-connect-lldb --json process info
```

### breakpoint
```bash
tarunai-connect-lldb --json breakpoint set --function main
tarunai-connect-lldb --json breakpoint set --file main.c --line 42 --condition "i > 10"
tarunai-connect-lldb --json breakpoint set --function LateLoadedSymbol --allow-pending
tarunai-connect-lldb --json breakpoint list
tarunai-connect-lldb --json breakpoint delete --id 1
tarunai-connect-lldb --json breakpoint enable --id 1
tarunai-connect-lldb --json breakpoint disable --id 1
```

### thread / frame / step
```bash
tarunai-connect-lldb --json thread list
tarunai-connect-lldb --json thread select --id 11111
tarunai-connect-lldb --json thread backtrace --limit 50
tarunai-connect-lldb --json frame select --index 0
tarunai-connect-lldb --json frame info
tarunai-connect-lldb --json frame locals
tarunai-connect-lldb --json step over
tarunai-connect-lldb --json step into
tarunai-connect-lldb --json step out
```

### expr / memory / core
```bash
tarunai-connect-lldb --json expr "argc"
tarunai-connect-lldb --json memory read --address 0x1000 --size 128
tarunai-connect-lldb --json memory find "needle" --start 0x1000 --size 4096
tarunai-connect-lldb --json core load --path /path/to/core
```

## Agent Usage Notes

- Prefer `--json` for all automated flows.
- Separate non-REPL invocations share a persistent session daemon by default.
- Use `--session-file PATH` or `TARUNAI_CONNECT_LLDB_SESSION_FILE` to pin an explicit session for a task.
- Run `tarunai-connect-lldb --json session close` when finished so attached processes detach and launched debuggees are cleaned up.
- Use REPL when a human-like interactive shell is more convenient, not because persistence requires it.
- Unresolved CLI breakpoints fail by default; pass `--allow-pending` only when a future module/symbol load is expected.
- DAP unresolved breakpoints use protocol semantics: `verified: false` until resolved.
- DAP `continue` is non-blocking for long-running GUI processes, and DAP `pause` uses async interrupt.
- DAP breakpoint changes during an active continue first interrupt and wait for a stopped state before mutating LLDB.
- Use DAP stop-rule profiles for app-specific internal traps; restart and re-attach/re-launch after profile changes.
- `memory find` uses a chunked scan capped at 1 MiB per call.
- Call `target create` before process or core commands.
- Expect structured errors: `{"error": "...", "type": "..."}`
