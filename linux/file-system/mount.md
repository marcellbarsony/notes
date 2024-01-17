# Mount

Get disk

```sh
lsblk
```

## Mount drive

```sh
sudo mount /dev/<drive_name> /mnt/<dir>
```

## LuksDrive

Unlock drive

```sh
sudo cryptsetup luksOpen /dev/sdx <drive_name>
```

Mount drive

```sh
sudo mount /dev/mapper/<drive_name> /mnt/<dir>
```
