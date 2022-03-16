# Frame tagging

To identify the VLAN a packet is belonging to, switches ise tagging to assign a numerical value to each frame in a network with multiple VLANs.
This is done to ensure that switches know out which ports to forward frames.

Example network topology:

<img src="https://www.dropbox.com/s/4qn30u2bw1xv1vv/frame_tagging.jpg?dl=1" alt="frame_tagging" class="inline" />

There are two VLANs (VLAN 3 & 4) in the topology pictured above:

- **Host A** sends a broadcast packet to **SW1**.
- **SW1** receives the packet, and tags it with the VLAN ID of 3 and sends it to **SW2**.
- **SW2** receives the packet, looks up the VLAN ID, and forwards the packet out of port **Fa0/1**.
- **Host B** and **C** will not receive the packet as they are on different VLANs.

[Study CCNA - Frame tagging](https://study-ccna.com/frame-tagging/)
