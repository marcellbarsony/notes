# SSH connection

Attempt to SSH to GitHub
```sh
ssh -T git@github.com
```

A warning like this should be visible:
```sh
> The authenticity of host 'github.com (IP ADDRESS)' can't be established.
> RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
> Are you sure you want to continue connecting (yes/no)?
```

Verify that the fingerprint matches [GitHub's SSH public key fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints), then type `yes`.

### Switch remote URLs from HTTPS to SSH

[GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories#switching-remote-urls-from-https-to-ssh)

Change current working directory to the local project.

List existing remotes in order to get the name of the remote we want to change.
```sh
$ git remote -v
> origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
> origin  https://github.com/USERNAME/REPOSITORY.git (push)
```

Change the remote's URL from HTTPS to SSH with the `git remote set-url` command
```sh
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

Verify that the remote URL has changed with `git remote -v`
