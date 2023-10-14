## Installation

[packettracer](https://aur.archlinux.org/packages/packettracer/) (AUR) cannot be installed using automated methods (e.g. AUR helper) as the software's tarball must be installed first before building the package.

[[ArchWiki](https://wiki.archlinux.org/title/PacketTracer)]

### 1. Acquire build files

Clone PacketTracer's git repository.

```sh
git clone https://aur.archlinux.org/packettracer.git
```

### 2. Acquire PacketTracer deb package

1. Log into [Cisco Networking Academy](https://www.netacad.com/)
2. Download Packet Tracer from _Resources_ > [Download Packet Tracer](https://www.netacad.com/portal/resources/packet-tracer)
3. Place the _.deb_ file where the build files are located

### 3. Build & Install

1. Make the package

```sh
makepkg -si
```

### 4. Dependencies

The QT5 theme is required to launch Packet Tracer (*as of 1/13/2022*)

```sh
sudo pacman -S qt5-multimedia qt5-webengine qt5-networkauth qt5-websockets qt5-script qt5-speech qt5svg
```

To check the missing dependencies, navigate to `/opt/packettracer/bin` and launch `PacketTracer`

```sh
cd /opt/packettracer/bin
./PacketTracer
```
