# Android Debug Bridge

[Arch Wiki - Android Debug Bridge](https://wiki.archlinux.org/title/Android_Debug_Bridge)<br>
[Android](https://wiki.archlinux.org/title/Android)

<!-- Sources {{{ -->
## Sources

- [Android Developers - ADB](https://developer.android.com/tools/adb)
- [Android Developers - Settings](https://developer.android.com/reference/android/provider/Settings)
- [Android Developers - Settings.System](https://developer.android.com/reference/android/provider/Settings.System)
- [Android Developers - Settings.Global](https://developer.android.com/reference/android/provider/Settings.Global)
- [Android Developers - Settings.Secure](https://developer.android.com/reference/android/provider/Settings.Secure)

- [3os.org - Cheat sheet](https://3os.org/android/adb-cheat-sheet/#phone-info)
- [XDA Forums - Optimization guide](https://xdaforums.com/t/samsung-galaxy-one-ui-optimization-guide.4376755)
- [Nebash.com - Optimization guide](https://nebash-com.custommapposter.com/article/samsung-galaxy-optimization-guide-battery-performance-stability-heat)
- [Samsung Community - Debloat (Spanish)](https://r1.community.samsung.com/t5/galaxy-a/debloat-e-comandos-para-desativar-recursos/td-p/24850189)
- [GitHub - ADB commands](https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8)
- [GitHub - Android Melody](https://github.com/ionuttbara/melody_android)
- [YouTube - Change these settings](https://www.youtube.com/watch?v=qKC2tlsfBSg)
<!-- }}} -->

<!-- Installation {{{ -->
## Installation

ADB is part of the [android-tools](https://archlinux.org/packages/extra/x86_64/android-tools/)
package

```sh
sudo pacman -S android-tools usbutils
```

[lsusb(8)](https://man.archlinux.org/man/lsusb.8.en) is provided by [usbutils](https://archlinux.org/packages/core/x86_64/usbutils/)
<!-- }}} -->

<!-- Setup {{{ -->
## Setup

<!-- 1. Enable USB debugging on the phone {{{-->
### 1. Enable USB debugging on the phone

- **Settings > Developer options > USB debugging**

- **Allow USB Debugging?** dialog should be presented when the device is
  physically connected.<br>
- Select **Always Allow**, then tap **OK**.<br>

If the dialog was never presented, try
**Settings > Developer Options > Revoke USB Debugging Authorizations**
<!-- }}} -->

<!-- 2. Find the device IDs {{{-->
### 2. Find the device IDs

```sh
 lsusb
...
Bus 004 Device 009: ID 04e8:6860 Samsung Electronics Co., Ltd Galaxy series, misc. (MTP mode)
...
```
Where vendor id is **04e8** and product id is **6860**
<!-- }}} -->

<!-- 3. Add udev rules {{{-->
### 3. Add udev rules

Create a custom udev rule by replacing `[VENDOR ID]` and `[PRODUCT ID]` in the
template
```
 sudoedit /etc/udev/rules.d/51-android.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", MODE="0660", GROUP="adbusers", TAG+="uaccess"
SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", ATTR{idProduct}=="[PRODUCT ID]", SYMLINK+="android_adb"
SUBSYSTEM=="usb", ATTR{idVendor}=="[VENDOR ID]", ATTR{idProduct}=="[PRODUCT ID]", SYMLINK+="android_fastboot"
```
<!-- }}} -->

<!-- 4. Reload udev rules {{{-->
### 4. Reload udev rules

`udev` automatically detects changes to rules files. However, the rules are not
re-triggered automatically on already existing devices. Hot-pluggable devices,
such as USB devices, have to be reconnected for the new rules to take effect.
```sh
 sudo su
 udevadm control --reload
 udevadm trigger
```
<!-- }}} -->

<!-- 5. Detect the device {{{-->

### 5. Detect the device

Restart the adb server (optional)
```sh
> adb kill-server                                                       /etc/udev/rules.d  as su
> adb start-server
```

```sh
 adb devices
List of devices attached
RFCNC09BXGE     device
```

<!-- }}} -->
<!-- }}} -->

<!-- {{{ Pair & Connect -->
## Pair & Connect

Pair
```sh
adb pair <ip:port>
```

Connect
```sh
adb connect <ip:port>
```
<!-- }}} -->

<!-- {{{ Packages -->
## Packages

[Call package manager (pm)](https://developer.android.com/tools/adb#pm)

List packages
```sh
adb shell pm list packages --user 0
adb shell pm list packages --user 0 | sed 's/.*://g'
adb shell cmd package list packages --user 0
adb shell cmd package list packages --user 0 | sed 's/.*://g'
adb shell cmd package list packages --user 0 | sed 's/.*://g' > packages-diff.txt
```

Install package
```sh
adb install /path/to/apk
```

Uninstall package
```sh
adb shell "pm uninstall --user 0 <package>"
```

Disable package
```sh
adb shell "pm disable-user --user 0 <package>"
adb shell "pm enable <package>"
```
[reddit](https://www.reddit.com/r/GalaxyS9/comments/iv4p3n/adb_list_to_safely_disable_samsung_bloatware/)
<!-- }}} -->

<!-- {{{ Settings -->
## Settings

List settings
```sh
adb shell settings list system
adb shell settings list global
adb shell settings list secure
adb shell getprop
```

List all settings (diff)
```sh
adb shell settings list system > adb_sys.txt && adb shell settings list global > adb_glo.txt && adb shell settings list secure > adb_sec.txt
adb shell settings list system > adb_sys2.txt && adb shell settings list global > adb_glo2.txt && adb shell settings list secure > adb_sec2.txt
```
<!-- }}} -->

<!-- {{{ Files -->
## Files

[Copy files to and from a device](https://developer.android.com/tools/adb#copyfiles)

Pull
```sh
adb pull remote local

# Example
adb pull sdcard/DCIM/Camera/ ~/tmp/droid
```

Push
```sh
adb push local remote

# Example
adb push ~/tmp/droid sdcard/DCIM/Camera/
```
<!-- }}} -->

<!-- {{{ Actions -->
## Actions

Notifications (send)
```sh
adb shell cmd notification post -t "Title" This is a test notification
```

Screenshot
```sh
adb shell screencap -p /sdcard/screenshot.png
```

Volume down (0)
```
adb shell input keyevent 164
```
<!-- }}} -->

<!-- {{{ Dumpsys -->
## Dumpsys

[Android Developers - dumpsys](https://developer.android.com/tools/dumpsys)
[ADB Shell - dumpsys](https://adbshell.com/commands/adb-shell-dumpsys)
<!-- }}} -->
