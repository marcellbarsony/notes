# Mount

## Get disk

```sh
lsblk
```

## Unencrypted

```sh
sudo mount /dev/<drive_name> /mnt/<dir>
```

## Encrypted

Unlock drive
```sh
sudo cryptsetup luksOpen /dev/sdx <drive_name>
```

Mount drive
```sh
sudo mount /dev/mapper/<drive_name> /mnt/<dir>
```
