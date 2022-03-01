# VTP Messages

**VTP packets** are either sent via ISL or 802.1Q frames.
**VTP messages** are sent to destination MAC address `01-00-0C-CC-CC-CC` with a logical link control (LLC) code of Subnetwork Access Protocol (SNAP) (AAAA) and a type of 2003 (in the SNAP header).

- VTP protocol version (1, 2, or 3)
- VTP message types:
  - Summary Advertisements
  - Subset Advertisements
  - Advertisement Requests
- Management domain length
- Management domain name

> **Note** <br>
> VTP does not advertise information about which switch ports are assigned to which VLAN.

### Summary Advertisements

**Summary Advertisements** inform adjacent Catalysts of the current VTP domain name and the configuration revision number.
By default, Catalyst switches issue **Summary Advertisements** in 5 minutes (300 seconds) increments.

When the switch receives a **Summary Advertisement** packet, it compares the VTP domain name to its own VTP domain name:

- If the name is different, the switch simply ignores the packet.
- If the name is the same, the switch then compares the configuration revision number to its own version:

  - If its own revision number is higher or equal, the packet is **ignored**.
  - If its own revision number is lower, an **advertisement request** is sent.

  <img src="" alt="summary_advert_packet_format" class="inline" />

- **Followers** - Indicates that this packet is followed by a Subset Advertisement packet.
- **Updater Identity** - IP address of the switch that is the last to have incremented the configuration revision.
- **Update Timestamp** - Date and time of the last increment of the configuration revision.
- **Message Digest 5 (MD5)** - Carries the VTP password if MD5 is configured and used to authenticate the validation of a VTP update.

### Subset Advertisements

When a change has been made on a VLAN in a Catalyst, the server Catalyst increments the configuration revision and issues a Summary Advertisement.
One or several **Subset Advertisements** follow the Summary advertisement.
A **Subset Advertisement** contains a list of VLAN information.
If there are several VLANs, more than one subset advertisement can be required in order to advertise all the VLANs.

  <img src="" alt="subset_advert_packet_format" class="inline" />

This formatted example shows that each VLAN information field contains information for a different VLAN.
It is ordered so that lowered-valued ISL VLAN IDs occur first:

  <img src="" alt="example" class="inline" />

- **Code** - 0x02 for Subset Advertisement
- **Sequence number** - This is the sequence of the packet in the stream of packets that follow a summary advertisement.

### Advertisement Requests

A switch needs a VTP request in the following situations:

- The switch has been reset.
- The VTP domain name has been changed.
- The switch has received a VTP summary advertisement with a higher configuration revision than its own.

  <img src="" alt="advertisement_request" class="inline" />

- **Code** - 0x03 for Advertisement Request.
- **Start-Value** - This is used in cases in which there are several subset advertisements.<br>
  If the first (n) subset advertisement has been received and the subsequent one (n+1) has not been received, the Catalyst only requests advertisements from the (n+1)th one.
