## Subnet Mask

An IP address is divided into two parts:

- Network
- Host

The **Subnet mask** determines which part is the network and which part is the host part.<br>
The **Subnet mask** also determines if the device is remote or local.

## Slash notation

**Subnet mask** can be also written in **slash notation**.<br>
To determine the slash notation of the subnet mask, convert the dotted decimal format into binary, count the series of 1s, and add a slash on the start.

For example, we have the dotted decimal **subnet mask** of **255.0.0.0**.<br>
In binary, it is **11111111.00000000.00000000.0000000**.<br>
The number of succeeding 1s are 8, therefore the slash notation of **255.0.0.0** is **/8**.

## Discontiguous Network Mask

Cisco devices do not support discontiguous masks:<br>
**11110000.11111111.00000110.11000000** = 140.255.3.91

Only contiguous subnet masks are supported:<br>
**11111111.11111111.11000000.00000000** = 255.255.192.0

[[Study CCNA](https://study-ccna.com/subnet-mask/)]
