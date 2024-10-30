# PipeWire

## Resources

- [PipeWire.org](https://pipewire.org/)
- [PipeWire.org - Docs](https://docs.pipewire.org/)

## Service

- [Reddit](https://www.reddit.com/r/archlinux/comments/nnczys/pipewireservice_not_found_after_installing/)

```sh
# Status
systemctl --user status pipewire
```

## ALSA vs. PipeWire

- [Debian Wiki - PipeWire](https://wiki.debian.org/PipeWire)

Some may describe this as "replacing ALSA", but as the PipeWire FAQ clarifies:
No, ALSA is an essential part of the Linux audio stack, it provides the
interface to the kernel audio drivers."

That said, the ALSA user space library has a lot of stuff in it that is
probably not desirable anymore these days, like effects plugins, mixing,
routing, slaving, etc. PipeWire uses a small subset of the core ALSA
functionality to access the hardware. All of the other features should be
handled by PipeWire.
