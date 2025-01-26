# BTRFS

<!-- Btrfs {{{-->
## Btrfs

[List snapshots (subvolumes)](https://wiki.archlinux.org/title/btrfs#Listing_subvolumes)
```sh
sudo btrfs subvolume list -p <path>

# Example
sudo btrfs subvolume list -p /home
```

[Delete snapshot (subvolume)](https://wiki.archlinux.org/title/snapper#Delete_a_snapshot)
```sh
sudo btrfs subvolume delete </path/to/subvolume>

# Example
sudo btrfs subvolume delete /home/.snapshots/1/snapshot
```

Filesystem usage
```sh
sudo btrfs filesystem usage /
```
<!-- }}} -->

<!-- Snapper {{{-->
## Snapper

[Arch Wiki - Snapper](https://wiki.archlinux.org/title/Snapper)

### Managing snapshots

[List configurations](https://wiki.archlinux.org/title/snapper#List_configurations)
```sh
sudo snapper list-configs
```

[List snapshots](https://wiki.archlinux.org/title/snapper#List_snapshots)
```sh
sudo snapper -c <config> list

# Example
sudo snapper -c home list
```

Set config
```sh
sudo snapper -c home set-config <configuration>

# Example
sudo snapper -c home set-config "TIMELINE_CREATE=no"
```
<!-- }}} -->
