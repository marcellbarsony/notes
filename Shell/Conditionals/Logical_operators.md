# Tests

## && Operator

```sh
mkdir /tmp/bak && cp test.txt /tmp/bak/
```

The folder `/tmp/bak` is created.
If it succeeds and returns with a `0` exit status, then the `cp` command is executed.
There's no need for the `cp` command to be executed if the directory wasn't created.

```sh
HOST="google.com"
ping -c 1 $HOST && echo "$HOST reachable"
```

If the `ping` command returns with exit code `0`, then `google.com reachable` would be echoed to the screen.

## || Operator

```sh
cp test.txt /tmp/bak/ || cp test.txt /tmp
```

The command following the double pipe (`||`) will only execute if the previous command fails.<br>
Only one command can successfully execute.

```sh
HOST="google.com"
ping -c 1 $HOST || echo "$HOST unreachable"
```

If the ping command fails, then `google.com unreachable` would be echoed to the screen.
