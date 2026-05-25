# App: Context, Variables, Dialogs, File Panels

## Workspace orientation
```bash
tarunai-connect-iterm2 --json app snapshot                # rich snapshot: all sessions with path, process, role, last output line
tarunai-connect-iterm2 --json app status                  # lightweight inventory: IDs and names only
```

`app snapshot` is the preferred orientation command — use it when landing in an existing workspace.
Set `user.role` on panes so snapshot can identify them: `session set-var user.role "api-server"`

## Context management
```bash
tarunai-connect-iterm2 --json app status                  # inventory all windows/tabs/sessions
tarunai-connect-iterm2 app current                        # focus → saves window/tab/session as context
tarunai-connect-iterm2 app context                        # show saved context
tarunai-connect-iterm2 app set-context --session-id <id>
tarunai-connect-iterm2 app clear-context
```

## App-level variables
```bash
tarunai-connect-iterm2 app get-var hostname
tarunai-connect-iterm2 app set-var user.myvar hello
```

## Modal dialogs
```bash
tarunai-connect-iterm2 app alert "Title" "Message"
tarunai-connect-iterm2 app alert "Deploy?" "Push?" --button Yes --button No
tarunai-connect-iterm2 app text-input "Rename" "Enter name:" --default "myapp"
```

## File panels
```bash
tarunai-connect-iterm2 app file-panel                              # macOS open picker
tarunai-connect-iterm2 app file-panel --ext py --ext txt --multi   # filter + multi-select
tarunai-connect-iterm2 app save-panel --filename output.txt        # save dialog
```
