# Dynamic vs. Static VLAN

**VLAN** is a collection of ports selected by the switch as belonging to the same broadcast domain.

## Static VLANs

**Static VLANs** (port-based VLANs) are manually configured VLANs providing a name, VLAN ID (VID) and port assignments.

When a deice is connected to a port, it automatically assumes the VLAN to which the port is assigned.
**Static VLANs** are generally used to reduce broadcast and increase security.

## Dynamic VLANs

**Dynamic VLANs** are created by storing the hardware addresses (MACs) of host devices in a database so that the switch can dynamically assign the VLAN at any time when a host is connected to the switch.

### VMPS

**Dynamic VLANs** use a central server (**VMPS - Virtual Membership Policy Server**) to manage the configurations of each switch on the VLAN.
The **VMPS server** contains a database containing the MAC addresses of all the the workstations with the VLAN to which it belongs.
This VLAN to MAC address mapping scheme allows hosts to roam the network and connect to any switch that is a part of the **VMPS network** while maintaining their VLAN configuration.
When a host is connected to a switch, the **VMPS** database is checked for membership in a VLAN before port activation and assignment to a VLAN.

## Voice VLAN

The **Voice VLAN** feature enables access ports to carry IP voice traffic form an IP phone.
When the switch is connected to an IP Phone, the phone sends voice traffic with Layer 3 IP precedence and Layer 2 class of service (CoS) values, which are both set to 5 by default.
Because the sound quality of an IP phone call can deteriorate if the data is unevenly sent, the switch supports quality of service (QoS) based on IEEE 802.1p CoS.
QoS uses classification and scheduling to send network traffic from the switch in a predictable manner.

The Cisco IP Phone contains an integrated three-port 10/100 switch.
The ports provide dedicated connections to these devices:

- **Port 1** connects to the switch or other voice-over-IP (VoIP) device.
- **Port 2** is an internal 10/100 interface that carries the IP Phone traffic.
- **Port 3** (Access port) connects to a PC or other device.
