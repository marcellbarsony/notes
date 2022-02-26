## Spanning Tree Priority: Root Primary and Root Secondary

**STP** is a Layer 2 loop prevention mechanism that will block one port on the network switch if it detects a loop of broadcast messages within its architecture.
By default, spanning trees are enabled on most interconnected Cisco switches.
Switches send out BDPU on all active interfaces.
BPDU contains STP information needed to elect a root switch and detect loops.

## STP Root Bridge Election

The switch assigns a **root bridge** within the interconnected switches.
A **root bridge** is the central point of all switches and will be responsible for forwarding the traffic.
The switch selects a **root bridge** by using the switch priority and the MAC address.
Each switch has its own bridge ID and has a default priority value of 32768.
The **root bridge** is taking precedence over the MAC address.
If a switch has the lowest bridge priority value among the switches withing the LAN, then it will be elected as the spanning tree root bridge.

If all the spanning tree bridge priority has the same priority value on all the switches, then the MAC address will be the tiebreaker.
The **lowest MAC address** will be elected as the **Root Bridge**.
Most of the older switches have a lower value of MAC address, have lower bandwidth, and limited CPU/memory as compared to newer switches.
Electing an older switch as the **Root Bridge** will cause a suboptimal operation on a network.
