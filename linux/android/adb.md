# Android Debug Bridge

[Arch Wiki - Android Debug Bridge](https://wiki.archlinux.org/title/Android_Debug_Bridge)

## Dependencies

ADB is part of the [android-tools](https://archlinux.org/packages/extra/x86_64/android-tools/) package

```sh
 sudo pacman -S android-tools usbutils
```

[lsusb(8)](https://man.archlinux.org/man/lsusb.8.en) is provided by [usbutils](https://archlinux.org/packages/core/x86_64/usbutils/)

## Usage

1. Enable USB debugging on the phone

**Settings > Developer options > USB debugging**

**Allow USB Debugging?** dialog should be presented when the device is physically connected.<br>
Select **Always Allow**, then tap **OK**.<br>
If the dialog was never presented, try **Settings > Developer Options > Revoke USB Debugging Authorizations**

2. Figure out device IDs

```sh
 lsusb
...
Bus 004 Device 009: ID 04e8:6860 Samsung Electronics Co., Ltd Galaxy series, misc. (MTP mode)
...
```
Where vendor id is **04e8** and product id is **6860**

3. Add udev rules

Create a custom udev rule by replacing `[VENDOR ID]` and `[PRODUCT ID]` in the template

```
 sudoedit /etc/udev/rules.d/51-android.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", MODE="0660", GROUP="adbusers", TAG+="uaccess"
SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", ATTR{idProduct}=="[PRODUCT ID]", SYMLINK+="android_adb"
SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", ATTR{idProduct}=="[PRODUCT ID]", SYMLINK+="android_fastboot"
```

4. Reload udev rules

udev automatically detects changes to rules files.<br>
However, the rules are not re-triggered automatically on already existing devices.<br>
Hot-pluggable devices, such as USB devices, have to be reconnected for the new rules to take effect.

```sh
 sudo su
 udevadm control --reload
 udevadm trigger
```

5. Detect the device

```sh
 adb devices
List of devices attached
RFCNC09BXGE     device
```

## Dumpsys

[Android Developers - dumpsys](https://developer.android.com/tools/dumpsys)
[ADB Shell - dumpsys](https://adbshell.com/commands/adb-shell-dumpsys)

