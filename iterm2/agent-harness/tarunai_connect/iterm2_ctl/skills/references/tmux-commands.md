# tmux Commands

```bash
tarunai-connect-iterm2 tmux bootstrap                     # start tmux -CC, wait for connection
tarunai-connect-iterm2 tmux bootstrap --attach            # attach to existing session
tarunai-connect-iterm2 tmux bootstrap --session-id <id> --timeout 15
tarunai-connect-iterm2 tmux list                          # active tmux -CC connections
tarunai-connect-iterm2 tmux tabs                          # iTerm2 tabs backed by tmux
tarunai-connect-iterm2 tmux create-window                 # new tmux window → iTerm2 tab
tarunai-connect-iterm2 tmux create-window --use-as-context
tarunai-connect-iterm2 tmux set-visible @1 off|on         # hide/show a tmux window's tab

# tmux protocol commands (sent to tmux server, not to a pane)
tarunai-connect-iterm2 tmux send "list-sessions"
tarunai-connect-iterm2 tmux send "list-windows -a"
tarunai-connect-iterm2 tmux send "list-panes -a -F '#{session_name}:#{window_index}:#{pane_index} #{pane_current_command} #{pane_current_path}'"
tarunai-connect-iterm2 tmux send "new-window -n work"
tarunai-connect-iterm2 tmux send "rename-session dev"
tarunai-connect-iterm2 tmux send "split-window -h"
tarunai-connect-iterm2 tmux send "select-pane -t 0"
tarunai-connect-iterm2 session run-tmux-cmd "rename-window mywork"
```

**Key distinction:** `tmux send` = tmux protocol commands (to tmux server). `session send` = shell text to a specific pane. Use both together.
