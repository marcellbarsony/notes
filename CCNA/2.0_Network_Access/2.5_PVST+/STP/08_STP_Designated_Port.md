# Selecting STP Designated port

The switch with the best path to reach the root switch is placed in forwarding state on the shared Ethernet segments.
This switch is called the **designated switch** and its port is known as the **designated port**.
To avoid loops, the **non-designated port** on the other end of the link is placed in blocking state.

[[Study CCNA](https://study-ccna.com/selecting-stp-designated-port-dp/)]

The designated switch is determined based on the following criteria:

1. The switch with the **lowest cost to reach the root** becomes the designated switch on the link.
2. In case of a tie, the switch with the **lowest BID** becomes the designated switch.

Lowest root cost to the bridge
Lowest BID
Lowest neighbor port priority (128 by default)
Lowest neighbor port number

## Blocking port

Ports that are not **Root Ports** or **Designated Ports** is put in the **blocking state**.
