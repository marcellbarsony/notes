# Network Time Protocol (NTP)

**Network Time Protocol (NTP)** is an application layer (Layer 7) networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks.

**NTP** (NTPv4 - RFC 5905) is intended to synchronize all participating computers withing a few milliseconds of Coordinated Universal Time (UTC).
The protocol is usually described in terms of a client-sever model (_NTP Host_ and _NTP Client_), but can be used in peer-to-peer relationships where both peers consider the other to be a potential time source.
Implementations send and receive timestamps using UDP port 123.

**Network Time Security (NTS)**, a secure version of NTP with TLS and AEAD is a proposed standard and documented in RFC 8915.

[[Wikipedia - Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol)]<br>
[[Study CCNA - NTP (Network Time Protocol)](https://study-ccna.com/ntp-network-time-protocol/)]<br>

## Configuration

A router's time can be set with the following command

```
R1#clock set 23:16:45 16 August 2022
```

A router's time configuration can be checked with the following command

```
R1#show ntp status
```
