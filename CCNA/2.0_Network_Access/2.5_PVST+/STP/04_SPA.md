## Spanning-Tree Algorithm (SPA)

**STP** uses the **Spanning-Tree Algorithm (SPA)** to create a topology database of the network.

To prevent loops, **SPA** places some interfaces in _forwarding state_ and other interfaces in _blocking state_.<br>
**STP** decides in which state the port will be placed based on the following criteria:

1. A **Root switch** is elected by the switches in a network.
   All working interfaces on the **Root switch** are placed in forwarding state.

2. **Nonroot switches** (all other switches) determine the best path to get to the **Root switch**.
   The port used to reach to **Root switch** (**Root port**) is placed in forwarding state.

3. The **Designated switch** - the switch with the best path to reach the **Root switch** - and its **Designated ports** are placed in forwarding state.

4. All other interfaces are placed in **blocking state** and will not forward frames.

> Note<br>
> STP considers working interfaces only - shutdown interfaces or interfaces without the cable installed are placed in an **STP disabled** state.

[[Study CCNA](https://study-ccna.com/how-stp-works/)]
