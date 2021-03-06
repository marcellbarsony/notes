# Spanning-Tree Algorithm (SPA)

**STP** uses the **Spanning-Tree Algorithm (SPA)** to create a topology database of the network.

To prevent loops, **SPA** places some interfaces in _forwarding state_ and other interfaces in _blocking state_.<br>
**STP** decides in which state the port will be placed based on the following criteria:

1. **Root Switch election**<br>
   A **Root switch** is elected by the switches in a network.<br>
   **All working interfaces** on the **Root switch** are placed in **forwarding state**.

2. **Root Port**<br>
   **Nonroot switches** (all other switches) determine the best path to get to the **Root switch**.<br>
   The **Root Port** - that is used to reach to **Root switch** - is placed in **forwarding state**.

3. **Designated Switch**<br>
   The **Designated switch** - the switch with the best path to reach the **Root switch** - and its **Designated ports** are placed in **forwarding state**.

4. All other interfaces are placed in **blocking state** and will not forward frames.

> Note<br>
> STP considers working interfaces only - shutdown interfaces or interfaces without the cable installed are placed in an **STP disabled** state.

[[Study CCNA - How STP works](https://study-ccna.com/how-stp-works/)]
