# Bridge Protocol Data Unit (BPDU)

**BPDU**s are messages used by the switches to share STP information with each other in order to elect a root switch and detect loops.
The most common messages are **Hello BPDU**s which include the following information:

- Root Switch ID
- Sender's switch ID
- Sender's root cost
- Hello, MaxAge, and forward delay timers

A bridge sends a **BPDU** information using the unique MAC address of the port itself as a source address, and a destination address of the STP multicast address 01:80:C2:00:00.

There are three types of **BPDU**s in the STP specification:

- **Configuration (CBPDU)** — Used for spanning tree computation
- **Topology Change Notification BPDU (TCN BPDU)** — Used to announce changes in the network topology.
- **Acknowledgement BPDU - (ABPDU)** — Used to confirm the receipt of a topology change in a notification.

**BPDU**s are exchanged regularly (2 seconds by default) and enable switches to keep track of network changes and to start and stop forwarding at ports as required.

[[Study CCNA - How STP works](https://study-ccna.com/how-stp-works/)]<br>
[[Wikipedia - STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol)]

## BPDU fields

IEEE 802.1D and IEEE 802.1aq BDPUs have the following format:

```
1. Protocol ID:       2 bytes (0x0000 IEEE 802.1D)
2. Version ID:        1 byte (0x00 Config & TCN / 0x02 RST / 0x03 MST / 0x04 SPT  BPDU)
3. BPDU Type:         1 byte (0x00 STP Config BPDU, 0x80 TCN BPDU, 0x02 RST/MST Config BPDU)
4. Flags:             1 byte
  bits  : usage
      1 : 0 or 1 for Topology Change
      2 : 0 (unused) or 1 for Proposal in RST/MST/SPT BPDU
    3–4 : 00 (unused) or
          01 for Port Role Alternate/Backup in RST/MST/SPT BPDU
          10 for Port Role Root in RST/MST/SPT BPDU
          11 for Port Role Designated in RST/MST/SPT BPDU
      5 : 0 (unused) or 1 for Learning in RST/MST/SPT BPDU
      6 : 0 (unused) or 1 for Forwarding in RST/MST/SPT BPDU
      7 : 0 (unused) or 1 for Agreement in RST/MST/SPT BPDU
      8 : 0 or 1 for Topology Change Acknowledgement
5. Root ID:           8 bytes (CIST Root ID in MST/SPT BPDU)
  bits  : usage
    1–4 : Root Bridge Priority
   5–16 : Root Bridge System ID Extension
  17–64 : Root Bridge MAC Address
6. Root Path Cost:    4 bytes (CIST External Path Cost in MST/SPT BPDU)
7. Bridge ID:         8 bytes (CIST Regional Root ID in MST/SPT BPDU)
  bits  : usage
    1–4 : Bridge Priority
   5–16 : Bridge System ID Extension
  17–64 : Bridge MAC Address
 8. Port ID:          2 bytes
 9. Message Age:      2 bytes in 1/256 secs
10. Max Age:          2 bytes in 1/256 secs
11. Hello Time:       2 bytes in 1/256 secs
12. Forward Delay:    2 bytes in 1/256 secs
13. Version 1 Length: 1 byte (0x00 no ver 1 protocol info present. RST, MST, SPT BPDU only)
14. Version 3 Length: 2 bytes (MST, SPT BPDU only)

The TCN BPDU includes fields 1–3 only.
```

## STP Timers

| Timer         | Default Value  | Description                                                                               |
| ------------- | -------------- | ----------------------------------------------------------------------------------------- |
| Hello         | 2 seconds      | Time between two consecutive Hello BPDU created by root switch                            |
| MaxAge        | 10\*Hello time | Max time a switch must wait if no Hello received before proceeding to do change           |
| Forward Delay | 15 seconds     | Time taken by switch to change status of ports from forwarding to blocking and vice-versa |

The reaction of switches are :

- When a switch does not get expected **Hello** within **Hello time**, it continues to work as normal and wait until **MaxAge** time.
- Switch waits for **MaxAge time** if Hello BPDU is received within **MaxAge time**, switch consider it as some delay in network and continues as before.
  If not then switch start changing their topology.
- Now the status of different ports may change according to new topology adopted by STP.
  Ports may change their status from forwarding to blocking and vice-versa.
  But this port status process changing does not do immediately, it goes through two intermediate states (i.e, Listening and Learning states).
- The change of state from blocking to forwarding along with intermediate listening and learning state is bounded by the time of **Forward Delay**.

[[GeekforGeeks - STP Convergence](https://www.geeksforgeeks.org/spanning-tree-topology-stp-convergence/)]
