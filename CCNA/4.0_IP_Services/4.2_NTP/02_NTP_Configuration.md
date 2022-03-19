# Configure NTP on a Cisco router

Cisco routers can be configured as both **NTP Servers** and **NTP Clients**.

## NTP Server

To configure a Cisco router as an **NTP server**, only a single command is needed:

```
Router1(config)#ntp master
```

After entering this command, all the devices in the LAN need to be pointed to use the router as **NTP Server**.

## NTP Client

To configure a Cisco router as an **NTP Client**, we can use the `ntp server <ip_address>` command:

```
Router1(config)#ntp server 192.168.0.100
```

> Note<br>
> To define a version of NTP, add the version NUMBER keywords at the end of the command (e.g. ntp server 192.168.0.100 version 3).

## NTP Status

To verify **NTP Status**, use the `show ntp status` command:

```
Router1#show ntp status
  Clock is synchronized, stratum 2, reference is 192.168.0.100
  nominal freq is 250.0000 Hz, actual freq is 249.9990 Hz, precision is 2**19
  reference time is DE4AB2B7.0000037A (18:49:27.890 UTC Thu Apr 5 2018)
  clock offset is 0.00 msec, root delay is 0.00 msec
  root dispersion is 0.02 msec, peer dispersion is 0.02 msec.
```
