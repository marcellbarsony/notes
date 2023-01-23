# Revert

Revert does not remove any old commit. Instead, it created a new commit that undoes all the changes from the old commit to preserve history of the repository.

Undo a commit on the current branch

```
git revert 486bdb2
```

Revert to the most recent commit

```
git revert HEAD
```

## Restore file from previous commit

Find the right commit hash (SHA1)
```
git log path/to/file
```

Check out file
```
git checkout <commit_hash> path/to/file
```

