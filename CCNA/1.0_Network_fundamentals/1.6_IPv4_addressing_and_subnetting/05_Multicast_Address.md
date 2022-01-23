## Multicast Address

**Multicast addresses** represent a group of devices in a LAN.
A frame sent to a multicast address will be forwarded to a group of devices on the LAN.

<img src="https://www.dropbox.com/s/ihovri2aw8oum33/multicast.png?dl=1" alt="multicast" class="inline" />

**Multicast frames** have a value of 1 in the least-significant bit of the first octet of the destination address.
This helps a network switch to distinguish between unicast and multicast addresses.

Example Ethernet multicast address: **01:00:0C:CC:CC:CC** used by Cisco Discovery Protocol (CDP)

[[Study CCNA](https://study-ccna.com/unicast-multicast-and-broadcast-addresses/)]
