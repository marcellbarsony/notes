# Git commands

## Stage files

Stage all files that have been modified.

```sh
# Excluding new files
git add .
git add -a -m "Commit message"

# Including new files
git add -A
git commit -A -m "Commit message"
```

## Reset & Revert

Wipe all the changes on the local branch and replace them with the code from the main remote branch

```sh
git reset --hard origin/main
```

Revert creates a new commit that undoes all the changes from the old commit to preserve history
```sh
# Undo a commit on the current branch
git revert <commit_hash>

# Revert to the most recent commit
git revert HEAD
```

Restore file from commit
```sh
# Find commit hash (SHA1)
git log /path/to/file

# Check out file
git checkout <commit_hash> path/to/file
```
