## STP Port states

All switch ports in the LAN where STP is enabled are categorized.

[[Wikipedia - STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol)]

|    STP mode    | Receive BPDUs | Send BPDUs | Forwards data frames? | Learn MAC Address | Transitory or Stable state? |
| :------------: | :-----------: | :--------: | :-------------------: | :---------------: | :-------------------------: |
|  **Blocking**  |      Yes      |    Yes     |          No           |        No         |           Stable            |
| **Listening**  |      Yes      |    Yes     |          No           |        No         |         Transitory          |
|  **Learning**  |      Yes      |    Yes     |          No           |        Yes        |         Transitory          |
| **Forwarding** |      Yes      |    Yes     |          Yes          |        Yes        |           Stable            |
|  **Disabled**  |      Yes      |    Yes     |          No           |        No         |           Stable            |

### Blocking

A port that would cause a switching loop if it were active.
To prevent the use of looped paths, no user data is sent of received over a blocking port.
BPDU data is still received in blocking state.
A blocked port may go into forwarding mode if the other links in use fail and the spanning tree algorithm determines the port may transition to the forwarding state.

### Listening

The switch processes BPDUs and awaits possible new information that would cause it to return to the blocking state.
It does not populate the MAC table and it does not forward frames.

### Learning

While the port does not yet forward frames, it does learn source addresses from frames received and adds them to the MAC table.

### Forwarding

A port in normal operation receiving and forwarding frames.
The port monitors incoming BPDUs that would indicate it should return to the blocking state to prevent a loop.

### Disabled

A network administrator has manually disabled the switch port.

When a device is first attached to a switch port, it will not immediately start to forward data.
It will instead go through a number of states while it processes BPDUs and determines the topology of the network.
The port attached to a host such as a computer, printer or server always goes into the forwarding state, albeit after a delay of about 30 seconds while it goes through the listening and learning states.
The time spent in the listening and learning states is determined by a value known as the forward delay (default 15 seconds and set by the root bridge).
If another switch is connected, the port may remain in blocking mode if it is determined that it would cause a loop in the network.
Topology Change Notification (TCN) BPDUs are used to inform other switches of port changes.
TCNs are injected into the network by a non-root switch and propagated to the root.
Upon receipt of the TCN, the root switch will set the Topology Change flag in its normal BPDUs.
This flag is propagated to all other switches and instructs them to rapidly age out their forwarding table entries.
