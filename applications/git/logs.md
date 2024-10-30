# Logs

Print a pretty log for commits and branches
```sh
git log --graph --decorate --oneline
```

## Searching logs

Use the following command to search for specific changes in the code
```sh
git log -S "Committing changes"
```

This command returns the commit where this text has been added.

## Reflog

See recent commits, pulls, resets, pushes, etc. on the local machine
```sh
git reflog
```
