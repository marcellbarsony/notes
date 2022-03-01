# STP modes

**STP** is enabled on all of the vendor's switches by default.<br>

### IEEE Open Standard modes

- **STP IEEE 802.1D** — The first and original implementation of the STP standard.<br>
  A single instance of spanning tree is allowed in the LAN.

- **RSTP IEEE 802.1w** — **Rapid STP** is an improved version of 802.1D STP.<br>
  RSTP provides significantly faster recovery in response to network changes or failures introducing new convergence behaviors and bridge port roles.
  RSTP was designed to be backwards-compatible with standard STP: only a single instance of spanning tree is allowed in the LAN.

- **MSTP IEEE 802.1s** — **Multiple STP** allows multiple separate spanning tree instances, and enables to map and allocate multiple VLANs to the instances.

### Cisco proprietary modes

- **PVST+** — **Per VLAN STP+** is a Cisco-proprietary enhancement to the IEEE 802.1D STP, and it is the default STP version for Cisco switches.
  A single instance of spanning tree is allowed per VLAN.

- **RPVST+** — **Rapid Per VLAN STP+** is a Cisco-proprietary enhancement to the IEEE 802.1w RSTP.<br>
  Similar to PVST+, it enables the creation of one STP instance per VLAN.
  Network convergence is also faster with RPVST+.

## Single vs. Multiple STPs

With **IEEE 802.1D STP** and **802.1w RSTP** standards, all of the VLANs will have one STP instance.
Some will be taking suboptimal paths just like in the example topology:

<img src="https://www.dropbox.com/s/2jldo96yzznb1wx/stp_modes1.png?dl=1" alt="stp_modes1" class="inline" />

Since it is a single STP instance, there will be a single root bridge (e.g. SW1) for all of the VLANs in the LAN.

Multiple ST modes (IEEE 802.1s, MSTP, PVST+, RPVST+) allow us to have various ST instances.
These instances can take different paths through the network by having different root bridges, enabling load balancing to be possible.
The traffic will be taking optimized paths for the same reason as well.

## MSTP Example

With **MSTP** spanning-tree mode, we have one instance of spanning tree for each group of VLANs.

<img src="https://www.dropbox.com/s/j33l6dz0t3yj3rc/stp_modes2.png?dl=1" alt="stp_modes2" class="inline" />

The Sales and the Management departments can be mapped to SW1 as their root bridge.<br>
The Engineering and Production departments can be mapped to SW2 as their root bridge.<br>
Now, there are 2 instances of spanning tree running.

For the first instance, the traffic for VLAN10 and VLAN30 will be forwarded to SW1, and the links to SW2 will be blocked.<br>
For the second instance, the traffic for VLAN20 and VLAN40 will be forwarded to SW2 and will be blocked on SW2.

## PVST+ & RPVST+ Example

**PVST+** and **RPVST+** Cisco spanning-tree modes are both Per VLAN spanning tree protocols.
Every VLAN ha a single instance of spanning tree.

<img src="https://www.dropbox.com/s/j33l6dz0t3yj3rc/stp_modes2.png?dl=1" alt="stp_modes2" class="inline" />

The traffic from the Sales and the Management department is forwarded to SW2 (root bridge) and blocked on SW1.<br>
The traffic from the Engineering and Production departments is forwarded to SW1 (root bridge) and blocked on SW2.

There are four spanning tree instances running, as we have four VLANs in the network.
Assuming that we have 100 VLANs in our network, we will also have 100 spanning tree instances.
It would be consuming more resources as compared to grouping the like in MSTP.

> Note<br>
> PVST+ uses Root ports, Designated ports, and Alternate ports.<br>
> The Alternate ports are blocking ports.

## Spanning tree mode command

Spanning tree modes can be selected with the following commands

```
SW1(config)# spanning-tree mode ?

  mst - Multiple spanning tree mode

  pvst - Per-Vlan spanning tree mode

  rapid-pvst - Per-Vlan rapid spanning tree mode
```
