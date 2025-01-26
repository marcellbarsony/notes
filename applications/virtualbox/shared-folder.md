# Shared folder

## Dependencies (Host)

1. Install `virtualbox-guest-utils`
2. Add user to `vboxsf` group

## Manual mounting

```sh
mount -t vboxsf myproject /mnt/mount/point/on/guest
```
Where `shared_folder_name` is the folder name assigned by the hypervisor when
the share was created.

## Unmount

```sh
umount shared_folder_name mount/point/on/guest/system
```
