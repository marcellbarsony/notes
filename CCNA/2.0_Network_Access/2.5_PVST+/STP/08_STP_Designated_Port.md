# Selecting STP Designated port

The switch with the best path to reach the **Root Switch** is placed in **Forwarding state** on the shared Ethernet segments.
This switch is called the **Designated Switch** and its port is known as the **Designated Port**.
To avoid loops, the **Non-Designated port** on the other end of the link is placed in **Blocking state**.

[[Study CCNA](https://study-ccna.com/selecting-stp-designated-port-dp/)]

The designated switch is determined based on the following criteria:

1. Lowest **Root Cost** — The switch with the **lowest cost to reach the root** becomes the Designated Switch on the link.
2. Lowest **BridgeID** — In case of a tie, the switch with the **lowest BID** becomes the Designated Switch.
3. Lowest **neighbor port priority** — (128 by default)
4. Lowest **neighbor port number**

## Blocking port

Ports that are not **Root Ports** or **Designated Ports** are put in the **blocking state**.
