# Shell Integration

Requires: `curl -L https://iterm2.com/shell_integration/install_shell_integration.sh | bash`

```bash
tarunai-connect-iterm2 session get-prompt                 # last prompt: command, cwd, state
tarunai-connect-iterm2 session wait-prompt --timeout 30   # block until next prompt appears
tarunai-connect-iterm2 session wait-command-end --timeout 120  # block until exit; returns exit_status
```

**Reliable execution pattern** (send → wait → read):
```bash
tarunai-connect-iterm2 session send "make build"
tarunai-connect-iterm2 session wait-command-end --timeout 120
tarunai-connect-iterm2 --json session scrollback --tail 50 --strip
```

`wait-command-end` returns `{"session_id": "...", "exit_status": 0, "timed_out": false}`.
