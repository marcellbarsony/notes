## Pacman

```sh
# Update GPG key database
pacman-key --refresh-keys # Trusted keys only
pacman-key --refresh # Untrusted keys

# Initialize GPG key database
pacman-key --init

# Add GPG keys to local keyring
pacman-key --populate archlinux # master signing keys
pacman-key --populate # all keys
```
