## Spanning Tree Protocol (STP)

**Spanning Tree Protocol (STP)** is a IEEE 802.1Q-2014 network protocol that builds a loop-free topology for Ethernet networks (on Layer 2).
The basic function of **STP** is to prevent [bridge loops](https://en.wikipedia.org/wiki/Switching_loop) and the [broadcast radiation](https://en.wikipedia.org/wiki/Broadcast_storm) that results from them.
Spanning tree also allows a network design to include backup links providing fault tolerance if an active link fails.

**STP** creates a spanning tree that characterizes the relationship of nodes within a network of connected Layer-2 bridges, and disables thos link that are not part of the spanning tree, leaving a single active path between any two network nodes.

In 2001, the IEEE introduced **Rapid Spanning Tree Protocol (RSTP)** as 802.1w.
**RSTP** provides faster recover in response to network changes or failures, introducing new convergence behaviors and bridge port roles to do this.
**RSTP** was designed to be backwards-compatible with standard **STP**.

[Wikipedia - STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol)

## How STP works?

**STP** uses the **Spanning-Tree Algorithm (SPA)** to create a topology database of the network.<br>
To prevent loops, **SPA** places some interfaces in forwarding state and other interfaces in blocking state.
**STP** decides in which state the port will be placed based on the following criteria:

- A **root switch** is elected by the switches in a network.
  All working interfaces on the root switch are placed in forwarding state.

- **Nonroot switches** (all other switches) determine the best path to get to the root switch.
  The port used to reach to root switch (root port) is placed in forwarding state.

- \*\*
