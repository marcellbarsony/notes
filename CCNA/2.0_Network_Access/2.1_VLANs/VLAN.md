# Virtual LAN

**VLANs** are logical grouping of devices in the **same broadcast domain.**<br>
VLANs are usually configured on switches by placing some interfaces into one broadcast domain and some interfaces into another.
Each VLAN acts as a subgroup of the switch ports in an Ethernet LAN.

A VLAN acts like a physical LAN, but it allows hosts to be grouped together in the same broadcast domain even if they are not connected to the same switch.

- **Security** — VLANs reduce security risks by reducing the number of hosts that receive copies of frames that the switches flood.<br>
  Hosts holding sensitive data can be kept on a separate VLAN.
- **Segmentation** — VLANs increase the number of broadcast domains while decreasing their size.
- **Flexibility** — VLANs can be configured more easily, without changing the physical infrastructure.

> NOTE<br>
> To reach a hosts on a different VLAN, a router is needed.

### Physical vs. Logical view

<img src="https://www.dropbox.com/s/yms6ef19ybjxzcn/VLAN_physical_logical.jpg?dl=1" alt="network" class="inline" />
