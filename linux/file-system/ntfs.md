# NTFS

[NTFS-3F - Arch Wiki](https://wiki.archlinux.org/title/NTFS-3G)<br>

## Unencrypted

```sh
# Mount
sudo ntfs-3g /dev/sdX /mnt/
sudo mount -t ntfs-3g /dev/sdaX /mnt/windows
```

## Bitlocker

[dislocker](https://github.com/Aorimn/dislocker)<br>

### Mount

[Dislocker Wiki](https://github.com/Aorimn/dislocker/wiki/Mounting)<br>

```sh
sudo dislocker -v -V /dev/sdX -u -- /mnt/tmp
sudo mount -o loop,rw /mnt/tmp/dislocker-file /media/dislocker/
```
