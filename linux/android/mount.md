# Mount

[Arch Wiki - Media Transfer Protocol](https://wiki.archlinux.org/title/Media_Transfer_Protocol#SIMPLE-MTPFS)

```sh
paru -S simple-mtpfs
```

List devices
```sh
mtpfs -l
```

Mount device to `/mnt/android`
```sh
sudo simple-mtpfs --device 1 /mnt/android
```

Open directory with graphical file manager
```sh
sudo thunar /mnt/android
```
