# Session I/O

```bash
# Send input
tarunai-connect-iterm2 session send "echo hello"          # sends text + newline
tarunai-connect-iterm2 session send "text" --session-id <id>
tarunai-connect-iterm2 session send "text" --no-newline

# Inject raw bytes
tarunai-connect-iterm2 session inject $'\x1b[2J'          # escape sequence
tarunai-connect-iterm2 session inject "1b5b324a" --hex    # same in hex

# Read visible screen — ALWAYS use --json, output is silently empty without it
tarunai-connect-iterm2 --json session screen              # visible area only
tarunai-connect-iterm2 --json session screen --lines 20

# Read full history
tarunai-connect-iterm2 --json session scrollback
tarunai-connect-iterm2 --json session scrollback --tail 100
tarunai-connect-iterm2 --json session scrollback --tail 500 --strip   # no null bytes
tarunai-connect-iterm2 --json session scrollback --lines 200          # first 200 lines

# Get selected text
tarunai-connect-iterm2 session selection
```

`session screen` = visible area only. `session scrollback` = entire history, atomically, oldest→newest.
`overflow` in scrollback response = lines lost when buffer was full (set profile limit to "unlimited" to avoid).
