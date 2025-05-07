# Mount

- [Arch Wiki - Media Transfer Protocol](https://wiki.archlinux.org/title/Media_Transfer_Protocol#SIMPLE-MTPFS)

```sh
paru -S simple-mtpfs
```

1. List devices
```sh
simple-mtpfs -l
```

2. Mount device to `/mnt/android`
```sh
sudo simple-mtpfs --device 1 /mnt/android
```

3. Open directory with graphical file manager
```sh
sudo dolphin /mnt/android
```

## Android File Transfer

- [Android File Transfer](https://wiki.archlinux.org/title/Media_Transfer_Protocol#Android_File_Transfer)

- [android-file-transfer](https://whoozle.github.io/android-file-transfer-linux/)

```sh
sudo pacman -S gvfs-mtf thunar
paru -S jmtpfs
```
