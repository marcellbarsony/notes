# Generate SSH key

[GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

1. Generate key with ssh-keygen
```sh
ssh-keygen -t ed25519 -C "email@domain.com"
```

2. Accept the default file location <kbd>Enter</kbd>
```sh
> Enter a file in which to save the key (/home/user/.ssh/ed25519)
```

3. Enter a secure passphrase

## Add SSH key to the agent

[GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

1. Start the SSH agent in the background
```sh
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```

```sh
exec ssh-agent zsh
```

2. Check if the agent is running
```sh
ps aux | grep ssh-agent
```

3. Add the SSH private key to the SSH agent.
To add an existing key with a different name, replace `id_ed25519` in the command.
```sh
ssh-add ~/.ssh/id_ed25519
```

## Add public SSH key to GitHub account

[GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

### Browser

Settings **>** SSH and GPG keys **>** New SSH Key

Paste the content of `~/.ssh/id_ed25519.pub`, click 'Add SSH key' and enter your GitHub password

### CLI

```sh
gh ssh-key add key.pub
```

To include a title, use the `-t` or `--title` flag.
```sh
gh ssh-key add key-file --title "personal laptop"
```
