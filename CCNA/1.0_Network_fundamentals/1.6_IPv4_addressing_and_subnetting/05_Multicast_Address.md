# Multicast Address

**Multicast addresses** represent a group of devices in a LAN (one-to-many communication).
A frame sent to a multicast address will be forwarded to a group of devices on the LAN.

<img src="https://www.dropbox.com/s/ihovri2aw8oum33/multicast.png?dl=1" alt="multicast" class="inline" />

**Multicast frames** have a value of 1 in the least-significant bit of the first octet of the destination address.
This helps a network switch to distinguish between unicast and multicast addresses.

Example Ethernet multicast address: **01:00:0C:CC:CC:CC** used by Cisco Discovery Protocol (CDP)

## Example

Multicast messages are sent to IP multicast group addresses.
Routers forward copies of the packet out to every interface that has hosts subscribed to that group address.
Only the hosts that need to receive the message will process the packets.
All other hosts on the LAN will discard them.

<img src="https://www.dropbox.com/s/7g1b0lg8gbxprjb/multicast_address.jpg?dl=1" alt="multicast" class="inline" />

**R1** has sent a multicast packet destined for 224.0.0.9.
This is an RIPv2 packet, and only routers on the network should read it.
All other hosts on the LAN will discard the packet.

[[Study CCNA - Unicast, multicast, and broadcast addresses](https://study-ccna.com/unicast-multicast-and-broadcast-addresses/)]
