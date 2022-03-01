# Git commands

Add all files that have been modified - excluding new files

```
git add .
git add -a
```

Add all files that have been modified - including new files

```
git add -A
```

Add all files that have been modified - including new files and a message

```
git commit -A -m "Commit message"
```

## Reset local changes

Wipe all the changes on the local branch and replace them with the code from the main branch in the remote

```
git reset --hard origin/main
```
