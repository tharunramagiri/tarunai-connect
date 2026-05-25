# Session Control

```bash
# List / activate / close
tarunai-connect-iterm2 session list [--window-id ID] [--tab-id ID]
tarunai-connect-iterm2 session activate [SESSION_ID]
tarunai-connect-iterm2 session close [SESSION_ID]

# Split panes
tarunai-connect-iterm2 session split                      # horizontal split
tarunai-connect-iterm2 session split --vertical           # side-by-side
tarunai-connect-iterm2 session split --use-as-context     # new pane becomes context

# Metadata
tarunai-connect-iterm2 session set-name "API Worker"
tarunai-connect-iterm2 session restart
tarunai-connect-iterm2 session resize --columns 220 --rows 50

# Session variables
# Built-in (read-only): hostname, username, path, pid, columns, rows
tarunai-connect-iterm2 session get-var hostname
tarunai-connect-iterm2 session get-var path
# Custom (read/write, must use user. prefix)
tarunai-connect-iterm2 session set-var user.role "api-worker"
tarunai-connect-iterm2 session get-var user.role
```
