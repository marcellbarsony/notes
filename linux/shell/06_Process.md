# Process Management

| Command                            | Description                       |
| ---------------------------------- | --------------------------------- |
| bg                                 | Resume process in background      |
| exec                               | Resume process in background      |
| fg                                 | Bring recent job to foreground    |
| fg <job>                           | Bring job to foreground           |
| job                                |                                   |
| kill <pid>                         | Kill process with process ID      |
| killall <process>                  | Kill process with name            |
| lsof                               | List files opened by processes    |
| pgrep <process>                    | Find ID of process                |
| pmap                               | Memory map of processes           |
| ps                                 | Active processes                  |
| ps -aux                            | All processes                     |
| pstree                             | Process tree                      |
| service --status-all               | Service status                    |
| top                                | All processes                     |

## Cron Job

| Command                            | Description                       |
| ---------------------------------- | --------------------------------- |

## Kill Processes
| Command           | Description        |
| ----------------- | ------------------ |
| kill -l           | List signals
| kill -15 <pid>    | Send SIGTERM
| kill -2  <pid>    | Send SIGINIT
| kill -1  <pid>    | Send SIGHUP
| kill -9  <pid>    | Send SIGKILL
