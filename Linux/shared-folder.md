# Shared folder

# Dependencies

1. Install `virtualbox-guest-utils`
2. Add user to `vboxsf` group

# Manual mounting

```
# mount -t vboxsf -o gid=vboxsf shared_folder_name mount/point/on/guest/system
```
where `shared_folder_name` is the folder name assigned by the hypervisor
when the share was created.

# Unmount

```
# umount shared_folder_name mount/point/on/guest/system
```
