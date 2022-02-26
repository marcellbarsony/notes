## Rapid Spanning Tree Protocol (RSTP)

**Rapid Spanning Tree Protocol (RSTP)**
**RSTP** was designed to be backward-compatible with standard STP.

**RSPT** provides significantly faster spanning tree convergence after a topology change, introducing new behaviors and bridge port roles to accomplish this.
While STP can take 30 to 50 seconds to respond to a topology change, RSTP is typically able to respond to changes within 3x _hello times_ (default: 3x2 seconds) or within a few milliseconds of a physical link failure.

### RST Operation

RSTP adds new bridge port roles in order to speed convergence following a link failure:

- **Root** — A forwarding port that is the best port from non-root bridge to root bridge.
- **Designated** — A forwarding port to every LAN segment.
- **Alternate** — An alternate path to the root bridge. This path is different from using the root port.
- **Backup** — A backup/redundant path to a segment where another bridge port already connects.
- **Disabled** — Not strictly part of STP, a network administrator can manually disable a port.

The number of switch port states a port can be in has been reduced to three instead of STP's original five:

- **Discarding** — No user data is sent over the port.
- **Learning** — The port is not forwarding frames yet, but is populating its MAC-address-table.
- **Forwarding** — The port is fully operational.

RSTP operational details:

- Detection of root switch failure is done in 3 hello times, which is 6 seconds if the default hello times have not been changed.
- Ports may be configured as edge ports if they are attached to a LAN that has no other bridges attached.
  These edge ports transition directly to the forwarding state.
  RSTP still continues to monitor the port for BPDUs in case a bridge is connected.
  RSTP can also be configured to automatically detect edge ports.
  As soon as the bridge detects a BPDU coming to an edge port, the port becomes a non-edge port.
- RSTP calls the connection between two or more switches as a "link-type" connection.
  A port that operates in full-duplex mode is assumed to be point-to-point link, whereas a half-duplex port (through a hub) is considered a shared port by default.
  This automatic link type setting can be overridden by explicit configuration.
  RSTP improves convergence on point-to-point links by reducing the Max-Age time to 3 times Hello interval, removing the STP listening state, and exchanging a handshake between two switches to quickly transition the port to forwarding state.
  RSTP does not do anything differently from STP on shared links.
- Unlike in STP, RSTP will respond to BPDUs sent from the direction of the root bridge.
  An RSTP bridge will propose its spanning tree information to its designated ports.
  If another RSTP bridge receives this information and determines this is the superior root information, it sets all its other ports to discarding.
  The bridge may send an agreement to the first bridge confirming its superior spanning tree information.
  The first bridge, upon receiving this agreement, knows it can rapidly transition that port to the forwarding state bypassing the listening/learning state transition
  This essentially creates a cascading effect away from the root bridge where each designated bridge proposes to its neighbors to determine if it can make a rapid transition.
  This is one of the major elements that allows RSTP to achieve faster convergence times than STP.
- As discussed in the port role details above, RSTP maintains backup details regarding the discarding status of ports.
  This avoids timeouts if the current forwarding ports were to fail or BPDUs were not received on the root port in a certain interval.
- RSTP will revert to legacy STP on an interface if a legacy version of an STP BPDU is detected on that port.

[[Wikipedia - STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol)]
