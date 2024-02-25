# Btrfs

## Snapper

[Arch Wiki](https://wiki.archlinux.org/title/Snapper)

### Managing snapshots

[List configurations](https://wiki.archlinux.org/title/snapper#List_configurations)
```sh

```

[List snapshots](https://wiki.archlinux.org/title/snapper#List_snapshots)
```sh
sudo snapper -c <config> list
sudo btrfs subvolume delete </path/to/subvolume>

# Example
sudo snapper -c home list
sudo btrfs subvolume list /home/.snapshots
```

[Delete snapshots](https://wiki.archlinux.org/title/snapper#Delete_a_snapshot)
```sh

```
