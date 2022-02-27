## Selecting STP Root port

All **Nonroot Switches** need to determine the best path to get to the root switch.
The port used to reach the root switch (**Root Port**) is placed in forwarding state.
The **Root port** is chosen based on lowest path cost.

In case the best root cost ties for two or more paths, the following tiebreakers are applied:

1. Lowest neighbor **Bridge ID**
2. Lowest neighbor **port priority** (128 by default)
3. Lowest neighbor **internal port number** (Port ID)

Verify the selected root port:

```
SW1#show spanning-tree root
```

On the **Root Switch**, all working interfaces are placed in forwarding state.

## Path cost

**Path cost** is the cost to get to the root bridge/root switch.<br>
**Path cost** is calculated from the cost of a port and the number of links.

**Path cost** for different port speed and STP variation

|  Data rate | Original STP (IEEE 1998) | RSTP/MSTP (IEEE 2004) |
| ---------: | -----------------------: | --------------------: |
|  10 Mbit/s |                      100 |             2,000,000 |
| 100 Mbit/s |                       19 |               200,000 |
|   1 Gbit/s |                        4 |                20,000 |
|  10 Gbit/s |                        2 |                 2,000 |
| 100 Gbit/s |                      N/A |                   200 |
|   1 Tbit/s |                      N/A |                    20 |

The default values can be overridden on per-interface basis with the following command:

```
SW1(config-if)#spanning-tree cost <value>
```
