# tarunai-connect-mubu

Canonical packaged entrypoint for the Mubu live bridge.

This package lives in the tarunAI Connect-aligned harness tree and exposes:

- `tarunai-connect-mubu` console script
- `python -m tarunai_connect.mubu`
- default REPL when no subcommand is supplied
- REPL banner with app version, packaged skill path, and history path
- persisted `current-doc` and `current-node` REPL context
- grouped `discover` / `inspect` / `mutate` / `session` commands

Daily helpers are now explicit by default:

- pass a daily-folder reference to `discover daily-current`, `inspect daily-nodes`, or `session use-daily`
- or set `MUBU_DAILY_FOLDER` if you want those helpers to work without an argument

Canonical source paths:

- `agent-harness/mubu_probe.py`
- `agent-harness/tarunai_connect/mubu/...`

Compatibility wrappers remain at:

- `mubu_probe.py`
- `tarunai_connect/mubu/...`

Primary operator documentation remains at the project root:

- `README.md`
- `SKILL.md`
