# Directed Broadcast Address

A **broadcast address** is a network address used to transmit to all devices connected to a multiple-access communications network.
A message sent to a broadcast address may be received by all network-attached hosts.

In contrast, a **multicast address** is used to address a specific group of devices, and a **unicast address** is used to address a single device.

For network layer communications, a broadcast address may be a specific IP address.<br>
At the data link layer on Ethernet networks, it is a specific MAC address.

### Demonstration

Example network: 172.31.0.0

```cmd
172. 31.  0.  0 = 10101100.00011111.00000000.00000000
                  10nnnnnn.nnnnnnnn.HHHHHHHH.HHHHHHHH
```

Directed Broadcast Address

The entire host portion of the address is populated with binary ones.

```cmd
172. 31.255.255 = 10101100.00011111.11111111.11111111
                  10nnnnnn.nnnnnnnn.HHHHHHHH.HHHHHHHH
```

Routers can route directed broadcast.
By default, directed broadcasts are not routed from one physical interface to another or from one VLAN to another.

## Local Broadcast Address

A **local broadcast address** is used to communicate with all the devices on a **local network**.

The entire address is populated with binary ones.

```cmd
255.255.255.255 = 11111111.11111111.11111111.11111111
```

A **local broadcast address** is used by hosts to request IP addresses from the DHCP server:<br>

- The **host** sends a broadcast to the broadcast address to request an IP address.<br>
- The **DHCP server** allocates an IP address from the pool of IP addresses.

By default, the local broadcast address is always dropped by routers and layer 3 switches; but one can override this by configuring the device with **DHCP forwarding** or **DHCP relay**.
