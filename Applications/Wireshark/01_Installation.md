Wireshark is an open-source packet analyzer used for network troubleshooting, analysis, software and communications protocol development, and education. 

[[Website](https://www.wireshark.org)]
[[Latest distribution](https://www.wireshark.org/download)]

[[GitLab](https://gitlab.com/wireshark/wireshark)]
[[GitHub (Read-only)](https://github.com/wireshark/wireshark)]

[[Arch Wiki - Wireshark](https://wiki.archlinux.org/title/wireshark)]

## Installation

Install the [wireshark-qt](https://archlinux.org/packages/community/x86_64/wireshark-qt/) (GUI) package
```sh
pacman -S wireshark-qt
```

[wireshark-cli](https://archlinux.org/packages/community/x86_64/wireshark-cli/) (CLI) package.
```sh
pacman -S wireshark-cli
```

## Capturing privileges

**Do not run** Wireshark as **root**, it is insecure.<br>
Wireshark has implemented privilege separation, which means Wireshark GUI (or the tshark CLI) can run as a normal user while the dumpcap capture utility runs as root.

The [wireshark-cli](https://archlinux.org/packages/community/x86_64/wireshark-cli/) install script sets packet capturing capabilities on the `/usr/bin/dumpcap` executable.

`/usr/bin/dumpcap`can only be executed by root and members of the `wireshark` group, therefore to use Wireshark as a normal user you have to add the normal user to the `wireshark` user group.

```
usermod -aG wireshark ${username}
```
